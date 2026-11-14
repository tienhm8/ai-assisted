# Glossary

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | PO (§2 Thuật ngữ nghiệp vụ dự án) |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | vision.md, scope.md, ../../README.md |

> **Mục đích.** Thuật ngữ dùng thống nhất cho người và AI. AI không tự đặt nghĩa mới.
>
> **Người quyết định:** Tech Lead (§1, thuộc khung), PO (§2 khi áp vào dự án).
>
> **Cách dùng:** Phần 1: Thuật ngữ chung. Phần 2: Thuật ngữ nghiệp vụ dự án.
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
| E2E | End-to-end test: kiểm thử toàn luồng từ giao diện đến dữ liệu. |  | 03-engineering/testing-strategy.md |
| BRD | Business Requirements Document: tài liệu yêu cầu nghiệp vụ ở mức mục tiêu và giá trị; nguồn để suy ra FR/NFR. |  | 01-requirements/BRD.md |
| BRQ | Business Requirement: một yêu cầu nghiệp vụ trong BRD, mã `BRQ-<NN>`. Mỗi BRQ được phủ bởi ít nhất một FR; FR ghi BRQ nguồn. | Yêu cầu nghiệp vụ | 01-requirements/BRD.md |
| BR | Business Rule: quy tắc nghiệp vụ, mã `BR-<MODULE>-<NN>`. | Quy tắc nghiệp vụ | 01-requirements/business-rules.md |
| Open / Assumption / Closed | Trạng thái của điểm chưa rõ, mã `OQ-<NN>`. `Open`: chưa có câu trả lời. `Assumption`: giả định tạm dùng để đi tiếp, cần xác nhận. `Closed`: đã quyết. | Câu hỏi mở | 00-project-overview/open-questions.md |
| Draft / Approved | Trạng thái tài liệu: Draft → In Review → Approved → Deprecated. `Draft`: bản nháp. `Approved`: đã được người có thẩm quyền duyệt, được dùng làm căn cứ; chỉ người có thẩm quyền chuyển sang. `Deprecated`: hết hiệu lực. |  | Bảng thuộc tính đầu mỗi tài liệu |
| OQ | Open Question: câu hỏi mở, mã `OQ-<NN>`. | Câu hỏi mở | 00-project-overview/open-questions.md |
| Traceability | Truy vết: chuỗi `OUT → BRQ → FR → BR → AC → module/API → Task → test/commit`. Mỗi liên kết khai báo một chiều ở bảng phía sau (bảng FR, AC, module, API, Task), tra ngược bằng cách lọc; để biết mỗi yêu cầu được làm và kiểm thử ở đâu. | Truy vết yêu cầu | .ai/skills/documentation/SKILL.md |
| DoD | Definition of Done: danh sách điều kiện để coi một Task là hoàn thành. Khác mục "Hoàn thành khi" của Skill (điều kiện kết thúc từng Skill). | Definition of Done | 03-engineering/testing-strategy.md §12 |
| DoR | Definition of Ready: điều kiện để một Task được giao cho AI. | Definition of Ready | 04-project-management/task-breakdown.md §7 |
| Task | Đơn vị công việc giao cho người hoặc AI, có mục tiêu, phạm vi làm/không làm, tiêu chí nghiệm thu, mức rủi ro và mức tự chủ. Mã `<KEY>-<N>`. |  | 04-project-management/task-breakdown.md |
| Rule | Điều bắt buộc AI và người phải tuân thủ. | Quy tắc | .ai/rules/ |
| Skill | Hướng dẫn cách làm một loại việc cụ thể (không thay Rule, không nâng mức tự chủ). | Kỹ năng | .ai/skills/ |
| Agent | Vai thực hiện của AI, định nghĩa theo chức năng và quyền: Planner, Executor, Tester, Reviewer, Security. Không bắt buộc là một AI riêng. AI chỉ là R trong RACI, không bao giờ là A. | Vai AI | .ai/agents/README.md |
| Workflow | Quy trình điều phối: các bước của một Task và chuỗi Skill theo loại việc (T1…T15). | Quy trình | .ai/workflows/ |
| RACI | Ma trận vai trò: R (thực hiện), A (chịu trách nhiệm cuối, một người duy nhất; khác A0–A4), C (được tư vấn), I (được thông báo). |  | .ai/agents/README.md |
| R1 / R2 / R3 | Mức rủi ro review của một Task, tăng dần từ R1 đến R3; mức càng cao review càng chặt (R3 cần hai người, một người độc lập). | Mức rủi ro | .ai/rules/project-rules.md (Thang dùng chung) |
| A0–A4 | Mức tự chủ của AI do Task cấp, từ A0 đến A4. Skill không được tự nâng mức; thiếu thì dừng và hỏi. | Mức tự chủ | .ai/rules/project-rules.md (Thang dùng chung); trần riêng của dự án: PROJECT.md §2.1 |
| D0–D3 | Mức nhạy cảm của dữ liệu quy định được đưa gì vào AI; D3 gồm secret, token, dữ liệu cá nhân, không được ghi/log. | Mức dữ liệu | .ai/rules/project-rules.md (Thang dùng chung); dữ liệu của dự án: PROJECT.md §3; xử lý theo mức: security-standards.md §1 |
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
| Cổng duyệt (G0–G7) | Điều kiện phải đạt để kết thúc một giai đoạn vòng đời `[01]`–`[08]` và sang giai đoạn kế; G0 đứng trước `[01]`. Có người có thẩm quyền duyệt và có bằng chứng. | Cổng, gate | 04-project-management/gates-and-rigor.md §1 |
| S1–S3 | Độ nghiêm ngặt quy trình của cả dự án (cổng duyệt, tài liệu, review, truy vết, nhật ký AI), tăng dần; độc lập với R của Task. | Mức nghiêm ngặt | 04-project-management/gates-and-rigor.md §2; giá trị của dự án: PROJECT.md §4 |
| Plan | Kế hoạch do AI soạn, Tech Lead duyệt, nối từ đặc tả sang Task; có mục Kết quả sau khi xong. | Kế hoạch | .ai/plans/ |
| Worktree | Môi trường cô lập, mỗi Task một nơi, để AI code và test. | Workspace cô lập | .ai/worktrees/ |
| MoSCoW | Thang ưu tiên duy nhất của khung: `Must` bắt buộc · `Should` nên có · `Could` có thì tốt · `Won't` không làm đợt này. | Ưu tiên | 01-requirements/FR/README.md |
| Mặc định khung / Chỗ dự án điền | Hai loại nội dung trong `docs/`: giá trị khung đặt sẵn, dự án được chỉnh (ghi "Mặc định khung"); và chỗ trống dự án điền (`<!-- Điền theo từng dự án: … -->`). Sàn không hạ được nằm ở `.ai/rules/`. | | 04-project-management/gates-and-rigor.md §3 |
| Tech Lead | Người quyết chia Task, mức rủi ro, mức tự chủ AI; duyệt khung `.ai/`, 03-engineering, 04-project-management và cổng G0, G4–G6. | | PROJECT.md §5; 04-project-management/gates-and-rigor.md §1 |
| Owner | Người quyết phát hành production; duyệt 05-operations và cổng G7. | | PROJECT.md §5; 05-operations/README.md |
| Kiến trúc sư | Người duyệt thiết kế ở 02-architecture, ADR và cổng G3. | | 02-architecture/README.md |
| Security | Người duyệt phần thay đổi chạm tiền, phân quyền, dữ liệu cá nhân, migration, secret. Khác vai AI Security (chỉ khuyến nghị). | | PROJECT.md §5; .ai/agents/README.md |
| DevOps | Người thực hiện triển khai, sao lưu, khôi phục và diễn tập. | | 05-operations/backup-recovery.md §14 |
| Dev | Người viết code, là tác giả chịu trách nhiệm bàn giao Task. | Developer | 04-project-management/gates-and-rigor.md §1 (G5) |
| Reviewer | Người review PR theo mức rủi ro R. Khác vai AI Reviewer (chỉ khuyến nghị, không thay người duyệt). | | .ai/agents/README.md; .ai/skills/code-review/SKILL.md |
| Epic · Feature/Story · Technical Task · Bug · Improvement · Spike | Loại việc trong backlog: nhóm lớn theo mốc/module · chức năng theo FR · việc kỹ thuật không gắn trực tiếp FR · lỗi so với FR/AC đã duyệt · cải tiến không đổi nghiệp vụ · khảo sát có giới hạn thời gian trước khi chia Task. | | 04-project-management/backlog.md §2 |
| Delivery Report | Báo cáo bàn giao Task do AI soạn theo DELIVERY-REPORT-TEMPLATE; điều kiện của cổng G5. | Báo cáo bàn giao | .ai/templates/DELIVERY-REPORT-TEMPLATE.md |
| Smoke test | Kiểm tra nhanh các chức năng chính ngay sau deploy để xác nhận bản phát hành chạy được. | | 05-operations/deployment.md §11 |
| Proposed / Rejected / Superseded | Trạng thái riêng của ADR: đang đề xuất · đã xem xét và không chọn · bị thay bởi ADR mới. | | 02-architecture/ADR/README.md |
| AP | Access Pattern: mẫu truy cập dữ liệu, mã `AP-<NN>`; mỗi index, partition, phi chuẩn hoá, cache phải truy ra một AP. | Mẫu truy cập | 02-architecture/database-design.md §3.4 |
| Waiver | Miễn trừ có thời hạn một yêu cầu của khung, có lý do và người duyệt; không bỏ qua âm thầm. | Miễn trừ | PROJECT.md |
| Hallucination | AI tự tạo nghiệp vụ, API hoặc thư viện không tồn tại. | | 03-engineering/ai-governance.md |
| Context Drift | AI làm theo quyết định cũ hoặc tài liệu không còn hiệu lực. | | 03-engineering/ai-governance.md |
| False Confidence | AI báo hoàn thành nhưng chưa chạy test hoặc chưa kiểm tra hết trường hợp. | | 03-engineering/ai-governance.md |

## 2. Thuật ngữ nghiệp vụ dự án

| Thuật ngữ | Định nghĩa | Đồng nghĩa / Tránh dùng | Nguồn |
| --- | --- | --- | --- |
|  |  |  |  |

## Lịch sử thay đổi
| Ngày | Thay đổi | Lý do | Người duyệt |
| --- | --- | --- | --- |
