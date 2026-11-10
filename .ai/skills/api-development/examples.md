# API Development – Examples

> Minh hoạ, không phải nghiệp vụ hay contract chính thức. Thay bằng ví dụ thật của dự án khi có.

## Ví dụ: API tạo bản ghi "tin đăng"

Giả định contract Approved trong api-design.md đã có `POST /listings`.

- **Cổng vào:** FR + AC đã duyệt; contract Approved. Nếu thiếu mã lỗi cho trường hợp trùng, dừng và ghi OQ.
- **Đối chiếu:** request/response/lỗi khớp contract; không thêm trường ngoài contract.
- **Hiện thực:** validation → guard (theo `authentication-rbac`) → handler → service (`backend-development`).
- **Test:** thành công; đầu vào sai; chưa xác thực; sai quyền; vi phạm business rule. Mã HTTP lấy từ ánh xạ lỗi của error-handling.md.
- **Review:** lộ dữ liệu, log, truy vấn N+1, trùng logic.
