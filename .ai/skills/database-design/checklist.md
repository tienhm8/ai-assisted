# Database Design – Checklist

> Bản nháp (Draft). Làm rõ dần theo Task thật. Rule tương ứng: [database-rules](../../rules/database-rules.md).

- [ ] Thiết kế theo schema đã duyệt.
- [ ] Mỗi thay đổi schema có migration.
- [ ] Migration có rollback (nếu khả thi) và đã chạy thử trên DB không phải production.
- [ ] Foreign key khai báo rõ ràng.
- [ ] Index dựa trên truy vấn thực tế, không thêm tuỳ tiện.
- [ ] Unique constraint phù hợp.
- [ ] Dữ liệu lịch sử nghiệp vụ không bị xoá khi chưa có chính sách lưu trữ.
- [ ] Đã đánh giá tác động lên dữ liệu hiện có.
- [ ] Đã cập nhật tài liệu database.
