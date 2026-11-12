# Task Breakdown

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.2 ·  |
| Tài liệu liên quan | backlog.md, roadmap.md, ../01-requirements/FR/, ../../.ai/workflows/task-execution.md, ../../.ai/workflows/skill-selection.md, ../../.ai/rules/project-rules.md |

> **Mục đích.** Chia Task từ plan đã duyệt (**người quyết: Tech Lead**): mỗi Task có objective, scope in/out, AC, mức rủi ro R1–R3, mức tự chủ A0–A4. Chi tiết plan nằm ở [.ai/plans/](../../.ai/plans/).

| Task ID | Objective | Phạm vi in / out | AC | Rủi ro | Tự chủ AI | Phụ thuộc | Plan |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRJ-1 |  | | | R1 | A1 | | |

## 1. Nguyên tắc chia Task

- **Nhỏ và nguyên tử:** một Task đạt một kết quả kiểm chứng được.
- **Một trách nhiệm:** không gộp nhiều chức năng hoặc nhiều module không liên quan.
- **Phạm vi rõ:** có In Scope và Out of Scope; AI không tự mở rộng.
- **Độc lập và kiểm thử được:** có AC và cách kiểm thử riêng.
- **Biết phụ thuộc:** ghi rõ Task phải xong trước.
- **Bàn giao tăng dần:** mỗi Task để lại hệ thống ở trạng thái chạy được.

## 2. Phân cấp và đặt tên

| Cấp | Ý nghĩa | Nguồn |
| --- | --- | --- |
| Epic | Nhóm lớn theo mốc/module | [roadmap](roadmap.md) |
| Feature / Story | Chức năng theo FR | [FR](../01-requirements/FR/README.md) |
| Task | Đơn vị giao cho AI, theo mẫu bên dưới | file này |
| Subtask | Bước nhỏ trong Task, nằm trong plan, không lập ID riêng | [.ai/plans/](../../.ai/plans/) |

- **ID:** `<KEY>-<N>` theo công cụ quản lý việc; KEY là mã dự án hoặc mã module (ví dụ PRJ-1, AUTH-01, RE-01 như bảng ví dụ bên dưới).
- **Tên:** bắt đầu bằng động từ, nêu rõ đối tượng (ví dụ "Tạo bất động sản").
- **Quan hệ:** cột Phụ thuộc ở bảng Task và cột Cha ở [backlog](backlog.md).

## 3. Phân loại Task

Gán một loại chính cho mỗi Task để chọn đúng tài liệu tham chiếu và kiểu kiểm thử.

| Loại | Tài liệu tham chiếu chính |
| --- | --- |
| Backend | [module-design](../02-architecture/module-design.md) |
| Frontend | [system-architecture](../02-architecture/system-architecture.md) |
| Database | [database-design](../02-architecture/database-design.md) |
| API | [api-design](../02-architecture/api-design.md) |
| Testing | [testing-strategy](../03-engineering/testing-strategy.md) |
| Infrastructure | [deployment](../05-operations/deployment.md) |
| Documentation | thư mục `docs/` liên quan |

Task chạm tiền, phân quyền, dữ liệu cá nhân hoặc migration phải đối chiếu [security-standards](../03-engineering/security-standards.md).

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
- Liên kết: FR-…, BR-…, NFR-…, ADR-…
- Phân loại: rủi ro R1 | R2 | R3 (lý do) · mức tự chủ AI A0–A4

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
- Implementation completed.
- Tests executed and passed.
- No unresolved critical issues.
- Documentation updated.
- Code review completed.

## 12. Delivery Report
- Files changed:
- Implementation summary:
- Tests and results:
- Known limitations:
- Remaining risks:
```

Mục 12 do AI điền khi bàn giao. Mục 2 có thêm dòng Liên kết và Phân loại để khớp với bảng Task ở trên (cột Rủi ro, Tự chủ AI).

### Duyệt khi bàn giao và khi sẵn sàng phát hành
- **Bàn giao Task** (người quyết: Dev): cổng tự động cục bộ đạt (xem [testing-strategy](../03-engineering/testing-strategy.md) §9); Delivery Report đủ mục; không có thay đổi ngoài phạm vi mà chưa khai.
- **Sẵn sàng phát hành** (người quyết: Reviewer/QA): cổng kiểm tra đạt; review đủ theo rủi ro; AC được xác nhận; lỗi nghiêm trọng đã xử lý hoặc được chấp nhận chính thức.

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
| AUTH-01 | Đăng ký tài khoản Customer |
| AUTH-02 | Xác minh email |
| AUTH-03 | Đăng nhập |
| AUTH-04 | Đăng xuất |
| RE-01 | Tạo bất động sản |
| RE-02 | Cập nhật bất động sản |
| RE-03 | Quản lý trạng thái tin |
| RE-04 | Tìm kiếm bất động sản |

## 5. Quản lý phụ thuộc

- **Loại phụ thuộc:** Task phải xong trước (chặn); dùng chung schema/API/hợp đồng; phụ thuộc hệ thống ngoài.
- **Thứ tự thực hiện:** database → backend/API → frontend → kiểm thử tích hợp, trừ khi Task ghi khác.
- **Task song song:** chỉ khi không chung file, schema hay hợp đồng API; nếu có, thực hiện tuần tự.
- Phụ thuộc ghi ở cột Phụ thuộc của bảng Task; không để AI tự suy ra.

## 6. Ước lượng

Ước lượng ghi ở mục Estimate của Task Specification, theo độ phức tạp (nhỏ / vừa / lớn) và công sức dự kiến. Rủi ro dùng thang R1–R3, không dùng thang riêng. Task lớn phải chia nhỏ trước khi giao AI.

## 7. Điều kiện sẵn sàng (Definition of Ready)

Task chỉ được giao AI khi:

- Có FR/BR/NFR tham chiếu đã duyệt, thiết kế liên quan đã Approved ([02-architecture](../02-architecture/README.md)).
- Objective, Scope in/out và AC đã điền.
- Rủi ro R1–R3 và mức tự chủ A0–A4 đã gán.
- Phụ thuộc đã xong hoặc đã ghi rõ.

Definition of Done nằm trong mẫu Task ở mục 4 (mục 11 của mẫu).

## 8. Checklist duyệt Task

- [ ] Task đủ nhỏ, một trách nhiệm.
- [ ] Scope in/out rõ, AC kiểm chứng được.
- [ ] Truy vết được tới FR/BR.
- [ ] Rủi ro và mức tự chủ phù hợp với nội dung Task.
- [ ] Phụ thuộc đầy đủ.
- [ ] Yêu cầu kiểm thử và tài liệu cần cập nhật đã nêu.

## 9. Tham chiếu

- Quy trình AI thực hiện một Task (bắt buộc áp dụng): [.ai/workflows/task-execution.md](../../.ai/workflows/task-execution.md).
- [backlog](backlog.md), [roadmap](roadmap.md), [testing-strategy](../03-engineering/testing-strategy.md).
