---
name: integration-testing
description: Thiết kế và chạy integration test để kiểm chứng tương tác giữa API, service, CSDL và phụ thuộc ngoài, truy vết về AC, báo cáo bằng TEST-REPORT-TEMPLATE.
---

# Integration Testing Skill

## 1. Mục tiêu

Chứng minh các thành phần phối hợp đúng qua các ranh giới đã định (API, CSDL, phân quyền, hệ thống ngoài).

## 2. Cổng vào

- Task có AC (`<FR>-AC<N>`) và mức rủi ro; thiếu thì dừng và hỏi.
- Có môi trường test cô lập (local hoặc CSDL tạm có thể huỷ). Không có thì ghi not-run kèm lý do và miễn trừ có thời hạn.

## 3. Đầu vào

- Task, acceptance-criteria, FR/BR liên quan
- testing-strategy, api-design, database-design, tài liệu kiến trúc (ranh giới, phân quyền)
- Rules: testing-rules, security-rules, database-rules
- Hạ tầng test hiện có

## 4. Quy trình

1. **Xác định ranh giới**: API-service, service-CSDL, service-service, xác thực-phân quyền, ứng dụng-hệ thống ngoài, producer-consumer.
2. **Liệt kê kịch bản** theo AC: thành công, request sai, vi phạm ràng buộc CSDL, giao dịch lỗi, đồng thời, timeout, hệ thống ngoài lỗi, và **ca không đủ quyền** (vai trò sai, sai chủ sở hữu bản ghi, chưa đăng nhập).
3. **Chuẩn bị môi trường**: CSDL test cô lập, áp migration, dữ liệu xác định, thông tin xác thực test là giả (không dùng secret thật), cô lập phụ thuộc ngoài.
4. **Dữ liệu**: chỉ dữ liệu giả hoặc ẩn danh. Không dùng và không chạm dữ liệu production, kể cả khi được duyệt.
5. **Viết test** kiểm: luồng dữ liệu thật, hợp đồng request/response, lưu trữ, giao dịch và rollback, lan truyền lỗi, thực thi phân quyền. Dùng hạ tầng thật ở ranh giới đang kiểm.
6. **Nhất quán dữ liệu**: khoá ngoại, unique, nguyên tử, cập nhật đồng thời, request trùng, phục hồi khi lỗi từng phần.
7. **Kiểm tra migration** (khi đổi schema): chạy trên CSDL sạch từ đầu đến cuối, kiểm cách khôi phục (rollback hoặc dựng lại), ghi lệnh và output.
8. **Chạy và phân tích lỗi**: phân loại lỗi ứng dụng, môi trường, dữ liệu test, cấu hình, phụ thuộc ngoài. Chưa có CI thì chạy tại máy và ghi miễn trừ có thời hạn.
9. **Dọn dẹp** dữ liệu và tài nguyên test.

## 5. Checklist

- [ ] Mỗi ranh giới quan trọng có test, mang ID AC.
- [ ] Có ca thành công, lỗi, và không đủ quyền.
- [ ] Ràng buộc CSDL, giao dịch, rollback được kiểm.
- [ ] Lỗi phụ thuộc ngoài được kiểm.
- [ ] Dữ liệu giả/ẩn danh, thông tin xác thực test là giả.
- [ ] Migration đã chạy trên DB sạch và có cách khôi phục (nếu đổi schema).
- [ ] Test lặp lại được, dọn dẹp an toàn.

## 6. Việc không được làm

- Dùng hoặc chạm dữ liệu production, kể cả khi được duyệt.
- Thay toàn bộ integration test bằng mock.
- Bỏ qua lỗi ràng buộc CSDL hoặc che lỗi môi trường mà không báo.
- Xoá, tắt, làm yếu test hoặc hạ ngưỡng để qua cổng.
- Sửa cấu hình production; đưa secret thật vào test.

## 7. Tiêu chí hoàn thành (DoD)

- Mọi AC trong phạm vi có test đạt; AC chưa có test ghi vào "Còn thiếu".
- Test chạy trong môi trường cô lập, kết quả lặp lại được.
- Lỗi đã xử lý hoặc ghi lại; không có skipped nào chưa báo.

## 8. Báo cáo bàn giao

Điền TEST-REPORT-TEMPLATE, gồm:
- Ranh giới đã test, kịch bản, AC tương ứng (file::tên)
- Môi trường dùng (local/DB tạm, phiên bản)
- Lệnh đã chạy và output thật; pass / fail / skipped / not-run kèm lý do
- Kết quả kiểm migration (nếu có)
- Phát hiện về toàn vẹn dữ liệu, còn thiếu và rủi ro còn lại
