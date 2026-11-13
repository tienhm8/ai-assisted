---
name: integration-testing
description: Thiết kế và chạy integration test để kiểm chứng tương tác giữa API, service, CSDL và phụ thuộc ngoài, truy vết về AC, báo cáo bằng TEST-REPORT-TEMPLATE.
---

# Integration Testing Skill

Chứng minh các thành phần phối hợp đúng qua ranh giới: API, CSDL, phân quyền, hệ thống ngoài.

## Cổng vào

- Task có AC. Thiếu thì dừng và hỏi.
- Có môi trường test cô lập (local hoặc CSDL tạm huỷ được). Không có thì ghi not-run kèm lý do và đề nghị miễn trừ có thời hạn.

Nguồn chính: plan (AC → test); hạ tầng test hiện có.
Plan thiếu thì tra đúng mục, không đọc cả file: testing-strategy §4 Các tầng test, §7 Dữ liệu test (giả/ẩn danh), §10 Môi trường test; api-design §1.2 Chi tiết API (endpoint liên quan); database-design §6 Transaction và đồng thời; module-design §4 Giao tiếp giữa các module; security-standards §4 Authorization.

## Quy trình

1. **Xác định ranh giới:** API–service, service–CSDL, service–service, xác thực–phân quyền, ứng dụng–hệ thống ngoài, producer–consumer.
2. **Liệt kê kịch bản** theo AC: thành công, request sai, vi phạm ràng buộc CSDL, giao dịch lỗi, đồng thời, timeout, hệ thống ngoài lỗi, không đủ quyền (sai vai trò, sai chủ sở hữu, chưa đăng nhập).
3. **Chuẩn bị môi trường:** CSDL test cô lập, áp migration, dữ liệu xác định, thông tin xác thực giả, cô lập phụ thuộc ngoài.
4. **Viết test** kiểm luồng dữ liệu thật, hợp đồng request/response, lưu trữ, transaction và rollback, lan truyền lỗi, thực thi phân quyền. Dùng hạ tầng thật ở ranh giới đang kiểm; test mang ID AC.
5. **Nhất quán dữ liệu:** khoá ngoại, unique, tính nguyên tử, cập nhật đồng thời, request trùng, phục hồi khi lỗi từng phần.
6. **Migration** (khi đổi schema): chạy từ đầu trên CSDL sạch, kiểm cách khôi phục.
7. **Chạy và phân loại lỗi:** ứng dụng, môi trường, dữ liệu test, cấu hình, phụ thuộc ngoài.
8. **Dọn dẹp** dữ liệu và tài nguyên test.

## Giới hạn

- Không dùng dữ liệu production, kể cả khi được duyệt.
- Không thay toàn bộ integration test bằng mock.
- Không che lỗi môi trường.

## Hoàn thành khi

- Mỗi ranh giới quan trọng có test cho ca thành công, lỗi và không đủ quyền.
- Test lặp lại được trong môi trường cô lập.

## Báo cáo

Điền TEST-REPORT-TEMPLATE: ranh giới và kịch bản đã test kèm AC, môi trường đã dùng, kết quả kiểm migration, phát hiện về toàn vẹn dữ liệu.
