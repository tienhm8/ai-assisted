# GIT WORKFLOW RULES

> Trạng thái: **Draft**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.
> Nguồn: [coding-standards](../../docs/03-engineering/coding-standards.md) §5.1. File này chỉ nêu điều bắt buộc, không chép lại sơ đồ.

1. Một Task tương ứng một branch hoặc một đơn vị thay đổi độc lập; làm trên nhánh riêng (`feature/TASK-ID`), không làm trực tiếp trên main.
2. Không cho AI tự merge vào main; merge do người thực hiện.
3. Không cấp quyền deploy production mặc định; không truy cập production database nếu chưa có cơ chế được phê duyệt.
4. Mọi thay đổi phải có Git diff và lịch sử commit.
5. Không force-push, không rewrite lịch sử nhánh chung.
6. Không dùng `--no-verify` hoặc cách tương đương để bỏ hook/cổng.
7. Không commit secret, `.env*`, dữ liệu production.
8. Thay đổi vùng 🔴 (rule, skill, workflow, cấu hình quyền/CI) tách Task và PR riêng, không lồng vào Task tính năng.
9. PR ghi `TASK-ID` và kèm báo cáo bàn giao (Delivery Report trong mẫu Task).
