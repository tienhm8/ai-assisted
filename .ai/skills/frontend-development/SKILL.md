---
name: frontend-development
description: Cài đặt trang, component, form, state và tích hợp API ở frontend theo yêu cầu Approved, thiết kế UI/UX và API contract, kèm test và báo cáo bàn giao.
---

# Frontend Development Skill

## 1. Mục tiêu

Hiện thực giao diện đúng FR/AC, UI/UX và API contract; xử lý đủ trạng thái tải/lỗi, truy cập được và có test.

## 2. Cổng vào

Dừng và ghi `open-questions.md` (OQ-<NN>) nếu thiếu:
- FR có AC đã duyệt.
- Tài liệu UI/UX và Design System: nếu dự án chưa có, dừng và ghi OQ.
- API contract Approved trong api-design.md. Chỉ chạy song song với `api-development` khi contract đã Approved.

## 3. Đầu vào

- FR, acceptance-criteria.md
- Tài liệu UI/UX, Design System (nếu có)
- api-design.md, system-architecture.md, coding-standards.md, security-standards.md
- Mã frontend hiện có

## 4. Quy trình

1. **Phân tích**: người dùng, màn hình, dữ liệu hiển thị, tương tác, trạng thái tải/lỗi/rỗng, hành vi phụ thuộc quyền.
2. **Khảo sát mã hiện có**: cấu trúc, routing, component dùng chung, cách gọi API; tái dùng trước khi tạo mới.
3. **Hiện thực**: component theo coding-standards.md (kiểu dữ liệu theo coding standards; ranh giới render nếu framework có khái niệm này).
4. **Form**: validate phía client chỉ để hỗ trợ người dùng, không thay backend; xử lý lỗi validation từ server, chặn gửi trùng, phản hồi thành công.
5. **Tích hợp API**: đúng contract; xử lý lỗi HTTP, mất mạng, tải; không lộ secret.
6. **Quyền hiển thị**: lấy từ backend/session; ẩn UI không phải kiểm quyền. Xử lý phiên hết hạn và phản hồi từ chối theo `authentication-rbac`.
7. **Truy cập và đáp ứng**: theo Design System và coding-standards.md.
8. **Test**: gọi `unit-testing` (component/form) và `e2e-testing` (luồng chính theo AC).
9. **Bàn giao**: theo mục 8.

## 5. Checklist

- [ ] Khớp UI/UX và AC.
- [ ] Tái dùng component/Design System sẵn có.
- [ ] Trạng thái tải, lỗi, rỗng được xử lý.
- [ ] Quyền hiển thị lấy từ backend/session.
- [ ] Không lộ secret.

## 6. Việc không được làm

- Không bịa hành vi nghiệp vụ.
- Không coi ẩn UI là phân quyền; không bỏ qua phân quyền backend.
- Không thêm thư viện UI không cần thiết hay nhân đôi component dùng chung.
- Không đổi quy ước giao diện toàn cục khi chưa được duyệt.
- Không đặt logic nghiệp vụ nhạy cảm chỉ ở frontend.

## 7. Tiêu chí hoàn thành (DoD)

- Cổng vào thoả; giao diện và tích hợp API hoàn tất đúng AC.
- Test đã chạy có bằng chứng; skip/fail ghi rõ.
- Checklist đạt; review hoàn tất.
- Tài liệu bị ảnh hưởng đã cập nhật hoặc ghi lại cần cập nhật.

## 8. Báo cáo bàn giao

- Trang/component tạo hoặc sửa
- API đã tích hợp
- Test đã chạy và kết quả
- OQ còn mở, quyết định cần duyệt
- Giới hạn đã biết
