# Requirements Engineering

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (khung) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | work-model.md, gates-and-rigor.md, ../../docs/01-requirements/README.md, ../../docs/00-project-overview/open-questions.md, ../../docs/04-project-management/product-backlog.md, ../skills/requirement-analysis/SKILL.md, ../skills/requirement-review/SKILL.md, ../workflows/task-types.md |

> **Mục đích.** Giải thích Requirements Engineering (RE) trong vòng đời phát triển phần mềm và chỉ ra từng nhóm công việc RE được khung này thực hiện ở đâu: tài liệu nào chứa kết quả, Skill nào hỗ trợ, ai quyết. Tài liệu cho người đọc; AI không nạp khi làm Task. Khái niệm BRQ, Epic, Feature, User Story ở [work-model](work-model.md); cổng duyệt ở [gates-and-rigor](gates-and-rigor.md).

## 1. RE là gì và nằm ở đâu trong vòng đời

**Mục tiêu:** chuyển những gì đã khám phá được (giai đoạn Khám phá sản phẩm) thành yêu cầu phần mềm đầy đủ, rõ ràng, nhất quán và kiểm thử được. Kết quả là đầu vào của giai đoạn Thiết kế.

RE gồm bốn nhóm công việc, đi tuần tự nhưng được lặp lại khi yêu cầu đổi:

```text
Khám phá sản phẩm ─▶ [2.1 Thu thập] ─▶ [2.2 Phân tích & mô hình hoá] ─▶ [2.3 Đặc tả] ─▶ [2.4 Xác nhận & quản lý] ─▶ Thiết kế
                                                                                              │
                                                                         cổng "Yêu cầu" (PO/BA duyệt) ◀┘
```

- Giai đoạn khung: `requirements`; cổng đóng giai đoạn: **Yêu cầu** (mọi FR trong phạm vi có AC kiểm thử được và truy được về `SRC`/BRQ; điểm chưa chốt ghi `Open`/`Asked`). Chưa qua cổng thì không sang thiết kế/code.
- Người quyết nội dung: PO/BA; QA rà khả năng kiểm thử. AI chỉ chuẩn bị và đề xuất, không tự chuyển `Approved`.

## 2. Bốn nhóm công việc RE

### 2.1 Thu thập yêu cầu (Requirements Elicitation)

**Mục tiêu:** khai thác và thu thập yêu cầu từ các bên liên quan.

| Công việc | Trong khung này |
| --- | --- |
| Xác định stakeholders và nguồn yêu cầu | Vai trò ở `PROJECT.md` §5; mỗi tài liệu nguồn đăng ký mã `SRC-<NN>` ở [sources](../../docs/00-project-overview/sources/README.md) |
| Phỏng vấn, workshop, quan sát quy trình, phân tích tài liệu nghiệp vụ | Việc của người (PO/BA, Đầu mối dự án). Kết quả được lưu thành nguồn `SRC-<NN>` thì AI mới dùng được |
| Thu thập business rules | Ghi vào [business-rules](../../docs/01-requirements/business-rules.md) (`BR-<MODULE>-<NN>`); phải có nguồn đã duyệt, AI không tự tạo |
| Thu thập yêu cầu chức năng, phi chức năng ban đầu | FR ở `FR/FR-<MODULE>.md`; NFR ở [NFR](../../docs/01-requirements/NFR.md) |
| Xác định assumptions và constraints | Ghi vào đúng sổ OQ theo cấp (sổ chung, Module, Feature) và thêm dòng vào mục lục ở [sổ chung](../../docs/00-project-overview/open-questions.md), với loại `Input`/`Clarify`/`Decision`; assumption có hạn rà soát |

**Sản phẩm:** Stakeholder Requirements và Business Requirements (BRQ trong [BRD](../../docs/01-requirements/BRD.md)); FR và NFR ban đầu; Business Rules.

**Skill hỗ trợ:** `product-discovery` (khi chưa có vision, scope), `requirement-analysis` bước 1–2 (ngữ cảnh, tác nhân). Câu hỏi cho khách hàng đi qua Đầu mối dưới dạng gói câu hỏi.

### 2.2 Phân tích và mô hình hoá yêu cầu (Requirements Analysis & Modeling)

**Mục tiêu:** phân tích, làm rõ, cấu trúc và xác định tính khả thi của yêu cầu.

| Công việc | Trong khung này |
| --- | --- |
| Phân loại yêu cầu (nghiệp vụ, người dùng, chức năng, phi chức năng, kỹ thuật) | BRQ → BRD; User Story → [product-backlog](../../docs/04-project-management/product-backlog.md); FR → `FR/`; NFR → `NFR.md`. Yêu cầu kỹ thuật không viết vào FR mà thuộc [02-architecture](../../docs/02-architecture/README.md) |
| Phân tích khả thi | `requirement-review` bước 7: chỉ nêu rủi ro (kỹ thuật, tích hợp, dữ liệu, hiệu năng, bảo mật) để chuyển cho `architecture-design`; không quyết kiến trúc |
| Phân tích dependency giữa yêu cầu | Ghi tại FR liên quan (`requirement-analysis` bước 8) |
| Phát hiện mâu thuẫn, thiếu sót; giải quyết xung đột | `requirement-review` bước 1–3; điểm chưa quyết ghi `OQ-<NN>`, người có thẩm quyền quyết |
| Phân rã yêu cầu | BRQ → Feature → FR → AC; Epic → User Story |
| Xác định quy trình nghiệp vụ, mô hình hoá | Dùng kỹ thuật ở bảng dưới; hình đặt ở tài liệu tương ứng |

**Kỹ thuật mô hình hoá thường dùng:**

| Kỹ thuật | Mục đích | Nên đặt ở |
| --- | --- | --- |
| Use Case Diagram | Tương tác giữa actor và hệ thống | [features](../../docs/01-requirements/features.md) hoặc `FR/FR-<MODULE>.md` |
| Activity Diagram | Luồng nghiệp vụ | `FR/FR-<MODULE>.md` (chỉ FR rủi ro cao hoặc mơ hồ) |
| BPMN | Mô hình hoá quy trình nghiệp vụ | `FR/FR-<MODULE>.md` hoặc [scope](../../docs/00-project-overview/scope.md) cho quy trình xuyên module |
| Sequence Diagram | Tương tác theo thời gian | Thiết kế: [system-architecture](../../docs/02-architecture/system-architecture.md), [api-design](../../docs/02-architecture/api-design.md) |
| Data Flow Diagram | Luồng dữ liệu | [system-architecture](../../docs/02-architecture/system-architecture.md) |
| ERD | Mô hình dữ liệu (khái niệm/logic) | [database-design](../../docs/02-architecture/database-design.md) |
| State Diagram | Trạng thái và chuyển trạng thái | `FR/FR-<MODULE>.md` (vòng đời nghiệp vụ) hoặc thiết kế |

Khung chưa có tài liệu riêng cho Use Case Model, Business Process Model hay Requirement Analysis Report: hình và phân tích nằm trong các tài liệu ở cột "Nên đặt ở"; báo cáo phân tích là báo cáo của `requirement-review`.

**Sản phẩm:** mô hình quy trình và use case (nếu dự án cần), danh mục business rules, mô hình dữ liệu khái niệm/logic, báo cáo phân tích (báo cáo review).

### 2.3 Đặc tả yêu cầu (Requirements Specification)

**Mục tiêu:** ghi nhận yêu cầu thành tài liệu hoặc backlog có cấu trúc, thống nhất, dễ hiểu.

| Công việc | Trong khung này |
| --- | --- |
| Business Requirements | [BRD](../../docs/01-requirements/BRD.md) (BRQ) |
| Product Requirements | [features](../../docs/01-requirements/features.md) (Feature) và [scope](../../docs/00-project-overview/scope.md); khung không có file PRD riêng |
| Functional Requirements | Bảng FR ở `FR/FR-<MODULE>.md`, mỗi FR một câu; FR rủi ro cao hoặc mơ hồ có thêm tiền điều kiện, luồng chính, luồng lỗi bên dưới bảng |
| Non-functional Requirements | [NFR](../../docs/01-requirements/NFR.md): mỗi NFR có chỉ số và cách đo |
| User Stories | [product-backlog](../../docs/04-project-management/product-backlog.md) §2, dạng "Là <vai>, tôi muốn…, để…" |
| Use Case Specifications, exception và alternative flows, input/output, validation rules | Phần chi tiết dưới bảng FR (luồng chính, luồng thay thế, luồng lỗi) |
| Business rules | [business-rules](../../docs/01-requirements/business-rules.md) |
| Acceptance Criteria | [acceptance-criteria](../../docs/01-requirements/acceptance-criteria.md): Given / When / Then, có luồng lỗi và giá trị biên |
| System constraints, external interfaces | Ràng buộc ghi ở FR/NFR; giao diện ngoài chi tiết hoá ở [api-design](../../docs/02-architecture/api-design.md) |

**Ví dụ User Story kèm AC** (theo mẫu khung):

> **Là** người dùng đã đăng ký, **tôi muốn** đăng nhập bằng email và mật khẩu, **để** truy cập tài khoản cá nhân.
>
> - **Given** người dùng có tài khoản hợp lệ, **When** nhập đúng email và mật khẩu, **Then** hệ thống cho đăng nhập và chuyển tới trang Dashboard.
> - **Given** người dùng nhập sai mật khẩu, **When** bấm Login, **Then** hệ thống hiển thị thông báo lỗi phù hợp.

**Sản phẩm:** BRD, FR (tương đương SRS của dự án), User Story, AC, NFR, danh mục business rules. Tài liệu đặc tả không ghi Plan, Task.

**Skill hỗ trợ:** `requirement-analysis` bước 3–9.

### 2.4 Xác nhận và quản lý yêu cầu (Requirements Validation & Management)

**Mục tiêu:** bảo đảm yêu cầu đúng nhu cầu thực tế, thực hiện được và được kiểm soát xuyên suốt dự án.

**Xác nhận (Validation):**

| Công việc | Trong khung này |
| --- | --- |
| Requirement review, inspection, acceptance criteria review | Skill `requirement-review`: kiểm đủ, rõ, nhất quán, kiểm thử được, truy vết được; chỉ khuyến nghị, không sửa tài liệu |
| Stakeholder review, walkthrough, prototype validation | Việc của người. AI soạn **gói xác nhận** theo [CONFIRMATION-PACK-TEMPLATE](../templates/CONFIRMATION-PACK-TEMPLATE.md) (phạm vi, quy trình, wireframe/mockup từng màn hình, quy tắc, câu hỏi, ô xác nhận); BA rà, xuất HTML/PDF bằng `python3 -I .ai/scripts/export-pack.py <gói>.md --pdf`, gửi khách hàng. Khách trả lời và duyệt thì Đầu mối lưu thành `SRC-<NN>` |
| Sign-off | Cổng **Yêu cầu**: PO/BA duyệt, QA rà khả năng kiểm thử, Đại diện khách hàng duyệt qua Đầu mối (nếu có). Kết quả duyệt có `SRC-<NN>` thì mới chuyển `Approved` |

**Quản lý (Management):**

| Công việc | Trong khung này |
| --- | --- |
| Ưu tiên hoá | MoSCoW, dùng chung cho BRD, Feature, FR, NFR, product-backlog. Khung chưa dùng WSJF; dự án muốn dùng thì ghi ở `PROJECT.md` §6 |
| Baseline và quản lý phiên bản | Tài liệu `Approved` là baseline; phiên bản là lịch sử git và PR |
| Quản lý thay đổi và phân tích tác động | Loại Task `requirement-change`: `requirement-analysis` → `requirement-review` → PO/BA duyệt → các Task `feature`/`schema-change` bị ảnh hưởng ([task-types](../workflows/task-types.md)). Đổi FR đã `Approved` phải ghi lịch sử thay đổi (ngày, FR, thay đổi, lý do, người duyệt) |
| Truy vết | Một chiều, ghi ở phía "con": Feature giữ BRQ; User Story giữ Epic, Feature, FR; FR giữ BRQ, Feature, BR; AC trỏ FR và BR. Không lập ma trận truy vết riêng và không khai báo chiều ngược |
| Theo dõi trạng thái yêu cầu | Chỉ ở cột trạng thái của bảng FR |

**Sản phẩm:** bộ yêu cầu `Approved` (baseline), các liên kết truy vết trong tài liệu, bảng "Lịch sử thay đổi" của từng tài liệu (thay cho Requirements Change Log), product backlog đã xếp ưu tiên, bằng chứng duyệt (`SRC-<NN>`).

## 3. Đối chiếu sản phẩm RE chuẩn với khung

| Sản phẩm RE thường gặp | Tương đương trong khung | Ghi chú |
| --- | --- | --- |
| Stakeholder / Business Requirements | BRD, `SRC-<NN>` | |
| Initial Functional / Non-functional Requirements | `FR/`, `NFR.md` | |
| Business Rules, Business Rules Catalogue | `business-rules.md` | AI không tự tạo |
| Business Process Model, Use Case Model | Hình trong `FR/`, `features.md`, `scope.md` | Không có file riêng |
| Data Model (khái niệm/logic) | `database-design.md` | Thuộc giai đoạn Thiết kế |
| Requirement Analysis Report | Báo cáo của `requirement-review` | |
| BRD | `BRD.md` | |
| PRD | `features.md` + `scope.md` | Không có file riêng |
| SRS | `FR/` + `NFR.md` + `business-rules.md` + `acceptance-criteria.md` | |
| User Stories | `product-backlog.md` | |
| Use Case Specifications | Phần chi tiết dưới bảng FR | |
| NFR Catalogue | `NFR.md` | |
| Approved Requirements Baseline | Tài liệu `Approved` | |
| Requirements Traceability Matrix | Liên kết một chiều trong tài liệu | Khung chủ động không dùng ma trận riêng để tránh hai nguồn lệch nhau |
| Requirements Change Log | Bảng "Lịch sử thay đổi" từng tài liệu | |
| Prioritized Product Backlog | `product-backlog.md` | |
| Requirements Sign-off | Cổng **Yêu cầu** + `SRC-<NN>` | |

## 4. Ai làm gì

| Việc | Người | AI |
| --- | --- | --- |
| Thu thập (phỏng vấn, workshop, quan sát) | PO/BA, Đầu mối dự án | Không thay người; soạn gói câu hỏi, tóm tắt nguồn đã đăng ký |
| Phân tích, đặc tả | PO/BA quyết | `requirement-analysis` soạn bản nháp |
| Rà soát | QA rà khả năng kiểm thử | `requirement-review` báo cáo, khuyến nghị |
| Duyệt, sign-off, đổi ưu tiên | PO/BA (và Đại diện khách hàng qua Đầu mối) | Không duyệt, không tự đặt `Approved` |

Điểm chưa rõ, giả định, mâu thuẫn luôn ghi vào đúng sổ OQ theo cấp (Feature/FR/BR/AC → sổ Feature; chung Module → sổ Module; còn lại → [sổ chung](../../docs/00-project-overview/open-questions.md)) và cập nhật mục lục ở sổ chung; AI không tự trả lời và không làm theo phỏng đoán.
