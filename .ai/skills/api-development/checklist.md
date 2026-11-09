# API Development – Checklist

> Bản nháp (Draft). Làm rõ dần theo Task thật. Rule tương ứng: `.ai/rules/`.

## Trước khi code
- [ ] Có FR, business rule và acceptance criteria đã duyệt.
- [ ] Có API specification ([api-design](../../../docs/02-architecture/api-design.md)).
- [ ] Có database schema liên quan ([database-design](../../../docs/02-architecture/database-design.md)).
- [ ] Đã xác định role và quyền truy cập.

## Thiết kế
- [ ] Endpoint, HTTP method theo convention.
- [ ] Schema request/response và error response rõ ràng.
- [ ] Quy tắc validation đầy đủ.

## Cài đặt
- [ ] Validate mọi đầu vào ngoài hệ thống.
- [ ] Phân quyền kiểm tra ở backend, không tin client.
- [ ] Logic nghiệp vụ nằm ở service, không nằm ở handler.
- [ ] Đổi schema thì có migration.
- [ ] Không hardcode secret, không lộ dữ liệu nhạy cảm.

## Test
- [ ] Thành công · đầu vào sai/thiếu · chưa đăng nhập (401) · sai quyền (403).
- [ ] Truy cập tài nguyên của người khác · vi phạm business rule · tương tác DB.
- [ ] Đã chạy test và có bằng chứng; ghi rõ test bị skip hoặc fail.

## Bàn giao
- [ ] Liệt kê file thay đổi, test đã chạy, rủi ro còn lại.
- [ ] Cập nhật tài liệu nếu cần.
