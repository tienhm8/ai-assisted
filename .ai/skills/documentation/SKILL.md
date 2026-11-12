---
name: documentation
description: Tạo và cập nhật tài liệu dự án (yêu cầu, kiến trúc, kỹ thuật, quản lý, vận hành, ADR nháp) cho khớp quyết định đã duyệt và hiện trạng hệ thống; không tự chuyển Approved, không tự quyết nghiệp vụ.
---

# Documentation Skill

Giữ tài liệu khớp với quyết định đã duyệt và hệ thống thật, không trùng lặp.

## Cổng vào

- Task nêu thay đổi cần ghi tài liệu. Thiếu thì dừng và hỏi.
- Xác định được nguồn (quyết định, yêu cầu, thiết kế đã duyệt). Không có nguồn thì ghi câu hỏi mở, không tự điền.

Đọc: Task, diff hoặc mô tả thay đổi, tài liệu hiện có liên quan, ADR liên quan.

## Quy trình

1. **Xác định tài liệu bị ảnh hưởng:**

   | Thay đổi | Tài liệu |
   | --- | --- |
   | Hành vi, quy tắc nghiệp vụ, AC | `01-requirements` |
   | Kiến trúc, schema, API, module | `02-architecture` |
   | Chuẩn code, bảo mật, kiểm thử, xử lý lỗi | `03-engineering` |
   | Tiến độ, backlog, KPI | `04-project-management` |
   | Triển khai, giám sát, sao lưu | `05-operations` |
   | Câu hỏi mở, giả định | open-questions |

2. **Xác minh nguồn** theo thứ tự ưu tiên: quyết định nghiệp vụ đã duyệt, yêu cầu Approved, thiết kế và ADR Approved, rồi mới tới hiện trạng code và tài liệu cũ. Hiện trạng code không tự thành yêu cầu. Nguồn mâu thuẫn thì báo, không tự chọn.
3. **Viết hoặc cập nhật** theo cấu trúc, cách đặt tên và mã chuẩn của dự án; giữ nguyên mã có sẵn.
4. **Một nơi duy nhất:** mỗi quy tắc, quyết định, trạng thái chỉ có một nơi quản lý; nơi khác tham chiếu bằng mã.
5. **Truy vết một chiều:** FR giữ liên kết tới BRQ/BR; AC trỏ tới FR; không tạo liên kết ngược.
6. **ADR**, chỉ khi quyết định thuộc diện cần ADR theo hướng dẫn của thư mục ADR: tạo `ADR-<NNNN>-<slug>.md` từ `_template.md` với số kế tiếp, trạng thái Proposed, ít nhất hai phương án; thêm một dòng vào danh mục. Quyết định nhỏ, dễ đảo ngược thì ghi ở tài liệu thiết kế.
7. **Rà lệch:** đối chiếu tài liệu với code, schema, API đang có; liệt kê chỗ lỗi thời, mâu thuẫn, còn thiếu.

## Giới hạn

- Không xoá quyết định lịch sử khi chưa có lý do.
- Không sửa tài liệu ngoài phạm vi Task.

## Hoàn thành khi

- Mọi tài liệu bị ảnh hưởng đã cập nhật hoặc ghi lý do không cần.
- Không có nội dung lặp ở hai nơi; mã chuẩn được giữ.
- ADR (nếu có) ở Proposed và đã vào danh mục.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: tài liệu đã tạo hoặc sửa, ADR đã tạo, mâu thuẫn nguồn, chỗ lỗi thời và khoảng trống còn lại.
