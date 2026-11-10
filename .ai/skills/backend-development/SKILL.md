---
name: backend-development
description: Cài đặt logic nghiệp vụ backend, service, truy cập dữ liệu, tích hợp và tác vụ nền trong ranh giới module và thiết kế đã Approved, kèm test và báo cáo bàn giao.
---

# Backend Development Skill

## 1. Mục tiêu

Hiện thực logic nghiệp vụ, truy cập dữ liệu và tích hợp ở backend: đúng business rule, an toàn, dễ test, đúng ranh giới module.

## 2. Cổng vào

Dừng và ghi `open-questions.md` (OQ-<NN>) nếu thiếu:
- FR có AC và business rule đã duyệt.
- Thiết kế Approved (module-design.md, database-design.md; contract trong api-design.md nếu có endpoint).

## 3. Đầu vào

- FR, acceptance-criteria.md, business-rules.md
- module-design.md, system-architecture.md, database-design.md
- api-design.md (spec tích hợp), error-handling.md, security-standards.md
- Mã backend hiện có; skill `authentication-rbac` cho phân quyền

## 4. Quy trình

1. **Phân tích**: thao tác nghiệp vụ, actor, tiền điều kiện, ràng buộc, chuyển trạng thái, kịch bản lỗi.
2. **Khảo sát mã hiện có**: cấu trúc, service, data access, tiện ích dùng chung, cách xử lý lỗi và log.
3. **Thiết kế service**: trách nhiệm, đầu vào/ra, phụ thuộc, ranh giới transaction. Ranh giới module theo module-design.md; không gọi chéo module trái thiết kế.
4. **Hiện thực**: theo business rule; tái dùng service sẵn có; chuyển trạng thái tường minh; kiểm bất biến quan trọng; truy vấn an toàn, tránh N+1.
5. **Lỗi**: theo error-handling.md; không lộ stack trace ra client.
6. **Log**: ghi sự kiện nghiệp vụ, thất bại, bảo mật; không ghi mật khẩu, token, dữ liệu nhạy cảm.
7. **Tích hợp ngoài**: giới hạn (timeout, retry, idempotency, rate limit) theo spec trong api-design.md; thiếu spec thì dừng, ghi OQ.
8. **Test**: gọi `unit-testing` và `integration-testing`; phủ business rule, kịch bản lỗi, transaction.
9. **Bàn giao**: theo mục 8.

## 5. Checklist

- [ ] Business rule được hiện thực đúng, không tự bịa.
- [ ] Không vượt ranh giới module.
- [ ] Transaction và truy vấn phù hợp.
- [ ] Phân quyền áp theo `authentication-rbac`.
- [ ] Lỗi xử lý tường minh; không lộ nội bộ.
- [ ] Không log dữ liệu nhạy cảm.

## 6. Việc không được làm

- Không bịa business rule.
- Không bỏ qua phân quyền.
- Không truy cập dữ liệu production khi chưa được duyệt.
- Cần đổi schema thì dừng và chuyển `database-design` (cần duyệt); không tự đổi.
- Không thêm service/abstraction không cần thiết.

## 7. Tiêu chí hoàn thành (DoD)

- Cổng vào thoả; logic đúng AC.
- Test đã chạy có bằng chứng; skip/fail ghi rõ.
- Checklist đạt; review hoàn tất.
- Tài liệu bị ảnh hưởng đã cập nhật hoặc ghi lại cần cập nhật.

## 8. Báo cáo bàn giao

- Service tạo/sửa và logic đã làm
- Tương tác DB, tích hợp ngoài
- Test đã chạy và kết quả
- Quyết định cần duyệt, OQ còn mở
- Rủi ro và giới hạn
