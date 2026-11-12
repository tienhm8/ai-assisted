---
name: backend-development
description: Cài đặt logic nghiệp vụ backend, service, truy cập dữ liệu, tích hợp và tác vụ nền trong ranh giới module và thiết kế đã Approved, kèm test và báo cáo bàn giao.
---

# Backend Development Skill

Hiện thực logic nghiệp vụ, truy cập dữ liệu và tích hợp ở backend: đúng business rule, đúng ranh giới module, dễ test.

## Cổng vào

Thiếu một điều kiện thì dừng và ghi câu hỏi mở:
- FR có AC và business rule đã duyệt.
- Thiết kế Approved: module-design, database-design; contract trong api-design nếu có endpoint hoặc tích hợp ngoài.

Đọc: FR, AC, business-rules; module-design, system-architecture, database-design, api-design; error-handling, security-standards; mã backend hiện có.

## Quy trình

1. **Phân tích:** thao tác nghiệp vụ, actor, tiền điều kiện, ràng buộc, chuyển trạng thái, kịch bản lỗi.
2. **Khảo sát mã hiện có:** cấu trúc, service, tầng truy cập dữ liệu, tiện ích dùng chung, cách xử lý lỗi và log. Tái dùng trước khi tạo mới.
3. **Thiết kế service:** trách nhiệm, đầu vào/ra, phụ thuộc, ranh giới transaction. Ranh giới module theo module-design.
4. **Hiện thực:** chuyển trạng thái tường minh; kiểm bất biến quan trọng; truy vấn tránh N+1.
5. **Lỗi và log:** theo error-handling; ghi log sự kiện nghiệp vụ, thất bại và sự kiện bảo mật.
6. **Tích hợp ngoài:** timeout, retry, idempotency, rate limit theo spec trong api-design; thiếu spec thì dừng, ghi câu hỏi mở.
7. **Phân quyền:** theo `authentication-rbac`.
8. **Test** bằng `unit-testing` và `integration-testing`: phủ business rule, kịch bản lỗi, transaction.

## Giới hạn

- Cần đổi schema thì dừng và chuyển `database-design`; không tự đổi.
- Không thêm service hoặc abstraction mà Task không cần.

## Hoàn thành khi

- Logic đúng từng AC và business rule liên quan; không gọi chéo module trái thiết kế.
- Transaction bao đủ các ghi phải cùng thành công hoặc cùng thất bại.
- Test đã chạy, có output thật.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: service đã tạo hoặc sửa, tương tác CSDL, tích hợp ngoài.
