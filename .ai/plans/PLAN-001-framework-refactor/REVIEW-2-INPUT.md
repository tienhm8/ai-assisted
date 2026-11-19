# Báo cáo bàn giao để review lần 2: PLAN-001

> Đầu vào cho `PLAN-001-REVIEW#2` theo cách mới của Skill `code-review` (FW-8): báo cáo bàn giao kèm dải commit. Không có PR. Thay cho lần 1 (`REVIEW-INPUT.md`).

## 1. Phạm vi và đối chiếu

- **Dải commit:** `git diff 226ad76..2813145 -- . ':!.ai/plans'` (85 file, +938 −1.172). `226ad76` là commit Plan được duyệt. `.ai/plans/` là Plan và công cụ của Orchestrator, không phải nội dung khung.
- **Task và commit tương ứng** (manifest ở `.ai/plans/PLAN-001-framework-refactor/tasks/`):

| Task | Việc | Commit |
| --- | --- | --- |
| FW-1 | từ vựng, bỏ rule 23; sửa review phần B | `8b07c11`, `54e10d1` |
| FW-2 | `CLAUDE.md`, vùng, worktree, cây README | `0126cff`, `acd8bff` |
| FW-3 | `ai-config.yaml`, rút `model-effort`, bỏ references, `auto_runs`; sửa review phần D | `4e0ff2e`, `ec36514`, `aa9bab2`, `09670e5` |
| FW-4 | chuyển tài liệu sang `.ai/guide/` | `bde0c2f`, `c669351` |
| FW-5 | `CHECKLIST.md`, `PROJECT.md`; sửa review phần B (bản tay giữ) | `dba33c9`, `5f5e09d` |
| FW-6 | đổi mã thành chữ, file cho AI | `3f6ba93` |
| FW-7 | đổi mã thành chữ, file cho người; sửa review phần B | `49abdcb`, `e8b80e4` |
| FW-8 | `code-review` nhận báo cáo bàn giao khi chưa có PR | `2813145` |

- **Sửa tay trên nhánh chính** (không thuộc Task, do người phát triển khung làm): `aac519e` (`CHECKLIST.md`, `PROJECT.md`, `gates-and-rigor.md`, `getting-started.md`, `security-standards.md`), `2b3277d` (đường dẫn link trong `PROJECT.md`), `de835d6` (bỏ phần khai báo đã chuyển khỏi `ai-tools.md`). Người phát triển khung quyết giữ các bản này khi xung đột.

## 2. Phát hiện lần 1 và trạng thái sửa

| # | Mức | Nội dung | Sửa ở | Trạng thái |
| --- | --- | --- | --- | --- |
| 1 | Medium | Task nhiều Skill: quy tắc `try` | FW-3 D (`model-effort` §2) | sửa: Skill cùng dòng `tasks`; Skill khác dòng thì `try` lấy mức cao hơn từng vị trí, cần duyệt lại |
| 2 | Medium | Thứ tự mức không định nghĩa | FW-3 D | sửa: thứ tự là vị trí trong `try`; cùng model thì `low < medium < high < xhigh < max` |
| 3 | Medium | Mất 4 ý về quyền khi `claude -p` | FW-3 D (`ai-tools` §3) | sửa: đã đưa lại 4 ý |
| 4 | Medium | Còn chữ R, A, S | FW-1 B, FW-7 B | sửa: `task-execution` và hướng dẫn đã đổi |
| 5 | Medium | Còn "sàn, trần, thang" | FW-3 D, FW-6, FW-7 B | sửa |
| 6 | Medium | Bước 6 phụ thuộc `check.py` của Plan | FW-3 D | sửa: so cây bằng `git ls-files`; Plan có thể cung cấp script |
| 7 | Medium | Việc 12 checklist không làm được | FW-5 B | khác: bản tay của người phát triển khung giữ; AC5 đổi kiểm theo số dòng mới |
| 8 | Low | "§5" thành "§3" | FW-7 B | sửa |
| 9 | Low | Định nghĩa cổng rút gọn | FW-1 B | sửa: thêm dòng trỏ tới `gates-and-rigor` §1 |
| 10 | Low | Cột "đánh giá bằng" đã mất | FW-3 D | sửa: liệt kê Skill trong rule 8 |

Câu hỏi 2 của lần 1 (`sessions.review` và dòng `tasks` của `code-review`): **chưa xử lý**, cần quyết.

## 3. Điều cần reviewer kiểm

- Xác nhận 9 phát hiện đã sửa đúng nghĩa (phát hiện 7 đã được người phát triển khung chấp nhận theo bản tay).
- Rà phần FW-8: cổng vào, Input, bước 8 và câu mở phiên có giữ nguyên tiêu chí review không.
- Không cần rà lại toàn bộ Plan (đã làm ở lần 1).

## 4. Kiểm đã chạy (Orchestrator, trên `2813145`)

- `check.py links`: 0 link hỏng.
- `check.py codes` trên toàn bộ phạm vi §2 của Plan: 0 mã.
- `check.py config`, `tree`, `types`, `vocab`: 0 lỗi.
- Các AC đã duyệt của FW-3 phần D, FW-7 phần B, FW-8 (AC1–AC3): đạt.
- FW-5-AC5 (đã đổi theo bản tay): đạt.

Kiểm chỉ bắt cú pháp và từ khóa. Nghĩa là việc của review.

## 5. Chưa xử lý và lý do

- Câu hỏi 2 lần 1 (nguồn mức của `code-review`): chờ người quyết.
- Trạng thái `status:` trong manifest các Task: vẫn `New`/`In Progress` (không đổi trong Plan).
- Chưa mở PR vào `master`: người phát triển khung làm.
