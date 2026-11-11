# Git Workflow Rules

> Trạng thái: **Draft**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.

1. Một Task tương ứng một nhánh hoặc một đơn vị thay đổi độc lập; làm trên nhánh riêng, không làm trực tiếp trên nhánh chính (main/master).
2. Tên nhánh: `<loại>/<TASK-ID>-<mô-tả-ngắn>`, loại là `feature`, `fix`, `refactor`, `docs` hoặc `chore`. Ví dụ: `fix/PRJ-12-login-timeout`.
3. Commit message **bắt buộc** theo Angular convention: dòng đầu `type(scope?): subject`, `type` thuộc `build`, `ci`, `chore`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`; thân nêu `TASK-ID`. Commit sai cú pháp bị `commitlint` (husky `commit-msg`) chặn. Mỗi commit chỉ chứa file thuộc phạm vi Task.
4. Không cho AI tự merge vào nhánh chính; người merge sau khi được duyệt và kiểm tra đạt (hoặc có miễn trừ có thời hạn).
5. AI không deploy production và không truy cập CSDL production nếu chưa có cơ chế được phê duyệt.
6. Không force-push, không rewrite lịch sử nhánh chung.
7. Không dùng `--no-verify` hoặc cách tương đương để bỏ hook hay cổng kiểm tra.
8. Không commit secret, `.env*`, dữ liệu production.
9. Thay đổi vùng 🔴 (rule, skill, workflow, cấu hình quyền/CI) tách Task và PR riêng, không lồng vào Task tính năng.
10. PR ghi `TASK-ID` và kèm báo cáo bàn giao.
