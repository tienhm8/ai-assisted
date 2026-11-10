---
name: bug-fixing
description: Sửa lỗi theo Bug Report (BUG-TEMPLATE) so với yêu cầu và AC đã duyệt - tái hiện, tìm nguyên nhân gốc, sửa tối thiểu, thêm test hồi quy; dừng khi lỗi do yêu cầu sai/thiếu.
---

# Bug Fixing Skill

## 1. Mục tiêu

Sửa đúng nguyên nhân gốc của lỗi (sai khác so với yêu cầu và AC đã duyệt) với thay đổi tối thiểu, không gây hồi quy.

## 2. Cổng vào

Đầu vào là Bug Report theo BUG-TEMPLATE. **Thiếu một trong các mục sau thì dừng và yêu cầu bổ sung:** BUG-ID, FR/BR/AC bị vi phạm, Task sửa lỗi, mức nghiêm trọng, mức rủi ro R1–R3 (lấy từ Task, không tự gán).

## 3. Đầu vào

Bug Report, Task, yêu cầu liên quan (FR/BR/AC), mã nguồn và test liên quan.

## 4. Quy trình

1. **Hiểu lỗi và xác định yêu cầu bị vi phạm** (FR/BR/AC). Nếu AC thiếu hoặc mơ hồ, hoặc tài liệu mâu thuẫn nhau: **dừng**, ghi `OQ-<NN>` và chuyển requirement-review; không tự quyết. Lỗi do yêu cầu sai/thiếu thì không sửa tại đây; không sửa BR.
2. **Tái hiện** ở local hoặc staging. Không truy cập CSDL production; che dữ liệu nhạy cảm; không dán log hay dữ liệu production thật. Không tái hiện được thì không tuyên bố đã tái hiện.
3. **Tìm nguyên nhân gốc,** phân biệt với triệu chứng. Không xác lập được đáng tin cậy thì dừng và báo.
4. **Đánh giá tác động:** module, vai trò, dữ liệu, bảo mật, hồi quy. Lỗi cần migration dữ liệu production thì tách Task riêng, có duyệt.
5. **Đề xuất sửa** (nguyên nhân, cách sửa, file, rủi ro, test). Cần duyệt trước khi sửa nếu: R3 hoặc mức tự chủ A2 (duyệt từng bước); hoặc đụng RBAC, kiến trúc, schema, contract.
6. **Viết test hồi quy** bằng unit-testing hoặc integration-testing: chạy thấy đỏ trước khi sửa, xanh sau khi sửa.
7. **Sửa tối thiểu** đúng nguyên nhân gốc; không refactor lan man.
8. **Chạy cổng kiểm tra** của dự án và hồi quy liên quan, tối đa **3 vòng** sửa–chạy; quá thì dừng và báo. Lỗi bảo mật Critical/High phát hiện thì quay lại security-review.
9. **Cập nhật tài liệu** nếu cần bằng skill documentation.
10. **Commit/PR** ghi TASK-ID. Bàn giao cho code-review ở phiên khác.

Lỗi Critical trên production: hotfix là Task riêng, vẫn qua code-review (quy trình phát hành xem deployment).

## 5. Checklist

- [ ] Bug Report đủ mục bắt buộc; yêu cầu bị vi phạm đã xác định.
- [ ] Tái hiện ghi lại, dữ liệu nhạy cảm đã che.
- [ ] Nguyên nhân gốc đã nêu; tác động đã đánh giá.
- [ ] Test hồi quy đỏ trước, xanh sau, kèm output thật.
- [ ] Không thay đổi ngoài phạm vi; test không bị làm yếu.
- [ ] Trong giới hạn 3 vòng; cần duyệt thì đã có duyệt.

## 6. Việc không được làm

- Không sửa BR hoặc tự suy ra nghiệp vụ; không sửa khi AC mơ hồ.
- Không che lỗi (nuốt lỗi, workaround), không tắt hay làm yếu test.
- Không truy cập hay sửa dữ liệu production để né lỗi.
- Không khẳng định đã sửa khi chưa chạy test.
- Không tự duyệt bản sửa của mình.

## 7. Tiêu chí hoàn thành (DoD)

- Nguyên nhân gốc đã ghi, bản sửa và test hồi quy đã có.
- Cổng kiểm tra và hồi quy liên quan đạt, có bằng chứng.
- Đã bàn giao cho code-review; chờ người xác nhận đóng lỗi.

## 8. Báo cáo bàn giao

Điền mục "Báo cáo bàn giao" trong BUG-TEMPLATE (nguyên nhân gốc, test hồi quy và kết quả trước/sau, AC được phủ lại, file đã sửa, tài liệu cần cập nhật, rủi ro còn lại). Giả định và OQ chưa giải quyết ghi kèm.
