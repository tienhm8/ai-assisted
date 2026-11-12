---
name: continuous-improvement
description: Tổng hợp KPI theo kỳ từ nguồn thật, so với baseline, tìm nguyên nhân gốc và đề xuất cải tiến rule, skill, workflow, agent vào ai-kpi.md; việc sửa vùng cấu hình AI chỉ đề xuất và do người duyệt.
---

# Continuous Improvement Skill

Dùng số liệu thật để biết AI có giúp phát triển tốt hơn không, và đề xuất cải tiến Rule, Skill, workflow, agent. Chỉ số để cải tiến hệ thống, không để xếp hạng cá nhân.

## Cổng vào

- Có dữ liệu của kỳ đo và baseline trong ai-kpi.
- Thiếu baseline: ghi rõ là thiếu và đề xuất cách đo. Thiếu dữ liệu kỳ đo: dừng và ghi câu hỏi mở.

Đọc: ai-kpi; báo cáo bàn giao, báo cáo kiểm thử, bug, release report, kết quả review, finding bảo mật của kỳ; roadmap; Rule, Skill, workflow liên quan.

## Quy trình

1. **Xác định kỳ** và phạm vi đo; chỉ dùng KPI đã có định nghĩa trong ai-kpi.
2. **Thu số liệu** từ nguồn thật, ghi nguồn. Không có thì ghi "chưa đo".
3. **Ghi kết quả** vào bảng kết quả theo kỳ, tách theo module và mức phức tạp, so với baseline.
4. **Phân tích xu hướng:** năng suất chỉ tính là cải thiện khi chất lượng và bảo mật không xấu đi.
5. **Nguyên nhân gốc** cho mỗi KPI xấu đi: lần từ báo cáo bàn giao, bug, review tới Rule, Skill, workflow liên quan. Chưa đủ chứng cứ thì ghi là giả thuyết.
6. **Đề xuất cải tiến** vào bảng hành động: vấn đề, đối tượng, hành động, người phụ trách, cách đo hiệu quả ở kỳ sau.
7. **Tách Task riêng** cho mỗi thay đổi Rule, Skill, workflow.

## Giới hạn

- Không làm tròn hay suy đoán số liệu.

## Hoàn thành khi

- Kết quả kỳ và hành động cải tiến đã ghi vào ai-kpi (Draft); mọi số liệu có nguồn.
- Mỗi KPI xấu đi có nguyên nhân gốc hoặc giả thuyết kèm cách kiểm chứng.

## Báo cáo

Kỳ đo, KPI đã cập nhật và nguồn, KPI xấu đi kèm nguyên nhân, hành động đề xuất và Task tách riêng, dữ liệu còn thiếu.
