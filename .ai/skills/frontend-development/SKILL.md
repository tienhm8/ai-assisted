---
name: frontend-development
description: Cài đặt trang, component, form, state và tích hợp API ở frontend theo yêu cầu Approved, thiết kế UI/UX và API contract, kèm danh sách ca cần test và báo cáo bàn giao.
---

# Frontend Development Skill

Hiện thực giao diện đúng FR/AC, thiết kế UI/UX và API contract; xử lý đủ trạng thái tải, lỗi, rỗng.

## Cổng vào

Ngoài `project-rules` 2, cần: tài liệu UI/UX và Design System của dự án; API contract trong api-design.

Nguồn chính: plan; tài liệu UI/UX và Design System phần màn hình liên quan; mã frontend hiện có.
Plan thiếu thì tra đúng mục, không đọc cả file: api-design §1.2 Chi tiết API (endpoint liên quan), §3.2 Quy ước chung; system-architecture §3.3 Các tầng và trách nhiệm; coding-standards §4 Naming Convention, §11.2 Frontend; security-standards §5 Kiểm tra đầu vào, §6.3 Che dữ liệu (masking).

## Quy trình

1. **Phân tích:** người dùng, màn hình, dữ liệu hiển thị, tương tác, trạng thái tải/lỗi/rỗng, hành vi phụ thuộc quyền.
2. **Khảo sát mã hiện có:** cấu trúc, routing, component dùng chung, cách gọi API. Tái dùng trước khi tạo mới.
3. **Hiện thực component** theo coding-standards và Design System.
4. **Form:** validate phía client chỉ để hỗ trợ người dùng, không thay backend; hiển thị lỗi validation từ server; chặn gửi trùng; phản hồi khi thành công.
5. **Tích hợp API** đúng contract; xử lý lỗi HTTP, mất mạng, đang tải.
6. **Quyền hiển thị** lấy từ backend hoặc session. Ẩn UI không phải kiểm quyền. Xử lý phiên hết hạn và phản hồi bị từ chối.
7. **Truy cập và đáp ứng** theo Design System.
8. **Ca cần test:** ghi vào plan §5, tầng unit (component, form) và e2e (luồng chính theo AC).

## Giới hạn

- Không thêm thư viện UI hoặc nhân đôi component dùng chung.
- Không đổi quy ước giao diện toàn cục khi chưa được duyệt.
- Không đặt logic nghiệp vụ nhạy cảm chỉ ở frontend.

## Hoàn thành khi

- Giao diện khớp UI/UX và từng AC; trạng thái tải, lỗi, rỗng đều có.
- Ca cần test ở bước 8 đã ghi vào plan.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: trang và component đã tạo hoặc sửa, API đã tích hợp, giới hạn đã biết.
