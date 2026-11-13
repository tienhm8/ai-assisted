---
name: e2e-testing
description: Thiết kế và chạy test end-to-end cho các hành trình người dùng quan trọng, truy vết về AC loại E2E, báo cáo bằng TEST-REPORT-TEMPLATE.
---

# E2E Testing Skill

Chứng minh các hành trình quan trọng chạy đúng từ góc nhìn người dùng.

## Cổng vào

- Task có AC loại E2E; hành trình lấy từ đó. Thiếu thì dừng và hỏi.
- Có môi trường chạy với dữ liệu giả. Không có thì ghi not-run kèm lý do và đề nghị miễn trừ có thời hạn.

Nguồn chính: plan (AC loại E2E → test); cấu hình tự động hoá trình duyệt hiện có.
Plan thiếu thì tra đúng mục, không đọc cả file: testing-strategy §4 Các tầng test, §7 Dữ liệu test (giả/ẩn danh), §8 Tự động hoá test; api-design §4 Authentication & Authorization; security-standards §4.2 Phân quyền theo vai trò.

## Quy trình

1. **Xác định hành trình** từ AC loại E2E.
2. **Persona:** một tài khoản test cho mỗi vai trò trong ma trận phân quyền, cộng khách chưa đăng nhập.
3. **Mô tả kịch bản** cho mỗi hành trình: tiền điều kiện, thao tác, hành vi UI mong đợi, thay đổi dữ liệu, hành vi khi lỗi.
4. **Viết test** bằng công cụ của dự án; selector ổn định (role, label, test id), không gắn với bố cục. Test mang ID AC.
5. **Ca âm:** đầu vào sai, truy cập trái phép, hành động bị cấm, phiên hết hạn, chuyển trạng thái sai, lỗi mạng, gửi trùng.
6. **Dữ liệu:** xác định, không dùng chung bản ghi sửa được, cô lập khi chạy song song, dọn sau khi chạy.
7. **Chạy:** test nhắm mục tiêu, bộ hành trình quan trọng, hồi quy. Khi lỗi thu ảnh chụp, trace, log.
8. **Phân loại lỗi:** ứng dụng, timing UI, môi trường, dữ liệu test, flaky.

## Giới hạn

- Không tăng timeout để che lỗi.
- Không bỏ qua xác thực hay phân quyền trong test.
- Không viết E2E cho từng hàm nhỏ; việc đó thuộc unit hoặc integration.

## Hoàn thành khi

- Mỗi hành trình trong phạm vi có test đạt cho luồng dương và luồng âm, đủ các vai trò liên quan.
- Test lặp lại được; test flaky đã điều tra.

## Báo cáo

Điền TEST-REPORT-TEMPLATE: hành trình và vai trò đã test kèm AC, ảnh chụp hoặc trace khi lỗi, test flaky đã biết.
