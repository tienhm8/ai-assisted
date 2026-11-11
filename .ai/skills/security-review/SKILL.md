---
name: security-review
description: Đánh giá rủi ro bảo mật của thay đổi hoặc hệ thống: xác thực, phân quyền, xử lý dữ liệu, input, phụ thuộc và cấu hình; có bằng chứng chạy thật và quy trình ngoại lệ.
---

# Security Review Skill

## 1. Mục tiêu

Phát hiện lỗ hổng và đánh giá hiệu quả của các biện pháp bảo vệ, dựa trên bằng chứng chạy thật khi có thể.

## 2. Cổng vào

- Có phạm vi review rõ (diff, module hoặc hệ thống) và mức rủi ro/mức dữ liệu của Task; thiếu thì dừng và hỏi.
- Chỉ kiểm thử trong phạm vi được phép. Không khai thác production, không kiểm thử phá huỷ khi chưa được duyệt.

## 3. Đầu vào

- Task, AC, security-standards, tài liệu kiến trúc (vai trò, ma trận phân quyền), api-design, database-design
- Rules: security-rules, testing-rules
- Mức dữ liệu D0–D3 (định nghĩa ở PROJECT.md và glossary)
- Mức ASVS mục tiêu (PROJECT.md §5) và bảng ánh xạ OWASP Top 10 (security-standards §13); chưa khai báo mức ASVS thì dừng và hỏi
- Mã nguồn, cấu hình triển khai, danh sách dependency

## 4. Quy trình

1. **Bề mặt tấn công**: endpoint công khai/đã xác thực/quản trị, upload, tích hợp ngoài, điểm nhận input, nơi lưu dữ liệu nhạy cảm. Gán mức D0–D3 cho dữ liệu liên quan.
2. **Xác thực**: lưu mật khẩu, đăng nhập, phiên, token, hết hạn, thu hồi, vòng đời tài khoản, rate limit và chống brute-force.
3. **Phân quyền**: thiếu kiểm quyền, leo thang đặc quyền, IDOR/BOLA, quyền trên chính bản ghi, ranh giới vai trò, truy cập chéo ứng dụng.
4. **Input/output**: injection (SQL, lệnh), XSS, CSRF, SSRF, path traversal, deserialization không an toàn, mã hoá đầu ra; upload (loại, kích thước, nội dung, nơi lưu, quyền truy cập).
5. **Bảo vệ dữ liệu**: lộ dữ liệu nhạy cảm, quản lý secret, mã hoá khi truyền/lưu, sao lưu. Dữ liệu D3 không được xuất hiện ở log, URL, thông báo lỗi hay prompt gửi AI.
6. **Audit log**: có ghi sự kiện bảo mật (đăng nhập, đổi quyền, truy cập bị từ chối, đổi cấu hình bảo mật) và không chứa D3.
7. **Dependency**: lỗ hổng đã biết, gói không còn hỗ trợ, quyền thừa, rủi ro chuỗi cung ứng.
8. **Hạ tầng/cấu hình**: biến môi trường, mức lộ CSDL, CORS, HTTPS, security headers, secret triển khai; toàn vẹn pipeline và artifact (security-standards §10.4).
9. **Đối chiếu OWASP/ASVS**: đi qua đủ A01–A10 theo bảng security-standards §13.2, ghi mỗi mục là áp dụng hay không áp dụng (kèm lý do); với mục áp dụng, đối chiếu các yêu cầu ở chương ASVS tương ứng tới mức dự án đã khai báo.
10. **Chạy bằng chứng thật khi có thể**: quét secret, quét dependency, test ranh giới quyền (vai trò sai, sai chủ sở hữu, chưa đăng nhập). Ghi lệnh và output. Công cụ chưa có thì ghi not-run kèm lý do, không suy diễn là an toàn.
11. **Đánh giá finding**: severity theo thang chung (Critical, High, Medium, Low, Informational) theo tác động, khả năng xảy ra, khả năng khai thác. Mỗi finding gắn mã OWASP Top 10 (ví dụ `A01:2025`) và mã yêu cầu ASVS bị vi phạm nếu xác định được (ví dụ `V8.2.1`).
12. **Xử lý finding**:
    - Critical/High: tạo BUG theo BUG-TEMPLATE; leo thang lên Tech Lead và Security.
    - Critical/High chưa sửa: hoặc chặn merge, hoặc có ngoại lệ ghi đủ lý do, biện pháp bù, người duyệt (Tech Lead và Security) và thời hạn.
    - Retest sau sửa, ghi vào TEST-REPORT.

## 5. Checklist

- [ ] Bề mặt tấn công và mức D của dữ liệu đã xác định.
- [ ] Xác thực (kể cả rate limit/brute-force) đã review.
- [ ] Phân quyền và quyền trên bản ghi đã review, có test ca không đủ quyền.
- [ ] Input/output, upload đã review.
- [ ] Dữ liệu D3 không ở log/URL/lỗi/prompt; audit log đủ sự kiện.
- [ ] Dependency, cấu hình, toàn vẹn pipeline/artifact đã review.
- [ ] Đã đi qua đủ A01–A10 (áp dụng / không áp dụng kèm lý do) và chương ASVS tương ứng ở mức đã khai báo.
- [ ] Bằng chứng chạy thật (hoặc not-run kèm lý do) cho secret scan, quét dependency, test ranh giới quyền.
- [ ] Mỗi finding có bằng chứng, tác động, biện pháp khả thi, mã OWASP (và mã ASVS nếu có).

## 6. Việc không được làm

- Kiểm thử ngoài phạm vi được phép; khai thác production; kiểm thử phá huỷ khi chưa duyệt.
- Truy cập dữ liệu khách hàng không liên quan; đưa secret vào báo cáo.
- Kết luận hệ thống an toàn chỉ nhờ đọc code.
- Tắt hoặc nới kiểm tra bảo mật (lint, scan, xác thực, test) để qua cổng.
- Tự đổi chính sách bảo mật khi chưa được duyệt.

## 7. Tiêu chí hoàn thành (DoD)

- Phạm vi đã review hết, finding có severity và biện pháp.
- Critical/High đã leo thang và được sửa, chặn merge hoặc có ngoại lệ hợp lệ còn hạn.
- Có yêu cầu retest; bằng chứng chạy thật đã ghi.

## 8. Báo cáo bàn giao

- Phạm vi, bề mặt tấn công, mức D liên quan, mức ASVS mục tiêu
- Bảng A01–A10: áp dụng / không áp dụng, chương ASVS đã đối chiếu, kết quả
- Biện pháp đã đánh giá và bằng chứng (lệnh, output; not-run kèm lý do)
- Finding theo severity: mã OWASP/ASVS, bằng chứng, tác động, biện pháp; mã BUG cho Critical/High
- Ngoại lệ đang áp dụng (lý do, biện pháp bù, người duyệt, thời hạn)
- Rủi ro còn lại và yêu cầu retest
