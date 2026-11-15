# Database Design – PostgreSQL

> Nguồn: github.com/supabase/agent-skills, skill `supabase-postgres-best-practices` v1.1.1 @ c9be0e9 · Ngày lấy: 2026-11-15 · Áp dụng cho: PostgreSQL 13–18 (đối chiếu tài liệu postgresql.org bản 18.7; dự án chưa chốt phiên bản ở system-architecture §4, rà lại khi chốt)
> Đã điều chỉnh: chỉ lấy điểm riêng PostgreSQL mà AI hay sai và chưa có trong file này: GIN cho `jsonb`/full-text, partial index với tham số, upsert `ON CONFLICT`, advisory lock, `idle_session_timeout`, `work_mem`, `pg_stat_statements`, autovacuum theo bảng, lỗi `ADD CONSTRAINT IF NOT EXISTS`, identifier có ngoặc kép, quyền `EXECUTE` mặc định, `ALTER DEFAULT PRIVILEGES`, hiệu năng RLS. Bỏ: phần riêng Supabase (`auth.uid()`, role `anon`/`authenticated`, dashboard, cổng pooler); kiến thức chung đã có ở file chủ đề hoặc Rule (index cột WHERE/JOIN/FK, composite, covering, N+1, keyset, batch insert, transaction ngắn, thứ tự lock, SKIP LOCKED, pooling, least privilege, partition); con số và ngưỡng cấu hình (công thức `max_connections`, `pool_size`, "> 100M dòng") vì ngưỡng lấy từ NFR và đo thực tế; khuyến nghị lỗi thời (`uuid_generate_v7()` của extension `pg_uuidv7`, nay có `uuidv7()` từ PG 18); `hashtext()` làm khoá advisory (hàm nội bộ, không có trong tài liệu). Sửa: `idle_session_timeout` không bật cho kết nối qua pooler (tài liệu PostgreSQL cảnh báo). Không lấy code minh hoạ.

> Reference for Skill `database-design`. Load only when the chosen DBMS is PostgreSQL, and only the section for the current step. Principles live in the topic file; this file states only PostgreSQL-specific syntax, limits and versions. Always check the project's version.

## 1. Key characteristics

| Topic | PostgreSQL |
| --- | --- |
| DDL in transactions | Yes, DDL can be rolled back |
| Partial index | Yes |
| CHECK | Always enforced |
| SQL mode | Strict, does not silently truncate strings or coerce invalid values |
| Clustered index | No (heap tables) |
| FK index | Not created automatically |
| String comparison | Case-sensitive by default |
| Index key length | Large |
| Default isolation level | READ COMMITTED |
| Connections | One process per connection |

## 2. Data types

| Data | Type |
| --- | --- |
| Numeric surrogate key | `bigint GENERATED ALWAYS AS IDENTITY` |
| UUID key | `uuid`; generate UUIDv7 in the application or `uuidv7()` from PG 18 |
| Money | `numeric(19,4)` or `bigint` in smallest unit; do not use `money` (locale-dependent), `real`, `double precision` |
| Exact quantities, ratios | `numeric(p,s)` |
| Approximate measurements | `double precision` |
| Point in time | `timestamptz` |
| Date / time of day | `date` / `time` + IANA time zone column |
| Duration | `interval`; date-time ranges: `tstzrange`, `daterange` |
| Bounded short text | `text` + CHECK `char_length(x) <= n`, or `varchar(n)` |
| Long text | `text` |
| Encoding | UTF-8 (DB default) |
| Case-insensitive | `citext` or index on `lower(x)` |
| Boolean | `boolean` |
| Fixed value set | `text` + CHECK, preferred over `ENUM` |
| JSON | `jsonb` |
| IP address | `inet` |
| Small binary, encrypted columns | `bytea` |
| Password (hash) | `text` |
| Geographic coordinates | PostGIS `geography(Point, 4326)` (extension: record ADR) |

`char(n)`: PostgreSQL docs recommend against it. There is no `NCHAR`/`NVARCHAR` type.

## 3. Indexes

- **Partial index** `WHERE …`: for the rare part of a skewed column, for sparse columns (`WHERE col IS NOT NULL`).
- **HOT update** is lost when an indexed column changes: avoid indexing constantly updated columns with no AP.
- **Covering:** `INCLUDE (…)`; plan shows `Index Only Scan`.
- **Expression index:** `CREATE INDEX … ON t (lower(email))`.
- **FK columns** must be indexed manually so joins and parent deletes do not scan the child table.
- **Redundant indexes:** `pg_stat_user_indexes.idx_scan`. No way to hide an index; drop via a migration with rollback.
- **Specialized types:** GIN for `jsonb`, arrays, full-text (`tsvector`), trigram (`pg_trgm`); GiST for ranges, geometry, exclusion; BRIN for very large time-ordered insert tables.
- **Non-write-blocking creation:** `CREATE INDEX CONCURRENTLY`; does not run in a transaction; mid-way failure leaves an `INVALID` index that must be dropped.
- **Skip scan:** from PG 18.
- **`LIKE 'abc%'`:** uses B-Tree only with collation `C` or an index created with `text_pattern_ops`/`varchar_pattern_ops`.
- **`OR` across columns:** BitmapOr over separate indexes.
- **Sort not served by index:** `Sort` node in the plan.
- **`jsonb`:** default GIN (`jsonb_ops`) serves `@>`, `?`, `?|`, `?&`, `@?`, `@@` applied to the indexed column itself; `col->>'k' = ?` does not use it: rewrite as `col @> '{"k": …}'` or add a B-Tree expression index on `(col->>'k')`. `jsonb_path_ops`: much smaller, only `@>`, `@?`, `@@`, no key-exists.
- **Full-text:** expression index must use the 2-argument `to_tsvector('config', …)` and queries must repeat the same config; or a stored generated `tsvector` column with GIN.
- **Partial index with parameters:** matched at plan time, the query `WHERE` must imply the predicate; `x < $1` never matches `WHERE x < 2`. Write the predicate literally in the query (`AND deleted_at IS NULL`).

## 4. Queries

- Keyset: row-value comparison `(created_at, id) < (?, ?)` can use the index.
- Correlated subqueries: rewrite with `JOIN` or `LATERAL`.
- Estimated count: `pg_class.reltuples`.
- Materialized view: `REFRESH MATERIALIZED VIEW CONCURRENTLY` (needs a UNIQUE index on the view).
- Bulk load: `COPY`.
- Timeouts: `statement_timeout`, `idle_in_transaction_session_timeout`.
- PL/pgSQL caches statement plans only per session.
- Insert-or-update: `INSERT … ON CONFLICT (cols) DO UPDATE SET c = EXCLUDED.c`, not select-then-insert. Conflict target must match a unique index/constraint exactly (partial unique index: add its `WHERE`), or `ON CONSTRAINT name`; `DO UPDATE` requires a target. `RETURNING` omits rows skipped by `DO NOTHING`. Duplicate keys in one statement raise a cardinality error: dedupe input first.
- Variable-length ID list: `= ANY($1::bigint[])` with one array parameter instead of building `IN ($1, …, $n)`.

## 5. Concurrency and connections

- Default isolation READ COMMITTED; `REPEATABLE READ`/`SERIALIZABLE` need retry on serialization errors.
- Queue in a table: `FOR UPDATE SKIP LOCKED`.
- Heavy load: PgBouncer. Transaction mode does not keep prepared statements (old drivers), session variables, advisory locks across transactions.
- Advisory lock: prefer `pg_advisory_xact_lock`/`pg_try_advisory_xact_lock` (released at commit/rollback). Session-level `pg_advisory_lock` survives `ROLLBACK`, stacks per call and needs a matching unlock. Key is one `bigint` or two `integer`; the two key spaces do not overlap.
- `idle_session_timeout` (PG ≥ 14) closes idle sessions outside transactions; avoid it on pooled connections (the pool does not expect the close), set it per role for interactive users.

## 6. Verification and monitoring

| | PostgreSQL |
| --- | --- |
| Update statistics | `ANALYZE`; column correlation: `CREATE STATISTICS` |
| Command | `EXPLAIN (ANALYZE, BUFFERS)`; actually executes the statement, wrap writes in `BEGIN … ROLLBACK` |
| Good | `Index Scan`, `Index Only Scan`, `Bitmap Index Scan` on large tables |
| Needs review | `Seq Scan` on a large table with a selective condition; `Sort`/`Hash` spilling to disk (`external merge`, `Batches > 1`); large `Rows Removed by Filter` |
| Index in use | Name in the `Index Scan using …` node |
| Misestimate | Estimated `rows` far from `actual rows` |
| Monitoring | `pg_stat_statements`, `auto_explain`, `log_min_duration_statement`; bloat and autovacuum on heavily updated tables |
| Tier 1 config | `shared_buffers`, `work_mem` |
| `work_mem` | Per sort/hash node, per parallel worker, per session: one query can use it many times. Hash nodes may use `work_mem × hash_mem_multiplier` (default 2.0 from PG 15) |
| `pg_stat_statements` | Needs `shared_preload_libraries` + restart, then `CREATE EXTENSION`; columns `total_exec_time`, `mean_exec_time` from PG 13 (`total_time`, `mean_time` before) |
| Autovacuum | Defaults trigger at 20 % dead rows (vacuum) / 10 % changed (analyze); hot tables: `ALTER TABLE … SET (autovacuum_vacuum_scale_factor = …)`; check `pg_stat_user_tables.n_dead_tup`, `last_autovacuum`, `last_autoanalyze` |
| Locks | `pg_stat_database.deadlocks`; `log_lock_waits` (default off) logs waits longer than `deadlock_timeout` |

## 7. Partition and sharding

- Declarative partitioning: PK and UNIQUE must include the partition key; FKs referencing partitioned tables allowed from PG 12.
- Create partitions ahead of time: scheduled job or `pg_partman`; bulk delete via `DETACH PARTITION`/`DROP`.
- Sharding: Citus.

## 8. Migration

- DDL runs in transactions: wrap each migration in a transaction, except commands that cannot run in a transaction (`CREATE INDEX CONCURRENTLY`).
- Lock wait limit: `SET lock_timeout = '5s'`.
- No `ADD CONSTRAINT IF NOT EXISTS` (syntax error); rerunnable form checks `pg_constraint` in a `DO` block. `ADD COLUMN IF NOT EXISTS`, `DROP CONSTRAINT IF EXISTS` exist. `CREATE INDEX IF NOT EXISTS` checks only the name, not the definition.

| Operation | Lock level / approach |
| --- | --- |
| Add NULL / constant DEFAULT column | Fast (PG ≥ 11 does not rewrite the table) |
| Add volatile DEFAULT column | Rewrites the whole table |
| Change column type | Usually rewrites table + exclusive lock |
| Set NOT NULL | CHECK `NOT VALID` → `VALIDATE CONSTRAINT` → `SET NOT NULL` |
| Add FK | `NOT VALID` then `VALIDATE CONSTRAINT` |
| Add index | `CREATE INDEX CONCURRENTLY` |
| Add UNIQUE | Unique index `CONCURRENTLY` then `ADD CONSTRAINT … USING INDEX` |

## 9. Modeling patterns

- Fixed value set: `text` + CHECK; `ENUM` can add values but removing or reordering is hard.
- Trees: recursive CTE; materialized path uses `ltree`.
- Preventing overlapping validity ranges: exclusion constraint with `btree_gist` + `tstzrange`.
- Past states of a table: no temporal tables; use history table + trigger.
- UNIQUE ignoring soft-deleted rows: partial unique index `WHERE deleted_at IS NULL`.
- Identifiers: unquoted names fold to lowercase; a quoted mixed-case name (`"userId"`, often generated by ORMs) must be quoted in every raw query, tool and view. Names follow the project's DB naming convention.

## 10. Security

- In-DB encryption with `pgcrypto` puts keys into statements: avoid, encrypt in the application.
- Revoke `CREATE` on schema `public` (default since PG 15).
- Row-Level Security: `ENABLE` + `FORCE ROW LEVEL SECURITY`, policy based on `current_setting('app.tenant_id')`; the App account has no `BYPASSRLS` and is not the table owner.
- Dynamic SQL: `format()` with `%I`, `%L` or `EXECUTE … USING`.
- `SECURITY DEFINER`: set a fixed `search_path` in the function definition.
- `SECURITY DEFINER` `search_path`: list `pg_temp` last. New functions grant `EXECUTE` to `PUBLIC` by default: `REVOKE ALL ON FUNCTION … FROM PUBLIC` in the same transaction as `CREATE FUNCTION`, then grant selectively.
- `ALTER DEFAULT PRIVILEGES` affects only objects created later by the role named in `FOR ROLE` (default: current role), never existing objects: run it for the Migrator role so the App account gets grants on tables created by later migrations.
- RLS performance: the policy expression runs per row; wrap row-independent calls in a subquery (`tenant_id = (SELECT current_setting('app.tenant_id')::bigint)`) so it runs once as an InitPlan; index the policy columns. UNIQUE/PK/FK checks bypass RLS, so constraint errors can reveal other tenants' rows.
