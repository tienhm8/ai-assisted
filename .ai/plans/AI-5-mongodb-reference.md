# PLAN: AI-5 — Bổ sung reference MongoDB từ mongodb/agent-skills

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 |

## 1. Mục tiêu và phạm vi
- Làm: bổ sung điểm còn thiếu vào `database-design/references/mongodb.md` từ skill `mongodb-schema-design` và `mongodb-query-optimizer`.
- Không làm: đổi tên/đánh số lại mục (Skill dẫn chiếu theo mục); tách file; phần chỉ có ở Atlas; MCP.

## 2. Yêu cầu và ngữ cảnh đã nạp
- Nguồn: github.com/mongodb/agent-skills @ 776c47f, Apache-2.0, cả hai skill v1.0.0, không có script.
- external-skills §Chọn lọc phần nào, §Ghi nguồn. document-database-rules, database-rules 6, 21 (không dùng xấp xỉ cho tiền, tồn kho, số liệu kiểm toán).
- Ngân sách: tăng ≤ 25 dòng vì file được nạp cả khi dùng MongoDB.

## 3. Rule và chuỗi Skill
- Rule: project-rules; git. Chuỗi Skill: `documentation`.

## 4. Thiết kế và file dự kiến thay đổi
Chỉ `mongodb.md`: thêm gạch đầu dòng vào đúng mục §1–§8, thêm hai cặp dòng nguồn.

## 5. Kế hoạch kiểm thử
Đối chiếu từng điểm phụ thuộc phiên bản với mongodb.com/docs/manual; `wc -l`; rà không trùng document-database-rules.

## 6. Rủi ro và điểm cần người quyết
Không có.

## 7. Kết quả
- 172 → 191 dòng (+25 −6). Không đổi số mục.
- Sửa một chỉ dẫn cũ sai: "`$project` sớm để giảm dữ liệu" trái tài liệu tối ưu pipeline của MongoDB.
- Đối chiếu trên tài liệu MongoDB: ESR (`$in` ≤ 200 là equality, `$ne`/`$nin`/`$regex` là range, ERS), gộp `$sort`+`$limit`, giới hạn 100 MB và `allowDiskUseByDefault` (≥ 6.0), `$facet`, `$lookup`, covered query, sparse index, giới hạn time series (index tự tạo ≥ 6.3, `granularity` mặc định `seconds`), `$nor` với `$jsonSchema`.
- Xác minh một phần: pre/post-image của `findOneAndUpdate` retryable (thấy ở trang tham số v7.0; trang 8.x bị cắt trước mục này). Câu chữ không phụ thuộc vị trí lưu.
- Đánh giá tách file: chưa cần ở 191 dòng; nếu vượt khoảng 250 dòng thì tách §5 (index, query; nạp ở bước 6, 7, 10) khỏi phần còn lại.
