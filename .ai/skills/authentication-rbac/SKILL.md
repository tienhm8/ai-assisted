---
name: authentication-rbac
description: Cài đặt và rà soát xác thực, phân quyền, RBAC, quản lý phiên và kiểm quyền theo tài nguyên theo chính sách truy cập đã Approved; mặc định từ chối, kiểm ở backend.
---

# Authentication & RBAC Skill

## 1. Mục tiêu

Hiện thực xác thực và phân quyền đúng chính sách đã duyệt, thực thi ở backend, mặc định từ chối.

## 2. Cổng vào

Dừng và ghi `open-questions.md` (OQ-<NN>) nếu thiếu:
- FR có AC và thiết kế Approved: RBAC, Permission Matrix, Session Policy.
- Chính sách chưa chốt: coi là OQ, không tự suy diễn.

Việc **đổi mô hình vai trò, quyền hoặc chính sách phiên** thì dừng: cần Tech Lead + Security duyệt. Trước khi sửa file auth, kiểm bản đồ vùng 🟢🟡🔴 của dự án.

Mặc định mức rủi ro R3: bắt buộc chạy `security-review`.

## 3. Đầu vào

- Tài liệu kiến trúc và bảo mật của dự án (RBAC, Permission Matrix, Session Policy)
- Đặc tả API, quy ước xử lý lỗi, FR/AC
- Mã xác thực/phân quyền hiện có

## 4. Quy trình

1. **Đọc chính sách đã duyệt**: phương thức xác thực, vai trò, quyền, phạm vi tài nguyên, ranh giới phiên, vòng đời tài khoản.
2. **Thiết kế xác thực** theo kiến trúc đã duyệt (đăng ký, đăng nhập, đăng xuất, mật khẩu, trạng thái tài khoản).
3. **Phân quyền ở backend**: kiểm vai trò, quyền, sở hữu, phạm vi; mặc định từ chối; không dựa vào hiển thị UI.
4. **Ranh giới ứng dụng**: nếu hệ thống có nhiều ứng dụng, giữ ranh giới truy cập và chính sách phiên theo spec; chặn truy cập chéo trái phép.
5. **Truy cập theo tài nguyên**: người dùng chỉ truy cập tài nguyên được cấp; không giả định vai trò nào có quyền tuyệt đối.
6. **Phiên**: theo security-standards.md; không tự đặt chính sách phiên chưa chốt.
7. **Test ranh giới quyền**: gọi `integration-testing` (và `e2e-testing` nếu cần). Phủ: chưa xác thực, sai vai trò, sai chủ sở hữu, ngoài phạm vi, phiên hết hạn/thu hồi, vai trò giả từ client, truy cập chéo ứng dụng. Mã 401/403/404 theo error-handling.md.
8. **Rà soát**: gọi `security-review`.
9. **Bàn giao**: theo mục 8.

## 5. Checklist

- [ ] Xác thực thực thi đúng; mật khẩu xử lý an toàn.
- [ ] Phân quyền ở backend, default-deny.
- [ ] Kiểm sở hữu và phạm vi.
- [ ] Thu hồi phiên được xét.
- [ ] Không chính sách chưa chốt nào bị ngầm giả định.

## 6. Việc không được làm

- Không bỏ qua phân quyền backend.
- Không tin vai trò do client gửi.
- Không tự gán quyền ngầm; không mặc định Admin có mọi quyền.
- Không đổi vai trò/quyền/chính sách phiên đã duyệt khi chưa có duyệt.
- Không nới xác thực để test qua.

## 7. Tiêu chí hoàn thành (DoD)

- Cổng vào thoả; phân quyền thực thi ở backend và đã test ranh giới.
- `security-review` hoàn tất; phát hiện nghiêm trọng đã xử lý.
- Thay đổi nhạy cảm đã được duyệt.
- Tài liệu bị ảnh hưởng đã cập nhật hoặc ghi lại cần cập nhật.

## 8. Báo cáo bàn giao

- Thay đổi xác thực, vai trò/quyền, phiên
- API/tài nguyên được bảo vệ
- Test ranh giới quyền đã chạy và kết quả
- Phát hiện từ security-review, rủi ro còn lại
- Quyết định cần duyệt, OQ còn mở
