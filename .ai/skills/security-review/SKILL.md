---
name: security-review
description: Đánh giá rủi ro bảo mật của thay đổi hoặc hệ thống: xác thực, phân quyền, xử lý dữ liệu, input, phụ thuộc và cấu hình; có bằng chứng chạy thật và quy trình ngoại lệ.
---

# Security Review Skill

Phát hiện lỗ hổng và đánh giá hiệu quả của biện pháp bảo vệ, dựa trên bằng chứng chạy thật khi có thể.

## Cổng vào

- Phạm vi review rõ (diff, module hoặc hệ thống), kèm mức rủi ro và mức dữ liệu. Thiếu thì dừng và hỏi.
- Mức ASVS mục tiêu đã khai báo ở PROJECT.md §5. Chưa có thì dừng và hỏi.

Đọc: Task, AC; security-standards; tài liệu kiến trúc (vai trò, ma trận phân quyền), api-design, database-design; PROJECT.md §4; mã nguồn, cấu hình triển khai, danh sách dependency.

## Quy trình

1. **Bề mặt tấn công:** endpoint công khai, đã xác thực, quản trị; upload; tích hợp ngoài; điểm nhận input; nơi lưu dữ liệu nhạy cảm. Gán mức dữ liệu.
2. **Xác thực:** lưu mật khẩu, đăng nhập, phiên, token, hết hạn, thu hồi, vòng đời tài khoản, rate limit và chống brute-force.
3. **Phân quyền:** thiếu kiểm quyền, leo thang đặc quyền, IDOR/BOLA, quyền trên từng bản ghi, ranh giới vai trò, truy cập chéo ứng dụng.
4. **Input và output:** injection (SQL, lệnh), XSS, CSRF, SSRF, path traversal, deserialization; upload (loại, kích thước, nội dung, nơi lưu, quyền truy cập).
5. **Bảo vệ dữ liệu:** lộ dữ liệu nhạy cảm, quản lý secret, mã hoá khi truyền và khi lưu, sao lưu; D3 trong log, URL, thông báo lỗi.
6. **Audit log:** đủ sự kiện bảo mật và không chứa D3.
7. **Dependency:** lỗ hổng đã biết, gói hết hỗ trợ, quyền thừa, rủi ro chuỗi cung ứng.
8. **Cấu hình:** biến môi trường, mức lộ CSDL, CORS, HTTPS, security headers; toàn vẹn pipeline và artifact.
9. **Đối chiếu OWASP Top 10 và ASVS** theo bảng ánh xạ trong security-standards: mỗi mục ghi áp dụng hay không kèm lý do; mục áp dụng thì đối chiếu chương ASVS tới mức dự án khai báo.
10. **Chạy bằng chứng thật:** quét secret, quét dependency, test ranh giới quyền (sai vai trò, sai chủ sở hữu, chưa đăng nhập). Công cụ chưa có thì ghi not-run kèm lý do; không suy ra là an toàn.
11. **Đánh giá finding** theo tác động, khả năng xảy ra, khả năng khai thác. Gắn mã OWASP Top 10 và mã yêu cầu ASVS nếu xác định được.
12. **Xử lý:** Critical/High tạo bug theo BUG-TEMPLATE và báo Tech Lead, Security. Chưa sửa thì chặn merge, hoặc có ngoại lệ ghi lý do, biện pháp bù, người duyệt và thời hạn. Kiểm lại sau khi sửa.

## Giới hạn

- Không kiểm thử ngoài phạm vi được phép; không khai thác production.
- Không kết luận an toàn chỉ nhờ đọc code.
- Chỉ khuyến nghị; không tự đổi chính sách bảo mật.

## Hoàn thành khi

- Đã đi hết phạm vi; mỗi finding có bằng chứng, tác động, mức nghiêm trọng, biện pháp.
- Critical/High đã sửa, chặn merge, hoặc có ngoại lệ còn hạn.

## Báo cáo

- Phạm vi, bề mặt tấn công, mức dữ liệu, mức ASVS mục tiêu.
- Bảng OWASP Top 10: áp dụng hay không, chương ASVS đã đối chiếu, kết quả.
- Bằng chứng: lệnh, output; not-run kèm lý do.
- Finding theo mức nghiêm trọng, kèm mã OWASP/ASVS và mã bug.
- Ngoại lệ đang áp dụng; rủi ro còn lại; yêu cầu kiểm lại.
