# Agents

> Trạng thái: **Draft**. Người quyết định: Tech Lead.
> Điều kiện chuyển Approved: đã điền model và effort ở [model-effort.md](../workflows/model-effort.md).
> Sửa file này cần Task riêng và người duyệt.

Agent là **vai thực hiện** của AI: ai làm, với quyền gì. Vai là chức năng, không bắt buộc là một agent hay model riêng.

**Mặc định: một phiên Orchestrator gửi từng Task tới một subagent hoặc phiên mới** theo Task Manifest ([task-execution](../workflows/task-execution.md), "Orchestration"). Mỗi Task chạy với vai, model·effort riêng; không đổi model trong một phiên. Task mức tự chủ A2 trở xuống chạy "Có người": người mở phiên tương tác, duyệt từng bước. Fast lane (một Task R1): một phiên đảm nhiệm lần lượt các vai, không cần nạp file này.

## Vai và quyền

| Vai | Skill | Được làm | Không được làm |
| --- | --- | --- | --- |
| Orchestrator | task-planning (lập Plan) | Lập Plan, viết manifest, gửi Task, đánh giá kết quả, nâng mức trong thang đã duyệt, ghi `runs.md`, tổng hợp | Tự viết code hoặc tài liệu của Task; duyệt; vượt trần, ngân sách; bỏ qua điểm ⏸ |
| Planner | product-discovery, requirement-analysis, requirement-review, architecture-design, database-design, task-planning, continuous-improvement | Soạn tài liệu Draft, ADR nháp, plan | Sửa code |
| Executor | backend-development, api-development, frontend-development, authentication-rbac, bug-fixing, refactoring, documentation | Sửa code và tài liệu trong phạm vi Task | Chạy migration production; đổi schema, API contract khi chưa được duyệt |
| Tester | unit-testing, integration-testing, e2e-testing, incident-analysis | Viết và chạy test; phân tích log do người xuất (chỉ đọc) | Sửa code production; truy cập production |
| Reviewer | code-review | Đọc và khuyến nghị, ở phiên khác phiên viết code | Sửa code; thay người duyệt |
| Security | security-review | Đọc, chạy công cụ quét, khuyến nghị | Sửa code; phê duyệt rủi ro; hạ cấu hình bảo mật |

Phát hành không phải vai AI: AI chỉ soạn nháp bằng Skill `deployment`; người quyết và thực hiện.

## Nguyên tắc

1. AI không giữ vai chịu trách nhiệm cuối (A trong RACI); AI chỉ thực hiện dưới sự giám sát của một người.
2. Mức tự chủ theo Task, không theo vai; vai không nâng mức.
3. Nhiều agent đồng ý không thay bằng chứng. Kết quả phải kiểm chứng bằng công cụ (test, diff, tài liệu Approved).
4. Agent trao đổi với nhau phải có tiêu chí dừng: giới hạn số vòng và ngân sách.
5. Agent giao việc cho agent khác phải nhận lại báo cáo bàn giao kèm bằng chứng test và danh sách giả định.
6. Chạy song song: mỗi agent một Task, một worktree, một mức tự chủ; không sửa chung file.

## Subagent theo vai và mức

Subagent khai báo theo **vai × mức** (ví dụ `executor-sonnet-low`, `executor-opus-high`, `reviewer-opus-high`; tên lấy từ các mức trong `ai-config.yaml`) khi công cụ chỉ đặt được model/effort trong file khai báo. Orchestrator chọn subagent khớp `agent` và mức hiện tại của manifest; không có file khớp thì dừng và hỏi, không tự chạy ở mức khác.

## Khi nào tách thành agent riêng

Ngoài việc chạy mỗi Task ở một subagent, chỉ tách thêm vai cố định khi có ít nhất một lý do:

| Lý do | Ví dụ |
| --- | --- |
| Context quá lớn cho một agent | Codebase nhiều repository |
| Cần quyền hạn khác nhau | Security chỉ đọc |
| Cần review độc lập | Reviewer không phải phiên vừa viết code |
| Việc chạy song song được | Frontend và backend khi API contract đã Approved |

Model/effort theo công cụ AI nằm ở [ai-config.yaml](../../ai-config.yaml); cách chạy Task với Claude Code: [ai-tools.md](../guide/ai-tools.md) §3.
