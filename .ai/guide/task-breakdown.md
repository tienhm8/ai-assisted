# Task Breakdown

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | work-model.md, ../../docs/04-project-management/goals.md, ../../docs/04-project-management/task-backlog.md, ../../docs/04-project-management/product-backlog.md, ../../docs/04-project-management/roadmap.md, ../../docs/01-requirements/FR/, ../../.ai/workflows/task-execution.md, ../../.ai/workflows/task-types.md, ../../.ai/rules/project-rules.md |

> **Mục đích.** Chia Task trong Plan (**người quyết: Tech Lead**, duyệt khi duyệt Plan): mỗi Task có objective, scope in/out, AC, mức rủi ro (thấp, vừa, cao), mức tự chủ. Plan và Task Manifest nằm ở [.ai/plans/](../../.ai/plans/); Goal ở [goals](../../docs/04-project-management/goals.md); ba nhóm khái niệm ở [work-model](work-model.md).

## 1. Nguyên tắc chia Task

- **Nhỏ và nguyên tử:** một Task đạt một kết quả kiểm chứng được.
- **Một trách nhiệm:** không gộp nhiều chức năng hoặc nhiều module không liên quan.
- **Phạm vi rõ:** có In Scope và Out of Scope; AI không tự mở rộng.
- **Độc lập và kiểm thử được:** có AC và cách kiểm thử riêng.
- **Biết phụ thuộc:** ghi rõ Task phải xong trước.
- **Bàn giao tăng dần:** mỗi Task để lại hệ thống ở trạng thái chạy được.

## 2. Vị trí của Task và đặt tên

Task thuộc nhóm B (lập kế hoạch và quản lý công việc) cùng Plan, Subtask, Dependency; khái niệm và liên kết đầy đủ ở [work-model](work-model.md). Đây là liên kết, không phải cây cha-con:

| Khái niệm | Quan hệ với Task | Ở đâu |
| --- | --- | --- |
| Plan | Một Plan chứa nhiều Task; Task thuộc một Plan (hoặc không, ở fast lane) | [.ai/plans/](../../.ai/plans/) |
| User Story / FR / BR | Task phục vụ một hoặc nhiều; một User Story có thể cần nhiều Task | [product-backlog](../../docs/04-project-management/product-backlog.md), [FR](../../docs/01-requirements/FR/README.md) |
| Subtask | Bước bên trong Task: thủ tục của Skill hoặc checklist trong Task Specification; không có ID riêng | `SKILL.md`; mục 3 của mẫu dưới |
| Dependency | Task phải xong trước | cột Phụ thuộc; `dependencies` trong manifest |
| Run (nhóm C) | Một lần thực thi Task; một Task có thể chạy nhiều lần khi nâng mức | `.ai/plans/<plan>/runs.md` |

- **ID:** `<KEY>-<N>` theo công cụ quản lý việc; KEY là mã dự án hoặc mã module (ví dụ PRJ-1, AUTH-1, RE-1 như bảng ví dụ bên dưới; không đệm số 0 để khác mã FR).
- **Tên:** bắt đầu bằng động từ, nêu rõ đối tượng (ví dụ "Tạo bất động sản").
- **Quan hệ:** cột Phụ thuộc, Plan ở bảng Task; cột Phục vụ, Tách từ ở [task-backlog](../../docs/04-project-management/task-backlog.md). Subtask không lập ID riêng; việc cần mức model·effort khác thì tách thành Task riêng.

## 3. Phân loại Task

Gán một loại chính cho mỗi Task để chọn đúng tài liệu tham chiếu và kiểu kiểm thử.

| Loại | Tài liệu tham chiếu chính |
| --- | --- |
| Backend | [module-design](../../docs/02-architecture/module-design.md) |
| Frontend | [system-architecture](../../docs/02-architecture/system-architecture.md) |
| Database | [database-design](../../docs/02-architecture/database-design.md) |
| API | [api-design](../../docs/02-architecture/api-design.md) |
| Testing | [testing-strategy](../../docs/03-engineering/testing-strategy.md) |
| Infrastructure | [deployment](../../docs/05-operations/deployment.md) |
| Documentation | thư mục `docs/` liên quan |

Task chạm tiền, phân quyền, dữ liệu cá nhân hoặc migration phải đối chiếu [security-standards](../../docs/03-engineering/security-standards.md).

## 4. Giao việc cho AI

Giao việc thiếu thông tin là nguyên nhân thường gặp khiến AI code sai nghiệp vụ.

**Ví dụ không tốt:** "Hãy làm chức năng đăng tin bất động sản."

AI sẽ phải tự suy đoán:

- Ai được đăng?
- Đăng loại bất động sản nào?
- Trạng thái tin là gì?
- Có duyệt tin không?
- Có hình ảnh không?
- Có giới hạn số lượng không?
- Có kiểm tra quyền không?

Kết quả có thể chạy được nhưng sai nghiệp vụ. Vì vậy mỗi Task **PHẢI** theo mẫu dưới đây. Scope, Objective và AC phải đủ rõ để AI không tự mở rộng việc; mục không liên quan thì để trống, không xoá.

### Task Specification Template

```markdown
# TASK: [TASK-ID] - [TASK-NAME]

## 1. Objective
Mục tiêu cần đạt được.

## 2. Business Context
Bối cảnh nghiệp vụ liên quan.
- Phục vụ: US-…, FR-…, BR-…, NFR-…; tham chiếu: ADR-…
- Phân loại: loại Task, rủi ro thấp | vừa | cao (lý do), mức tự chủ của AI; ví dụ sửa lỗi · rủi ro thấp (dễ hoàn tác) · làm trọn Task (người duyệt kết quả cuối)
- Thuộc: Plan `PLAN-<NNN>` (Goal, nếu có, ghi ở Plan)

## 3. Requirements
Danh sách yêu cầu chức năng.

## 4. Business Rules
Các quy tắc nghiệp vụ bắt buộc.

## 5. Technical Constraints
- Architecture:
- Database:
- API:
- Security:
- Dependencies:

## 6. Scope
### In Scope
Những gì phải thực hiện.

### Out of Scope
Những gì không được thực hiện.

## 7. Acceptance Criteria
- [ ] FR-XXX-NN-AC1:
- [ ] FR-XXX-NN-AC2:
- [ ] FR-XXX-NN-AC3:

## 8. Testing Requirements
- Unit tests
- Integration tests
- E2E tests (if applicable)
- Security tests

## 9. Documentation
Các tài liệu phải cập nhật.

## 10. Estimate
Độ phức tạp (nhỏ / vừa / lớn) và công sức dự kiến.

## 11. Definition of Done
Theo testing-strategy §12. Điều kiện riêng của Task (nếu có):

## 12. Delivery Report
Theo DELIVERY-REPORT-TEMPLATE: một báo cáo cho cả Plan chứa Task này (fast lane: cho riêng Task).
```

Mục 12 do AI điền khi bàn giao. Mục 2 có thêm dòng Liên kết và Phân loại để khớp với bảng Task ở trên (cột Rủi ro, Tự chủ AI).

Task giao cho AI chạy trong một Plan còn có Task Manifest ([TASK-MANIFEST-TEMPLATE](../../.ai/templates/TASK-MANIFEST-TEMPLATE.yaml)): manifest lấy mục 1, 3, 6, 7 từ Task Specification và thêm cấu hình chạy (agent, thứ tự thử `try` (mức bắt đầu đến mức tối đa), ngân sách, nâng mức). Task Specification là bản cho người; manifest là bản cho bên thực thi; nội dung trùng thì Task Specification là gốc.

### Duyệt khi bàn giao và khi sẵn sàng phát hành
Bàn giao Task là cổng Code xong, sẵn sàng phát hành là cổng Sẵn sàng phát hành; điều kiện qua và người duyệt ở [gates-and-rigor](gates-and-rigor.md) §1.

### Quy tắc giao việc

Một Task nên đủ nhỏ để:

- AI hiểu chính xác.
- Phạm vi thay đổi có thể kiểm soát.
- Có thể kiểm thử độc lập.
- Có thể review.
- Có thể rollback khi cần.

Không giao Task kiểu "Xây dựng toàn bộ hệ thống quản lý bất động sản". Chia nhỏ, ví dụ:

| Task ID | Nội dung |
| --- | --- |
| AUTH-1 | Đăng ký tài khoản Customer |
| AUTH-2 | Xác minh email |
| AUTH-3 | Đăng nhập |
| AUTH-4 | Đăng xuất |
| RE-1 | Tạo bất động sản |
| RE-2 | Cập nhật bất động sản |
| RE-3 | Quản lý trạng thái tin |
| RE-4 | Tìm kiếm bất động sản |

## 5. Quản lý phụ thuộc

- **Loại phụ thuộc:** Task phải xong trước (chặn); dùng chung schema/API/hợp đồng; phụ thuộc hệ thống ngoài.
- **Thứ tự thực hiện:** database → backend/API → frontend → kiểm thử tích hợp, trừ khi Task ghi khác.
- **Task song song:** chỉ khi không chung file, schema hay hợp đồng API; nếu có, thực hiện tuần tự.
- Phụ thuộc ghi ở cột Phụ thuộc của bảng Task; không để AI tự suy ra.

## 6. Ước lượng

Ước lượng ghi ở mục Estimate của Task Specification, theo độ phức tạp (nhỏ / vừa / lớn) và công sức dự kiến. Rủi ro dùng thang thấp, vừa, cao, không dùng thang riêng. Task lớn phải chia nhỏ trước khi giao AI.

## 7. Điều kiện sẵn sàng (Definition of Ready)

Task chỉ được giao AI khi:

- Có FR/BR/NFR tham chiếu đã duyệt, thiết kế liên quan đã Approved ([02-architecture](../../docs/02-architecture/README.md)).
- Có Task Specification theo mẫu ở mục 4: Objective, Scope in/out và AC đã điền.
- Ưu tiên, rủi ro và mức tự chủ đã gán (trực tiếp, hoặc qua Plan đã duyệt).
- Task chạy trong Plan: có Task Manifest, mọi AC có cách kiểm.
- Phụ thuộc đã xong hoặc đã ghi rõ.

Đây là nguồn duy nhất của DoR; task-backlog chỉ trỏ tới.

Definition of Done ở [testing-strategy](../../docs/03-engineering/testing-strategy.md) §12; mục 11 của mẫu Task chỉ ghi điều kiện riêng của Task.

## 8. Checklist duyệt Task

- [ ] Task đủ nhỏ, một trách nhiệm.
- [ ] Scope in/out rõ, AC kiểm chứng được.
- [ ] Lưu được nguồn gốc: Task ghi User Story/FR/BR mà nó phục vụ (hoặc lý do), Plan ghi Nguồn.
- [ ] Rủi ro và mức tự chủ phù hợp với nội dung Task.
- [ ] Phụ thuộc đầy đủ.
- [ ] Yêu cầu kiểm thử và tài liệu cần cập nhật đã nêu.

## 9. Tham chiếu

- Quy trình AI thực hiện một Task (bắt buộc áp dụng): [.ai/workflows/task-execution.md](../../.ai/workflows/task-execution.md).
- [task-backlog](../../docs/04-project-management/task-backlog.md), [product-backlog](../../docs/04-project-management/product-backlog.md), [roadmap](../../docs/04-project-management/roadmap.md), [testing-strategy](../../docs/03-engineering/testing-strategy.md).
