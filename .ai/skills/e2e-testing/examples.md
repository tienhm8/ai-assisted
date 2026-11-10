# E2E Testing – Examples

> Bản nháp (Draft). Đây là **ví dụ minh hoạ** cho dự án bất động sản có Web và ERP. Journey và persona thật lấy từ AC loại E2E và tài liệu kiến trúc của dự án.

## Journey quan trọng (ví dụ)

- Đăng ký người dùng và xác thực email
- Đăng nhập, đăng xuất
- Tạo, cập nhật, duyệt tin đăng (listing)
- Tìm kiếm bất động sản
- Gửi yêu cầu tư vấn / liên hệ khách
- Quy trình quản lý nội bộ trên ERP

## Persona kiểm thử (ví dụ)

Vai trò thực lấy từ tài liệu kiến trúc (phần phân quyền) của dự án; bảng dưới chỉ minh hoạ.

| Persona | Ghi chú |
| --- | --- |
| Owner | Chỉ dùng quyền đã được duyệt |
| Admin | Không mặc định có mọi quyền |
| CTV | Chỉ trong phạm vi được duyệt |
| Sale | Chỉ dữ liệu được phân công |
| Customer | |
| Visitor | Chưa đăng nhập |

## Công cụ

Ví dụ giả định dùng Playwright. Đây là lựa chọn công cụ của dự án, không phải yêu cầu của Skill.
