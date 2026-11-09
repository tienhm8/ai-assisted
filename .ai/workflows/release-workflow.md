# Release Workflow

> Trạng thái: **Draft**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.
> Môi trường và rollback: [deployment](../../docs/05-operations/deployment.md), [backup-recovery](../../docs/05-operations/backup-recovery.md). Skill: [deployment](../skills/deployment/SKILL.md). Người quyết phát hành là Owner (tham khảo Tech Lead); điều kiện: smoke test đạt, không có sự cố nghiêm trọng trong khung theo dõi, rollback dùng được.

**AI chuẩn bị, người quyết định và thực hiện.** AI không tự merge vào nhánh bảo vệ, không deploy production, không chạm dữ liệu production.

| Bước | Nội dung | Ai làm | Đầu ra |
| --- | --- | --- | --- |
| 1 | Kiểm tra mọi PR trong bản phát hành đã đạt DoD và cổng | AI kiểm, người xác nhận | Danh sách PR |
| 2 | Chốt thứ tự merge (migration, hợp đồng API phá vỡ tương thích) | AI đề xuất | Thứ tự merge |
| 3 | Soạn release note, kế hoạch rollback, script chạy migration | AI | Bản nháp |
| 4 | Chạy hồi quy và smoke test ở môi trường staging/local | AI chạy, người xem | [TEST-REPORT](../templates/TEST-REPORT-TEMPLATE.md) |
| 5 | **Quyết định phát hành** | Owner (tham khảo Tech Lead) | Approved / Hoãn |
| 6 | Merge và deploy | **Người** | Bản phát hành |
| 7 | Theo dõi sau phát hành theo [monitoring](../../docs/05-operations/monitoring.md); rollback nếu vượt ngưỡng | Người | Trạng thái |
| 8 | Lập [RELEASE-REPORT](../templates/RELEASE-REPORT-TEMPLATE.md); ghi bài học | AI soạn, người duyệt | Báo cáo |

Ví dụ: dự án chưa có server (có miễn trừ có thời hạn) thì bước 4 và 6 làm ở môi trường local; khi có server phải cập nhật workflow này.
Hotfix khẩn cấp: phân tích tối thiểu, hồ sơ bổ sung trong 2 ngày làm việc.
