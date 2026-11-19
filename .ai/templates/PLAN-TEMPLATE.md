# PLAN: PLAN-<NNN> — <Tên ngắn>

> AI (Orchestrator) soạn; Tech Lead duyệt trước khi chạy Task ([task-execution](../workflows/task-execution.md), "Plan approval"). Duyệt Plan là duyệt mức rủi ro, mức tự chủ, thứ tự thử model/effort, ngân sách, phạm vi của mọi Task trong Plan. Mục "Kết quả" điền sau khi xong.
> Lưu ở `.ai/plans/PLAN-<NNN>-<slug>/PLAN.md`; manifest của Task ở `tasks/<KEY>-<N>.yaml`; các lần chạy ở `runs.md` cùng thư mục.

| Mục | Giá trị |
| --- | --- |
| ID | `PLAN-<NNN>` |
| Nguồn (Source) | Đúng một: `GOAL-<NN>` / `EPIC-<NN>` / `US-<MODULE>-<NN>` / yêu cầu độc lập (ai yêu cầu, ngày, nội dung) |
| Goals (tuỳ chọn) | `GOAL-<NN>`, … ([goals](../../docs/04-project-management/goals.md)); để trống nếu không phục vụ Goal nào |
| Trạng thái | Draft / Approved / In Progress / Done / Cancelled |
| Người duyệt · Ngày duyệt | |
| Ngày tạo | |
| Model/effort của Orchestrator | Theo `sessions.orchestrator` trong `ai-config.yaml` (ví dụ opus/high); mức ghi chú trong file đó nếu Plan có Task loại `architecture-change` (đổi kiến trúc hoặc API contract) |
| Ngân sách tối đa của Plan | Ghi công thức `NganSachToiDa >= NganSachTask + QuyDuPhong + Review + PhienDieuPhoi` với số cụ thể. `NganSachTask` là tổng ngân sách ban đầu của các Task. Quỹ nằm bên trong, không cộng thêm; không tự tăng; vượt thì dừng, hỏi người |
| Quỹ dự phòng | Số tiền (USD); mặc định `budget_pool_pct` % tổng ngân sách ban đầu của các Task (ghi lý do nếu khác); không có quỹ thì ghi 0 |

## 1. Mục tiêu và phạm vi
- Đầu ra của Plan (khác các Plan khác cùng Nguồn hoặc cùng Goal ở chỗ nào):
- Làm:
- Không làm:
- Vì sao là một Plan riêng (tiêu chí ở task-execution, "New Plan"):

## 2. Tiêu chí hoàn thành
Điều kiện kiểm chứng được để coi Plan là Done; thường là cổng duyệt cuối chặng (`requirements`, `design`, `code-complete`…) và AC của các Task.

## 3. Yêu cầu và ngữ cảnh đã nạp
User Story (`US-…`) và FR mà Plan hiện thực (Plan kỹ thuật ghi lý do thay); BR, AC, ADR, SRC, câu hỏi mở.
Điểm áp dụng từ tài liệu thiết kế, kỹ thuật: tài liệu, § và tên mục → điều áp dụng (ví dụ: error-handling §5.2 Ánh xạ HTTP status → lỗi hạn mức trả 422). Manifest của từng Task chỉ trỏ tới các điểm ở đây hoặc mục `docs/` cần nạp.

## 4. Chiến lược
Vì sao chia Task như vậy, thứ tự, chỗ chạy song song, điểm dừng ⏸. Chuỗi Skill mặc định của loại Task (task-types §1) và Skill bỏ hoặc thêm kèm lý do.

## 5. Task

Chi tiết ở manifest; bảng này chỉ tóm tắt. Cột Loại, Rủi ro · Tự chủ ghi từ của thang (`project-rules` 23), kèm nghĩa tiếng Việt trong ngoặc để người đọc không phải tra. Cột "Thứ tự thử" ghi `model/effort` theo `try` của manifest, mức đầu là mức bắt đầu, mức cuối là mức tối đa. Mức tự chủ và rủi ro do AI đề xuất, kèm lý do trong manifest. Task `step-by-step` trở xuống chạy "Có người" (phiên tương tác, duyệt từng bước). Cột "Lệch mặc định" khác "Không" thì Plan luôn phải chờ duyệt. Không tạo Task cho `code-review`, `security-review`: chúng chạy ở bước 8 theo dòng "Review" (dòng này không phải Task, không có mã `<KEY>-<N>`).

| Task | Tên | Loại | Rủi ro · Tự chủ | Cách chạy | Agent | Skill | Thứ tự thử | Ngân sách (USD) | Lệch mặc định | Phụ thuộc | Cổng | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <KEY>-<N> | | `feature` (làm tính năng đã có yêu cầu) | `medium` (ảnh hưởng nhiều module) · `full-task` (làm trọn, người duyệt kết quả cuối) | Gửi đi | executor | backend-development | sonnet/low → sonnet/high → opus/high | 2 | Không | | — | New |
| Review (bước 8) | Review code, bảo mật nếu cần | `pr-review` (review Pull Request) | theo Task rủi ro cao nhất · `read-only` (chỉ đọc và báo cáo) | Gửi đi | reviewer, security | code-review, security-review | opus/high → opus/xhigh | | Không | mọi Task | — | New |

Dòng "Review" luôn có: không có manifest riêng; mức theo `sessions.review` và dòng `tasks` của Skill trong `ai-config.yaml`, ngân sách ghi ở cột "Ngân sách", duyệt cùng Plan; lần chạy ghi `runs.md` dạng `PLAN-<NNN>-REVIEW#<n>`. Lần review trượt (nâng mức) khi báo cáo thiếu mục bắt buộc trong "Report" của Skill `code-review` hoặc `security-review`; phát hiện lỗi trong code không phải trượt của review mà mở lỗi mới cho Task chịu trách nhiệm.

## 6. Thiết kế và file dự kiến thay đổi
Quyết định thiết kế chung cho nhiều Task; file của từng Task nằm ở `outputs`, `scope` của manifest.

## 7. Kế hoạch kiểm thử
Mỗi AC ứng với test nào, Task nào chạy, lệnh nào (trùng với `acceptance_criteria[].check` của manifest). Cổng kiểm tra chung chạy ở bước 6 trên kết quả gộp.

## 8. Rủi ro và điểm cần người quyết
Điểm cần người quyết ghi mã `OQ-<NN>` kèm bản tóm tắt đủ để quyết theo `project-rules` 21 (vấn đề, mỗi phương án một dòng được/mất, đề xuất, nếu chưa quyết); chi tiết và lịch sử ở [open-questions](../../docs/00-project-overview/open-questions.md).

## 9. Kết quả (điền sau khi xong)
Đầu ra của từng Task, lệch kế hoạch ở đâu, Task nào phải nâng mức (tóm tắt từ `runs.md`), bằng chứng test, trạng thái tiêu chí hoàn thành §2.
Ngân sách: các lần cấp thêm, thu hồi và số dư quỹ cuối Plan (từ bảng "Điều chỉnh ngân sách" trong `runs.md`).
