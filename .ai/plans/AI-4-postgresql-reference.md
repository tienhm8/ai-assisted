# PLAN: AI-4 — Bổ sung reference PostgreSQL từ supabase-postgres-best-practices

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 |

## 1. Mục tiêu và phạm vi
- Làm: bổ sung điểm riêng PostgreSQL còn thiếu vào `database-design/references/postgresql.md`.
- Không làm: phần riêng Supabase (`auth.uid()`, role `anon`/`authenticated`, cổng pooler); đổi số/tên mục; sửa `performance-scaling.md`, `security.md`, `code-review` (khoảng trống chung ghi ở §6).

## 2. Yêu cầu và ngữ cảnh đã nạp
- Nguồn: github.com/supabase/agent-skills @ c9be0e9, MIT, v1.1.1, không có script.
- external-skills: không đưa ngưỡng bắt buộc vào reference → bỏ công thức `max_connections`, `work_mem`, pool size, mốc partition.
- Bảng References của `database-design/SKILL.md` nạp postgresql.md theo mục; thêm vào đúng mục nên bảng không đổi.

## 3. Rule và chuỗi Skill
- Rule: project-rules; git. Chuỗi Skill: `documentation`.

## 4. Thiết kế và file dự kiến thay đổi
Chỉ `postgresql.md`: §3, §4, §5, §6, §8, §9, §10; thêm cặp dòng nguồn.

## 5. Kế hoạch kiểm thử
Đối chiếu từng điểm phiên bản/cú pháp với postgresql.org (bản 18.7); `wc -l`.

## 6. Rủi ro và điểm cần người quyết
Không có điểm chặn. Khoảng trống chung phát hiện, đề xuất Task riêng nếu cần:
- `performance-scaling.md` §3: upsert nguyên tử thay cho kiểm tra rồi chèn.
- `performance-scaling.md` §5: khoá hàng theo thứ tự (`SELECT … ORDER BY id FOR UPDATE`).
- `security.md` §3: role App không phải superuser, có quyền `USAGE` trên sequence.
- `code-review/references/runtime.md`: kiểm "select rồi insert không có ràng buộc unique" là race.

## 7. Kết quả
- 125 → 144 dòng; bảng References không đổi.
- Đã đối chiếu: `ALTER TABLE` (không có `ADD CONSTRAINT IF NOT EXISTS`), `CREATE INDEX IF NOT EXISTS`, toán tử `jsonb_ops`/`jsonb_path_ops`, `to_tsvector` 2 tham số, partial index với tham số, `ON CONFLICT`, advisory lock, `idle_session_timeout` (14), `work_mem` và `hash_mem_multiplier` (2.0 từ 15), `pg_stat_statements`, mặc định autovacuum, `log_lock_waits`, case folding, `EXECUTE` cho `PUBLIC`, `ALTER DEFAULT PRIVILEGES`, RLS bỏ qua kiểm UNIQUE/PK/FK.
- Xác minh yếu: đổi tên cột `pg_stat_statements` "từ PG 13" (so tài liệu PG 12 với bản hiện hành); RLS bọc subquery chạy một lần (suy từ hành vi InitPlan, trang RLS không ghi); `->>` không dùng GIN cả cột (suy từ quy tắc "toán tử áp trực tiếp lên cột được index").
