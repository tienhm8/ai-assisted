# Task Breakdown

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | backlog.md, ../01-requirements/FR/ |

> **Mục đích.** Chia Task từ plan đã duyệt (**người quyết: Tech Lead**): mỗi Task có objective, scope in/out, AC, mức rủi ro R1–R3, mức tự chủ A0–A4. Chi tiết plan nằm ở thư mục plans của công cụ AI.

| Task ID | Objective | Phạm vi in / out | AC | Rủi ro | Tự chủ AI | Phụ thuộc | Plan |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRJ-1 |  | | | R1 | A1 | | |

## Giao việc cho AI

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
- [ ] AC-01:
- [ ] AC-02:
- [ ] AC-03:

## 8. Testing Requirements
- Unit tests
- Integration tests
- E2E tests (if applicable)
- Security tests

## 9. Documentation
Các tài liệu phải cập nhật.

## 10. Definition of Done
- Implementation completed.
- Tests executed and passed.
- No unresolved critical issues.
- Documentation updated.
- Code review completed.

## 11. Delivery Report
- Files changed:
- Implementation summary:
- Tests and results:
- Known limitations:
- Remaining risks:
```

Mục 11 do AI điền khi bàn giao. Mục 2 có thêm dòng Liên kết và Phân loại để khớp với bảng Task ở trên (cột Rủi ro, Tự chủ AI).

### Duyệt khi bàn giao và khi sẵn sàng phát hành
- **Bàn giao Task** (người quyết: Dev): cổng tự động cục bộ đạt (xem [testing-strategy](../03-engineering/testing-strategy.md) §2); Delivery Report đủ mục; không có thay đổi ngoài phạm vi mà chưa khai.
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

Quy trình AI thực hiện một Task (bắt buộc áp dụng): [.ai/workflows/task-execution.md](../../.ai/workflows/task-execution.md).
