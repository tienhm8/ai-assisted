# Release Workflow

> Trạng thái: **Approved**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.
> Skill: deployment. Người quyết phát hành là Owner (tham khảo Tech Lead); điều kiện: smoke test đạt, không có sự cố nghiêm trọng trong khung theo dõi, rollback dùng được.

**AI chuẩn bị, người quyết định và thực hiện.** AI không tự merge vào nhánh bảo vệ, không deploy production, không chạm dữ liệu production.

| Bước | Nội dung | Ai làm | Đầu ra |
| --- | --- | --- | --- |
| 1 | Kiểm tra mọi PR trong bản phát hành đã đạt DoD và cổng | AI kiểm, người xác nhận | Danh sách PR |
| 2 | Chốt thứ tự merge (migration, hợp đồng API phá vỡ tương thích) | AI đề xuất | Thứ tự merge |
| 3 | Soạn release note, kế hoạch rollback, script chạy migration | AI | Bản nháp |
| 4 | Chạy hồi quy và smoke test ở môi trường staging/local | AI chạy, người xem | TEST-REPORT |
| 5 | **Quyết định phát hành** | Owner (tham khảo Tech Lead) | Approved / Hoãn |
| 6 | Merge và deploy | **Người** | Bản phát hành |
| 7 | Theo dõi sau phát hành theo ngưỡng giám sát của dự án; rollback nếu vượt ngưỡng | Người | Trạng thái |
| 8 | Lập RELEASE-REPORT; ghi bài học | AI soạn, người duyệt | Báo cáo |

Môi trường chưa có (staging, server, CI/CD): ghi miễn trừ có thời hạn và người duyệt theo khai báo của dự án; bước tương ứng làm ở môi trường thay thế đã khai báo.
Hotfix khẩn cấp: phân tích tối thiểu, hồ sơ bổ sung trong thời hạn dự án khai báo, có người duyệt hotfix.
