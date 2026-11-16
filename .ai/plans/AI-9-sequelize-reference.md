# PLAN: AI-9 — Tiếp nhận skill Sequelize vào reference Sequelize

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (giống AI-2, Tech Lead yêu cầu "tương tự" 2026-11-16); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 |

## 1. Mục tiêu và phạm vi
- Làm: tạo `backend-development/references/sequelize.md` (truy vấn, transaction, raw SQL, lỗi) và `database-design/references/sequelize-migrations.md` (`sequelize-cli`/`queryInterface`); thêm một dòng vào bảng References của mỗi Skill. Cách chia giống AI-2 (Prisma).
- Không làm: Sequelize v7 (vẫn alpha); `sequelize-typescript` (chỉ nhắc theo codebase); bật CLS (quyết định kiến trúc, thêm dependency).

## 2. Yêu cầu và ngữ cảnh đã nạp
- Không có skill chính thức của Sequelize (khác Prisma có `prisma/skills`). Ba ứng viên cộng đồng đã xem: `agents-inc/skills` `api-database-sequelize` @ 845a1f2 (MIT, có mục transaction và migration riêng) được chọn; `mindrally/skills` `sequelize` @ 7682ca7 (Apache-2.0, hướng dẫn chung, không thêm điểm nào chưa có); `bankkroll/skills-builder` `sequelize` (chép tài liệu chính thức ~63k token) không lấy.
- Đọc toàn bộ nguồn đã chọn: SKILL.md, reference.md, 4 file examples; không có script.
- Rule đối chiếu: database-rules 1, 6, 9, 11, 12, 13, 15–19, 24, 25; security-rules 3; coding-rules 10, 12; project-rules 6, 13, 16, 17.

## 3. Rule và chuỗi Skill
- Rule: project-rules; git. Chuỗi Skill: `documentation`.

## 4. Thiết kế và file dự kiến thay đổi
- `sequelize.md` §1 phiên bản và khởi tạo, §2 truy vấn, §3 transaction, §4 raw SQL, §5 lỗi; cùng khung bước với `prisma.md`.
- `sequelize-migrations.md` §1 viết migration, §2 kiểm chứng, §3 an toàn khi AI chạy lệnh.
- `backend-development/SKILL.md`, `database-design/SKILL.md`: bảng References.

## 5. Kế hoạch kiểm thử
`npm pack sequelize@6.37.8 sequelize-cli@6.6.5 umzug@2.3.0 @nestjs/sequelize@12.0.1`, chỉ đọc mã (không chạy code package); lệnh đọc một mục chạy với mọi `##` của hai file; mục `docs/` và số Rule được trỏ tới tồn tại.

## 6. Rủi ro và điểm cần người quyết
Không chặn Task. Nguồn là skill cộng đồng ít người dùng (28 lượt cài), nên mọi điểm giữ lại đều đã đối chiếu với mã 6.37.8; chạy thử bằng một Task thật trước khi chuyển Approved (external-skills, Quy trình bước 5).

## 7. Kết quả
- `sequelize.md` 52 dòng, `sequelize-migrations.md` 32 dòng; hai bảng References thêm một dòng mỗi bảng; lệnh đọc một mục trả exit 0 cho cả 8 mục.
- Nguồn trái Rule, đã bỏ: `logging: console.log` (coding-rules 12); `SELECT *` trong raw SQL (database-rules 11); CLS qua `cls-hooked` (project-rules 6); backfill một câu UPDATE trong migration cấu trúc (database-rules 18); seed mật khẩu mẫu (database-rules 25); tìm kiếm `Op.iLike '%x%'` và phân trang offset làm mẫu (database-rules 12); tự đặt thông báo lỗi (error-handling).
- Nguồn sai hoặc thiếu so với mã 6.37.8, đã sửa hoặc thêm: `where` chứa `undefined` ném lỗi (`query-generator.js` `whereItemQuery`), nhưng `where: {}` vẫn qua `_optionsMustContainWhere` và áp lên mọi dòng; pool mặc định `max` 5, `acquire` 60000 ms (nguồn dùng 10/30000 như mặc định); `bulkCreate` mặc định `validate: false`; `UniqueConstraintError` là lớp con của `ValidationError`; `whereMergeStrategy` mặc định `overwrite` có thể ghi đè bộ lọc tenant trong scope; `changeColumn` PostgreSQL bỏ NOT NULL/DEFAULT khi không ghi lại và thêm UNIQUE thứ hai (ví dụ gốc mắc lỗi này); `addIndex` có `concurrently`; `SequelizeMeta` chỉ lưu tên, không checksum (umzug 2.3.0); seeder mặc định `none`; `@nestjs/sequelize` 12.0.1 chạy `sync()` khi `autoLoadModels` bật và `synchronize` chưa đặt.
- Chưa kiểm: hành vi chạy thật (không có database); kiểu trả về `BIGINT`/`DECIMAL` trên MySQL/MariaDB chỉ ghi "tuỳ kích thước, chuẩn hoá ở biên" vì phụ thuộc cấu hình driver; `dropTable` không xoá ENUM chỉ đúng khi không có model đăng ký trùng tên bảng (migration không import model), suy từ `postgres/query-interface.js`.
