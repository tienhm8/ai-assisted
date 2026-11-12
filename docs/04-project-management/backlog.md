# Backlog

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.2 ·  |
| Tài liệu liên quan | roadmap.md, task-breakdown.md, ../01-requirements/FR/, ../01-requirements/business-rules.md |

> **Mục đích.** Danh sách việc chờ, ưu tiên. Task có ID theo công cụ quản lý việc (<KEY>-<N>). Backlog chỉ liệt kê và xếp thứ tự; Objective, Scope, AC chi tiết của từng Task nằm ở [task-breakdown](task-breakdown.md), không chép vào đây.

## 1. Quy tắc quản lý backlog

- Mỗi việc có đúng một dòng và một ID duy nhất.
- Mọi việc phải truy vết về FR/BR (định danh `FR-<MODULE>-<NN>`, `BR-<MODULE>-<NN>`); việc không có FR/BR (bug, kỹ thuật) ghi rõ lý do ở cột Tên hoặc Ghi chú.
- Product Owner quyết ưu tiên; Tech Lead quyết rủi ro. Việc chưa Ready không được giao AI.

## 2. Loại việc và ID

| Loại | Ý nghĩa |
| --- | --- |
| Epic | Nhóm lớn, tương ứng một mốc/module ở [roadmap](roadmap.md) |
| Feature / Story | Chức năng theo FR |
| Technical Task | Việc kỹ thuật không gắn trực tiếp FR (hạ tầng, refactor) |
| Bug | Lỗi so với FR/AC đã duyệt |
| Improvement | Cải tiến không đổi nghiệp vụ |
| Spike | Khảo sát có giới hạn thời gian để làm rõ trước khi chia Task |

ID theo công cụ quản lý việc: `<KEY>-<N>` (KEY là mã dự án hoặc mã module, ví dụ PRJ-1, AUTH-01). Quan hệ cha-con (Epic → Feature → Task) ghi ở cột Cha.

## 3. Danh sách công việc

| Task ID | Loại | Tên | Cha | FR/BR | Module | Ưu tiên | Rủi ro | Phụ thuộc | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRJ-1 | | | | | | | R1 | | |

## 4. Ưu tiên

Dùng thang MoSCoW chung với BRD, FR, NFR: `Must` · `Should` · `Could` · `Won't` (xem [FR/README](../01-requirements/FR/README.md)). Task kế thừa ưu tiên của FR nguồn; Bug và việc kỹ thuật do PO xếp.

Tiêu chí xếp thứ tự trong cùng mức: giá trị nghiệp vụ, mức phụ thuộc của việc khác, rủi ro, công sức. Rủi ro R1–R3 và mức tự chủ A0–A4 định nghĩa ở [task-breakdown](task-breakdown.md).

## 5. Trạng thái

`New` → `Ready` → `In Progress` → `In Review` → `Done`. Có thể chuyển sang `Blocked` hoặc `Cancelled` ở bất kỳ bước nào, ghi lý do.

Đây là trạng thái của Task. Trạng thái hoàn thành FR (`☐ ◐ ☑`) chỉ nằm ở [FR/](../01-requirements/FR/README.md); backlog không chép.

## 6. Làm rõ backlog (refinement)

- **Tần suất:** định kỳ theo nhịp dự án, và trước mỗi mốc ở roadmap.
- **Definition of Ready:** có FR/BR tham chiếu, ưu tiên và rủi ro đã gán, phụ thuộc đã rõ, đã có Task Specification ở [task-breakdown](task-breakdown.md).
- **Ước lượng:** ghi ở mục Estimate của Task Specification ([task-breakdown](task-breakdown.md)), không ghi ở backlog.
- **Rà soát phụ thuộc:** kiểm tra cột Phụ thuộc khi đổi ưu tiên hoặc thứ tự.

## 7. Quản lý thay đổi backlog

- Thêm, bỏ hoặc đổi ưu tiên việc thuộc mốc đang chạy phải được Product Owner duyệt.
- Đổi phạm vi phải đồng bộ với [roadmap](roadmap.md) và [scope](../00-project-overview/scope.md).

## 8. Tham chiếu

- [roadmap](roadmap.md), [task-breakdown](task-breakdown.md)
- [FR](../01-requirements/FR/README.md), [business-rules](../01-requirements/business-rules.md)
