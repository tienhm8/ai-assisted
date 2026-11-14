# Database Design – PostgreSQL

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

## 4. Queries

- Keyset: row-value comparison `(created_at, id) < (?, ?)` can use the index.
- Correlated subqueries: rewrite with `JOIN` or `LATERAL`.
- Estimated count: `pg_class.reltuples`.
- Materialized view: `REFRESH MATERIALIZED VIEW CONCURRENTLY` (needs a UNIQUE index on the view).
- Bulk load: `COPY`.
- Timeouts: `statement_timeout`, `idle_in_transaction_session_timeout`.
- PL/pgSQL caches statement plans only per session.

## 5. Concurrency and connections

- Default isolation READ COMMITTED; `REPEATABLE READ`/`SERIALIZABLE` need retry on serialization errors.
- Queue in a table: `FOR UPDATE SKIP LOCKED`.
- Heavy load: PgBouncer. Transaction mode does not keep prepared statements (old drivers), session variables, advisory locks across transactions.

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

## 7. Partition and sharding

- Declarative partitioning: PK and UNIQUE must include the partition key; FKs referencing partitioned tables allowed from PG 12.
- Create partitions ahead of time: scheduled job or `pg_partman`; bulk delete via `DETACH PARTITION`/`DROP`.
- Sharding: Citus.

## 8. Migration

- DDL runs in transactions: wrap each migration in a transaction, except commands that cannot run in a transaction (`CREATE INDEX CONCURRENTLY`).
- Lock wait limit: `SET lock_timeout = '5s'`.

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

## 10. Security

- In-DB encryption with `pgcrypto` puts keys into statements: avoid, encrypt in the application.
- Revoke `CREATE` on schema `public` (default since PG 15).
- Row-Level Security: `ENABLE` + `FORCE ROW LEVEL SECURITY`, policy based on `current_setting('app.tenant_id')`; the App account has no `BYPASSRLS` and is not the table owner.
- Dynamic SQL: `format()` with `%I`, `%L` or `EXECUTE … USING`.
- `SECURITY DEFINER`: set a fixed `search_path` in the function definition.
