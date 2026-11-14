# Database Design – MongoDB

> Reference for Skill `database-design`, used when the chosen DBMS is MongoDB. Replaces the relational parts of steps 4–5, 7, 9–10; steps 1–3, 6, 8, 11 stay unchanged. MongoDB version, migration tool, driver/ODM follow the project; for features with a stated minimum version, check the version in use before applying.

Term mapping for database-design.md: table → collection, row → document, column → field, FK → reference (`_id` of another document), CHECK/NOT NULL → schema validation.

## 1. Modeling principles

Relational: normalize first, optimize later. MongoDB is the reverse: **design by access pattern**. Data read together is stored together. So the `AP-NN` table (step 2) must exist before drawing documents. No AP, no design.

For each relationship in the ERD, choose embed or reference:

| Relationship | Default | Switch to reference when |
| --- | --- | --- |
| 1-1 | Embed in parent | Child part is large, rarely read with parent, or has different access rights |
| 1-few (tens of elements, clearly bounded) | Embed array | Child is read/modified independently or shared by many parents |
| 1-many (hundreds to thousands) | `_id` array in parent, or `parent_id` in child | No upper bound → `parent_id` in child |
| 1-very many (unbounded: logs, events, comments) | `parent_id` in child, indexed | — |
| n-n | `_id` array on the side with fewer elements | Relationship needs attributes → separate link collection |

Decision questions per relationship; answer from APs, do not guess:

1. Is child data always read with the parent?
2. What is the max number of child elements? Is there a business limit?
3. Is the child modified independently, frequently, or by many concurrent processes?
4. Is the child queried on its own (not via the parent)?
5. Must the embedded copy sync when the source changes, or is it a snapshot at transaction time?

Record the choice and reason in the design decision table (Report section item 5 of Skill `database-design`).

## 2. Recommended modeling patterns

| Pattern | Use when | Note |
| --- | --- | --- |
| Extended reference | AP reading the parent needs a few fields of another document (customer name on order) | Copy only rarely-changing fields; record the source of truth and sync method, or state explicitly that it is a snapshot |
| Subset | Parent needs the N newest child elements (10 latest reviews) | Rest in a separate collection; cap the array with `$push` + `$slice` |
| Computed | High-frequency AP reads totals/counts | Update in the same write with `$inc`; have a reconciliation job |
| Bucket | Time-based data, write-heavy, read by range | MongoDB ≥ 5.0: use time series collection before hand-rolling buckets |
| Outlier | Most documents small, a few have very large arrays | `has_overflow` flag + side collection for overflow |
| Polymorphic | One collection holds several variants queried together | Discriminator field (`type`) required; per-variant validator via `oneOf` |
| Schema versioning | Any collection whose structure may change | `schema_version` field in every document (§6) |

## 3. Anti-patterns

| Anti-pattern | Consequence | Replacement |
| --- | --- | --- |
| Unbounded growing array | Hits the 16 MB per-document limit; multikey index bloats; every write rewrites a large document | Reference from child to parent; subset or bucket pattern |
| Splitting always-read-together data into many collections then `$lookup` in high-frequency APs | Loses document advantage, slower than relational join | Embed or extended reference |
| Embedding data modified from many places (customer info embedded in every order, synced on change) | Wide-spread updates, data drift | Reference; embed only snapshots or near-immutable fields |
| Bloated document (many rarely used fields) | Wastes cache (working set), slow reads | Move rarely used parts to another collection |
| One collection per tenant/day/user | Large numbers of collections and indexes waste resources, hard to operate | One collection + indexed discriminator field |
| Dynamic field names (value as key: `{"2026-11-11": 5}`) | Cannot be indexed or validated | `{ k, v }` array (attribute pattern) with `(k, v)` index |
| No schema validation | Wrong-typed data and missing fields slip in, surfacing only on read | `$jsonSchema` validator for every collection (§4) |

## 4. Data types and schema validation

| Data | BSON type | Do not use |
| --- | --- | --- |
| Money, quantities needing exactness | `Decimal128`, or `long` in smallest unit when single currency | `double` |
| Point in time | `Date` (always UTC); store display time zone separately if business needs it | Date-time string |
| Identifier | `ObjectId` by default; UUID stored as `Binary` subtype 4, not string | Self-managed auto-increment numbers (need a counter, write bottleneck) unless business requires |
| User-facing business code | `string` + unique index, separate from `_id` | Business code as `_id` when its format may change |
| Status, enum | `string` + `enum` in validator | Magic numbers |
| Reference | Same type as target `_id` (`ObjectId` with `ObjectId`) | Mixed types: comparing `string` to `ObjectId` does not match and cannot use the index |

Every collection has a `$jsonSchema` validator declared via migration: `required`, `bsonType`, `enum`, `minimum`, `maxItems` for embedded arrays, `additionalProperties: false` once structure is stable. Default `validationLevel: "strict"`, `validationAction: "error"`. Use `moderate`/`warn` only temporarily during schema transition (§6) and record the removal deadline.

Validators cannot replace cross-document constraints. Map each BR to one of:

| BR | How to enforce in MongoDB |
| --- | --- |
| Uniqueness | Unique index (scoped unique: compound including scope fields; account for soft delete with partial index) |
| Required fields, value domain, relations between fields in one document | Validator (`$jsonSchema`, or query expression in validator) |
| Reference exists, no deleting parent while children exist | No FK: check in application within a transaction, or block hard delete (soft delete only); state the handling and the reconciliation job |
| Invariant across documents | Merge into one document if possible (single-document write is atomic); otherwise multi-document transaction |

## 5. Indexes and queries

### 5.1 Indexes

1. Each index serves at least one AP; note the AP next to the index. `_id` is indexed by default.
2. **ESR rule** for compound indexes: Equality fields → Sort fields → Range fields. Index `(a, b, c)` serves prefixes `a`, `a,b`, `a,b,c`.
3. Index sort direction must match, or be fully reversed from, the AP's `sort` to avoid an in-memory `SORT` stage.
4. Index types to know:
   - Unique; partial (`partialFilterExpression`), often for unique ignoring soft-deleted documents.
   - TTL for self-expiring data (sessions, OTP, short-lived logs). TTL deletes on a background cycle, not to the second.
   - Multikey (array fields): a compound index may have at most one array field.
   - Wildcard only for the attribute pattern when field names are unknown in advance.
   - Text index or a separate search service for full-text search.
5. Index with collation for case-insensitive queries; queries must use that same collation.
6. Check redundant indexes with `$indexStats`. Before dropping an index in production, hide it first with `hideIndex` (≥ 4.4), monitor, then drop.
7. Index builds on large collections run in the background but still cost I/O and replicate: run off-peak, monitor replication lag. Unique index fails midway on duplicate data, so check duplicates first.

### 5.2 Conditions that weaken indexes

| Condition | Replacement |
| --- | --- |
| Unanchored regex (`/abc/`), case-insensitive regex (`/^abc/i`) | Anchored, case-sensitive regex (`/^abc/`); collation index; text/search index |
| `$ne`, `$nin`, `$not` | Invert to positive condition (`$in`); partial index for the target subset |
| `$or` across many fields | Each branch has its own index; verify with explain |
| `$where`, `$expr` with functions on fields | Store precomputed value (computed pattern) and index it |
| Parameter type differs from field type (`"123"` vs `123`, string vs `ObjectId`) | Cast in the application before querying |

### 5.3 Query patterns

- Always use projection; do not return whole documents when the AP needs only a few fields.
- Lists always have `limit`. Large lists paginate by key (`{ created_at: { $lt: ? } }` plus `_id` as tie-breaker), not large `skip`.
- No N+1: batch load with `$in`, or a single `$lookup`. `$lookup` in a high-frequency AP signals the model should be reviewed.
- Aggregation: put `$match` and `$sort` (index-usable) at the start of the pipeline; `$project` early to reduce data passed between stages.
- Atomic updates with operators (`$set`, `$inc`, `$push`), not read-whole-document-then-overwrite.
- Multi-document writes use `bulkWrite`/`insertMany` in moderate batches.
- Set `maxTimeMS` on application queries.

### 5.4 Verify with explain

`explain("executionStats")` on sufficiently large fake data:

| Good | Needs review |
| --- | --- |
| `IXSCAN`, `totalKeysExamined` and `totalDocsExamined` close to `nReturned` | `COLLSCAN` on a large collection |
| No `SORT` stage (sorted by index) | In-memory `SORT` stage; `totalDocsExamined` much larger than `nReturned` |
| The chosen index is the one designed for the AP (`winningPlan`) | Another index chosen; many plans rejected (`rejectedPlans`) due to overlapping indexes |

Monitor under real load: profiler (`slowms`), slow query log, `$indexStats`, `$collStats`.

## 6. Schema changes (migration)

MongoDB has no mandatory DDL, but **every structural change still goes through a migration in source code**: create/drop collections, indexes, validators; data transformation. Migration tool follows the project.

- Every document has `schema_version`. The application reads both old and new versions during transition.
- Apply expand → migrate data → contract as in relational:
  1. Application reads both forms, writes the new form; validator relaxed (`oneOf` two versions, or time-limited `moderate`).
  2. Backfill in batches by `_id` (`{ _id: { $gt: last }, schema_version: { $lt: N } }`), rerunnable, monitor replication lag.
  3. Only after reconciliation, tighten the validator to the new version and remove old-form read code.
- Renaming a field: add new field, write both, backfill, then drop the old field. Do not `$rename` on large collections while old code still runs.
- Rollback part: drop new indexes/collections, restore old validator. If backfill destroys old-form data, state how to restore (back up before running).
- Verify on MongoDB of the same version and topology as production (replica set; sharded if production is sharded, since transactions and `$lookup` have different constraints):
  1. Up → down → up on a clean DB.
  2. Negative cases: insert documents violating the validator and unique index, confirm rejection.
  3. Explain for key APs after loading fake data.

## 7. Concurrency, transactions, durability

- A single-document write is atomic. Prefer models where a business operation touches only one document.
- Multi-document transactions exist only on replica sets (≥ 4.0) or sharded clusters (≥ 4.2): keep short (aborted after 60 seconds by default), few documents, handle `TransientTransactionError` / `UnknownTransactionCommitResult` with retry. Do not call external services inside a transaction.
- Optimistic locking: `version` field, `updateOne({ _id, version }, { $set: …, $inc: { version: 1 } })`; `matchedCount = 0` means report a conflict.
- State transitions include the source-state condition in the filter (`{ _id, status: "pending" }`).
- Hot counters: conditional `$inc` (`{ _id, qty: { $gte: n } }`, `{ $inc: { qty: -n } }`).
- Idempotency: unique index on `(scope, idempotency_key)`.
- Write concern `majority` for business data (default since 5.0); do not lower to `w: 1` without an ADR. For read-after-write in critical operations, use causal consistency or read from primary. Read from secondaries only for APs that accept stale data.
- One `MongoClient` per process, bounded `maxPoolSize`; total connections across all processes below the server's connection limit.

## 8. Scaling

Scaling tiers as in `performance-scaling.md` §6. Specific differences:

- Time series collections (≥ 5.0) and TTL indexes replace time-based partitioning.
- Archiving old data: move to an archive collection/cluster via a job.
- **Sharding** requires an ADR that also answers:
  - Shard key appears in nearly every query (avoid scatter-gather), high cardinality, not monotonically increasing with ranged sharding (`ObjectId`, timestamps funnel writes into one shard; use hashed or compound).
  - Unique indexes on a sharded collection must have the shard key as prefix.
  - Changing the shard key (`reshardCollection` ≥ 5.0) is costly; choose correctly from the start.

## 9. Security

Apply `security.md`, plus:

- Enable authentication (SCRAM or x.509) and TLS. Do not expose the port outside the internal network.
- The application account has only `readWrite` on its database (or a narrower custom role), no `dbAdmin`, `dbOwner`, `root`. A separate migration account creates indexes and changes validators.
- **Prevent NoSQL injection:** do not pass request objects into filters as-is (`{ password: { $ne: null } }`). Cast each field; reject keys starting with `$` or containing `.`. Do not use `$where`, `$function`, `$accumulator` with user input; disable server-side JavaScript if not needed.
- D3 data: encrypt in the application, or Client-Side Field Level Encryption / Queryable Encryption (≥ 7.0) if the project chooses. Disk encryption per infrastructure.
- Enable audit log if the version/infrastructure supports it and legal requirements need it.
