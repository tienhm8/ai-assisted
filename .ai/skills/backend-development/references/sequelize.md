# Backend Development – Sequelize

> Áp dụng cho: Sequelize 6.x với `@nestjs/sequelize` 11 và 12 (dùng chung một file).

Rules and error-handling win over anything here. NestJS wiring: `nestjs-11.md` or `nestjs-12.md` matching `stack`; migrations: `database-design/references/sequelize-migrations.md`.

## 1. Version check and setup (steps 2, 3)

- Read the installed version first. v6 imports from `sequelize`, defines models with `Model.init()` or `sequelize-typescript` decorators; v7 alpha is `@sequelize/core` with different decorators and dialect classes. Follow what the codebase uses; switching major version or model style is not part of a feature Task.
- One `Sequelize` instance per process, created where the codebase already creates it. Do not construct it in services or per request.
- Pool defaults in 6.37.8 are `max` 5, `min` 0, `acquire` 60000 ms, `idle` 10000 ms. Size the pool per `database-rules` 13 in the existing config, not by guessing.
- Default `logging` is `console.log` and prints every SQL statement. Route it to the project logger or turn it off per `coding-rules` 12; never enable `logQueryParameters` where queries carry `sensitive` or `secret` data.
- Never call `sequelize.sync()` or `Model.sync()` (with or without `alter`/`force`) outside a throwaway test database; schema changes go through migrations (`database-rules` 1). `@nestjs/sequelize` runs `sync()` on startup when `autoLoadModels` is true and `synchronize` is not set: the module config must say `synchronize: false`.
- TypeScript models: attribute properties use `declare`. A plain class field (`id!: number`) shadows Sequelize's getters, so values read as `undefined`; 6.37.8 only logs a warning.
- Physical names: Sequelize pluralizes table names and keeps camelCase columns unless `tableName`, `underscored`, or `field` say otherwise. Read these options before writing raw SQL or a migration for the model.

## 2. Queries (step 4)

- A `where` value of `undefined` throws `WHERE parameter "x" has invalid "undefined" value`. A `where` built from optional inputs that ends up `{}` is not rejected: `Model.update(..., { where: {} })` and `Model.destroy({ where: {} })` touch every row. Validate filter inputs before bulk writes; pass `where: {}` only when the AC means "all rows".
- `null` in `where` means `IS NULL`; skipping the key means "no condition". Do not map missing input to `null` or the reverse.
- Select only needed columns with `attributes`, also inside `include` (`database-rules` 11). Lists have a `limit` (`database-rules` 9).
- `include` of a to-many relation with `limit` on the parent: Sequelize builds a subquery, and `required: true` turns the join into INNER JOIN, dropping parents without children. A `limit` inside an `include` switches it to `separate: true` (a second query). Check the generated SQL when combining these.
- `findAndCountAll` with a to-many `include` counts joined rows, not parents, unless `distinct: true` (and `col` if needed).
- `defaultScope` applies to every finder, including `findByPk`. `unscoped()` removes all scopes, including a tenant or permission filter placed in a scope; scopes merge `where` by overwriting the same key (`whereMergeStrategy` default `overwrite`), so a later scope can replace a tenant filter. Do not call `unscoped()` or combine scopes on a filtered model without the design saying so.
- Paranoid models need `timestamps: true`; without it `destroy()` deletes the row. `paranoid: false`, `force: true`, raw SQL, and `queryInterface` all ignore the soft-delete filter: add `deleted_at IS NULL` yourself in raw SQL.
- Static `Model.update`, `Model.destroy`, `bulkCreate` fire only bulk hooks; per-row hooks (audit, normalization, derived fields) do not run unless `individualHooks: true`, which loads every matching row into memory. Check which hooks the model has before choosing a bulk write. `bulkCreate` also skips model validation unless `validate: true`.
- `BIGINT` and `DECIMAL` come back as strings on PostgreSQL; on MySQL/MariaDB the type depends on size. Normalize at the boundary; do not convert money to `Number` for arithmetic (`database-rules` 6).
- `upsert` returns `[instance, created]`, but `created` is not reliable on every dialect; do not branch business logic on it.
- `findOrCreate` runs find then create in an internal transaction and relies on a UNIQUE constraint on the `where` columns to resolve races. Without that constraint it creates duplicates under concurrency.

## 3. Transactions and concurrency (step 4)

- Without CLS, every call inside `sequelize.transaction(async (t) => ...)` must pass `{ transaction: t }`, including calls made by hooks (`options.transaction`) and by services the callback invokes. A call without it runs on another pool connection, outside the transaction, and is not rolled back. Check whether the codebase enabled CLS (`Sequelize.useCLS`) before relying on auto-passing; enabling CLS is an architecture decision, not part of a feature Task.
- `sequelize.transaction({ transaction: t }, cb)` creates a savepoint inside `t`. Without the `transaction` option it opens a separate transaction on another connection.
- Use the callback (managed) form. An unmanaged `sequelize.transaction()` must `rollback()` in `catch`, or the connection stays checked out.
- Side effects after commit (events, emails, cache invalidation) go in `t.afterCommit(...)`, which does not run on rollback (`database-rules` 24, error-handling §9).
- Isolation is set per transaction (`isolationLevel: Transaction.ISOLATION_LEVELS.*`); use the level database-design §6 records. Row locks: `lock: t.LOCK.UPDATE`, `skipLocked: true` for queues.
- Counters and balances: use `increment`/`decrement` (one atomic UPDATE) or a conditional `Model.update` and check the affected count; do not read-modify-write across two queries without a lock. `version: true` on the model enables optimistic locking and throws `OptimisticLockError` on a stale instance save.

## 4. Raw SQL (step 4)

- `sequelize.query()` with `replacements` (`:name`, `?`) or `bind` (`$name`, `$1`) parameterizes values. Interpolating input into the SQL string, into `sequelize.literal()`, or into `sequelize.where(sequelize.literal(...))` is injection (`security-rules` 3). Dynamic identifiers (sort column) come from an allowlist of constants.
- Without `type`, `sequelize.query()` returns `[results, metadata]`; for reads pass `type: QueryTypes.SELECT` to get rows. The generic type parameter is only a cast; validate or map the result.
- Raw SQL uses physical table and column names (§1), lists columns explicitly (`database-rules` 11), and inside a transaction passes `{ transaction: t }`.

## 5. Errors (step 5)

- Error classes: `UniqueConstraintError` (unique violation), `ForeignKeyConstraintError`, `ValidationError` (model validators), `EmptyResultError` (`rejectOnEmpty`), `OptimisticLockError`, `TimeoutError`, `ConnectionError`. `UniqueConstraintError` extends `ValidationError`: check the subclass first, or a unique violation is mapped as a validation error.
- Map to the project's codes in one place per error-handling §3, §4. Do not expose `error.sql`, `error.parent`, `error.original`, `error.fields` values in responses or logs at levels the data level forbids (`coding-rules` 10).
- Do not catch `UniqueConstraintError` to implement "insert if absent" unless the design chose that; otherwise the constraint is the guard and the error is mapped.
