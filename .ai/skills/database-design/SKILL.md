---
name: database-design
description: Act as Database Architect for relational databases (PostgreSQL, MariaDB/MySQL...) and document databases (MongoDB): analyze business logic, list access patterns, design conceptual → logical → physical models, choose data types, constraints, indexes, partitioning/sharding, security, then write verified migrations; record in database-design.md.
---

# Database Design Skill

Design data as a Database Architect, not just generate SQL: every table, column, constraint, index and scaling decision has a reason traceable to business logic or an access pattern.

## Entry gate

- **Implementation mode** (migrations go into source code): requires FR with AC, related BR and Approved architecture; DBMS and version known. If missing, stop and record an open question.
- **Sketch mode** (design before any Approved FR): do steps 1–8, record every assumption as an open question, label the result "Sketch – not for implementation" ("Phác thảo – chưa dùng để triển khai"). SQL stays only in the design document; do not create migration files.
- DBMS unclear: ask. If asked to propose one, compare options and draft an ADR.
- Partitioning, sharding, splitting the database, changing DBMS, multi-tenancy: require `architecture-design` and an ADR; this Skill supplies the data analysis for the ADR.

Read: FR, BR, AC; glossary; NFR (latency, throughput, RPO/RTO, volume, retention period); architecture (data-owning module, DBMS and version); api-design; existing schema and migrations; the project's DB conventions in database-design; real metrics if available (table sizes, slow queries, execution plans).

## References

Load only the file for the current step, and read only the listed sections.

| File in `references/` | Load at step |
| --- | --- |
| `modeling-patterns.md` | 3, 4, 6 |
| `data-types.md` | 5 |
| `performance-scaling.md` | Step 2: §1 · Step 6: §5 · Step 7: §2, §3, §6–§8 (§7–§8 only when moving to the partitioning/sharding tier) · Step 10: §4 |
| `security.md` | 8 |
| `migration.md` | Step 9: §1–§4, §6 · Step 10: §5 |
| `postgresql.md` or `mysql-mariadb.md` (only the file of the chosen DBMS) | Step 4: §9 · Step 5: §1, §2 · Step 6: §5, §9 · Step 7: §3, §4 (§7 only when moving to the partitioning/sharding tier) · Step 8: §10 · Step 9: §8 · Step 10: §6 |
| `mongodb.md` | DBMS is MongoDB: replaces the relational parts of steps 4, 5, 7, 9, 10 |

## Procedure

### A · Understand the business

1. **Business analysis.** From FR/BR derive candidate entities, data-producing events, state lifecycles, invariants, who creates, edits, views. Each point below must have an answer from the documents or be recorded as an open question:
   - Relationship cardinality, mandatory or optional, whether it changes over time.
   - Need history (value at transaction time, who changed what when) or only current state.
   - Business identifier, unique within what scope (whole system, per tenant, per parent).
   - Multi-tenant, multi-currency, multi-language, multi-timezone.
   - Soft delete, hard delete, archiving, deletion on data-subject request; retention period.
2. **Access patterns.** Build an `AP-<NN>` table: operation, filter, sort, pagination, frequency, target latency, rows returned. Estimate volume per table (now, after 1 and 3 years), read/write ratio, concurrent-write hotspots. Without metrics, record assumptions and open questions.

### B · Modeling

3. **Conceptual model.** Entities and relationships at business level, draw an ERD (Mermaid). Each entity traces to FR/BR and belongs to exactly one owning module.
4. **Logical model.** Normalize to 3NF. Choose a pattern per case (lookup, junction table, hierarchy, state machine, transaction-value snapshot, change history, multi-tenancy) and avoid anti-patterns per the reference file. Denormalize only when an access pattern needs it and there are metrics; record how copies stay consistent.
5. **Physical model** for the chosen DBMS and version:
   - Data type per column per the reference file.
   - Primary key is a surrogate key, plus UNIQUE on the business key; record the reason.
   - NOT NULL by default; a nullable column must mean "unknown" or "not applicable".
   - Standard columns per project convention: audit, version for optimistic locking, soft delete.
   - Name constraints and indexes explicitly per convention; do not let the DBMS auto-generate names.

### C · Integrity, performance, security

6. **Integrity and concurrency.**
   - Map each BR to a DB constraint. A BR not expressible in the DB: record where it is checked and how race conditions are avoided.
   - Foreign keys: RESTRICT for business data; CASCADE only for data fully dependent on the parent.
   - Each multi-table write: transaction boundary, isolation level, optimistic or pessimistic locking, idempotency key for operations that may be resent.
7. **Performance.**
   - Design indexes from the `AP-<NN>` table; each index records the access pattern it serves. Remove duplicate indexes or ones covered by another index.
   - Write queries that can use indexes, with limits and pagination.
   - Limit the connection pool.
   - Cache only after queries and indexes for that access pattern are optimized; if the cacheability conditions of Rule `cache` are met, hand the caching part to Skill `caching`.
   - Scale by tiers, move to the next tier only when the previous is insufficient and there are metrics: optimize queries and indexes → cache, read replicas → partitioning → archive old data → split database by module → sharding. From partitioning upward, record the partition key, reason, consequences and put it in an ADR.
8. **Data security.** Assign a data level to each column; hash passwords, encrypt D3 columns, mask data outside production; separate DB accounts by role (schema owner, migration runner, application, read-only); tenant isolation; audit tables; data lifecycle.

### D · Migration and verification

9. **Write migrations** per the project's migration tool conventions:
   - One migration per change, with a descriptive name, an up part and a rollback part.
   - Tables with data: expand → migrate data → contract; record which release contains which step.
   - Record lock level, estimated run time, online DDL options; backfill separately.
   - Seed contains only mandatory lookup data or fake data.
10. **Real verification** on a non-production database with the same DBMS and version:
    - Run up → rollback → up again on a clean database; for changes to existing tables, run on a copy of the current schema.
    - Negative cases: insert data violating each important constraint and confirm rejection.
    - Important access patterns: load enough fake data, run EXPLAIN and record the index used.
    - Anything not runnable: record not-run with reason.
11. **Document.** Update database-design (ERD, tables, constraints ↔ BR, indexes ↔ AP, lifecycle, security, transactions, migrations). Scaling decisions or convention exceptions go into a draft ADR. Do not create a parallel schema report.

## Limits

- Do not generate SQL before analyzing business logic and access patterns.
- Do not decide relationship cardinality, business keys or retention rules on your own when the documents are silent.
- Do not drop or loosen constraints to work around errors; do not move a BR from the DB to the application just to make a migration run.
- Do not drop or rename columns or tables before analyzing impact on code, reports, integrations and existing data.
- Do not use features of a DBMS other than the chosen one.

## Done when

- Every table traces to FR/BR; the `AP-<NN>` table and volume estimates exist, or are clearly marked as assumptions.
- Each important BR has a DB constraint or a recorded check location; each index serves an access pattern.
- D2/D3 columns are marked; DB accounts are separated by role.
- Migrations (implementation mode) have run up, rollback, up on a clean database; negative cases and EXPLAIN have evidence.
- Reviewer: Architect; add Security when there are migrations, money or personal data.

## Report

1. Mode, DBMS and version, business scope.
2. Entities, invariants, assumptions and open questions.
3. Access patterns and volume estimates.
4. ERD and table list (owning module, data level).
5. Notable design decisions with reasons and rejected options.
6. Constraints ↔ BR; indexes ↔ AP.
7. Cache (if any): per the Report of Skill `caching`.
8. Security: D2/D3 columns, encryption, accounts and permissions.
9. Migrations: files, release order, lock level and run time, rollback method.
10. Verification evidence.
11. Who must approve and ADRs to decide.
