---
name: code-review
description: Review có cấu trúc một thay đổi code theo phiếu Task, AC, kiến trúc và rules trước khi merge; đối chiếu Task với diff và kiểm bằng chứng test.
---

# Code Review Skill

## 1. Mục tiêu

Xác nhận thay đổi đúng phạm vi Task, đáp ứng AC, tuân thủ kiến trúc và rules, và có bằng chứng kiểm thử thật trước khi merge.

## 2. Cổng vào

- Có phiếu Task (phạm vi, AC, mức rủi ro, Definition of Done), diff và kết quả test; thiếu thì dừng và hỏi.
- Mức review R1–R3 được xác định ở Bước 0.

## 3. Đầu vào

- Task, AC (acceptance-criteria), FR/BR liên quan
- Tài liệu kiến trúc, coding-standards, testing-strategy
- Rules: project-rules, coding-rules, architecture-rules, database-rules, security-rules, testing-rules
- Git diff và báo cáo test (TEST-REPORT)

## 4. Quy trình

### Bước 0: Xác định mức review (R1–R3)

Task phải mang mức rủi ro review; thiếu thì dừng và hỏi, không tự gán.

| Mức | Khi nào | Cách review |
| --- | --- | --- |
| R1 (thấp) | Thay đổi nhỏ, không chạm vùng 🟡/🔴, không chạm xác thực, phân quyền, tiền, dữ liệu cá nhân hay migration | Một reviewer |
| R2 (vừa) | Logic nghiệp vụ, API, schema trong phạm vi Task, hoặc có file vùng 🟡 | Một reviewer; kích hoạt `security-review` nếu chạm điều kiện bảo mật |
| R3 (cao) | Chạm tiền, phân quyền, dữ liệu cá nhân, secret, migration production, hoặc file vùng 🔴 | Hai reviewer, trong đó một người độc lập với người/AI viết code; thiếu người thì ghi miễn trừ có thời hạn |

Mức càng cao review càng chặt. AI không tự duyệt thay đổi do chính mình viết.

### Bước 1: Đối chiếu Task với diff

- Liệt kê file đổi, module bị ảnh hưởng; so với phạm vi trong phiếu Task.
- Báo file thuộc vùng 🟡/🔴 và file ngoài phạm vi.
- Báo test bị xoá, tắt hoặc làm yếu; cột/bảng bị xoá ngoài phạm vi.
- Kiểm Definition of Done của Task đã đạt từng mục.

### Bước 2: Tính đúng đắn

Logic nghiệp vụ, kiểm tra đầu vào, ca biên, chuyển trạng thái, xử lý lỗi, nhất quán dữ liệu.

### Bước 3: Kiến trúc và chất lượng

Ranh giới tầng, hướng phụ thuộc, trách nhiệm module, trùng lặp, đặt tên, độ phức tạp, dead code, cơ chế nới lỏng kiểu thiếu lý do, trừu tượng thừa.

### Bước 4: Hiệu năng

Mẫu truy vấn, N+1, tính toán và gọi mạng thừa, bộ nhớ.

### Bước 5: Bảo mật

Nếu diff chạm xác thực, phân quyền, dữ liệu nhạy cảm hoặc input từ bên ngoài thì kích hoạt `security-review`; không tự làm thay trong skill này.

### Bước 6: Kiểm thử và bằng chứng

- Mỗi AC của Task có test truy vết (tên/chú thích mang ID AC) và output test thật. AC không có bằng chứng là finding High.
- Nhánh quan trọng và ca lỗi/từ chối quyền được test; test có ý nghĩa, không bị làm yếu.
- Sửa lỗi có regression test đỏ trước, xanh sau.
- Kết quả các cổng (build, lint, kiểm tra kiểu, test, quét secret) lấy từ CI; chưa có CI thì lấy từ lần chạy cục bộ ghi trong báo cáo, kèm lệnh và output. Không có thì coi là not-run.

### Bước 7: Báo cáo phát hiện

Phân loại theo thang severity chung (Critical, High, Medium, Low, Informational). Mỗi finding nêu file và vị trí khi có thể, kèm bằng chứng kỹ thuật.

## 5. Checklist

- [ ] Thay đổi đáp ứng Task và AC; không có thay đổi ngoài phạm vi chưa khai báo.
- [ ] Không tự suy diễn quy tắc nghiệp vụ.
- [ ] Tuân thủ rules (coding, architecture, database, security, testing).
- [ ] Phân quyền kiểm ở backend; đầu vào được kiểm; không lộ secret hay dữ liệu nhạy cảm (bảo mật chi tiết do `security-review` khi được kích hoạt).
- [ ] Xử lý lỗi tường minh; không trùng logic, không dead code, không cơ chế nới lỏng kiểu thiếu lý do.
- [ ] Hiệu năng truy vấn hợp lý.
- [ ] Mỗi AC có test truy vết và output thật; test fail/skip được báo rõ; không test bị làm yếu.
- [ ] Tài liệu liên quan được cập nhật.
- [ ] Definition of Done của Task đạt.
- [ ] Không còn finding Critical/High chưa xử lý.

## 6. Việc không được làm

- Duyệt khi còn finding Critical/High chưa xử lý.
- Cho rằng code đúng chỉ vì test pass.
- Viết lại code ngoài phạm vi trong lúc review.
- Bịa lỗi không có bằng chứng kỹ thuật.
- Tự duyệt thay đổi do chính mình viết, hoặc coi đó là review độc lập.

## 7. Tiêu chí hoàn thành (DoD)

- Mọi finding có severity, vị trí và yêu cầu sửa.
- Bằng chứng test đã được đánh giá.
- Có kết luận merge: duyệt / duyệt có điều kiện / không duyệt.

## 8. Báo cáo bàn giao

- Tóm tắt review, mức R, file đã review (kể cả file vùng 🟡/🔴 và ngoài phạm vi)
- Finding theo severity, mỗi cái có file/vị trí và yêu cầu sửa
- Đánh giá test: AC có/thiếu bằng chứng, nguồn kết quả cổng (CI hoặc cục bộ)
- Điểm tốt đáng ghi nhận
- Kết luận merge
