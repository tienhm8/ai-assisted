# Git Workflow Rules

> Trạng thái: **Approved**
>
> Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.
1. Một Task tương ứng một nhánh hoặc một đơn vị thay đổi độc lập; làm trên nhánh riêng, không làm trực tiếp trên nhánh dài hạn (`master`, `develop`) hay nhánh `release/*`.
2. Mô hình nhánh theo Gitflow (nvie), chi tiết và luồng ví dụ ở [gitflow.md](../../docs/05-operations/gitflow.md). Nhánh làm việc đặt tên `<loại>/<TASK-ID>-<mô-tả-ngắn>`, loại là `feature`, `fix`, `refactor`, `docs` hoặc `chore`, tách từ `develop`. Ví dụ: `fix/PRJ-12-login-timeout`. Hai loại nhánh đặc biệt:
   - `release/<X.Y.0>`: tách từ `develop` khi chốt sprint, deploy Staging, chỉ nhận sửa lỗi (không thêm tính năng), đóng bằng merge vào `master` (gắn tag `vX.Y.0`) và merge ngược về `develop`.
   - `hotfix/<X.Y.Z>`: tách từ `master` để xử lý lỗi nghiêm trọng trên Production, merge vào `master` (gắn tag `vX.Y.Z`) và vào `develop` (hoặc `release/*` đang mở).
   Merge các nhánh này dùng `--no-ff`; tag có dạng `vMAJOR.MINOR.PATCH`.
3. Commit message **bắt buộc** theo Angular convention: dòng đầu `type(scope?): subject`, `type` thuộc `build`, `ci`, `chore`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`; thân nêu `TASK-ID`. Commit sai cú pháp bị `commitlint` (husky `commit-msg`) chặn. Mỗi commit chỉ chứa file thuộc phạm vi Task. Không thêm dòng `Co-Authored-By` hay dòng ghi công AI nào vào commit message.
4. Commit xong phải hiển thị cho người review: nhánh, hash ngắn và **toàn văn message** (dòng đầu + thân) của từng commit vừa tạo, kèm danh sách file của mỗi commit (`git show --stat --format=full`). Không chỉ báo "đã commit".
5. Không cho AI tự merge vào `master`, `develop` hay `release/*`, không tự tạo tag phát hành; người merge và gắn tag sau khi được duyệt và kiểm tra đạt (hoặc có miễn trừ có thời hạn).
6. AI không deploy production và không truy cập CSDL production nếu chưa có cơ chế được phê duyệt.
7. Không force-push, không rewrite lịch sử nhánh chung.
8. Không dùng `--no-verify` hoặc cách tương đương để bỏ hook hay cổng kiểm tra.
9. Không commit secret, `.env*`, dữ liệu production.
10. Thay đổi vùng 🔴 (rule, skill, workflow, cấu hình quyền/CI) tách Task và PR riêng, không lồng vào Task tính năng.
11. PR ghi `TASK-ID` và kèm báo cáo bàn giao.
