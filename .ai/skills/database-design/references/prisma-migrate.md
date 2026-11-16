# Database Design – Prisma Migrate

> Nguồn: github.com/prisma/skills, skill `prisma-cli` v7.9.1 (migrate-dev, migrate-deploy, migrate-diff, migrate-resolve, migrate-status, migrate-reset, db-push, db-execute, agent-safety) và `prisma-upgrade-v7` (chỉ phần CLI khác v6) @ a6f1929 · Ngày lấy: 2026-11-15 · Áp dụng cho: Prisma ORM 7.x (đối chiếu help và mã CLI `prisma` 7.10.1, kiểu `@prisma/config` 7.10.1; dự án chưa chốt phiên bản ở system-architecture §4, rà lại khi chốt)
> Đã điều chỉnh: chỉ giữ lỗi AI hay mắc khi viết và kiểm chứng migration bằng Prisma Migrate, cùng cờ/hành vi v7 khác v6. Bỏ: AI tự chạy `migrate deploy`, `migrate resolve` trên môi trường dùng chung/production, CI/Docker chạy migrate khi khởi động (trái `database-rules` 19, `project-rules` 13); quy trình xin đồng ý rồi đặt `PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION` để chạy `migrate reset`/`db push --force-reset`/`--accept-data-loss` (trái `project-rules` 17, đổi thành cấm); `db push` làm đường đổi schema và cho MongoDB (trái `database-rules` 1); `prisma init`, `prisma dev`, studio, mcp, seed, Bun (công cụ/hạ tầng). Sửa theo 7.10.1: `directUrl` không còn trong kiểu `prisma.config.ts` (bản gốc vẫn ghi); file cấu hình tìm `prisma7.config.*` trước, rồi `prisma.config.*`; `migrate dev` không chạy generate/seed dù help vẫn ghi "trigger generators". Không lấy code minh hoạ.

Reference for Skill `database-design`. Load only when the project's migration tool (database-design §7) is Prisma Migrate on a SQL database, and only the section for the current step. `migration.md` and `database-rules` win over anything here.

## 1. Writing a migration (step 9)

- Migrations are `prisma/migrations/<timestamp>_<name>/migration.sql` (path from `migrations.path` in the Prisma config). Prisma has no down migration: write the rollback SQL yourself, in the location database-design §7 fixes, and verify it per §3.
- Generate with `prisma migrate dev --create-only --name <name>` against a disposable local database, then read and edit the SQL before applying. Prisma's generated SQL does not follow `migration.md` §2–§3 on its own: a rename becomes drop + add (data loss), a required column on a filled table fails or needs a default, indexes are created without `CONCURRENTLY`, there is no lock timeout.
- Never edit a migration already applied anywhere shared (`database-rules` 16); Prisma stores a checksum and reports "modified after it was applied". Write a new migration.
- Names: set `map:` on `@@index`/`@@unique`/`@relation`/`@id` so constraint and index names follow the convention (step 5); Prisma's default names are derived from the model.
- Constraints Prisma schema cannot express (CHECK, partial index unless the `partialIndexes` preview is enabled, exclusion) are added by hand in `migration.sql`. Record them in database-design, since a later `migrate dev` diff does not know them.
- `relationMode = "prisma"` creates no foreign keys; it conflicts with `database-rules` 4 unless an ADR records it.
- Each `migration.sql` is applied as one script; statements that cannot run in a transaction (`CREATE INDEX CONCURRENTLY`) go in their own migration.
- `migrate dev` is interactive: without a TTY it refuses when there are data-loss warnings. On drift (database differs from migration history) it stops and suggests `migrate reset`: do not reset; stop and report.

## 2. v7 CLI differences (steps 9, 10)

- Connection URLs live in `prisma.config.ts` (`datasource.url`, `datasource.shadowDatabaseUrl`); `url`/`directUrl`/`shadowDatabaseUrl` in `schema.prisma` is a schema error. The CLI does not load `.env` by itself; the config file does (e.g. `import 'dotenv/config'`). Check which database the config points to before any command.
- Commands take `--config`/`--schema`; `migrate dev`, `db push` also take `--url`. `migrate deploy`, `status`, `resolve`, `reset`, `db execute` have no `--url`.
- Removed: `--skip-generate`, `--skip-seed`; `migrate diff --from-url/--to-url/--from-schema-datasource/--to-schema-datasource` (use `--from-config-datasource`/`--to-config-datasource`), `--from-schema-datamodel` (use `--from-schema`); `db execute --url/--schema`.
- `migrate dev` and `migrate reset` no longer run `prisma generate` or the seed. Run `prisma generate` explicitly when code needs the new client.

## 3. Verification (step 10)

- Run only against a disposable local/container database of the same DBMS and version (`migration.md` §5). Before running, confirm the resolved datasource in the config is that database.
- Up → rollback → up: apply with `migrate dev`; run your rollback SQL with `prisma db execute --file`; prove the schema is back with `migrate diff --from-config-datasource --to-migrations <dir without the new migration> --exit-code`; re-apply the new `migration.sql` with `db execute --file` and diff against `--to-schema`. `migrate resolve --rolled-back` only accepts a migration in a failed state, so it cannot undo a successful one. Record commands and output.
- Schema check: `prisma migrate diff --from-migrations <dir> --to-schema <schema> --exit-code` (exit 0 = in sync, 2 = differences) proves the migrations match the schema; `--script` prints the SQL. `migrate diff` is read-only; `--from-migrations` replays migrations on the shadow database (`datasource.shadowDatabaseUrl`).
- `prisma migrate status` reports unapplied, failed and diverged migrations; it exits 1 in those cases, not only on error.

## 4. Agent safety (steps 9, 10)

- AI never runs `prisma migrate reset`, `prisma db push --force-reset` or `--accept-data-loss`. Prisma 7 blocks these for agents; never set `PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION` or hide agent-detection variables to bypass it. To get a clean database, recreate the disposable container; if that is not possible, record not-run with reason (`project-rules` 17).
- AI never runs `migrate deploy`, `migrate resolve` or `db execute` against a shared, staging or production database (`database-rules` 19, `project-rules` 13). Deployment notes (`migration.md` §6) state the `migrate deploy` step and any `resolve` needed for recovery for a human to run.
- Do not use `db push` to change any schema, even locally, as a substitute for a migration (`database-rules` 1).
