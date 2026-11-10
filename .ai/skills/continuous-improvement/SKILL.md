---
name: continuous-improvement
description: Tổng hợp KPI theo kỳ từ nguồn thật, so với baseline, tìm nguyên nhân gốc và đề xuất cải tiến rule, skill, workflow, agent vào ai-kpi.md; việc sửa vùng cấu hình AI chỉ đề xuất và do người duyệt.
---

# Continuous Improvement Skill

## 1. Mục tiêu

Dùng số liệu thật để biết AI có giúp phát triển tốt hơn không, và cải tiến hệ thống (rule, skill, workflow, agent). Chỉ số dùng để cải tiến hệ thống, không để xếp hạng cá nhân.

## 2. Cổng vào

- Có dữ liệu của kỳ đo và baseline trong ai-kpi.md.
- Thiếu baseline: ghi rõ là thiếu, đề xuất cách đo, không suy đoán. Thiếu dữ liệu kỳ đo thì dừng và ghi OQ-<NN>.

## 3. Đầu vào

- ai-kpi.md (nhóm KPI, định nghĩa, baseline, kết quả)
- Delivery Report, TEST-REPORT, BUG, release report, kết quả review, finding bảo mật
- roadmap.md (mốc rà soát); .ai/rules, .ai/skills, .ai/workflows liên quan

## 4. Quy trình

1. **Xác định kỳ** và phạm vi đo; chỉ dùng KPI đã có định nghĩa đầy đủ trong ai-kpi.md.
2. **Thu số liệu** từ nguồn thật, ghi nguồn. Không có thì ghi "chưa đo".
3. **Ghi kết quả** vào bảng Kết quả theo kỳ, tách theo module và mức phức tạp, so với baseline.
4. **Phân tích xu hướng**: đối chiếu cả năng suất và chất lượng, bảo mật. Năng suất chỉ tính là cải thiện khi chất lượng và bảo mật không xấu đi.
5. **Nguyên nhân gốc** cho mỗi KPI xấu đi: lần theo Delivery Report, BUG, review đến rule, skill, workflow hay agent liên quan. Chưa đủ chứng cứ thì ghi là giả thuyết.
6. **Đề xuất cải tiến** và ghi vào bảng Hành động cải tiến: vấn đề, đối tượng (rule, skill, workflow, agent), hành động, người phụ trách.
7. **Tách Task riêng** cho mỗi thay đổi rule/skill/workflow (vùng 🔴): AI chỉ đề xuất, người có thẩm quyền duyệt, AI không tự sửa.
8. **Kiểm tra kỳ sau**: ghi cách đo hiệu quả của hành động.

## 5. Checklist

- [ ] Mọi số liệu có nguồn; chỗ thiếu ghi "chưa đo".
- [ ] So với baseline; baseline thiếu đã nêu.
- [ ] Chất lượng và bảo mật được xét cùng năng suất.
- [ ] Nguyên nhân gốc phân biệt rõ với giả thuyết.
- [ ] Mỗi hành động có đối tượng, người phụ trách, cách đo kết quả.

## 6. Việc không được làm

- Không bịa hay làm tròn số liệu; không suy đoán baseline.
- Không xếp hạng hay quy lỗi cho cá nhân.
- Không tự sửa rule, skill, workflow, agent; chỉ đề xuất qua Task riêng.
- Không kết luận cải thiện khi chất lượng hoặc bảo mật xấu đi.
- Không đưa dữ liệu D3 vào báo cáo.

## 7. Tiêu chí hoàn thành (DoD)

- Kết quả kỳ và hành động cải tiến đã ghi vào ai-kpi.md (Draft).
- Mỗi KPI xấu đi có nguyên nhân gốc hoặc giả thuyết kèm cách kiểm chứng.
- Task đề xuất cho thay đổi vùng 🔴 đã nêu; người duyệt được chỉ định.

## 8. Báo cáo bàn giao

- Kỳ đo, KPI đã cập nhật, nguồn dữ liệu
- KPI xấu đi và nguyên nhân gốc (xác nhận / giả thuyết)
- Hành động đề xuất và Task tách riêng
- Dữ liệu còn thiếu, OQ, mục cần người duyệt
