# PR: <KEY>-<N> <tiêu đề ngắn>

> Người viết PR điền trước khi yêu cầu review. Thiếu mục bắt buộc (*) thì reviewer trả PR về, chưa review code. Mục không áp dụng ghi "Không" kèm lý do ngắn, không xoá mục. Dự án có thể chép mẫu này vào nơi nền tảng Git đọc (ví dụ `.github/pull_request_template.md`, `.gitlab/merge_request_templates/`).

## 1. Vấn đề và mục tiêu (*)
- Task: `<KEY>-<N>` · FR/BR/AC liên quan:
- Báo cáo bàn giao (PR của AI; link hoặc dán):
- Vấn đề đang giải quyết (bug thì nêu cách tái hiện):

## 2. Loại thay đổi (*)
- [ ] Thay đổi hành vi (tính năng / sửa lỗi)
- [ ] Chỉ refactor (hành vi bên ngoài giữ nguyên)
- [ ] Khác:

## 3. Phạm vi ảnh hưởng (*)

| Hạng mục | Có/Không | Chi tiết |
| --- | --- | --- |
| Dữ liệu / schema / migration | | Bảng, khối lượng dữ liệu bị ảnh hưởng, có khoá bảng không, tương thích ngược với code đang chạy không |
| API / hợp đồng với bên gọi | | Breaking change? |
| Job / tác vụ nền / message / event | | Idempotent khi chạy lại? |
| Cache | | Khoá, thời gian sống, khi nào làm mất hiệu lực |
| Cấu hình / biến môi trường | | Đã có giá trị cho mọi môi trường? |
| Xác thực / phân quyền / dữ liệu nhạy cảm | | Mức dữ liệu D |
| Dependency mới | | Lý do |

## 4. Ngoài phạm vi
Những gì cố ý không làm trong PR này.

## 5. Kiểm thử (*)
PR của AI: ghi "Xem báo cáo bàn giao §3", không chép lại. PR do người viết: điền bên dưới.
- Test đã thêm/sửa, gắn ID AC:
- Lệnh đã chạy và kết quả (hoặc link CI):
- Kiểm thử thủ công / ảnh chụp (nếu có UI):

## 6. Triển khai và rollback
- Thứ tự deploy (code trước hay migration trước), feature flag:
- Cách rollback:

## 7. Điểm reviewer nên xem kỹ
PR của AI: ghi "Xem báo cáo bàn giao §2", không chép lại. PR do người viết: đoạn rủi ro cao, logic khó, chỗ lệch thiết kế.
