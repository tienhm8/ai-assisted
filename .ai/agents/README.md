# Agents

> Trạng thái: **Draft**. Người quyết định: Tech Lead.
> Điều kiện chuyển Approved: đã điền model và effort ở [model-effort.md](../workflows/model-effort.md).
> Sửa file này cần Task riêng và người duyệt.

Agent là **vai thực hiện** của AI: ai làm, với quyền gì. Vai là chức năng, không bắt buộc là một agent hay model riêng.

**Mặc định dùng một AI Coding Agent đảm nhiệm lần lượt các vai.** Khi đó không cần nạp file này: Rule, chuỗi Skill và model đã có ở `task-types.md`. File này dùng khi tách vai thành agent riêng.

## Vai và quyền

| Vai | Skill | Được làm | Không được làm |
| --- | --- | --- | --- |
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

## Khi nào tách thành agent riêng

Chỉ tách khi có ít nhất một lý do:

| Lý do | Ví dụ |
| --- | --- |
| Context quá lớn cho một agent | Codebase nhiều repository |
| Cần quyền hạn khác nhau | Security chỉ đọc |
| Cần review độc lập | Reviewer không phải phiên vừa viết code |
| Việc chạy song song được | Frontend và backend khi API contract đã Approved |

Ánh xạ model/effort và cấu hình theo công cụ AI: [references/](references/): [claude-code.md](references/claude-code.md), [cursor.md](references/cursor.md), [copilot.md](references/copilot.md), [gemini.md](references/gemini.md), [codex.md](references/codex.md). Dùng file của công cụ dự án chọn.
