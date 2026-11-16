# Database Design – Sequelize migrations

> Nguồn: github.com/agents-inc/skills, skill `api-database-sequelize` (examples/advanced, mục Migrations with queryInterface và Migration Gotchas) @ 845a1f2, MIT · Ngày lấy: 2026-11-16 · Áp dụng cho: `sequelize-cli` 6.x với Sequelize 6.x (đối chiếu mã `sequelize-cli` 6.6.5, `umzug` 2.x đi kèm, `sequelize` 6.37.8; dự án chưa chốt phiên bản ở system-architecture §4, rà lại khi chốt)
> Đã điều chỉnh: chỉ giữ lỗi AI hay mắc khi viết và kiểm migration bằng `sequelize-cli`/`queryInterface`. Bỏ: backfill bằng một câu UPDATE cả bảng trong migration cấu trúc (trái `database-rules` 18); seed mật khẩu mẫu thật trong migration (trái `database-rules` 25); bảng method `queryInterface` (kiến thức chung). Sửa theo mã nguồn: ví dụ gốc gọi `changeColumn` với `unique: true` sau `addColumn` đã `unique: true`, trên PostgreSQL sinh thêm một UNIQUE constraint thứ hai; `changeColumn` trên PostgreSQL bỏ NOT NULL và DEFAULT nếu định nghĩa mới không ghi lại; `dropTable` trong migration không xoá kiểu ENUM; seeder mặc định không lưu trạng thái. Thêm phần an toàn khi AI chạy lệnh theo `project-rules` 13, 17 và `database-rules` 19. Không lấy code minh hoạ.

Reference for Skill `database-design`. Load only when the project's migration tool (database-design §7) is `sequelize-cli` (or `umzug` with `queryInterface`) on a SQL database, and only the section for the current step. `migration.md` and `database-rules` win over anything here.

## 1. Writing a migration (step 9)

- A migration exports `up(queryInterface, Sequelize)` and `down(queryInterface, Sequelize)`; paths come from `.sequelizerc` (`migrations-path`). Write `down` for every `up` (`database-rules` 15).
- Sequelize does not generate migrations from model changes: `model:generate` writes a new model plus its `createTable` migration once, and `migration:generate` writes an empty skeleton. Model definitions and migrations are kept in sync by hand: change both in the same Task and check that names, types, nullability, and defaults match (`backend-development/references/sequelize.md` §1).
- Do not import application models in a migration; models change later and the migration must keep producing the same schema. Model hooks and validators never run in `queryInterface` calls.
- The applied-migrations table (`SequelizeMeta`) stores names only, with no checksum: editing an applied migration is not detected by the tool. Never do it (`database-rules` 16); write a new migration.
- No transaction by default: if a step of `up` fails, earlier steps stay applied and the migration is not recorded. On PostgreSQL wrap the steps in `queryInterface.sequelize.transaction(async (t) => ...)` and pass `{ transaction: t }` to every call. On MySQL/MariaDB DDL commits implicitly, so keep one structural change per migration.
- `addIndex(table, fields, { name, concurrently: true })` emits `CREATE INDEX CONCURRENTLY` on PostgreSQL; it cannot run inside a transaction, so put it in its own migration without the wrapper. Always set `name` on indexes and constraints so `down` can remove them and names follow the convention (step 5).
- `changeColumn` on PostgreSQL rewrites the column from the full new definition: an omitted `allowNull: false` drops NOT NULL, an omitted `defaultValue` drops the default, and `unique: true` adds another UNIQUE constraint even if one exists. Restate the full definition and do not repeat `unique`; use `addConstraint`/`removeConstraint` for constraints.
- `renameColumn`, `removeColumn`, and type changes break the running code version (`database-rules` 17); follow expand → migrate → contract in `migration.md` §2.
- PostgreSQL ENUM: `createTable` creates a type `enum_<table>_<column>`; `dropTable` in a migration does not drop it, so `down` drops the type explicitly. Adding a value needs raw `ALTER TYPE ... ADD VALUE`. Changing allowed values is a schema change per `migration.md` §3.
- Backfills are not a single UPDATE inside the structural migration; follow `migration.md` §4 (batched, re-runnable, separate).
- Raw SQL in a migration (`queryInterface.sequelize.query`) uses physical names and parameters like any raw SQL (`security-rules` 3).

## 2. Verification (step 10)

- Run only against a disposable local/container database of the same DBMS and version (`migration.md` §5). `sequelize-cli` picks the config entry from `--env`, else `NODE_ENV`, else `development`; `--url` overrides the config. Confirm which database that resolves to before any command.
- Up → down → up: `db:migrate`, then `db:migrate:undo` (last migration) or `db:migrate:undo --name <file>`, then `db:migrate` again. Compare the schema after `down` with the schema before `up` (for example `pg_dump --schema-only` diff); a `down` that leaves an index, constraint, or ENUM type behind fails. Record commands and output.
- `db:migrate:status` lists `up`/`down` per file; use it to show the state before and after.

## 3. Agent safety (steps 9, 10)

- AI never runs `db:migrate`, `db:migrate:undo`, `db:migrate:undo:all`, `db:seed`, `db:seed:all`, or raw SQL against a shared, staging, or production database (`database-rules` 19, `project-rules` 13). Deployment notes (`migration.md` §6) state the command and the undo step for a human to run.
- AI never runs `db:drop`, `db:create` on a shared database, `sequelize.sync({ force: true })` or `sync({ alter: true })` anywhere but a throwaway test database (`project-rules` 17). To get a clean database, recreate the disposable container.
- Seeders: default seeder storage is `none`, so `db:seed:all` re-runs every seeder each time and duplicates data. Seed data is fake (`database-rules` 25); a seeder that must run once needs `seederStorage` set in the config, which is a project decision.
