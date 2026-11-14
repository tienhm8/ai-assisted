# Release Workflow

> Trạng thái: **Approved**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.
> Skill: deployment. Người quyết phát hành là Owner (tham khảo Tech Lead); điều kiện: smoke test đạt, không có sự cố nghiêm trọng trong khung theo dõi, rollback dùng được.

**AI chuẩn bị theo Skill deployment, người quyết định và thực hiện.** AI không tự merge vào nhánh bảo vệ, không deploy production, không chạm dữ liệu production.

| Bước | Nội dung | Ai làm | Đầu ra |
| --- | --- | --- | --- |
| 1–4 | Chuẩn bị: Skill deployment bước 1–8 | AI; người xác nhận danh sách PR và xem TEST-REPORT | Bản nháp, TEST-REPORT |
| 5 | **Quyết định phát hành** ⏸ | Owner (tham khảo Tech Lead) | Approved / Hoãn |
| 6 | Merge `release/*` vào `master`, tag và deploy | **Người** | Bản phát hành |
| 7 | Theo dõi sau phát hành theo ngưỡng giám sát của dự án; rollback nếu vượt ngưỡng | Người | Trạng thái |
| 8 | RELEASE-REPORT: Skill deployment bước 9 | AI soạn, người duyệt | Báo cáo |
