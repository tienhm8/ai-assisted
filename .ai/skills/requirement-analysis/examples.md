# Requirement Analysis – Examples

> Bản nháp (Draft). Chỉ là **ví dụ minh hoạ** (bối cảnh bất động sản), không phải nghiệp vụ chính thức; nghiệp vụ thật nằm trong docs của dự án.

## Các nhóm business rule cần làm rõ

| Nhóm | Câu hỏi cần làm rõ |
| --- | --- |
| Điều kiện tài khoản | Ai đủ điều kiện đăng tin? |
| Quyền sở hữu tin đăng | Ai là chủ tin đăng? Có chuyển giao được không? |
| Duyệt tin đăng | Ai duyệt? Tiêu chí? Sửa có phải duyệt lại không? |
| Chuyển trạng thái | Các trạng thái hợp lệ, ai được chuyển? |
| Hiển thị dữ liệu | Vai nào thấy trường nào? |
| Giới hạn phân công | Tin đăng giao cho Sale nào? |

Câu hỏi chưa có quyết định đã duyệt thì ghi thành OQ-NN, không tự trả lời.

## Ví dụ một FR và AC (minh hoạ)

- FR-LISTING-01: Người môi giới đủ điều kiện có thể tạo tin đăng ở trạng thái nháp. (BRQ-01; BR-LISTING-01)
- FR-LISTING-01-AC1: Given môi giới đủ điều kiện, When gửi thông tin hợp lệ, Then tin được tạo ở trạng thái nháp.
- FR-LISTING-01-AC2: Given thiếu trường bắt buộc, When gửi, Then bị từ chối kèm lỗi nêu rõ trường thiếu.
