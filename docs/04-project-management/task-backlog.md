# Task Backlog

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead (PO quyết ưu tiên) |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | ../../.ai/guide/work-model.md, product-backlog.md, goals.md, ../../.ai/guide/task-breakdown.md, roadmap.md, ../01-requirements/FR/, ../01-requirements/business-rules.md |

> **Mục đích.** Danh sách Task (nhóm B, lập kế hoạch và quản lý công việc, [work-model](../../.ai/guide/work-model.md)) chờ làm, có ưu tiên. Task có ID theo công cụ quản lý việc (<KEY>-<N>). Epic và User Story ở [product-backlog](product-backlog.md), không ở đây. Backlog chỉ liệt kê và xếp thứ tự; Objective, Scope, AC chi tiết của từng Task nằm ở [task-breakdown](../../.ai/guide/task-breakdown.md), không chép vào đây.

## 1. Quy tắc quản lý task backlog

- Mỗi việc có đúng một dòng và một ID duy nhất.
- Mọi Task phải lưu được nguồn gốc yêu cầu: cột "Phục vụ" ghi một hoặc nhiều User Story, FR, BR (`US-<MODULE>-<NN>`, `FR-<MODULE>-<NN>`, `BR-<MODULE>-<NN>`); một Task có thể phục vụ nhiều User Story. Task không có yêu cầu nguồn (bug, kỹ thuật) ghi lý do. Goal và BRQ truy qua Plan và User Story/FR, không ghi lại ở đây.
- Product Owner quyết ưu tiên; Tech Lead quyết rủi ro. Việc chưa Ready không được giao AI.

## 2. Loại việc và ID

| Loại | Ý nghĩa |
| --- | --- |
| Story Task | Hiện thực một hoặc nhiều User Story / FR |
| Technical Task | Việc kỹ thuật không gắn trực tiếp FR (hạ tầng, refactor) |
| Bug | Lỗi so với FR/AC đã duyệt |
| Improvement | Cải tiến không đổi nghiệp vụ |
| Spike | Khảo sát có giới hạn thời gian để làm rõ trước khi chia Task |

ID theo công cụ quản lý việc: `<KEY>-<N>` (KEY là mã dự án hoặc mã module, ví dụ PRJ-1, AUTH-1; không đệm số 0 để khác mã FR). File này chỉ chứa Task. Goal, Epic, User Story (nhóm A) ở [goals](goals.md), [product-backlog](product-backlog.md); Plan ở `.ai/plans/`. Cột Phục vụ ghi yêu cầu nguồn; cột Plan ghi Task thuộc Plan nào (`PLAN-<NNN>`, trống nếu chạy fast lane); cột Phụ thuộc là Dependency; cột Tách từ chỉ dùng khi Task tách từ Task khác (Spike → Task). Subtask là bước trong Task, không thành dòng.

## 3. Danh sách công việc

| Task ID | Loại | Tên | Tách từ | Plan | Phục vụ (US/FR/BR) | Module | Ưu tiên | Rủi ro | Phụ thuộc | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <KEY>-<N> | | | | PLAN-<NNN> | US-<MODULE>-<NN>, … | | | thấp | | |

## 4. Ưu tiên

Dùng thang MoSCoW chung với BRD, FR, NFR: `Must` · `Should` · `Could` · `Won't` (xem [FR/README](../01-requirements/FR/README.md)). Task kế thừa ưu tiên cao nhất của User Story/FR mà nó phục vụ; Bug và việc kỹ thuật do PO xếp.

Tiêu chí xếp thứ tự trong cùng mức: giá trị nghiệp vụ, mức phụ thuộc của việc khác, rủi ro, công sức. Rủi ro (thấp, vừa, cao) và mức tự chủ định nghĩa ở [project-rules](../../.ai/rules/project-rules.md) (Thang dùng chung).

## 5. Trạng thái

`New` → `Ready` → `In Progress` → `In Review` → `Done`. Có thể chuyển sang `Blocked` hoặc `Cancelled` ở bất kỳ bước nào, ghi lý do.

Đây là trạng thái của Task. Trạng thái hoàn thành FR (`☐ ◐ ☑`) chỉ nằm ở [FR/](../01-requirements/FR/README.md); backlog không chép.

## 6. Làm rõ backlog (refinement)

- **Tần suất:** định kỳ theo nhịp dự án, và trước mỗi mốc ở roadmap.
- **Definition of Ready:** theo [task-breakdown](../../.ai/guide/task-breakdown.md) §7.
- **Ước lượng:** ghi ở mục Estimate của Task Specification ([task-breakdown](../../.ai/guide/task-breakdown.md)), không ghi ở backlog.
- **Rà soát phụ thuộc:** kiểm tra cột Phụ thuộc khi đổi ưu tiên hoặc thứ tự.

## 7. Quản lý thay đổi backlog

- Thêm, bỏ hoặc đổi ưu tiên việc thuộc mốc đang chạy phải được Product Owner duyệt.
- Đổi phạm vi phải đồng bộ với [roadmap](roadmap.md) và [scope](../00-project-overview/scope.md).

## 8. Tham chiếu

- [roadmap](roadmap.md), [task-breakdown](../../.ai/guide/task-breakdown.md)
- [FR](../01-requirements/FR/README.md), [business-rules](../01-requirements/business-rules.md)
