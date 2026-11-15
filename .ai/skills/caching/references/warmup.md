# Cache warm-up

Stampede-prevention patterns and the shared loader are in `patterns.md` §3, §6. The job's scope is selective: load only keys whose absence makes the first request slow or floods the DB. All other keys are loaded by the read path on miss.

## 1. When to run

L2 does not lose data when the application is redeployed, so a normal deploy does **not** need re-warm-up. The job runs on signals, not blindly on every deploy:

| Trigger | How to detect |
| --- | --- |
| Cache lost data (restart, failover, flush) | Marker key `<service>:cache:epoch` missing. The job writes this key after finishing tier 1 |
| Key or value format change | Bump the group's version prefix, leaving the new group empty. Warm up the new group **before** the code reading the new version takes traffic |
| Invalidating a large group (config change, bulk import) | Event emitted by the owning module |
| Before known peak hours | Schedule |
| Refresh-ahead for tier 1 | Run periodically with a period shorter than TTL |
| Cache failover (deletes may be lost) | Failover event or alert from the cache's HA; runbook per `patterns.md` §4 |

## 2. Tiers

| Tier | Content | How to load | Blocks opening traffic |
| --- | --- | --- | --- |
| W1 · mandatory | Keys nearly every request needs: config, catalogs, role permissions. Small, fully enumerable | Load all; periodic refresh-ahead | Yes, with timeout. On timeout, open traffic anyway (fail-open) |
| W2 · hot | Record details, top N by actual access | Run in background after opening traffic, rate-limited | No |
| Rest | — | Read path loads on miss | — |

Do not load the whole DB: it wastes memory, pushes hot keys out, and the job itself becomes a stampede source.

## 3. Managing the warm-up key set

A mechanism is needed, but it is a **group registry**, not a hard-coded key list. A hard-coded list drifts as soon as data changes.

- **Registry in code:** each module declares its warm-up groups: group name, tier, ID-listing function, loader, max N, batch size, and concurrency.
  - ID-listing function: W1 queries everything; W2 reads the hot list.
  - The loader **is the read path's own function**: same key, same serializer, same TTL.
  - The module owning the data owns its warm-up group.
- **Hot list for W2:**
  - Sample access (a few percent of requests) and record into sorted set `<service>:<module>:hot:<thực thể>` via `ZINCRBY`, split by daily window.
  - Periodically trim to about 2N elements.
  - Periodically snapshot the hot list to durable storage (DB or file). Reason: when the cache is lost, the hot list is lost with it, exactly when it is needed most.
  - No snapshot yet: derive from business sources (recently updated or used records), or run W1 only.
- **Epoch marker key:** no TTL. If the eviction policy evicts this key, the job runs one extra time. That is harmless because the job is idempotent.

## 4. Job rules

- **Only one instance runs:** distributed lock with TTL and periodic renewal, or a scheduler with dedupe. N instances warming up together cause a self-inflicted herd.
- **Has a DB load budget:**
  - Load in batches, limit concurrency, and use only a small share of the connection pool.
  - Read from a read-only replica only if the cache row allows replica reads (`patterns.md` §3); otherwise read the primary within the load budget.
  - Pause when DB latency rises.
- **Spread expiry times:** bulk-loaded keys need TTL spread wider than normal jitter, e.g. random within TTL × [0.5; 1]. Otherwise they all expire exactly one TTL later.
- **Do not overwrite newer data:**
  - W2 writes only when the key does not exist and no invalidation marker exists (`patterns.md` §4), in one atomic step.
  - W1 refresh-ahead overwrites with version or timestamp comparison.
- **Rerunnable:** store progress checkpoints; on failure midway, the next run continues.
- **Job failure:** log and alert.
- **Measure:**
  - Hit ratio in the first 5–15 minutes after the trigger.
  - W1 run time.
  - Count of keys loaded and keys failed.
  - DB load while the job runs.
