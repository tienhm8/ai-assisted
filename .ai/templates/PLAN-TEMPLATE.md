# PLAN: <GOAL>-P<N> — <Tên ngắn>

> AI (Orchestrator) soạn; Tech Lead duyệt trước khi chạy Task ([task-execution](../workflows/task-execution.md), "Plan approval"). Duyệt Plan là duyệt mức rủi ro, mức tự chủ, khoảng model·effort, ngân sách, phạm vi của mọi Task trong Plan. Mục "Kết quả" điền sau khi xong.
> Lưu ở `.ai/plans/<GOAL>-P<N>-<slug>/PLAN.md`; manifest của Task ở `tasks/<KEY>-<N>.yaml`; các lần chạy ở `runs.md` cùng thư mục.

| Mục | Giá trị |
| --- | --- |
| Goal | `GOAL-<NN>` — <tên Goal> ([goals](../../docs/04-project-management/goals.md)) |
| Trạng thái | Draft / Approved / In Progress / Done / Cancelled |
| Người duyệt · Ngày duyệt | |
| Ngày tạo | |
| Model · Effort của Orchestrator | M3·E3 (model mạnh, effort cao); M3·E4 (model mạnh, effort rất cao) nếu Goal có Task T7 (đổi kiến trúc hoặc API contract) |
| Ngân sách cả Plan | Tổng `budget` các Task cộng chi phí phiên Orchestrator; vượt thì dừng, hỏi người |

## 1. Mục tiêu và phạm vi
- Đầu ra của Plan (khác các Plan khác của cùng Goal ở chỗ nào):
- Làm:
- Không làm:
- Vì sao là một Plan riêng (tiêu chí ở task-execution, "New Plan"):

## 2. Tiêu chí hoàn thành
Điều kiện kiểm chứng được để coi Plan là Done; thường là cổng duyệt cuối chặng (G2, G3, G5…) và AC của các Task.

## 3. Yêu cầu và ngữ cảnh đã nạp
FR, BR, AC, ADR, SRC, câu hỏi mở.
Điểm áp dụng từ tài liệu thiết kế, kỹ thuật: tài liệu, § và tên mục → điều áp dụng (ví dụ: error-handling §5.2 Ánh xạ HTTP status → lỗi hạn mức trả 422). Manifest của từng Task chỉ trỏ tới các điểm ở đây hoặc mục `docs/` cần nạp.

## 4. Chiến lược
Vì sao chia Task như vậy, thứ tự, chỗ chạy song song, điểm dừng ⏸. Chuỗi Skill mặc định của loại Task (task-types §1) và Skill bỏ hoặc thêm kèm lý do.

## 5. Task

Chi tiết ở manifest; bảng này chỉ tóm tắt. Cột Loại, Rủi ro · Tự chủ, Thang mức ghi mã kèm nghĩa trong ngoặc (`project-rules` 23), người đọc không phải tra. Mức tự chủ và rủi ro do AI đề xuất, kèm lý do trong manifest. Task A2 trở xuống chạy "Có người" (phiên tương tác, duyệt từng bước). Cột "Lệch mặc định" khác "Không" thì Plan luôn phải chờ duyệt. Không tạo Task cho `code-review`, `security-review`: chúng chạy ở bước 8 theo dòng "Review" (dòng này không phải Task, không có mã `<KEY>-<N>`).

| Task | Tên | Loại | Rủi ro · Tự chủ | Cách chạy | Agent | Skill | Thang mức | Ngân sách (USD) | Lệch mặc định | Phụ thuộc | Cổng | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <KEY>-<N> | | T2 (làm tính năng đã có yêu cầu) | R2 (ảnh hưởng nhiều module) · A3 (làm trọn, người duyệt kết quả cuối) | Gửi đi | executor | backend-development | M2·E1 (chuẩn, thấp) → M2·E3 (chuẩn, cao) → M3·E3 (mạnh, cao) | 2 | Không | | — | New |
| Review (bước 8) | Review code, bảo mật nếu cần | T9 (review Pull Request) | theo Task rủi ro cao nhất · A1 (chỉ đọc và báo cáo) | Gửi đi | reviewer, security | code-review, security-review | M3·E3 (mạnh, cao) → M3·E4 (mạnh, rất cao) | | Không | mọi Task | — | New |

Dòng "Review" luôn có: không có manifest riêng; mức theo model-effort §2, ngân sách ghi ở cột "Ngân sách", duyệt cùng Plan; lần chạy ghi `runs.md` dạng `<GOAL>-P<N>-REVIEW#<n>`. Lần review trượt (nâng mức) khi báo cáo thiếu mục bắt buộc trong "Report" của Skill `code-review` hoặc `security-review`; phát hiện lỗi trong code không phải trượt của review mà mở lỗi mới cho Task chịu trách nhiệm.

## 6. Thiết kế và file dự kiến thay đổi
Quyết định thiết kế chung cho nhiều Task; file của từng Task nằm ở `outputs`, `scope` của manifest.

## 7. Kế hoạch kiểm thử
Mỗi AC ứng với test nào, Task nào chạy, lệnh nào (trùng với `acceptance_criteria[].check` của manifest). Cổng kiểm tra chung chạy ở bước 6 trên kết quả gộp.

## 8. Rủi ro và điểm cần người quyết
Điểm cần người quyết ghi mã `OQ-<NN>` kèm bản tóm tắt đủ để quyết theo `project-rules` 21 (vấn đề, mỗi phương án một dòng được/mất, đề xuất, nếu chưa quyết); chi tiết và lịch sử ở [open-questions](../../docs/00-project-overview/open-questions.md).

## 9. Kết quả (điền sau khi xong)
Đầu ra của từng Task, lệch kế hoạch ở đâu, Task nào phải nâng mức (tóm tắt từ `runs.md`), bằng chứng test, trạng thái tiêu chí hoàn thành §2.
