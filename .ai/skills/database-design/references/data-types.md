# Database Design – Choosing data types

> Types fixed in database-design §2 take priority. Concrete type names: the chosen DBMS file (§2). Check the DBMS version before using a type.

## 1. Lookup table by data kind

| Data | Choose | Avoid |
| --- | --- | --- |
| Numeric surrogate key | 64-bit auto-increment integer | 32-bit integer for transaction tables (easily exhausted) |
| UUID key | Time-ordered UUID (v7), stored as native UUID type or 16-byte binary | Random UUID (v4) on systems with PK-clustered index: index fragmentation, slow writes |
| Money | Exact decimal (19,4) or integer in smallest unit | Floating point; locale-dependent money type |
| Exact quantities, ratios | Decimal `(p,s)` per business needs | |
| Scientific measurements, approximate coordinates | Double-precision floating point | Using it where error is unacceptable |
| Instant (event that happened) | Timestamp with time zone, or UTC by application convention | Types limited to year 2038 or auto-converted by session time zone |
| Date (birthday, effective date) | Date type | Storing dates as timestamps |
| Local time, future appointments | Local time + IANA time zone column | Converting to UTC early |
| Time range | Range type if available; otherwise two columns `start`, `end` + CHECK `start < end` | |
| Short text with business limit | Variable-length string, limit `n` with justification | `255` by habit |
| Long text | Long text type | Full-column index (usually needs prefix or full-text) |
| Character set | Full UTF-8 (4 bytes/char) at DB/table level | 3-byte UTF-8 variant (missing emoji, some characters); `NCHAR`/`NVARCHAR` |
| Case-insensitive comparison | Case-insensitive collation/type, or index on normalized form | Email: UNIQUE on non-normalized form |
| Boolean | Boolean type | Flag with more than two states: use a status column |
| Fixed value set | String + CHECK (see modeling-patterns §2) | `ENUM` when values may change or be reordered |
| JSON | JSON type (binary if available) for semi-structured attributes | Frequently queried JSON keys: move to real columns |
| IP address | Native IP type if available; otherwise 16-byte binary | String |
| Binary data, files | Object storage path/key + checksum | Storing files in the DB; binary only for small data (keys, signatures) |
| Password | String holding a hash (argon2id/bcrypt) | Plain or reversibly encrypted password |
| Column-level encrypted data | Binary, plus key version column if keys rotate | |
| Phone number, postal code, account number | String | Numeric type: loses leading zeros, not a computed quantity |
| Geographic coordinates | Spatial type SRID 4326 + spatial index | Needs extension/engine: record ADR |

## 2. Selection rules

1. **By business meaning, not sample data.** "Order code consists of digits" is still text if not used for computation.
2. **Smallest sufficient with growth headroom.** Estimate the max value over many years; transaction PKs use 64 bits.
3. **FK type matches the referenced PK type**, including sign, charset and collation.
4. **NOT NULL by default**, DEFAULT only when the default has business meaning.
5. **Do not store formatted values** (money with separators, dates as strings).
6. **State the unit** in the column name when not obvious (`weight_grams`, `duration_seconds`).
7. **Generated columns** for derived values needing an index or constraint; do not store derived values manually.
8. **Fixed-length strings only for truly fixed values** (ISO country code, currency code): fixed types pad with spaces, waste space, compare unpredictably.
9. **Smaller types give smaller indexes**, especially when the PK is in every secondary index (clustered index); but do not trade away growth capacity (rule 2).
