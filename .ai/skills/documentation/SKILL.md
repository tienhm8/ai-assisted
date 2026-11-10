---
name: documentation
description: Tạo và cập nhật tài liệu dự án (yêu cầu, kiến trúc, kỹ thuật, quản lý, vận hành, ADR nháp) cho khớp quyết định đã duyệt và hiện trạng hệ thống; không tự chuyển Approved, không tự quyết nghiệp vụ.
---

# Documentation Skill

## 1. Mục tiêu

Giữ tài liệu chính xác, nhất quán và không trùng lặp với hệ thống thật. Khi hành vi, API, schema, kiến trúc hoặc vận hành thay đổi, tài liệu liên quan được cập nhật **trong cùng thay đổi**.

## 2. Cổng vào

- Có Task nêu thay đổi cần ghi tài liệu. Thiếu thì dừng và hỏi.
- Xác định được thông tin gốc (quyết định, yêu cầu, thiết kế đã duyệt). Không có nguồn thì ghi câu hỏi mở `OQ-<NN>`, không tự điền.

## 3. Đầu vào

Task, diff hoặc mô tả thay đổi, tài liệu hiện có liên quan, ID yêu cầu (FR/BR/AC), ADR liên quan. Với ADR: ADR template và danh mục ADR.

## 4. Quy trình

1. **Xác định tài liệu bị ảnh hưởng** theo bản đồ:

| Thay đổi | Tài liệu |
| --- | --- |
| Hành vi, quy tắc nghiệp vụ, AC | 01-requirements |
| Kiến trúc, schema, API, module | 02-architecture |
| Chuẩn code, bảo mật, kiểm thử, xử lý lỗi | 03-engineering |
| Tiến độ, backlog, KPI | 04-project-management |
| Triển khai, giám sát, sao lưu | 05-operations |
| Câu hỏi mở, giả định | open-questions.md |

2. **Xác minh nguồn.** Thứ tự ưu tiên: quyết định nghiệp vụ đã duyệt, yêu cầu Approved, thiết kế và ADR Approved, rồi mới đến hiện trạng code và tài liệu cũ. Tài liệu **Draft không phải nguồn sự thật**. Hiện trạng code không tự thành yêu cầu. Nguồn mâu thuẫn thì báo, không tự chọn.
3. **Viết hoặc cập nhật** theo cấu trúc, đặt tên, ID chuẩn của dự án (`FR-<MODULE>-<NN>`, `BR-<MODULE>-<NN>`, `<FR>-AC<N>`, `ADR-<NNNN>`, `OQ-<NN>`, Task `<KEY>-<N>`). Giữ nguyên ID có sẵn.
4. **Một nơi duy nhất.** Mỗi quy tắc, quyết định hoặc trạng thái chỉ có một nơi quản lý; nơi khác chỉ tham chiếu bằng ID. Không chép nội dung sang tài liệu thứ hai.
5. **Truy vết một chiều.** Chỉ khai báo liên kết ở phía được giao (FR giữ liên kết tới BRQ/BR; AC trỏ tới FR); không tạo liên kết ngược thủ công.
6. **ADR (chỉ khi thuộc diện cần ADR** theo hướng dẫn của thư mục ADR; quyết định nhỏ, dễ đảo ngược, gọn trong một module thì ghi ở tài liệu thiết kế):
   - tạo `ADR-<NNNN>-<slug>.md` từ `_template.md`, số kế tiếp, không tái sử dụng;
   - trạng thái **Proposed**, nêu ít nhất hai phương án;
   - thêm một dòng vào danh mục ADR; tài liệu thiết kế chỉ ghi kết quả và trỏ `ADR-<NNNN>`;
   - **không** chuyển Approved.
7. **Vòng đời tài liệu:** Draft, In Review, Approved, Deprecated. AI chỉ soạn ở Draft (hoặc đề xuất In Review); không chuyển Approved.
8. **Rà soát lệch:** đối chiếu tài liệu với code, schema, API đang có; liệt kê chỗ lỗi thời, mâu thuẫn, chỗ còn thiếu. Kiểm ID, trạng thái, ví dụ.
9. **Vùng 🔴:** sửa rule, skill hoặc workflow chỉ **đề xuất** trong báo cáo, không tự sửa; cần Task riêng và người duyệt.

## 5. Checklist

- [ ] Mọi tài liệu bị ảnh hưởng đã cập nhật hoặc ghi lý do không cần.
- [ ] Nội dung khớp nguồn đã duyệt, không có khẳng định thiếu căn cứ.
- [ ] ID chuẩn được giữ; không có nội dung lặp ở hai nơi.
- [ ] Trạng thái tài liệu rõ; không có Approved do AI đặt.
- [ ] ADR (nếu có): đúng diện, Proposed, đã có dòng trong danh mục.
- [ ] Câu hỏi mở vẫn mở; mâu thuẫn nguồn đã báo.

## 6. Việc không được làm

- Không bịa quyết định nghiệp vụ; không biến hiện trạng code hoặc giả định thành yêu cầu.
- Không chuyển trạng thái sang Approved; không đánh dấu ADR Approved.
- Không âm thầm giải quyết mâu thuẫn nguồn; không xoá quyết định lịch sử khi chưa có lý do.
- Không sao chép nội dung có chủ quản lý ở nơi khác; không sửa tài liệu ngoài phạm vi Task.
- Không sửa rule, skill, workflow trong Task thường (chỉ đề xuất).

## 7. Tiêu chí hoàn thành (DoD)

- Tài liệu bị ảnh hưởng đã cập nhật cùng thay đổi, nguồn đã xác minh.
- Mâu thuẫn, chỗ lỗi thời và khoảng trống còn lại đã báo.
- ADR nháp (nếu có) ở Proposed và đã vào danh mục; chờ người duyệt.

## 8. Báo cáo bàn giao

Điền DELIVERY-REPORT-TEMPLATE, nêu thêm: tài liệu đã tạo/sửa, ADR đã tạo (mã, trạng thái Proposed), mâu thuẫn nguồn, thông tin lỗi thời, đề xuất sửa vùng 🔴, khoảng trống còn lại.
