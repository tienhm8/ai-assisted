# Backend Development – Prisma

> Nguồn: github.com/prisma/skills, skill `prisma-client-api` v7.9.1 và `prisma-upgrade-v7` (chỉ phần khác biệt v6 → v7) @ a6f1929 · Ngày lấy: 2026-11-15 · Áp dụng cho: Prisma ORM 7.x (đối chiếu `prisma`, `@prisma/client`, `@prisma/adapter-pg`, `@prisma/config` 7.10.1; dự án chưa chốt phiên bản ở system-architecture §4, rà lại khi chốt)
> Đã điều chỉnh: chỉ giữ lỗi AI hay mắc khi dùng Prisma Client (khởi tạo client, `undefined` trong `where`, `select`/`omit`, Decimal/JSON null, transaction, raw SQL, mã lỗi) và API v6 đã bỏ ở v7. Bỏ: bảng liệt kê method, toán tử lọc, phân trang, quan hệ, aggregate (kiến thức chung); singleton qua `globalThis` và pattern Next.js (quyết định kiến trúc, NestJS dùng DI); log `console.log` qua `$on` (không có correlation ID, trái `coding-rules` 12; log query có thể lộ tham số `secret`); Accelerate, SQL commenter, `queryPlanCacheMaxSize`, Bun, ESM/tsconfig (hạ tầng); lệnh `npm install` adapter/dotenv (trái `project-rules` 6); ví dụ soft delete bằng extension (quy ước dự án chưa chốt). Sửa theo 7.10.1: mặc định `maxWait` 2000 ms, `timeout` 5000 ms (bản gốc ghi 5000/10000 như mặc định); thêm `tx.$transaction` lồng qua savepoint; pool do driver quyết định, `connection_limit` trong URL không có tác dụng với adapter. Không lấy code minh hoạ.

Reference for Skill `backend-development`. Load only when the backend uses Prisma ORM, and only the section for the current step. Rules (`database-rules`, `security-rules`, `coding-rules`) and error-handling win over anything here; for NestJS wiring see `nestjs-11.md` or `nestjs-12.md` (the one matching `stack`).

## 1. Version check and client construction (steps 2, 3)

- Before writing Prisma code, read the installed `prisma`/`@prisma/client` version and the `generator` block. Code written from v6 memory breaks on v7.
- Generator `prisma-client` (v7 default) requires `output`; import `PrismaClient` and `Prisma` from that output path, not from `@prisma/client`. Legacy `prisma-client-js` still exists: follow whichever the codebase uses; switching generator is not part of a feature Task.
- v7 SQL providers: `new PrismaClient({ adapter })` with a driver adapter (e.g. `PrismaPg`), or `accelerateUrl`. Constructor options `datasources`/`datasourceUrl` no longer exist; a datasource `url` in `schema.prisma` is a schema error.
- Removed in v7: `$use()` middleware (use `$extends({ query })`), `$metrics`, `Prisma.validator()` under `prisma-client` (use `satisfies Prisma.UserSelect`). `rejectOnNotFound` is gone; use `findUniqueOrThrow`/`findFirstOrThrow`.
- Pool size and timeouts come from the driver (`pg` pool default `max` 10), not Prisma v6 defaults; `connection_limit`/`pool_timeout` in the URL are ignored by the adapter. Size it per `database-rules` 13 in the existing adapter config.
- One client instance per process, created where the codebase already creates it; do not construct `PrismaClient` in services or per request.
- `$extends()` returns a new client; code that injects the base client bypasses the extension. Use the extended instance the codebase exposes.
- After a schema change, the generated client is stale until `prisma generate` runs (v7 `migrate dev` does not run it). Schema changes themselves stop per this Skill's Limits.
- MongoDB: Prisma 7.10.1 has no MongoDB query compiler; the source recommends staying on 6.x or moving to 8. That is a version decision: record an open question, do not choose.

## 2. Queries (step 4)

- A `where` field set to `undefined` is dropped, not matched (unless the `strictUndefinedChecks` preview is on): `deleteMany({ where: { tenantId: undefined } })` deletes every row. Validate filter inputs before `updateMany`/`deleteMany`; never pass `where: {}` unless the AC means "all rows".
- `null` filters "is null"; `undefined` means "no condition". Do not map missing input to `null` or the reverse.
- `select` with `omit`, or `select` with `include`, on the same level is a validation error. Choose `select` for list/API reads (`database-rules` 11); `omit` only hides fields and still loads the rest.
- `include` loads every related row; add `take`/`where` on to-many relations in list reads (`database-rules` 9). For N+1, load relations in the same query (`include`/`select`) or with one `in` query, never per row.
- Cursor pagination needs `orderBy` on a unique field (or ending with one) matching the cursor; `skip` with large offsets scans.
- `Decimal` columns return `Prisma.Decimal`; do not convert money to `Number` for arithmetic (`database-rules` 6).
- JSON columns: to store or filter SQL NULL vs JSON `null` use `Prisma.DbNull`/`Prisma.JsonNull`/`Prisma.AnyNull`, not literal `null`.
- `update`/`delete` on a missing row throws `P2025`; `findUnique` returns `null`. Map both per error-handling §4; do not choose a status code yourself.
- `updateMany`/`deleteMany`/`createMany` return `{ count }`; `createManyAndReturn`/`updateManyAndReturn` return rows. Do not chain a re-read for data the `...AndReturn` variant returns.

## 3. Transactions and concurrency (step 4)

- Everything in an interactive transaction uses `tx`; `prisma.*` inside the callback runs on another connection outside the transaction (see `nestjs-11.md` or `nestjs-12.md` §6). A service called from the callback must receive `tx`, per the pattern the codebase uses.
- `tx.$transaction(...)` nests through a savepoint in 7.x (adapter must support savepoints). A new `prisma.$transaction` inside the callback is a separate transaction, not nested.
- Defaults are `maxWait` 2000 ms, `timeout` 5000 ms; past `timeout` every further `tx` call fails with "expired transaction". Keep the transaction short (`database-rules` 24). Raising `timeout` needs a reason in the plan, not as a fix for slow work inside.
- Array form `$transaction([q1, q2])` cannot use the result of one query in the next; use the interactive form for dependent steps.
- Nested writes (`create` with nested `create`/`connect`) are already atomic; do not wrap a single nested write in `$transaction`.
- Isolation is set per call (`isolationLevel`) or in `transactionOptions`; choose the level the design's database-design §6 records. Under `Serializable`/`RepeatableRead`, write conflicts surface as `P2034`: retry the whole transaction only if error-handling §8 allows it.
- Counters and balances: use atomic `{ increment }`/`{ decrement }` or a conditional `updateMany` and check `count`; do not read-modify-write across two queries without a lock.

## 4. Raw SQL (step 4)

- `$queryRaw`/`$executeRaw` as tagged templates parameterize `${}` values. Building SQL in a string and passing it to `$queryRawUnsafe`/`$executeRawUnsafe`, or interpolating input into `Prisma.raw()`, is injection (`security-rules` 3).
- Compose dynamic parts with `Prisma.sql`, `Prisma.join`, `Prisma.empty`. Dynamic identifiers (sort column) come from an allowlist of constants, never from input.
- Raw SQL uses physical names: table/column names after `@@map`/`@map`, and on PostgreSQL quoted mixed-case names (`"createdAt"`). Field names from the Prisma model do not work.
- Raw results are not typed or mapped: `COUNT(*)` on PostgreSQL returns `bigint`, numeric returns `Decimal`; the generic `$queryRaw<T>` is only a cast. Validate or map before returning.
- Inside a transaction use `tx.$queryRaw`, not `prisma.$queryRaw`. Raw SQL still lists columns explicitly, no `SELECT *` (`database-rules` 11).

## 5. Errors (step 5)

- Prisma errors are `Prisma.PrismaClientKnownRequestError` with `code`: `P2002` unique violation (`meta` carries model and target), `P2003` foreign key, `P2025` record not found, `P2028` transaction API (often timeout), `P2034` write conflict. Map to the project's codes in one place per error-handling §3, §4; do not leak `meta` or SQL in responses (`coding-rules` 10).
- `P2039` wraps an unmapped database error from the driver adapter with the original code; do not parse the message text.
- Do not catch `P2002` to implement "insert if absent" unless the design chose that; otherwise the UNIQUE constraint is the guard and the error is mapped.
