# agents

> Trạng thái: **Draft**. Làm rõ dần theo Task thật; người có thẩm quyền mới chuyển sang Approved.
> Sửa file này thuộc vùng 🔴 (luật chơi của AI): cần Task riêng và người duyệt.

Agent là **vai thực hiện** của AI, định nghĩa theo chức năng. Rule là điều bắt buộc, Skill là cách làm một loại việc, Agent là vai đứng ra làm.

## Vai là mũ, không phải AI riêng

Vai là **chức năng**, không bắt buộc là một agent hay model riêng. Mỗi vai gồm: Rule áp dụng, Skill được nạp, quyền được cấp.

Giai đoạn đầu dùng **một AI Coding Agent nhiều mũ**, mỗi mũ là một Skill hoặc prompt riêng (ví dụ `/po`, `/architect`, `/qa`, `/review`). Không vội xây hệ thống nhiều agent.

## Nguyên tắc

1. Mỗi vai ghi rõ: trách nhiệm, đầu ra bàn giao, giới hạn, mức tự chủ tối đa.
2. **AI không bao giờ giữ vai A** (chịu trách nhiệm cuối, một người duy nhất) trong RACI. AI chỉ là R dưới sự giám sát của một người.
3. **Nhiều agent đồng ý không thay thế bằng chứng.** Kết quả phải kiểm chứng bằng công cụ (test, diff, tài liệu Approved).
4. **CẤM** vòng lặp trao đổi giữa agent không có tiêu chí dừng; đặt giới hạn số vòng và ngân sách.
5. Agent giao việc cho agent khác **PHẢI** yêu cầu báo cáo bàn giao.
6. Mũ không được nâng mức tự chủ. Mức tự chủ do Task cấp, trần theo bảng (loại việc × rủi ro).

## Mô hình vai chi tiết và ánh xạ sang vai chuẩn

Luồng: yêu cầu → AC → thiết kế → code (FE/BE song song) → kiểm thử và bảo mật → review → release.

```text
Product Owner → Architect → Frontend ∥ Backend → QA ∥ Security → Reviewer → Release (người)
```

Các vai chi tiết là **mũ con** của 5 vai chuẩn (Planner, Executor, Tester, Reviewer, Security), không thay chúng.

| Mũ | Vai chuẩn | Skill chính | Đầu ra bàn giao | Giới hạn |
| --- | --- | --- | --- | --- |
| Product Owner | Planner | [requirement-analysis](../skills/requirement-analysis/SKILL.md), [requirement-review](../skills/requirement-review/SKILL.md) | AC đề xuất, câu hỏi mở | Chỉ đề xuất; PO/BA chốt AC (A trong RACI duyệt AC) |
| Architect | Planner | [architecture-design](../skills/architecture-design/SKILL.md), [database-design](../skills/database-design/SKILL.md) | Phương án, ADR nháp, thiết kế API/DB | Chỉ đọc, không sửa code; Tech Lead chốt kiến trúc (duyệt thiết kế trước khi build) |
| Frontend | Executor | [frontend-development](../skills/frontend-development/SKILL.md) | Diff + báo cáo bàn giao | Trong phạm vi Task; không tự mở rộng scope |
| Backend | Executor | [backend-development](../skills/backend-development/SKILL.md), [api-development](../skills/api-development/SKILL.md) | Diff + báo cáo bàn giao | Như trên; đổi schema/API/contract cần được duyệt |
| QA | Tester | [unit-testing](../skills/unit-testing/SKILL.md), [integration-testing](../skills/integration-testing/SKILL.md), [e2e-testing](../skills/e2e-testing/SKILL.md) | Test, kết quả chạy, phân tích lỗi | Không nới tiêu chí hoặc xoá assertion để pass |
| Security | Security | [security-review](../skills/security-review/SKILL.md), [authentication-rbac](../skills/authentication-rbac/SKILL.md) | Phát hiện bảo mật, đề xuất khắc phục | Không tự phê duyệt rủi ro, không tự hạ cấu hình bảo mật; đổi authn/authz chỉ đề xuất, thực hiện ở A2 |
| Reviewer | Reviewer | [code-review](../skills/code-review/SKILL.md) | Danh sách phát hiện có mức độ và `file:dòng` | Không thay người duyệt; chạy ở phiên khác phiên đã viết code |
| Release | Không phải vai AI | [deployment](../skills/deployment/SKILL.md), [documentation](../skills/documentation/SKILL.md) | Báo cáo release / bảng review | AI chỉ soạn báo cáo; **không tự deploy** (RACI duyệt phát hành), merge do người quyết |

`bug-fixing` và `refactoring` dùng mũ Executor.

**Khác mô hình gốc:** mô hình gốc gộp "Reviewer / Release". Ở đây tách ra vì Reviewer là vai AI (R trong "Review code"), còn Release là quyết định của người (duyệt phát hành).

### Mức tự chủ tối đa

Không gán theo mũ. Lấy theo **loại việc × rủi ro**, mặc định của Core, profile chỉ được siết:

| Mũ | Loại việc tương ứng ở | R1 / R2 / R3 |
| --- | --- | --- |
| Product Owner, Architect | Phân tích, đề xuất, soạn tài liệu | A3 / A3 / A3 (đầu ra R3 luôn là Proposed) |
| Frontend, Backend | Viết/sửa code tính năng | A3 / A3 / A2 |
| QA | Viết test | A4 / A3 / A3 |
| Security, Reviewer | Chưa có dòng riêng ở (xem "Điểm cần làm rõ") | — |

Mặc định khởi đầu **không có A4**; A4 chỉ bật cho danh mục việc hẹp do EPG duyệt.

## Khi nào mới tách thành agent riêng

Chỉ tách một mũ thành subagent khi có ít nhất một lý do rõ ràng:

| Lý do | Ví dụ |
| --- | --- |
| Context quá lớn, một agent không giữ nổi | Codebase nhiều repository |
| Cần quyền hạn khác nhau | Security chỉ đọc, không được sửa code |
| Cần review độc lập, tránh thiên kiến | Reviewer không phải phiên vừa viết code |
| Việc chạy song song được | FE và BE khi hợp đồng API đã chốt |

Không có lý do nào thì giữ một agent nhiều mũ. Chạy song song: mỗi agent một Task, một worktree, một mức tự chủ, không sửa chung file.

## Điểm cần làm rõ

1. **Hình thức triển khai mỗi mũ** trên Claude Code: slash command, Skill hay subagent. Cần một Task thử nghiệm.
2. **Mức tự chủ của Security và Reviewer:** bảng mức tự chủ không có dòng riêng. Cần quyết: coi là "phân tích, đề xuất" (A3) hay siết xuống A1 (chỉ đọc) trong adapter.
3. **Reviewer độc lập khi dự án một người** (như mybds): quy tắc review yêu cầu phiên khác phiên viết code. Cần chốt phiên mới của cùng agent là đủ, hay phải là subagent với quyền chỉ đọc.
4. **"Hợp đồng API đã chốt"** cho FE/BE song song: định nghĩa cụ thể và gắn với tài liệu nào trong `docs/`.
5. **Báo cáo Release:** ai soạn (AI hay DevOps), khi dự án chưa có CI hoặc server.
6. **Quan hệ với workflow:** bước nào của [skill-orchestration](../workflows/skill-orchestration.md) gọi mũ nào.
