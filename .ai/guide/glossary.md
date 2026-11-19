# Glossary

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | ../../docs/00-project-overview/glossary.md, ../../README.md |

> **Mục đích.** Thuật ngữ của khung, dùng thống nhất cho người và AI. AI không tự đặt nghĩa mới.
>
> **Người quyết định:** Tech Lead.

## 1. Thuật ngữ chung

| Thuật ngữ | Định nghĩa | Đồng nghĩa / Tránh dùng | Nguồn |
| --- | --- | --- | --- |
| FR | Functional Requirement: yêu cầu chức năng, hệ thống phải làm gì. Mã `FR-<MODULE>-<NN>`. | Yêu cầu chức năng | 01-requirements/FR/ |
| NFR | Non-Functional Requirement: yêu cầu phi chức năng (hiệu năng, bảo mật, độ sẵn sàng…), mã `NFR-<NN>`. | Yêu cầu phi chức năng | 01-requirements/ |
| AC | Acceptance Criteria: tiêu chí nghiệm thu, điều kiện kiểm thử được để coi một FR là xong. Mã `<FR>-AC<N>`. | Tiêu chí nghiệm thu | 01-requirements/acceptance-criteria.md |
| Given / When / Then | Cách viết AC theo 3 bước: **Given** (bối cảnh ban đầu), **When** (hành động xảy ra), **Then** (kết quả mong đợi). VD: Given người dùng đã đăng nhập, When bấm "Đăng xuất", Then hệ thống quay về trang đăng nhập. | GWT | 01-requirements/acceptance-criteria.md |
| ADR | Architecture Decision Record: ghi lại một quyết định kiến trúc lớn và lý do, mã `ADR-<NNNN>`. | Quyết định kiến trúc | 02-architecture/ADR/ |
| PO | Product Owner: người quyết định phạm vi và ưu tiên sản phẩm. |  | PROJECT.md |
| BA | Business Analyst: người phân tích và làm rõ yêu cầu nghiệp vụ. |  | PROJECT.md |
| Đại diện khách hàng | Người phía khách hàng cung cấp tài liệu nguồn, trả lời câu hỏi làm rõ, duyệt tài liệu được gửi sang. AI không làm việc trực tiếp mà qua Đầu mối (BA hoặc PO nội bộ); Đầu mối chỉ chuyển `Approved` khi khách hàng đã duyệt. |  | PROJECT.md §5 |
| SRC | Tài liệu nguồn: tài liệu đầu vào từ khách hàng, PO, bên liên quan, hoặc biên bản câu trả lời, mã `SRC-<NN>`. | Tài liệu nguồn | 00-project-overview/sources/README.md |
| E2E | End-to-end test: kiểm thử toàn luồng từ giao diện đến dữ liệu. |  | 03-engineering/testing-strategy.md |
| BRD | Business Requirements Document: tài liệu yêu cầu nghiệp vụ ở mức mục tiêu và giá trị; nguồn để suy ra FR/NFR. |  | 01-requirements/BRD.md |
| BRQ | Business Requirement: một yêu cầu nghiệp vụ trong BRD, mã `BRQ-<NN>`. Mỗi BRQ được phủ bởi ít nhất một FR; FR ghi BRQ nguồn. | Yêu cầu nghiệp vụ | 01-requirements/BRD.md |
| Epic | Nhóm chức năng/công việc lớn theo phạm vi sản phẩm, lộ trình ("nhóm công việc lớn nào cần thực hiện?"), mã `EPIC-<NN>`. Nhóm A. Ghi BRQ và Goal mà nó đóng góp (nhiều-nhiều). Không phải loại Plan, không bị Goal thay thế. | Nhóm công việc lớn | 04-project-management/product-backlog.md §1 |
| Function / Feature | Chức năng hệ thống ("hệ thống cần có chức năng gì?"), mã `FEAT-<NN>`. Nhóm A. Ghi BRQ (nhiều-nhiều); chi tiết hoá bằng nhiều FR (bảng FR ghi Feature). | Chức năng | 01-requirements/features.md |
| User Story | Nhu cầu của người dùng ("người dùng muốn làm gì và vì sao?", mẫu "Là…, tôi muốn…, để…"), mã `US-<MODULE>-<NN>`. Nhóm A. Ghi Epic, Feature, FR; một User Story có thể cần nhiều Task, một Task có thể phục vụ nhiều User Story. | Story | 04-project-management/product-backlog.md §2 |
| BR | Business Rule: quy tắc nghiệp vụ, mã `BR-<MODULE>-<NN>`. | Quy tắc nghiệp vụ | 01-requirements/business-rules.md |
| Open / Asked / Assumption / Closed | Trạng thái của điểm chưa rõ, mã `OQ-<NN>`. `Open`: chưa có câu trả lời. `Asked`: đã gửi người trả lời, đang chờ. `Assumption`: giả định tạm dùng để đi tiếp, cần xác nhận. `Closed`: đã quyết. | Câu hỏi mở | 00-project-overview/open-questions.md |
| Draft / Approved | Trạng thái tài liệu: Draft → In Review → Approved → Deprecated. `Draft`: bản nháp. `Approved`: đã được người có thẩm quyền duyệt, được dùng làm căn cứ; chỉ người có thẩm quyền chuyển sang. `Deprecated`: hết hiệu lực. |  | Bảng thuộc tính đầu mỗi tài liệu |
| OQ | Open Question: câu hỏi mở, mã `OQ-<NN>`. | Câu hỏi mở | 00-project-overview/open-questions.md |
| Traceability | Truy vết: lưu được nguồn gốc yêu cầu để biết Task đáp ứng BRQ, User Story hay Goal nào. Dùng liên kết (danh sách mã, khai một chiều ở đối tượng đứng sau), không dùng cây cha-con; tra ngược bằng cách lọc. Bảng liên kết: 04-project-management/work-model.md §3. | Truy vết yêu cầu | 04-project-management/work-model.md |
| DoD | Definition of Done: danh sách điều kiện để coi một Task là hoàn thành. Khác mục "Hoàn thành khi" của Skill (điều kiện kết thúc từng Skill). | Definition of Done | 03-engineering/testing-strategy.md §12 |
| DoR | Definition of Ready: điều kiện để một Task được giao cho AI. | Definition of Ready | 04-project-management/task-breakdown.md §7 |
| Task | Đơn vị công việc chính thức ("cần thực hiện công việc cụ thể nào?"), mã `<KEY>-<N>`, có loại (Type `T<N>`), mức rủi ro (Risk), mức tự chủ (Autonomy), mục tiêu, phạm vi làm/không làm, tiêu chí nghiệm thu. Nhóm B. Ghi Plan và User Story/FR/BR mà nó phục vụ. | | 04-project-management/task-breakdown.md; task-backlog.md |
| Subtask | Bước bên trong một Task: thủ tục của Skill hoặc checklist trong Task Specification; thực thể nội bộ, không có ID riêng. Nhóm B. | Bước | 04-project-management/work-model.md |
| Dependency | Quan hệ "Task phải xong trước Task khác". Nhóm B. | Phụ thuộc | 04-project-management/task-backlog.md; Task Manifest |
| Nhóm A · B · C | Ba nhóm khái niệm của khung: A định nghĩa nghiệp vụ và sản phẩm (WHAT/WHY: BRD, BRQ, Goal, Epic, Feature, User Story) · B lập kế hoạch và quản lý công việc (HOW: Plan, Task, Subtask, Dependency) · C thực thi bằng AI (DO: Agent, Run, model·effort, Tool, Result, Review). | | 04-project-management/work-model.md §1 |
| Rule | Điều bắt buộc AI và người phải tuân thủ. | Quy tắc | .ai/rules/ |
| Skill | Hướng dẫn cách làm một loại việc cụ thể (không thay Rule, không nâng mức tự chủ). | Kỹ năng | .ai/skills/ |
| Agent | Vai thực hiện của AI, định nghĩa theo chức năng và quyền: Planner, Executor, Tester, Reviewer, Security. Không bắt buộc là một AI riêng. AI chỉ là R trong RACI, không bao giờ là A. | Vai AI | .ai/agents/README.md |
| Workflow | Quy trình điều phối: các bước của một Task và chuỗi Skill theo loại việc (mười lăm loại việc, từ tính năng mới đến rà soát định kỳ). | Quy trình | .ai/workflows/ |
| RACI | Ma trận vai trò: R (thực hiện), A (chịu trách nhiệm cuối, một người duy nhất; khác mức tự chủ của AI), C (được tư vấn), I (được thông báo). |  | .ai/agents/README.md |
| Rủi ro thấp / vừa / cao | Mức rủi ro review của một Task, tăng dần; mức càng cao review càng chặt (rủi ro cao cần hai người, một người độc lập). | Mức rủi ro | .ai/rules/project-rules.md (Thang dùng chung) |
| Mức tự chủ | Mức tự chủ của AI do Task cấp: chỉ trả lời, chỉ đọc, duyệt từng bước, làm trọn Task, miễn duyệt từng Task. Skill không được tự nâng mức; thiếu thì dừng và hỏi. | Mức tự chủ | .ai/rules/project-rules.md (Thang dùng chung); trần riêng của dự án: PROJECT.md §2.1 |
| Công khai / nội bộ / nhạy cảm / bí mật | Mức nhạy cảm của dữ liệu quy định được đưa gì vào AI; mức bí mật gồm secret, token, dữ liệu cá nhân, không được ghi/log. | Mức dữ liệu | .ai/rules/project-rules.md (Thang dùng chung); dữ liệu của dự án: PROJECT.md §3; xử lý theo mức: security-standards.md §1 |
| RBAC | Role-Based Access Control: phân quyền theo vai trò. | Phân quyền | 03-engineering/security-standards.md |
| OWASP Top 10 | Danh sách 10 nhóm rủi ro bảo mật web phổ biến nhất của OWASP, mã `A01:2025`…`A10:2025`; dùng để phân loại finding. |  | 03-engineering/security-standards.md §13 |
| ASVS / L1–L3 | OWASP Application Security Verification Standard: bộ yêu cầu kiểm chứng bảo mật, mã `V<chương>.<mục>.<yêu cầu>`. L1–L3: mức kiểm chứng tăng dần, dự án khai báo mức mục tiêu. | Mức ASVS | PROJECT.md §4; 03-engineering/security-standards.md §13 |
| UAT | User Acceptance Test: người dùng/PO thử nghiệm để chấp nhận trước khi phát hành. |  | 03-engineering/testing-strategy.md |
| CI / CD | Continuous Integration / Continuous Delivery: tự động build, test và phát hành. |  | 05-operations/deployment.md |
| ERD | Entity Relationship Diagram: sơ đồ quan hệ giữa các bảng dữ liệu. |  | 02-architecture/database-design.md |
| RPO / RTO | RPO: lượng dữ liệu tối đa chấp nhận mất khi sự cố. RTO: thời gian tối đa để khôi phục dịch vụ. |  | 05-operations/backup-recovery.md |
| KPI | Key Performance Indicator: chỉ số đo hiệu quả (VD: lead time, thời gian review). |  | 04-project-management/ai-kpi.md |
| QA | Quality Assurance: vai kiểm thử đảm bảo chất lượng. |  | .ai/agents/README.md |
| OUT | Outcome đo được của sản phẩm, mã `OUT-<NN>`, khai báo ở vision.md; BRD tham chiếu trong Tiêu chí thành công. | Kết quả mong đợi | 00-project-overview/vision.md |
| Cổng duyệt | Điều kiện phải đạt để kết thúc một giai đoạn vòng đời (Khám phá sản phẩm đến Cải tiến) và sang giai đoạn kế; cổng Khai báo dự án đứng trước Khám phá sản phẩm. Có người có thẩm quyền duyệt và có bằng chứng. | Cổng, gate | 04-project-management/gates-and-rigor.md §1 |
| Gọn / chuẩn / nghiêm ngặt | Độ nghiêm ngặt quy trình của cả dự án (cổng duyệt, tài liệu, review, truy vết, nhật ký AI), tăng dần; độc lập với rủi ro của Task. | Mức nghiêm ngặt | 04-project-management/gates-and-rigor.md §2; giá trị của dự án: PROJECT.md §4 |
| Goal | Desired Outcome: kết quả đầu ra người dùng hoặc tổ chức muốn đạt ("muốn đạt kết quả gì?"), mã `GOAL-<NN>` (không viết `G<N>` để khỏi nhầm cổng duyệt). Nhóm A. Nguồn: BRQ, OUT, chiến lược kinh doanh hoặc yêu cầu trực tiếp. Liên kết nhiều-nhiều với Epic và Plan, không phải cha-con. | Mục tiêu | 04-project-management/goals.md |
| Plan | Kế hoạch thực hiện một hoặc nhiều công việc ("sẽ thực hiện như thế nào?"), mã `PLAN-<NNN>`. Nhóm B. Có đúng một Nguồn (Goal, Epic, User Story hoặc yêu cầu độc lập) và danh sách Goals tuỳ chọn; chứa nhiều Task, thứ tự, điểm dừng; AI (Orchestrator) soạn, Tech Lead duyệt; có mục Kết quả sau khi xong. | Kế hoạch | .ai/plans/; 04-project-management/work-model.md |
| Task Manifest | File khai báo một Task cho bên thực thi: làm gì, chạy bằng cấu hình nào (agent, model·effort bắt đầu, trần, ngân sách, nâng mức), kiểm thế nào (AC kèm lệnh kiểm). Chỉ là metadata, không tự đổi model nếu bên thực thi không áp dụng. | Manifest | .ai/templates/TASK-MANIFEST-TEMPLATE.yaml |
| Run | Một lần thực thi Task trong phiên hoặc subagent riêng, mã `<KEY>-<N>#<n>`; ghi agent, model·effort thật, kết quả, bằng chứng, chi phí. | Lần chạy | .ai/templates/RUNS-TEMPLATE.md |
| Orchestrator | Phiên AI chính: lập Plan, gán model·effort cho từng Task, gửi Task tới subagent, đánh giá kết quả, nâng mức, kiểm tra phụ thuộc, tổng hợp. Không tự viết code của Task, không duyệt thay người. | Điều phối | .ai/workflows/task-execution.md |
| Nâng mức động | Task chạy ở mức model·effort thấp trước; kết quả không đạt vì năng lực thì chạy lại ở bậc cao hơn, tới mức trần đã duyệt. Thiếu đầu vào, yêu cầu mâu thuẫn, ngoài phạm vi thì dừng, không nâng. | Dynamic escalation | .ai/workflows/model-effort.md §3 |
| model/effort | Mức chạy của một Run, ghi như trong ai-config.yaml (ví dụ sonnet/low); văn bản chung nói "mức bắt đầu", "mức kế tiếp", "mức tối đa". | Mức model·effort | .ai/workflows/model-effort.md |
| Worktree | Môi trường cô lập, mỗi Task một nơi, để AI code và test. | Workspace cô lập | .claude/worktrees/ |
| MoSCoW | Thang ưu tiên duy nhất của khung: `Must` bắt buộc · `Should` nên có · `Could` có thì tốt · `Won't` không làm đợt này. | Ưu tiên | 01-requirements/FR/README.md |
| Mặc định khung / Chỗ dự án điền | Hai loại nội dung trong `docs/`: giá trị khung đặt sẵn, dự án được chỉnh (ghi "Mặc định khung"); và chỗ trống dự án điền (`<!-- Điền theo từng dự án: … -->`). Sàn không hạ được nằm ở `.ai/rules/`. | | 04-project-management/gates-and-rigor.md §3 |
| Tech Lead | Người quyết chia Task, mức rủi ro, mức tự chủ AI; duyệt khung `.ai/`, 03-engineering, 04-project-management và các cổng Khai báo dự án, Sẵn sàng giao việc, Code xong, Sẵn sàng phát hành. | | PROJECT.md §5; 04-project-management/gates-and-rigor.md §1 |
| Owner | Người quyết phát hành production; duyệt 05-operations và cổng Vận hành. | | PROJECT.md §5; 05-operations/README.md |
| Kiến trúc sư | Người duyệt thiết kế ở 02-architecture, ADR và cổng Thiết kế. | | 02-architecture/README.md |
| Security | Người duyệt phần thay đổi chạm tiền, phân quyền, dữ liệu cá nhân, migration, secret. Khác vai AI Security (chỉ khuyến nghị). | | PROJECT.md §5; .ai/agents/README.md |
| DevOps | Người thực hiện triển khai, sao lưu, khôi phục và diễn tập. | | 05-operations/backup-recovery.md §14 |
| Dev | Người viết code, là tác giả chịu trách nhiệm bàn giao Task. | Developer | 04-project-management/gates-and-rigor.md §1 (cổng Code xong) |
| Reviewer | Người review PR theo mức rủi ro. Khác vai AI Reviewer (chỉ khuyến nghị, không thay người duyệt). | | .ai/agents/README.md; .ai/skills/code-review/SKILL.md |
| Story Task · Technical Task · Bug · Improvement · Spike | Loại Task trong task backlog: hiện thực User Story/FR · việc kỹ thuật không gắn trực tiếp FR · lỗi so với FR/AC đã duyệt · cải tiến không đổi nghiệp vụ · khảo sát có giới hạn thời gian trước khi chia Task. Epic, User Story ở product backlog, không phải Task. | | 04-project-management/task-backlog.md §2 |
| Product Backlog / Task Backlog | Product Backlog: Epic và User Story có ưu tiên (PO quyết). Task Backlog: Task có ưu tiên, rủi ro (Tech Lead quyết rủi ro). | | 04-project-management/product-backlog.md; task-backlog.md |
| Delivery Report | Báo cáo bàn giao Task do AI soạn theo DELIVERY-REPORT-TEMPLATE; điều kiện của cổng Code xong. | Báo cáo bàn giao | .ai/templates/DELIVERY-REPORT-TEMPLATE.md |
| Smoke test | Kiểm tra nhanh các chức năng chính ngay sau deploy để xác nhận bản phát hành chạy được. | | 05-operations/deployment.md §11 |
| Proposed / Rejected / Superseded | Trạng thái riêng của ADR: đang đề xuất · đã xem xét và không chọn · bị thay bởi ADR mới. | | 02-architecture/ADR/README.md |
| AP | Access Pattern: mẫu truy cập dữ liệu, mã `AP-<NN>`; mỗi index, partition, phi chuẩn hoá, cache phải truy ra một AP. | Mẫu truy cập | 02-architecture/database-design.md §3.4 |
| Waiver | Miễn trừ có thời hạn một yêu cầu của khung, có lý do và người duyệt; không bỏ qua âm thầm. | Miễn trừ | PROJECT.md |
| Hallucination | AI tự tạo nghiệp vụ, API hoặc thư viện không tồn tại. | | 03-engineering/ai-governance.md |
| Context Drift | AI làm theo quyết định cũ hoặc tài liệu không còn hiệu lực. | | 03-engineering/ai-governance.md |
| False Confidence | AI báo hoàn thành nhưng chưa chạy test hoặc chưa kiểm tra hết trường hợp. | | 03-engineering/ai-governance.md |

Thuật ngữ nghiệp vụ của dự án nằm ở [docs/00-project-overview/glossary.md](../../docs/00-project-overview/glossary.md).
