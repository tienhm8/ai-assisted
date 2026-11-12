---
name: frontend-development
description: Cài đặt trang, component, form, state và tích hợp API ở frontend theo yêu cầu Approved, thiết kế UI/UX và API contract, kèm test và báo cáo bàn giao.
---

# Frontend Development Skill

Hiện thực giao diện đúng FR/AC, thiết kế UI/UX và API contract; xử lý đủ trạng thái tải, lỗi, rỗng.

## Cổng vào

Thiếu một điều kiện thì dừng và ghi câu hỏi mở:
- FR có AC đã duyệt.
- Tài liệu UI/UX và Design System của dự án.
- API contract Approved trong api-design. Chỉ chạy song song với `api-development` khi contract đã Approved.

Đọc: FR, AC; tài liệu UI/UX, Design System; api-design, system-architecture, coding-standards, security-standards; mã frontend hiện có.

## Quy trình

1. **Phân tích:** người dùng, màn hình, dữ liệu hiển thị, tương tác, trạng thái tải/lỗi/rỗng, hành vi phụ thuộc quyền.
2. **Khảo sát mã hiện có:** cấu trúc, routing, component dùng chung, cách gọi API. Tái dùng trước khi tạo mới.
3. **Hiện thực component** theo coding-standards và Design System.
4. **Form:** validate phía client chỉ để hỗ trợ người dùng, không thay backend; hiển thị lỗi validation từ server; chặn gửi trùng; phản hồi khi thành công.
5. **Tích hợp API** đúng contract; xử lý lỗi HTTP, mất mạng, đang tải.
6. **Quyền hiển thị** lấy từ backend hoặc session. Ẩn UI không phải kiểm quyền. Xử lý phiên hết hạn và phản hồi bị từ chối.
7. **Truy cập và đáp ứng** theo Design System.
8. **Test** bằng `unit-testing` (component, form) và `e2e-testing` (luồng chính theo AC).

## Giới hạn

- Không thêm thư viện UI hoặc nhân đôi component dùng chung.
- Không đổi quy ước giao diện toàn cục khi chưa được duyệt.
- Không đặt logic nghiệp vụ nhạy cảm chỉ ở frontend.

## Hoàn thành khi

- Giao diện khớp UI/UX và từng AC; trạng thái tải, lỗi, rỗng đều có.
- Test đã chạy, có output thật.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: trang và component đã tạo hoặc sửa, API đã tích hợp, giới hạn đã biết.
