---
name: incident-analysis
description: Phân tích sự cố từ log, metric, trace do người xuất và đã che dữ liệu D3, dựng timeline, tách nguyên nhân đã xác nhận khỏi giả thuyết, soạn báo cáo sự cố Draft và bug; AI chỉ đọc và báo cáo.
---

# Incident Analysis Skill

## 1. Mục tiêu

Hiểu điều gì đã xảy ra, vì sao và ảnh hưởng ra sao, từ dữ liệu người cung cấp. Mức tự chủ A1: chỉ đọc và báo cáo. Quyết định xử lý (rollback, hotfix) do người.

## 2. Cổng vào

- Có log/metric/trace do người có quyền xuất, đã che dữ liệu D3 (secret, token, dữ liệu cá nhân). Phát hiện D3 chưa che thì dừng, báo và không dùng.
- Có mô tả sự cố: thời điểm, triệu chứng, môi trường.
- Thiếu thì dừng, ghi OQ-<NN> nêu cần dữ liệu gì.

## 3. Đầu vào

- Log, metric, trace đã che; báo cáo người dùng
- Release report, Delivery Report, PR/Task gần thời điểm sự cố
- Tài liệu vận hành của dự án: monitoring, deployment, backup-recovery
- BUG-TEMPLATE, FR/AC liên quan

## 4. Quy trình

1. **Dựng timeline** theo thời gian, ghi nguồn mỗi mốc (phát hiện, tăng lỗi, thay đổi, xử lý).
2. **Liên hệ thay đổi gần nhất**: release, migration, cấu hình, hạ tầng trước thời điểm sự cố.
3. **Phân biệt** nguyên nhân đã xác nhận (có bằng chứng) với giả thuyết (kèm cách kiểm chứng).
4. **Đánh giá tác động**: người dùng, module, dữ liệu, bảo mật, thời lượng.
5. **Đề xuất hành động tức thời**: rollback hay hotfix là đề xuất, người quyết, theo deployment và backup-recovery.
6. **Đề xuất phòng ngừa**: test, giám sát, cảnh báo, runbook còn thiếu.
7. **Tạo bug** theo BUG-TEMPLATE cho mỗi lỗi; không dán dữ liệu production thật.
8. **Chuyển tiếp**: `bug-fixing` (sửa), `security-review` (nếu liên quan bảo mật), `documentation` (runbook, post-incident), `continuous-improvement`.
9. **Soạn báo cáo sự cố** (Draft) theo mục 8.

## 5. Checklist

- [ ] Dữ liệu đầu vào đã che D3.
- [ ] Timeline có nguồn cho từng mốc.
- [ ] Nguyên nhân gốc tách rõ xác nhận / giả thuyết.
- [ ] Tác động đã đánh giá.
- [ ] Bug đã tạo; đã nêu skill chuyển tiếp.
- [ ] Đã nêu dữ liệu còn thiếu.

## 6. Việc không được làm

- Không truy cập hệ thống hay CSDL production, không chạy lệnh trên production, không đổi dữ liệu production.
- Không tự rollback, hotfix hay deploy; chỉ đề xuất cho người quyết.
- Không coi giả thuyết là nguyên nhân đã xác nhận.
- Không ghi secret, token, dữ liệu cá nhân vào báo cáo.
- Không quy lỗi cho cá nhân.

## 7. Tiêu chí hoàn thành (DoD)

- Báo cáo sự cố Draft đủ mục; mọi kết luận có bằng chứng hoặc ghi là giả thuyết.
- Bug đã tạo và chuyển đúng skill.
- Dữ liệu còn thiếu và OQ đã ghi; người quyết hành động tức thời đã được nêu.

## 8. Báo cáo bàn giao

Báo cáo sự cố (Draft) gồm:
- Tóm tắt
- Timeline
- Nguyên nhân gốc (đã xác nhận / giả thuyết)
- Tác động
- Hành động tức thời và phòng ngừa đề xuất
- Dữ liệu còn thiếu; bug và OQ đã tạo
