# Database Design – MySQL and MariaDB

> Principles are in the topic files; this file has only syntax, limits and versions. The two systems differ: check the exact system and version.

## 1. Key characteristics

| Topic | MySQL / MariaDB (InnoDB) |
| --- | --- |
| DDL in transactions | No; each DDL auto-commits, a migration failing midway leaves a partial state |
| Partial index | No; use generated columns |
| CHECK | Enforced only from MySQL 8.0.16, MariaDB 10.2 |
| SQL mode | Needs `STRICT_TRANS_TABLES` (or equivalent) to avoid silently truncating strings and coercing invalid values |
| Clustered index | By PK: random or wide PKs slow writes and bloat every secondary index (PK is in every secondary index) |
| FK index | Created automatically if missing |
| String comparison | By collation, usually case-insensitive |
| Index key length | Byte limit (3072 with row format DYNAMIC); `utf8mb4` counts 4 bytes/char |
| Default isolation level | REPEATABLE READ, with gap locks |

## 2. Data types

| Data | Type |
| --- | --- |
| Numeric surrogate key | `BIGINT UNSIGNED AUTO_INCREMENT` |
| UUID key | MariaDB ≥ 10.7: `UUID`; MySQL: `BINARY(16)` + `UUID_TO_BIN(…, 1)` |
| Money | `DECIMAL(19,4)` or `BIGINT` in smallest unit; do not use `FLOAT`/`DOUBLE` |
| Exact quantities, ratios | `DECIMAL(p,s)` |
| Approximate measurements | `DOUBLE` |
| Point in time | `DATETIME(6)` stored as UTC (application convention). `TIMESTAMP` is limited to 2038 and converts by session time zone |
| Date / time of day | `DATE` / `TIME` + time zone column |
| Duration / range | No range type: two columns `start`, `end` + CHECK `start < end` |
| Bounded short text | `VARCHAR(n)` |
| Long text | `TEXT`/`MEDIUMTEXT`; older versions disallow DEFAULT, indexing needs a prefix length |
| Encoding | `utf8mb4` + suitable collation (`utf8mb4_0900_ai_ci`, `utf8mb4_unicode_520_ci`, `uca1400` in newer MariaDB); do not use `utf8`/`utf8mb3` |
| Case-insensitive | `_ci` collation |
| Fixed value set | `VARCHAR` + CHECK; `ENUM` stores by index, reordering values breaks sorting |
| JSON | MySQL `JSON`; MariaDB `JSON` is `LONGTEXT` + CHECK `JSON_VALID` |
| IP address | MariaDB `INET4`/`INET6`; MySQL `VARBINARY(16)` |
| Small binary, encrypted columns | `VARBINARY`/`BLOB` |
| Geographic coordinates | `POINT SRID 4326` + `SPATIAL` index |

`NVARCHAR` is treated as `VARCHAR` with charset `utf8mb3`: do not use. FKs must match the PK type exactly, including `UNSIGNED`, charset and collation.

## 3. Indexes

- **No partial index:** for skewed columns use a composite with the selective column after; for sparse columns use a normal index (NULLs are still stored).
- **Covering:** secondary indexes already contain the PK; plan shows `Using index` in `Extra`.
- **Expression index:** MySQL ≥ 8.0.13 functional index; MariaDB uses an indexed generated column.
- **Redundant indexes:** MySQL `sys.schema_unused_indexes`; MariaDB enable `userstat` then view `INFORMATION_SCHEMA.INDEX_STATISTICS`. Disable first before dropping: MySQL ≥ 8.0 `INVISIBLE`, MariaDB ≥ 10.6 `IGNORED`.
- **Non-write-blocking creation:** `ALGORITHM=INPLACE, LOCK=NONE`.
- **`LIKE 'abc%'`:** can use B-Tree with the column's collation.
- **`OR` across columns:** index merge over separate indexes.

## 4. Queries

- Keyset: if the optimizer does not use the index for row-value comparison, split as `created_at < ? OR (created_at = ? AND id < ?)`.
- Estimated count: `information_schema.TABLES.TABLE_ROWS`.
- No materialized views: use summary tables.
- Bulk load: `LOAD DATA`.
- Timeouts: MariaDB `max_statement_time`; MySQL `max_execution_time` (SELECT only).

## 5. Concurrency and connections

- REPEATABLE READ has gap locks: locks the gaps between keys too, easily causing waits or deadlocks on concurrent inserts.
- Queue in a table: `FOR UPDATE SKIP LOCKED` (MySQL ≥ 8.0, MariaDB ≥ 10.6).

## 6. Verification and monitoring

| | MySQL / MariaDB |
| --- | --- |
| Update statistics | `ANALYZE TABLE`; histograms: MariaDB ≥ 10.4 `ANALYZE TABLE … PERSISTENT FOR …`, MySQL 8.0 `ANALYZE TABLE … UPDATE HISTOGRAM` |
| Command | `EXPLAIN`; actual figures: MariaDB `ANALYZE FORMAT=JSON`, MySQL ≥ 8.0.18 `EXPLAIN ANALYZE` |
| Needs review | `type = ALL` (full table scan); `type = index` (full index scan); `Extra`: `Using filesort`, `Using temporary` |
| Index in use | `key` column (`possible_keys` are only candidates); `rows`/`filtered` far from actual means a misestimate |
| Monitoring | Slow query log (`long_query_time`), `performance_schema` |
| Tier 1 config | `innodb_buffer_pool_size` |

## 7. Partition and sharding

- Every UNIQUE (including PK) must include the partition key.
- **Partitioned InnoDB tables do not support FKs**, neither referencing nor referenced.
- Sharding: Vitess (MySQL), Spider (MariaDB).

## 8. Migration

- DDL auto-commits: one DDL per migration, or make it rerunnable (`IF NOT EXISTS`, pre-checks).
- Lock wait limit: `SET SESSION lock_wait_timeout = 5`.

| Operation | Lock level / approach |
| --- | --- |
| Add NULL / constant DEFAULT column | MySQL ≥ 8.0 `ALGORITHM=INSTANT`; MariaDB ≥ 10.3 instant ADD COLUMN |
| Add volatile DEFAULT column | Rewrites the table |
| Change column type | `ALGORITHM=COPY`, blocks writes; large tables use online tools (gh-ost, pt-online-schema-change) |
| Set NOT NULL | Rewrites the table |
| Add FK | Locks the child table during validation |
| Add index | `ALGORITHM=INPLACE, LOCK=NONE` |
| Add UNIQUE | INPLACE; duplicate data fails the migration, check first |

## 9. Modeling patterns

- Fixed value set: `VARCHAR` + CHECK (CHECK enforced only from MySQL 8.0.16, MariaDB 10.2); `ENUM` stores by index, reordering breaks sorting.
- Trees: recursive CTE from MySQL 8.0, MariaDB 10.2.
- Preventing overlapping validity ranges: no exclusion constraint; check in the application within a locking transaction.
- Past states of a table: MariaDB `WITH SYSTEM VERSIONING`; MySQL uses history table + trigger.
- UNIQUE ignoring soft-deleted rows: generated column that is NULL when `deleted_at` is not NULL, UNIQUE on that column.

## 10. Security

- Whole-DB encryption: MariaDB data-at-rest encryption, MySQL InnoDB tablespace encryption.
- Encryption with `AES_ENCRYPT` puts keys into statements: avoid, encrypt in the application.
- No Row-Level Security: tenant filtering is mandatory in the shared data access layer, with cross-tenant access tests.
