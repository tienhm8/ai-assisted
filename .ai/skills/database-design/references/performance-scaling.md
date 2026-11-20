# Database Design – Performance and scaling

> Thresholds (latency, throughput) come from the project NFRs. DBMS-neutral; syntax and version limits: `postgresql.md`, `mysql-mariadb.md`.

## 1. Access pattern (AP) profile

Every performance decision starts from this table. No AP, no index, partition or denormalization.

| AP | Description | Type | Filter conditions | Sort / pagination | Frequency (estimate) | Target latency | Rows returned | Serving index / structure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AP-01 | Customer's order list | Read | `customer_id = ?`, `status IN (…)` | `created_at DESC`, keyset | 200/sec | p95 < NFR | ≤ 50 | `ix_order_customer_status_created` |

Add volume estimates per table: current rows, growth/month, average row size, after 1 and 3 years; read/write ratio; hot spots (one row written by many concurrent sessions, e.g. balance, stock, counters).

## 2. Index design

### 2.1 Principles

1. **Start from APs**, not columns. Each index records the AP it serves.
2. **Candidates to consider:** columns in `WHERE`, `JOIN` conditions, `ORDER BY`, `GROUP BY` of key APs; FK columns; high-cardinality (highly selective) columns often used for search and filtering.
3. **Usually not worth indexing:**
   - Very small tables (a few thousand rows or fewer): full scan is cheaper, the optimizer ignores the index.
   - Low-cardinality, evenly distributed columns (boolean, status 0/1) on their own. Exception: skewed distribution and the AP looks only for the rare part (e.g. 1% `pending` orders); then use a partial index if available, or a composite with the selective column after.
   - Columns updated constantly with no AP filtering on them: every UPDATE must modify the index too and may lose the DBMS's in-place update optimization.
4. **Sparse columns (mostly NULL):** if the AP looks for non-NULL rows, the index is highly selective. If partial indexes are available, use `WHERE col IS NOT NULL` for compactness; otherwise a normal index.
5. **Covering index:** include returned columns in the index to avoid table reads; with a clustered index, secondary indexes already contain the PK.
6. **Expression index** when the filter must use a function (`lower(email)`): expression index, or an indexed generated column.
7. **FK columns** need indexes so joins and parent deletes do not scan the child table; check whether the DBMS creates them automatically.
8. **Remove redundant indexes:** indexes that are prefixes of another index, duplicates of UNIQUE/PK, indexes no AP uses (check with the DBMS's index usage stats). Before dropping an index in production, hide it first if supported; otherwise drop via a migration with rollback.
9. **Create indexes on tables with data** using the DBMS's non-write-blocking mode; record consequences of mid-way failure.

### 2.2 Multi-column (composite) indexes

- **Left-most prefix rule:** index `(a, b, c)` can be used to seek on conditions on `a`, `a,b`, `a,b,c`; not to seek when `a` is missing. Exception: skip scan (if available) works when `a` has few values; do not design around it.
- **Column order:** equality columns first, then range (`>`, `<`, `BETWEEN`, `LIKE 'x%'`) or sort columns. After the first range column, subsequent columns no longer narrow the seek range (only filter within the index).
- **Serving `ORDER BY … LIMIT` too:** when sort columns follow the equality columns in the same direction (or fully reversed), the DB reads in index order and stops early, with no sort (no sort step in the execution plan).
- Do not mechanically put the most selective column first; APs decide the order. A good composite index often replaces several single-column indexes.

### 2.3 Conditions that weaken or prevent index use

| Condition | Reason | Alternative query / design |
| --- | --- | --- |
| `LIKE '%abc'`, `LIKE '%abc%'` | B-Tree sorts by string prefix; without a known prefix the range cannot be determined | Full-text or trigram index; suffix search: index on `reverse(col)` |
| `LIKE 'abc%'` | Can use B-Tree depending on collation | Check the DBMS's collation/operator class conditions |
| Function or arithmetic on the column: `DATE(created_at) = ?`, `col + 1 = ?`, `lower(email) = ?` | Index stores raw values, not function results | Rewrite as range `created_at >= ? AND created_at < ?`; move arithmetic to the constant side; or expression index (§2.1 item 6) |
| `!=`, `<>`, `NOT IN` | Usually matches most of the table, so full scan is cheaper | Invert to positive condition (`status IN (…)`); partial index if the target subset is small |
| `OR` across columns (`a = ? OR b = ?`) | One composite index cannot serve both branches | Separate index per column (optimizer merges results) or split into `UNION ALL`; verify with EXPLAIN |
| Implicit casts: string column vs number, differing collation or charset in joins | DB must convert the column value per row | Correctly typed parameters; FK of same type, charset and collation |
| `IS NULL` | Common B-Trees can use the index | No need to avoid; mostly-NULL columns see §2.1 item 4 |

## 3. Query patterns

| Problem | Handling |
| --- | --- |
| Large `OFFSET` pagination (lists always have `LIMIT`) | Keyset: `WHERE (created_at, id) < (?, ?) ORDER BY created_at DESC, id DESC LIMIT n`; if the optimizer does not use the index for row-value comparison, split as `created_at < ? OR (created_at = ? AND id < ?)` |
| N+1 | Join, or batch load `WHERE id IN (…)`; detect by counting queries per request in tests or logs |
| Scalar subquery in `SELECT` (re-run per row) | Rewrite with `JOIN` (plus `GROUP BY` if needed) or `LATERAL` if available; the optimizer does not always decorrelate automatically, verify with EXPLAIN |
| Existence check | `EXISTS (SELECT 1 …)` stops at the first match; do not use `COUNT(*) > 0`. With `IN (subquery)`, modern DBMSs usually convert to semi-join so performance is equivalent; the significant difference is `NOT IN`: a subquery with NULL returns empty, always use `NOT EXISTS` |
| Filtering with `HAVING` on non-aggregate conditions | Move to `WHERE` to eliminate rows before grouping; `HAVING` only for conditions on aggregate results (`HAVING SUM(x) > ?`) |
| Joining large tables then filtering | Put each table's filter in `WHERE`/`ON` to shrink sets before joining; join columns indexed and same type |
| `UNION` when branches do not overlap or duplicates are acceptable | `UNION ALL`: no sort/hash cost for deduplication |
| `DISTINCT` to fix row-multiplying joins | Fix the join condition or use `EXISTS` instead of join then `DISTINCT` |
| Frequent full-table counts | Separately maintained counter, estimate from DBMS stats, or accept approximation |
| Reports/statistics scanning large tables on every call | Summary table updated in batches or by events, materialized view if available; record refresh frequency and acceptable data staleness (tier 3 in §6) |
| Row-by-row writes in a loop | Batch insert/update (multi-row `INSERT`, DBMS bulk load command); moderate batches to avoid holding locks long |
| Unbounded queries | Set statement timeout and idle-in-transaction timeout |

**Denormalization to reduce joins** (storing a redundant column from another table, summary tables) is tier 3 in §6: do it only when APs and metrics prove the join is the bottleneck; record the data's source of truth and how copies sync (same transaction, trigger, job, event).

**Stored procedures, functions, triggers** are not a default speed-up (`database-rules` 14). Prepared statements at the driver layer give most of the "precompiled" benefit; the real gain is fewer round trips for multi-step work over many rows.

## 4. Verification and monitoring

Verify key APs with execution plans on fake data with near-real size and distribution. Small tables always get full scans, so they prove nothing. After loading large data, update statistics before measuring.

Reading execution plans:

- Record the index name used. **Needs review:** full scan of a large table with a selective condition; full index scan; sort or temp table (especially spilling to disk); many rows filtered out.
- **Misestimate:** estimated rows far from actual due to stale stats or column correlation; update statistics, add extended statistics or histograms.

Monitor continuously in environments with real load using the DBMS's query statistics and slow query log. Prioritize optimization by total time (frequency × latency), not only the slowest query. Specific commands and indicators: §6 of the DBMS file.

## 5. Concurrency and transactions

- Optimistic locking (`version` column, `UPDATE … WHERE id = ? AND version = ?`) for rare conflicts; pessimistic locking (`SELECT … FOR UPDATE`) for hot spots needing serialization.
- Job queues in a table: `FOR UPDATE SKIP LOCKED` if supported.
- Avoid deadlocks: lock in a fixed order (e.g. ascending `id`).
- Know the default isolation level of the chosen DBMS. If business logic needs stricter, state it and handle serialization errors with retry.
- Hot counter updates: `UPDATE … SET qty = qty - ? WHERE id = ? AND qty >= ?` instead of read-then-write.
- **Connections:** more connections are not faster; beyond CPU cores and I/O capacity contention grows. Under heavy load consider a connection pooler in front of the DB. Record pool size and `max_connections` in environment configuration, derived from the instance count (`database-rules` 13), not guessed.

## 6. Scaling tiers

Go top-down; move to the next tier only when the previous is insufficient and backed by metrics. Tier 4 onward requires an ADR.

| Tier | Measure | Trigger | Cost / consequence |
| --- | --- | --- | --- |
| 1 | Fix queries, add/remove indexes, update statistics, DB configuration (cache memory, sort memory), connection pool | Specific slow queries | Low |
| 2 | Application cache; read replica | Reads dominate, sync lag acceptable | Stale data on replica; read/write routing |
| 3 | Controlled denormalization; summary tables; materialized views | Expensive, repeated reports/aggregations | Syncing derived data |
| 4 | Partition | Very large table by time or a clear key; need bulk delete/archive; queries always filter by partition key | Constraints on PK/UNIQUE, FK, partition operations |
| 5 | Archive old data to a separate table/store | Hot data is only a small part | Slower history queries, archiving procedure |
| 6 | Split DB by module / move OLAP to an analytics store | Fundamentally different workloads, clear module boundaries | Lose cross joins and transactions; need data sync (CDC, events) |
| 7 | Sharding | One server cannot handle writes or capacity even after the tiers above | Very high: cross-shard queries, distributed transactions, rebalancing |

## 7. Partition

- **Types:** RANGE (time, most common), LIST (region, large tenant), HASH (even distribution when no natural key).
- **Partition key** is a column present in most queries to enable partition pruning; verify with EXPLAIN.
- **Constraint consequences:**
  - PK and UNIQUE usually must include the partition key.
  - FK support with partitioned tables differs between DBMSs, some do not support it: check §7 of the DBMS file before choosing.
- **Operations:** create partitions ahead of time (scheduled job or partition management tool), a default partition catches stray data, delete/archive via DETACH/DROP partition instead of DELETE.
- **Size:** do not split too finely; thousands of partitions slow query planning.
- Partitioning does not replace indexes; each partition still needs indexes for APs.

## 8. Sharding

Propose only when metrics prove tiers 1–6 are insufficient. The ADR must answer:

- **Shard key:** a column in nearly every query and transaction (usually `tenant_id` or `customer_id`), evenly distributed, not changing over time.
- **Routing strategy:** hash, range, or directory table; how to add shards and rebalance.
- **Shared data** (catalogs, configuration): replicated to every shard or a separate DB.
- **Cross-shard queries and transactions:** eliminated by design, or accept saga / application-level aggregation.
- **Identifiers:** generate globally unique IDs (UUIDv7, Snowflake), not relying on per-shard auto-increment.
- **Tooling:** the DBMS's sharding solution (§7 of the DBMS file) or application-level routing; operations, backup, restore cost.
- **Rejected alternatives** and reasons.
