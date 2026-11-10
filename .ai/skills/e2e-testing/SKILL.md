---
name: e2e-testing
description: Thiết kế và chạy test end-to-end cho các hành trình người dùng quan trọng, truy vết về AC loại E2E, báo cáo bằng TEST-REPORT-TEMPLATE.
---

# E2E Testing Skill

## 1. Mục tiêu

Chứng minh các hành trình quan trọng chạy đúng từ góc nhìn người dùng.

## 2. Cổng vào

- Task có AC (`<FR>-AC<N>`); journey quan trọng lấy từ AC loại E2E. Thiếu thì dừng và hỏi.
- Chạy tại máy với dữ liệu giả. Không có môi trường chạy thì ghi not-run kèm lý do và miễn trừ có thời hạn.

## 3. Đầu vào

- Task, acceptance-criteria (AC loại E2E), user story
- testing-strategy, api-design, tài liệu kiến trúc (vai trò/ma trận phân quyền)
- Rules: testing-rules, security-rules
- Cấu hình tự động hoá trình duyệt hiện có

## 4. Quy trình

1. **Xác định journey**: các journey quan trọng lấy từ AC loại E2E. Ví dụ xem examples.md (chỉ minh hoạ).
2. **Xác định persona**: một tài khoản test cho mỗi vai trò trong ma trận phân quyền, cộng khách chưa đăng nhập; chỉ dùng quyền đã được duyệt.
3. **Mô tả kịch bản** cho mỗi journey: tiền điều kiện, thao tác, hành vi UI mong đợi, phản hồi hệ thống, thay đổi dữ liệu, hành vi khi lỗi. Test mang ID AC.
4. **Viết test** bằng công cụ tự động hoá của dự án; selector ổn định (role, label, test id), không gắn với bố cục.
5. **Ca âm**: đầu vào sai, truy cập trái phép, hành động bị cấm, phiên hết hạn, chuyển trạng thái sai, lỗi mạng, gửi trùng.
6. **Dữ liệu**: dữ liệu giả xác định, không dùng chung bản ghi có thể sửa, cô lập khi chạy song song, dọn an toàn. Không dùng dữ liệu D3 thật.
7. **Chạy**: test nhắm mục tiêu, bộ journey quan trọng, hồi quy. Khi lỗi thu ảnh chụp, trace, log. Chưa có CI thì chạy tại máy và ghi miễn trừ có thời hạn.
8. **Phân tích lỗi**: lỗi ứng dụng, timing UI, môi trường, dữ liệu test, flaky. Không tăng timeout để che lỗi.

## 5. Checklist

- [ ] Mỗi journey từ AC E2E có test, mang ID AC.
- [ ] Mọi vai trò liên quan và khách chưa đăng nhập được đại diện.
- [ ] Có luồng dương và luồng âm; ranh giới quyền được kiểm.
- [ ] Dữ liệu cô lập, selector ổn định, test lặp lại được.
- [ ] Có bằng chứng khi lỗi; flaky được điều tra.

## 6. Việc không được làm

- Chạy test phá huỷ trên production; dùng thông tin đăng nhập hay dữ liệu D3 thật.
- Làm yếu assertion, xoá hay tắt test, hạ ngưỡng để che lỗi.
- Bỏ qua xác thực/phân quyền trong test.
- Viết E2E cho từng hàm nhỏ (thuộc unit/integration).

## 7. Tiêu chí hoàn thành (DoD)

- Mọi journey trong phạm vi có test đạt; AC chưa có test ghi vào "Còn thiếu".
- Lỗi đã điều tra; không có skipped chưa báo; có bằng chứng chạy.

## 8. Báo cáo bàn giao

Điền TEST-REPORT-TEMPLATE, gồm:
- Journey và vai trò đã test, AC tương ứng (file::tên)
- Lệnh đã chạy và output thật; pass / fail / skipped / not-run kèm lý do
- Ảnh chụp/trace khi lỗi, test flaky đã biết
- Còn thiếu và rủi ro còn lại
