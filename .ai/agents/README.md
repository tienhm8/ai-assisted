# Agents

> Trạng thái: **Approved**. Làm rõ dần theo Task thật; người có thẩm quyền mới chuyển sang Approved.
> Sửa file này thuộc vùng 🔴 (luật chơi của AI): cần Task riêng và người duyệt.

Agent là **vai thực hiện** của AI, định nghĩa theo chức năng. File này chỉ nêu các vai và nguyên tắc dùng chung cho mọi dự án; giá trị riêng của dự án (mức tự chủ, người duyệt, công cụ) do dự án khai báo.

## Vai là chức năng, không phải AI riêng

Vai là **chức năng**, không bắt buộc là một agent hay model riêng. Mỗi vai gồm: Rule áp dụng, Skill được nạp, quyền được cấp.

Giai đoạn đầu dùng **một AI Coding Agent đảm nhiệm lần lượt nhiều vai**; không vội xây hệ thống nhiều agent.

## Nguyên tắc

1. Mỗi vai ghi rõ: trách nhiệm, đầu ra bàn giao, giới hạn. Mức tự chủ tối đa theo loại việc × rủi ro, không theo vai.
2. **AI không bao giờ giữ vai A** (chịu trách nhiệm cuối, một người duy nhất) trong RACI. AI chỉ là R dưới sự giám sát của một người.
3. **Nhiều agent đồng ý không thay thế bằng chứng.** Kết quả phải kiểm chứng bằng công cụ (test, diff, tài liệu Approved).
4. Không để agent trao đổi vòng lặp không có tiêu chí dừng; đặt giới hạn số vòng và ngân sách.
5. Agent giao việc cho agent khác phải yêu cầu báo cáo bàn giao: Delivery Report, gồm bằng chứng đã chạy test và danh sách giả định.
6. Vai không được nâng mức tự chủ. Mức do Task cấp, không vượt trần của dự án.
7. AI chỉ tạo tài liệu ở trạng thái Draft; chuyển Approved do người có thẩm quyền.
8. Không bịa nghiệp vụ, API, thư viện: thiếu thông tin thì dừng và ghi vào danh sách câu hỏi mở.
9. Chỉ dựa vào tài liệu Approved; tài liệu Draft hoặc Deprecated chỉ để tham khảo và phải nói rõ khi dùng. Khi bàn giao, nêu tài liệu và phiên bản đã dùng.

## Mô hình vai chi tiết và ánh xạ sang vai chuẩn

Luồng: yêu cầu → AC → thiết kế → code (FE/BE song song) → kiểm thử và bảo mật → review → release.

```text
Product Owner → Architect → Frontend ∥ Backend → QA ∥ Security → Reviewer → Release (người)
```

Có hai tầng: **5 vai chuẩn** (Planner, Executor, Tester, Reviewer, Security) và các **vai chi tiết** (Product Owner, Architect, Frontend…) mỗi vai chi tiết thuộc đúng một vai chuẩn. Vai chi tiết cụ thể hoá vai chuẩn, không thay thế nó.

| Vai chi tiết | Vai chuẩn | Skill chính | Đầu ra bàn giao | Giới hạn |
| --- | --- | --- | --- | --- |
| Product Owner | Planner | product-discovery, requirement-analysis, requirement-review, task-planning | AC đề xuất, câu hỏi mở | Chỉ đề xuất; PO/BA chốt AC |
| Architect | Planner | architecture-design, database-design | Phương án, ADR nháp, thiết kế API/DB | Không sửa code; thay đổi ranh giới module hoặc ngoại lệ phụ thuộc phải có ADR; Kiến trúc sư chốt (thêm Security khi có dữ liệu D2/D3) |
| Frontend | Executor | frontend-development | Diff + Delivery Report | Trong phạm vi Task; không tự mở rộng scope |
| Backend | Executor | backend-development, api-development, authentication-rbac (triển khai theo policy đã duyệt) | Diff + Delivery Report | Đổi schema/API/contract cần được duyệt; không truy cập trực tiếp dữ liệu của module khác; không tự chạy migration production |
| QA | Tester | unit-testing, integration-testing, e2e-testing | Test, TEST-REPORT, phân tích lỗi | Không nới tiêu chí, hạ ngưỡng, xoá assertion hay bỏ hook để pass |
| Security | Security | security-review, authentication-rbac (rà soát) | Phát hiện bảo mật, đề xuất khắc phục | Chỉ khuyến nghị; không tự phê duyệt rủi ro, không hạ cấu hình bảo mật; không đưa secret hoặc dữ liệu D3 vào AI; đổi authn/authz do Executor thực hiện sau khi người duyệt |
| Reviewer | Reviewer | code-review | Danh sách phát hiện có mức độ và `file:dòng` | Không thay người duyệt; chạy ở phiên khác phiên đã viết code |
| Release | Không phải vai AI | deployment | RELEASE-REPORT | AI chỉ soạn nháp báo cáo; **không tự deploy**, không truy cập production DB; người quyết phát hành do dự án chỉ định |

Skill khác:
- `documentation` là Skill dùng chung: Executor dùng khi cập nhật tài liệu cùng thay đổi; vai Release dùng khi soạn báo cáo phát hành.
- `bug-fixing` và `refactoring` dùng vai Executor, đầu vào của `bug-fixing` là BUG-TEMPLATE.
- `incident-analysis` dùng vai Tester (chỉ đọc, A1): phân tích log do người xuất và đã che D3; không truy cập production.
- `continuous-improvement` dùng vai Planner: chỉ đề xuất cải tiến; sửa rule/skill/workflow qua Task riêng.

Reviewer và QA dùng checklist của Skill code-review.

## Vai nào làm ở bước nào của workflow

Chi tiết bước ở workflow skill-orchestration, task-execution, release-workflow.

| Bước | Vai |
| --- | --- |
| Tiếp nhận, nạp ngữ cảnh, lập plan | Product Owner, Architect (Planner) |
| Duyệt plan | Người (không phải vai AI) |
| Implement | Frontend, Backend (Executor) |
| Chạy test | QA (Tester) |
| Self review | Executor; không thay Reviewer độc lập |
| Review, kiểm tra bảo mật | Reviewer, Security; sau đó người duyệt |
| Merge và deploy | Người |
| Chuẩn bị release (release note, rollback) và RELEASE-REPORT | Release (soạn nháp) |
| Cập nhật tri thức | Executor (`documentation`) |

## Khi nào mới tách thành agent riêng

Chỉ tách một vai chi tiết thành subagent khi có ít nhất một lý do rõ ràng:

| Lý do | Ví dụ |
| --- | --- |
| Context quá lớn, một agent không giữ nổi | Codebase nhiều repository |
| Cần quyền hạn khác nhau | Security chỉ đọc, không được sửa code |
| Cần review độc lập, tránh thiên kiến | Reviewer không phải phiên vừa viết code |
| Việc chạy song song được | FE và BE khi hợp đồng API đã chốt |

Không có lý do nào thì giữ một agent đảm nhiệm nhiều vai. Chạy song song: mỗi agent một Task, một worktree, một mức tự chủ, không sửa chung file.

**Hợp đồng API đã chốt** (điều kiện để FE ∥ BE): đặc tả API (và OpenAPI nếu có) cùng interface liên module ở trạng thái Approved bởi Kiến trúc sư. Thay đổi sau đó cần ADR và báo bên dùng.
