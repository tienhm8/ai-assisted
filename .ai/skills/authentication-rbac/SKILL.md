---
name: authentication-rbac
description: Cài đặt và rà soát xác thực, phân quyền, RBAC, quản lý phiên và kiểm quyền theo tài nguyên theo chính sách truy cập đã Approved; mặc định từ chối, kiểm ở backend.
---

# Authentication & RBAC Skill

Hiện thực xác thực và phân quyền đúng chính sách đã duyệt, thực thi ở backend, mặc định từ chối. Mặc định là việc R3.

## Cổng vào

Ngoài `project-rules` 2, thiết kế phải có mô hình vai trò, ma trận quyền, chính sách phiên. Phần chưa chốt là câu hỏi mở, không tự suy diễn.

Việc **đổi** mô hình vai trò, quyền hoặc chính sách phiên: dừng, cần Tech Lead và Security duyệt. Trước khi sửa file auth, kiểm bản đồ vùng của dự án.

Nguồn chính: plan; mã xác thực và phân quyền hiện có.
Plan thiếu thì tra đúng mục, không đọc cả file: system-architecture §6 Authentication & Authorization (thiết kế); security-standards §3 Authentication, §4 Authorization, §9 Logging và Audit; api-design §4 Authentication & Authorization; error-handling §5.2 Ánh xạ HTTP status.

## Quy trình

1. **Đọc chính sách đã duyệt:** phương thức xác thực, vai trò, quyền, phạm vi tài nguyên, ranh giới phiên, vòng đời tài khoản.
2. **Xác thực** theo kiến trúc đã duyệt: đăng ký, đăng nhập, đăng xuất, mật khẩu, trạng thái tài khoản.
3. **Phân quyền ở backend:** kiểm vai trò, quyền, chủ sở hữu, phạm vi; mặc định từ chối. Không giả định vai trò nào có mọi quyền.
4. **Ranh giới ứng dụng:** hệ thống có nhiều ứng dụng thì giữ ranh giới truy cập và chính sách phiên theo spec; chặn truy cập chéo.
5. **Phiên** theo security-standards, kể cả hết hạn và thu hồi.
6. **Ca cần test ranh giới quyền:** ghi vào plan §5, tầng integration (e2e nếu cần). Phủ: chưa xác thực, sai vai trò, sai chủ sở hữu, ngoài phạm vi, phiên hết hạn hoặc đã thu hồi, vai trò giả do client gửi, truy cập chéo ứng dụng. Mã phản hồi theo error-handling.

## Hoàn thành khi

- Mọi tài nguyên trong phạm vi được kiểm quyền ở backend, mặc định từ chối.
- Ca cần test ở bước 6 đã ghi vào plan.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: thay đổi về xác thực, vai trò, quyền, phiên; tài nguyên được bảo vệ.
