# Glossary

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | vision.md, scope.md, ../../README.md |

> **Mục đích.** Thuật ngữ dùng thống nhất cho người và AI. AI không tự đặt nghĩa mới.
>
> **Người quyết định:** PO (phần nghiệp vụ dự án), Tech Lead (phần khung).
>
> **Cách dùng:** Phần 1: Thuật ngữ chung. Phần 2: Thuật ngữ nghiệp vụ dự án.
>
> **Về đường dẫn `.ai/`:** đổi tên theo công cụ chính (ví dụ Claude Code: `.claude/`) và cập nhật cột "Nguồn" cho khớp.

## 1. Thuật ngữ chung

| Thuật ngữ | Định nghĩa | Đồng nghĩa / Tránh dùng | Nguồn |
| --- | --- | --- | --- |
| FR | Functional Requirement: yêu cầu chức năng, hệ thống phải làm gì. | Yêu cầu chức năng | 01-requirements/FR/ |
| NFR | Non-Functional Requirement: yêu cầu phi chức năng (hiệu năng, bảo mật, độ sẵn sàng…). | Yêu cầu phi chức năng | 01-requirements/ |
| AC | Acceptance Criteria: tiêu chí nghiệm thu, điều kiện kiểm thử được để coi một FR là xong. | Tiêu chí nghiệm thu | 01-requirements/acceptance-criteria.md |
| Given / When / Then | Cách viết AC theo 3 bước: **Given** (bối cảnh ban đầu), **When** (hành động xảy ra), **Then** (kết quả mong đợi). VD: Given người dùng đã đăng nhập, When bấm "Đăng xuất", Then hệ thống quay về trang đăng nhập. | GWT | 01-requirements/acceptance-criteria.md |
| ADR | Architecture Decision Record: ghi lại một quyết định kiến trúc lớn và lý do. | Quyết định kiến trúc | 02-architecture/ADR/ |
| PO | Product Owner: người quyết định phạm vi và ưu tiên sản phẩm. |  | PROJECT.md |
| BA | Business Analyst: người phân tích và làm rõ yêu cầu nghiệp vụ. |  | PROJECT.md |
| E2E | End-to-end test: kiểm thử toàn luồng từ giao diện đến dữ liệu. |  | 03-engineering/testing-strategy.md |
| BRD | Business Requirements Document: tài liệu yêu cầu nghiệp vụ ở mức mục tiêu và giá trị; nguồn để suy ra FR/NFR. |  | 01-requirements/BRD.md |
| BRQ | Business Requirement: một yêu cầu nghiệp vụ trong BRD, mã `BRQ-<NN>`. Mỗi BRQ được phủ bởi ít nhất một FR; FR ghi BRQ nguồn. | Yêu cầu nghiệp vụ | 01-requirements/BRD.md |
| BR | Business Rule: quy tắc nghiệp vụ, mã `BR-<MODULE>-<NN>`. | Quy tắc nghiệp vụ | 01-requirements/business-rules.md |
| Open / Assumption / Closed | Trạng thái của điểm chưa rõ, mã `OQ-<NN>`. `Open`: chưa có câu trả lời. `Assumption`: giả định tạm dùng để đi tiếp, cần xác nhận. `Closed`: đã quyết. | Câu hỏi mở | 00-project-overview/open-questions.md |
| Draft / Approved | Trạng thái tài liệu. `Draft`: bản nháp. `Approved`: đã được người có thẩm quyền duyệt, được dùng làm căn cứ. |  | Bảng thuộc tính đầu mỗi tài liệu |
| OQ | Open Question: câu hỏi mở, mã `OQ-<NN>`. | Câu hỏi mở | 00-project-overview/open-questions.md |
| Traceability | Truy vết: liên kết BRQ → FR → AC → test (khai báo một chiều ở bảng FR và AC, tra ngược bằng cách lọc) để biết mỗi yêu cầu được làm và kiểm thử ở đâu. | Truy vết yêu cầu | .ai/skills/documentation/SKILL.md |
| DoD | Definition of Done: danh sách điều kiện để coi một việc là hoàn thành. | Definition of Done | .ai/skills/*/SKILL.md mục 7 |
| Task | Đơn vị công việc giao cho người hoặc AI, có mục tiêu, phạm vi làm/không làm, tiêu chí nghiệm thu, mức rủi ro và mức tự chủ. Mã `<KEY>-<N>`. |  | 04-project-management/task-breakdown.md |
| Rule | Điều bắt buộc AI và người phải tuân thủ. | Quy tắc | .ai/rules/ |
| Skill | Hướng dẫn cách làm một loại việc cụ thể (không thay Rule, không nâng mức tự chủ). | Kỹ năng | .ai/skills/ |
| Agent | Vai thực hiện của AI, định nghĩa theo chức năng. Có 5 vai chuẩn (Planner, Executor, Tester, Reviewer, Security). AI chỉ là R trong RACI, không bao giờ là A. | Vai AI | .ai/agents/README.md |
| Vai chi tiết | Vai cụ thể thuộc đúng một vai chuẩn (VD: Product Owner và Architect thuộc Planner; QA thuộc Tester), gồm Rule, Skill và quyền; không phải một AI riêng. | Vai chi tiết | .ai/agents/README.md |
| Workflow | Chuỗi Skill được sắp xếp theo loại việc (T1…T15). | Quy trình | .ai/workflows/ |
| RACI | Ma trận vai trò: R (thực hiện), A (chịu trách nhiệm cuối, một người duy nhất; khác A0–A4), C (được tư vấn), I (được thông báo). |  | .ai/agents/README.md |
| R1 / R2 / R3 | Mức rủi ro review của một Task, tăng dần từ R1 đến R3; mức càng cao review càng chặt (R3 cần hai người, một người độc lập). | Mức rủi ro | PROJECT.md; testing-strategy.md |
| A0–A4 | Mức tự chủ của AI do Task cấp, từ A0 đến A4. Skill không được tự nâng mức; thiếu thì dừng và hỏi. | Mức tự chủ | PROJECT.md (mức tự chủ) |
| D0–D3 | Mức nhạy cảm của dữ liệu quy định được đưa gì vào AI; D3 gồm secret, token, dữ liệu cá nhân, không được ghi/log. | Mức dữ liệu | PROJECT.md (mức dữ liệu); security-standards.md |
| RBAC | Role-Based Access Control: phân quyền theo vai trò. | Phân quyền | 03-engineering/security-standards.md |
| UAT | User Acceptance Test: người dùng/PO thử nghiệm để chấp nhận trước khi phát hành. |  | 03-engineering/testing-strategy.md |
| CI / CD | Continuous Integration / Continuous Delivery: tự động build, test và phát hành. |  | 05-operations/deployment.md |
| ERD | Entity Relationship Diagram: sơ đồ quan hệ giữa các bảng dữ liệu. |  | 02-architecture/database-design.md |
| RPO / RTO | RPO: lượng dữ liệu tối đa chấp nhận mất khi sự cố. RTO: thời gian tối đa để khôi phục dịch vụ. |  | 05-operations/backup-recovery.md |
| KPI | Key Performance Indicator: chỉ số đo hiệu quả (VD: lead time, thời gian review). |  | 04-project-management/ai-kpi.md |
| QA | Quality Assurance: vai kiểm thử đảm bảo chất lượng. |  | agents/README.md |
| OUT | Outcome đo được của sản phẩm, mã `OUT-<NN>`, khai báo ở vision.md; BRD tham chiếu trong Tiêu chí thành công. | Kết quả mong đợi | 00-project-overview/vision.md |
| G0–G7 | Các cổng duyệt giữa các giai đoạn vòng đời; chỉ qua cổng khi có bằng chứng. | Cổng, gate | README.md (Cấu trúc tài liệu) |
| Profile / S1–S3 | Profile: bộ tailoring theo loại dự án. S1–S3: mức nghiêm ngặt về truy vết và kiểm soát, tăng dần. | Mức nghiêm ngặt | PROJECT.md |
| Plan | Kế hoạch do AI soạn, Tech Lead duyệt, nối từ đặc tả sang Task; có mục Kết quả sau khi xong. | Kế hoạch | .ai/plans/ |
| Worktree | Môi trường cô lập, mỗi Task một nơi, để AI code và test. | Workspace cô lập | .ai/worktrees/ |
| MoSCoW | Thang ưu tiên duy nhất của khung: `Must` bắt buộc · `Should` nên có · `Could` có thì tốt · `Won't` không làm đợt này. | Ưu tiên | 01-requirements/FR/README.md |
| Waiver | Miễn trừ có thời hạn một yêu cầu của khung, có lý do và người duyệt; không bỏ qua âm thầm. | Miễn trừ | PROJECT.md |
| Hallucination | AI tự tạo nghiệp vụ, API hoặc thư viện không tồn tại. | | README.md (Năm rủi ro) |
| Context Drift | AI làm theo quyết định cũ hoặc tài liệu không còn hiệu lực. | | README.md (Năm rủi ro) |
| False Confidence | AI báo hoàn thành nhưng chưa chạy test hoặc chưa kiểm tra hết trường hợp. | | README.md (Năm rủi ro) |

## 2. Thuật ngữ nghiệp vụ dự án

| Thuật ngữ | Định nghĩa | Đồng nghĩa / Tránh dùng | Nguồn |
| --- | --- | --- | --- |
|  |  |  |  |
