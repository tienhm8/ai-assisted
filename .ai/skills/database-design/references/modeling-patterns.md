# Database Design – Modeling patterns

> Project conventions (naming, key types) in database-design §2 take priority. DBMS syntax: `postgresql.md` or `mysql-mariadb.md`.

## 1. From business logic to entities

| Phrase in FR/BR | Model hint |
| --- | --- |
| "Each X belongs to one Y" | FK `x.y_id NOT NULL` → Y |
| "X may (or may not) have one Y" | Nullable FK, or a 1-1 child table if Y's attributes are sparse |
| "X has many Y, Y belongs to many X" | Junction table `x_y(x_id, y_id)` with PK or UNIQUE `(x_id, y_id)` |
| Link with its own attributes (quantity, role, from date) | Junction table becomes an entity with a business name (e.g. `enrollment`, `order_line`) |
| "Status changes from A to B" | Status column + CHECK value set; status transition history table if traceability needed |
| "Price at time of purchase" | Snapshot the value into the transaction row, do not reference the current price |
| "Keep change history" | History table or time-validity model (section 5) |
| "Code unique within each store" | UNIQUE `(store_id, code)`, not UNIQUE `code` table-wide |

Check cardinality with two-way questions: "How many B does one A have?" and "How many A does one B have?", including over time (does "before" differ from "now").

## 2. Lookup: lookup table or CHECK/enum

| Criterion | CHECK (or enum type) | Lookup table + FK |
| --- | --- | --- |
| Value set | Small, stable, tied to code logic | Changed by operators, has attributes (label, order, active) |
| Changing values | Needs migration | Add a row |
| Multi-language labels | No | Yes |

- Prefer string + CHECK over `ENUM`: removing or reordering `ENUM` values is hard and some systems sort by index. Check whether the chosen DBMS enforces CHECK (§1 of the DBMS file).

## 3. Hierarchies

| Pattern | Fits when | Note |
| --- | --- | --- |
| Adjacency list (`parent_id`) | Shallow tree, write-heavy, read by level | Whole-branch queries use recursive CTE (check version support) |
| Materialized path (`path` = `/1/4/9/`) | Branch reads frequent, nodes rarely move | Prefix index; dedicated tree type if the DBMS has one |
| Closure table (`ancestor_id, descendant_id, depth`) | Read any ancestors/descendants, need full FKs | Writes cost extra rows |
| Nested set | Almost read-only | Very expensive writes; avoid for changing data |

## 4. State machines

- Check valid transitions in the application or a trigger, with a condition in the UPDATE (`WHERE id = ? AND status = 'pending'`) to avoid race conditions.
- Traceability needed: table `<entity>_status_history(entity_id, from_status, to_status, changed_by, changed_at, reason)`.
- State-dependent constraints use conditional CHECK, e.g. `CHECK (status <> 'paid' OR paid_at IS NOT NULL)`.

## 5. History and validity time

| Need | Pattern |
| --- | --- |
| Know who changed what, when (audit) | Append-only audit table, written by application or trigger; no UPDATE/DELETE |
| Value correct at a point in time (price, policy, tax rate) | Version table `valid_from`, `valid_to`; prevent overlap with an exclusion constraint if available, or check in the application within a locking transaction |
| Query past state of the whole table | System-versioned (temporal) table if available; otherwise history table + trigger |
| Source of truth is an event stream | Append-only event store; requires ADR |

## 6. Soft delete

- Use only when the business needs restore or traceability; not by default for every table.
- UNIQUE must ignore deleted rows: partial unique index `WHERE deleted_at IS NULL`, or a generated column that is NULL when deleted with UNIQUE on it (NULL does not violate UNIQUE).
- FKs to soft-deleted rows remain valid; child rows are a business decision.
- Personal data under deletion request: soft delete is not enough; hard delete or anonymize.

## 7. Multi-tenancy

| Pattern | Isolation | Operational cost | Fits when |
| --- | --- | --- | --- |
| `tenant_id` column in shared tables | Logical (needs RLS or mandatory checks) | Low | Many small tenants |
| Schema per tenant | Medium | Migrations multiply by tenant count | Tens to hundreds of tenants |
| Database per tenant | High | High | Legal requirements, large tenants |

With a `tenant_id` column: present in every business table, leading in PK or UNIQUE and composite indexes, composite FK `(tenant_id, parent_id)` to prevent cross-tenant references; enable row-level security as a second layer if available (security §4). Choosing the pattern is an architecture decision: requires ADR.

## 8. Money and financial transactions

- Amounts use exact numeric types plus currency code (ISO 4217) when multi-currency.
- Ledger: immutable (append-only) entries; correct errors with reversing entries, not UPDATE.
- Balance computed from entries, or stored balance with a version column for optimistic locking.
- UNIQUE idempotency key for payment operations.

## 9. Anti-patterns to avoid

| Anti-pattern | Problem | Replace with |
| --- | --- | --- |
| EAV (`entity, attribute, value`) | Loses types, loses constraints, complex queries | Real columns; rarely used dynamic attributes in a JSON column |
| Polymorphic association (`target_type`, `target_id`) | No FK | One FK column per type with CHECK "exactly one column non-NULL", or separate junction tables |
| Column holding a list (`"1,4,9"`) | No joins, no constraints | Junction table |
| Repeated columns (`phone1`, `phone2`, `phone3`) | Hard limit, repetitive queries | Child table |
| "God" table with many sparse columns for many kinds | Rampant NULLs, weak constraints | Split by kind (shared parent table + child tables) |
| Storing derived values without a sync mechanism | Data drift | Compute on read, generated column, or document the sync mechanism |
| Primary key is mutable business data (email, tax ID) | Key changes cascade to every FK | Surrogate key + UNIQUE on the business key |
