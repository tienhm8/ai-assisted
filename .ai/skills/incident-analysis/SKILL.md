---
name: incident-analysis
description: Phân tích sự cố từ log, metric, trace do người xuất và đã che dữ liệu D3, dựng timeline, tách nguyên nhân đã xác nhận khỏi giả thuyết, soạn báo cáo sự cố Draft và bug; AI chỉ đọc và báo cáo.
---

# Incident Analysis Skill

Hiểu điều gì đã xảy ra, vì sao và ảnh hưởng ra sao, từ dữ liệu do người cung cấp. Chỉ đọc và báo cáo (A1); người quyết định cách xử lý.

## Cổng vào

- Log, metric, trace do người có quyền xuất và đã che D3. Thấy D3 chưa che thì dừng, báo và không dùng.
- Mô tả sự cố: thời điểm, triệu chứng, môi trường.
- Thiếu thì dừng và nêu cần dữ liệu gì.

Đọc: dữ liệu đã che, báo cáo người dùng; release report, báo cáo bàn giao, PR gần thời điểm sự cố; monitoring, deployment, backup-recovery; FR/AC liên quan.

## Quy trình

1. **Dựng timeline**, ghi nguồn cho mỗi mốc: phát hiện, tăng lỗi, thay đổi, xử lý.
2. **Liên hệ thay đổi gần nhất:** release, migration, cấu hình, hạ tầng.
3. **Tách** nguyên nhân đã xác nhận (có bằng chứng) khỏi giả thuyết (kèm cách kiểm chứng).
4. **Đánh giá tác động:** người dùng, module, dữ liệu, bảo mật, thời lượng.
5. **Đề xuất hành động tức thời** (rollback hay hotfix) theo deployment và backup-recovery; người quyết.
6. **Đề xuất phòng ngừa:** test, giám sát, cảnh báo, runbook còn thiếu.
7. **Tạo bug** theo BUG-TEMPLATE cho mỗi lỗi.
8. **Đề xuất Task tiếp theo** cho người quyết: sửa lỗi (T3) cho mỗi bug; kiểm tra bảo mật (T10) nếu liên quan bảo mật; cập nhật runbook (T12).

## Giới hạn

- Không chạy lệnh trên production; không tự rollback hay hotfix.
- Không quy lỗi cho cá nhân.

## Hoàn thành khi

- Mọi kết luận có bằng chứng hoặc ghi là giả thuyết.
- Bug đã tạo; dữ liệu còn thiếu đã nêu.

## Báo cáo

Báo cáo sự cố (Draft): tóm tắt, timeline, nguyên nhân gốc (đã xác nhận và giả thuyết), tác động, hành động tức thời và phòng ngừa đề xuất, dữ liệu còn thiếu, bug và câu hỏi mở đã tạo.
