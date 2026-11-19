# Data cache (L1/L2): design and implementation patterns

Mandatory rules are in Rule `cache`; this file only describes how.

## 1. Model

- **L1:** local cache, within one request or in one process's RAM. Optional.
- **L2:** cache shared across instances. Concrete technology per the project's architecture.
- **DB:** the single source of truth.
- Cache is a layer on top of an optimized query, not a way to dodge optimization. A query slow from a missing index is only hidden by a cache: on every miss, warm-up, or cache outage, that slow query runs again.
- Cached data reads the nearest tier first: L1 → L2 → DB. Data not meeting cache conditions reads DB directly.

## 2. Data classification

The table below is an initial suggestion. Each cache must still meet all six conditions in Rule `cache`.

| Data type | Cache? | Accompanying condition |
| --- | --- | --- |
| Master data, reference data, category lists | Yes | |
| System configuration | Yes | |
| Product catalog | Yes | |
| Read-heavy query results | Yes | Key determinable from parameters, deletable correctly |
| Aggregate reports | Yes | |
| Dashboard statistics | Yes | Business accepts staleness; state the staleness window |
| User profile | Yes | Invalidation covers every write path; per §8 if it contains `secret` data |
| Permission / Role | Conditional | On permission change, delete immediately, including L1 on every instance; short TTL |
| Search result | Conditional | Short TTL; limit key count (first page, common parameters only) |
| Free-form filtered or paginated lists | Not by default | Unbounded key combinations, cannot delete correctly. If needed, delete by group with version prefix, only when write frequency is low |

Question that decides the staleness window: *"If users see data X minutes old, is anyone harmed?"* If yes, do not cache, or reduce X.

## 3. Read path

```
L1 hit           → return
L1 miss, L2 hit  → load L1 → return
L2 miss          → single-flight → read DB → write L2 then L1 → return
L2 error         → skip cache → read DB → return; log, count fail-open
```

- **Distinguish miss from error:** miss means key absent; error means timeout, lost connection, broken deserialize. On miss, load and write back to cache; on error, do not write back, only read the source. Measure these two separately.
- **Single-flight is the default** and lives in one shared read function (shaped like `remember(key, ttl, loader)`), not rewritten in each path:
  - Within a process: merge requests for the same key into one promise.
  - Across instances: `SET NX` lock with TTL, only for keys marked hot. Hot keys are marked in the "Chống dồn tải" column of the database-design cache table, based on frequency in the AP table. Normal keys accept at most one query per instance.
    - Lock TTL ≥ loader timeout, otherwise a second loader runs while the first is still loading. Only the owner releases the lock (token check); a plain delete can remove another instance's lock. Redis: `redis.md` §3.
  - Waiting requests are bounded (e.g. 5 × 50 ms; real threshold derived from the AP's target latency). On timeout, read DB directly, do not return an error; concurrent DB queries are still bounded by the connection pool.
- **Placement in Repository:** wrap the read repository with a caching layer (decorator) or split out a query repository; both call `remember`. Service keeps its interface and does not know data is cached.
- **Write paths bypass cache:** functions used by write paths (`findForUpdate`, reads inside a writing transaction) read DB directly. Modifying a cached copy and saving overwrites newer changes (lost update).
- **Loader reads the primary.** With DB read replicas, a loader reading a replica right after delete-after-commit can reload the old row and cache it for a full TTL. Read a replica only when the acceptable staleness window covers max replica lag plus TTL; record it in the cache row. Same for warm-up.
- **Read model:** map results to a dedicated value type before caching. ORM entities lose lazy relations and identity map through serialization.

## 4. Write path and invalidation

```
Transaction commit → delete L2 key → emit invalidation event → every instance deletes L1
```

- **After commit:** attach to the transaction's after-commit hook, or outbox. Deleting before commit lets an interleaved read reload the old value; on rollback the delete was needless.
- **Delete, do not update.** If two concurrent writes both update the cache, observer order does not follow commit order, and the cache may hold the old value until TTL expires. Deleting lets the next read reload the correct value.
- **Stale write-back race:** delete-after-commit alone does not prevent it. Read A misses and loads the old row; write B commits and deletes the key; A then writes the old value, which lives until TTL. Choose one per cache, record it in the cache row:
  - **Invalidation marker (default when read-after-write matters):** the delete step first sets a short marker for the key (TTL ≥ loader timeout), then deletes the key. Write-back is an atomic conditional write: skip if the marker exists, just return the DB value. Marker and key must be usable in one atomic step (Redis: one Lua script, same hash slot, `redis.md` §3, §5).
  - **Version overwrite:** writes overwrite with version comparison instead of deleting, and write-back also compares versions (W1 keys).
  - **Accept TTL:** only when the staleness window ≥ that key's TTL.
- **Cache failover can undo deletes:** with asynchronous replication, deletes acknowledged shortly before a failover may be lost and old values reappear. For groups whose staleness window is shorter than TTL, the failover runbook clears the group (version prefix bump or batched scan + delete) then triggers warm-up (`warmup.md` §1); otherwise record that TTL covers it.
- **Update only with a version:** the cached value carries a version (or a sufficiently precise `updated_at`); write with a compare-then-write script, writing only when the version is newer. Use for W1 keys (config, catalogs) when you do not want the cache empty after a write.
- **Read right after write must be correct:** use the stale write-back guard above (marker or version); never delete before commit.
- **Failed deletes must not be ignored** like failed reads: the old key lives until TTL expires. Retry with a limit; when exhausted, push to a reprocessing queue and log a warning.
- **L1 invalidation events** have retry or a recovery mechanism. An instance that loses its connection to the event channel clears all of L1 on reconnect. Short L1 TTL is the safety net when events still slip through.
- **ORM observers do not catch** bulk updates, raw SQL, migrations, imports, jobs, other services writing the same DB: these paths delete keys after commit or emit events themselves.
- **Aggregate caches in other modules** listen to the owning module's events and delete their own keys.
- Do not use write-behind (write cache first, flush to DB later) for business data.

## 5. Key and TTL

- **Key format** per project convention; default `<service>:<module>:<thực thể>:<mã>[:<biến thể>]`. The key shows the owning module and allows group deletion.
- **Version in key** (`v42:…`) when changing value structure or needing to delete a whole group: bumping the version invalidates the whole group.
- **TTL by data type**, not one shared TTL. Catalogs, config: minutes to hours. Display data: short. Permissions: short.
- **L1 TTL:** if it lives longer than one request, keep a few seconds to a few tens of seconds.
- **Jitter ±10–20%** so keys loaded together do not expire in the same second.
- **Negative caching:** only when the AP table shows significant lookups of nonexistent IDs; only for lookups by ID or natural key, not lists.
  - Store a dedicated sentinel value (e.g. `{"_neg":1}`), distinct from a miss; `null` or empty string reads like a miss in many clients, so the DB is hit every time.
  - TTL short, not longer than the acceptable staleness window.
  - The create path deletes the empty-result keys after commit, including natural-key ones (slug, code); list them in the cache row as write-path deletion events.
- **Group deletion:** version prefix or batched `SCAN`.

## 6. Stampede prevention

| Symptom | Default measure | Add when needed |
| --- | --- | --- |
| Many keys expire at once (after deploy, warm-up, group delete) | TTL jitter; group delete via version prefix | Paced warm-up (`warmup.md`) |
| One key misses, N requests hit DB together | Single-flight (§3) | Extremely hot key: **stale-while-revalidate**. Store soft TTL < hard TTL; past soft TTL still return the old value and only one request reloads in the background. Hot keys known in advance: put in warm-up W1 |
| Lookups for nonexistent IDs always hit DB | Validate input at the boundary | Negative caching (§5), when the AP table shows it; Bloom filter, only with data showing large junk-ID traffic |
| Whole cache tier down | Fail-open (§7); limit concurrent DB queries | Cache HA, circuit breaker, rate limit at the boundary, per availability NFR |

Preventing double-selling and duplicate writes uses transactions, DB locks, or a separate distributed lock, not the stampede-prevention lock.

## 7. Errors and fail-open

- Connection pool to the cache is bounded.
- When the cache is down, all requests fall to DB: limit concurrency (pool, bulkhead) so the DB does not go down too. A circuit breaker helps skip the cache immediately instead of waiting for a timeout per request.
- Do not depend on request processing order across instances.

## 8. Personal data (`secret`)

Mandatory conditions are in Rule `cache`. How to meet them:

- **Cache only needed fields:** create a dedicated type for the cache value per the screen or API using it; do not serialize the whole entity. If a screen needs a name, the value has only ID and name.
- **Key:** `<service>:<module>:<thực thể>:<mã nội bộ>`, plus tenant ID when multi-tenant. When looking up by email or phone, query DB for the internal ID first; do not build keys from email.
- **TLS and accounts:** one cache account per service, with permission only on its key prefix (prefix ACL if the technology supports it). Do not use shared passwords.
- **Disk persistence:** if the cache enables snapshot or append log, encrypt the disk, or put the `secret` key group on a cache instance with persistence off. Replicas and cache backup files are also in this scope.
- **Short TTL:** per the acceptable staleness window, and no longer than the deadline by which deletion requests must take effect.
- **Delete on request:** the account-deletion flow deletes every `secret` key of that person (listed in the database-design cache row), including L1 on every instance; a test proves that after deletion nothing can be read from cache.

## 9. Pitfalls

- **Serialization loses types:** through JSON, datetimes, big numbers, decimals become strings. Convert types back on read, with tests.
- **Large values:** limit value size per the project ceiling; if exceeded, cache only the needed part, or compress.
- **Missing `maxmemory` and eviction policy:** a full cache fails writes. A policy that only evicts keys with TTL never evicts keys lacking TTL.

## 10. Metrics

Minimum:

- L1, L2 hit rate and miss rate.
- L2 call latency (p95, p99); count of timeouts, errors, and fail-opens.
- Memory used; eviction rate.
- DB load on miss.
- Count of single-flight waits; hot keys.
- Count of failed key deletions; count and latency of failed invalidation events.

Without metrics you cannot prove the cache helps, nor know when it breaks.

## 11. Recording in the design

Each cache is one row in the database-design cache table. Besides the table columns, also record:

- Acceptable staleness window as a number, not "short" or "a few minutes".
- Value contains `secret` data: protection per §8.
- Has warm-up: the group's trigger and DB load budget.
- Stale write-back guard chosen (§4), loader source primary or replica with reason (§3), failover handling (§4).
