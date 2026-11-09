# E2E Testing – Examples

> Bản nháp (Draft). Đây là **ví dụ minh hoạ** cho dự án bất động sản có Web và ERP. Hành trình và persona thật lấy từ User Story, AC và RBAC trong `docs/`.

## Hành trình quan trọng (ví dụ)

- Đăng ký người dùng và xác thực email
- Đăng nhập, đăng xuất
- Tạo tin đăng (listing)
- Cập nhật tin đăng
- Duyệt tin đăng
- Tìm kiếm bất động sản
- Gửi yêu cầu tư vấn
- Quy trình quản lý trên ERP

## Persona kiểm thử (ví dụ)

| Persona | Ghi chú |
| --- | --- |
| Owner | Chỉ dùng quyền đã được duyệt |
| Admin | Không mặc định có mọi quyền |
| CTV | Chỉ trong phạm vi được duyệt |
| Sale | Chỉ dữ liệu được phân công |
| Customer | |
| Visitor | Chưa đăng nhập |

## Công cụ

Skill giả định dự án dùng Playwright. Đây là lựa chọn công cụ của dự án, không phải yêu cầu của Skill; xác nhận trong `docs/03-engineering/testing-strategy.md` khi chốt.

Ghi chú khi áp dụng cho dự án: thay bằng hành trình và persona thật sau khi có FR và AC được duyệt.
