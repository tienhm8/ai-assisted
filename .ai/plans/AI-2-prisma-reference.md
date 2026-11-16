# PLAN: AI-2 — Tiếp nhận skill prisma/skills vào reference Prisma

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 |

## 1. Mục tiêu và phạm vi
- Làm: tạo `backend-development/references/prisma.md` (Prisma Client) và `database-design/references/prisma-migrate.md` (Prisma Migrate); thêm dòng vào bảng References của hai Skill.
- Không làm: skill `prisma-postgres`, `prisma-compute`, `prisma-mongodb-upgrade` (gắn dịch vụ hosting hoặc chỉ dùng khi nâng cấp); chọn phiên bản Prisma cho MongoDB.

## 2. Yêu cầu và ngữ cảnh đã nạp
- Nguồn: github.com/prisma/skills @ a6f1929, MIT, `prisma-client-api` và `prisma-cli` v7.9.1, `prisma-upgrade-v7` (chỉ phần khác biệt v6 → v7); không có script.
- Chia hai file theo Skill dùng: viết query thuộc `backend-development`, viết và kiểm migration thuộc `database-design`. Mỗi bước chỉ nạp mục cần.
- Rule đối chiếu: database-rules 1, 4, 6, 9, 11, 13, 16, 19, 24; security-rules 3; coding-rules 10, 12; project-rules 6, 13, 17.

## 3. Rule và chuỗi Skill
- Rule: project-rules; git. Chuỗi Skill: `documentation`.

## 4. Thiết kế và file dự kiến thay đổi
- `prisma.md` §1 phiên bản và khởi tạo client, §2 query, §3 transaction, §4 raw SQL, §5 lỗi.
- `prisma-migrate.md` §1 viết migration, §2 khác biệt CLI v7, §3 kiểm chứng, §4 an toàn khi AI chạy lệnh.

## 5. Kế hoạch kiểm thử
`npm pack prisma @prisma/client @prisma/adapter-pg @prisma/config` 7.10.1, đọc help, `.d.ts` và mã CLI (không chạy code package); lệnh đọc một mục chạy với `## 1`, `## 4` của cả hai file; `wc -l`.

## 6. Rủi ro và điểm cần người quyết
Không chặn Task. Khi dự án dùng Prisma với MongoDB: Prisma 7.10.1 chưa hỗ trợ query compiler cho MongoDB, phải chọn ở lại 6.x hay lên 8. Reference ghi AI lập câu hỏi mở, không tự chọn.

## 7. Kết quả
- `prisma.md` 54 dòng, `prisma-migrate.md` 37 dòng; hai bảng References thêm một dòng mỗi bảng; lệnh đọc một mục trả exit 0.
- Nguồn trái Rule, đã đổi hoặc bỏ: quy trình xin đồng ý rồi đặt `PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION` để AI chạy `migrate reset`/`--accept-data-loss` (trái project-rules 17, đổi thành cấm); AI chạy `migrate deploy`/`resolve` trên production, CI/Docker chạy migrate khi khởi động (trái project-rules 13, database-rules 19); `db push` làm đường đổi schema (trái database-rules 1); `npm install` adapter (trái project-rules 6); log `console.log` (trái coding-rules 12).
- Nguồn sai so với 7.10.1, đã sửa: `directUrl` không còn trong kiểu `prisma.config.ts`; mặc định transaction là `maxWait` 2000 ms, `timeout` 5000 ms (nguồn ghi 5000/10000); `migrate resolve --rolled-back` chỉ nhận migration ở trạng thái lỗi, nên kiểm rollback dùng `db execute` + `migrate diff`.
- Chưa kiểm: hành vi "`undefined` trong `where` bị bỏ qua" chỉ xác nhận gián tiếp qua sự tồn tại của preview `strictUndefinedChecks`; không chạy với database thật.
