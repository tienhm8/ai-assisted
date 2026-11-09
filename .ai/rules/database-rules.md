# DATABASE RULES

1. Follow the approved database schema.
2. Every schema change requires a migration.
3. Never modify production data directly.
4. Define foreign key relationships explicitly.
5. Use indexes based on query requirements.
6. Apply appropriate unique constraints.
7. Do not delete historical business data without an approved retention policy.
8. All migrations must have a rollback strategy where technically feasible.
