# Database Rules

> Status: **Approved**. Mandatory Rule, DBMS-neutral. For a document database, "table" means collection, "column" means field.

## Design

1. Change the schema only per an Approved design; every change goes through a migration in source code, no manual edits.
2. Every table, column, constraint, and index traces to a recorded requirement, business rule, or access pattern; do not create tables or columns "for later".
3. Naming, standard data types, and primary key strategy follow the project's fixed DB conventions. If an item is not fixed: propose and wait for approval; do not apply on your own.
4. Every table has a primary key. Relationships are declared with foreign keys with explicitly chosen delete/update behavior; when not using a foreign key (cross-module, partition, shard), record the reason and how integrity is maintained.
5. Business invariants are declared in the DB with NOT NULL, UNIQUE, CHECK, foreign keys; do not rely only on application checks.
6. Money and quantities requiring precision use exact numeric types, not floating point. Timestamps are stored with time zone or normalized to UTC. Text uses an encoding with full Unicode support.
7. Do not pack multiple values into one column to avoid creating a table or relationship. Semi-structured data is only for attributes without integrity constraints and is not used as a primary query condition.

## Performance and scaling

8. Each index serves at least one recorded query. Adding or dropping an index on a large table must include the execution plan (EXPLAIN) before and after.
9. Queries returning lists must have a row limit; do not load an entire table unbounded.
10. Denormalization, partitioning, sharding, splitting the DB, or changing the DBMS is done only with measured data or a non-functional requirement, and requires an approved ADR.
11. Application queries select only needed columns, no `SELECT *`; no repeated queries per result row (N+1).
12. Filter and join conditions of important queries must be able to use indexes: do not wrap indexed columns in functions or expressions, no `LIKE` starting with a wildcard on B-Tree, parameters have the same type and collation as the column.
13. The application connects to the DB through a bounded connection pool; total max connections across all processes must be less than the server's `max_connections`.
14. Do not put business logic in stored procedures, functions, or triggers just for speed without measured data and an approved ADR.

## Migration

15. Migrations run on a clean DB and have a rollback. If rollback is impossible, record the reason and the recovery method for the reviewer to confirm.
16. A migration already run in a shared environment is not edited; to change it, write a new migration.
17. Schema changes are compatible with the running application version (expand → migrate data → contract). Do not rename or drop columns/tables in the same release as code still using them.
18. Migrations touching large tables must record lock level and estimated run time. Data migration (backfill) is batched, re-runnable, not wrapped in one long transaction; separate from structural migrations.
19. Running migrations on production must be approved; AI only writes migrations, does not run them.

## Data and transactions

20. Do not modify or delete production data directly; handle data with approved scripts.
21. Do not delete historical business data without an approved retention policy.
22. Columns holding `sensitive` or `secret` data must be marked in the design. Passwords are stored only as one-way hashes; other `secret` data is stored encrypted in the approved way.
23. DDL privileges are granted only to the migration account; the application account has no DDL privileges.
24. An error mid-transaction must roll back fully, never commit partially. Keep transactions short; do not call external services while a transaction is open.
25. Seed data is fake or anonymized data.
