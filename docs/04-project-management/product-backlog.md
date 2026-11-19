# Product Backlog

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | PO (BA soạn) |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | work-model.md, goals.md, roadmap.md, task-backlog.md, ../01-requirements/BRD.md, ../01-requirements/features.md, ../01-requirements/FR/ |

> **Mục đích.** Danh sách Epic và User Story của sản phẩm (nhóm A, định nghĩa nghiệp vụ và sản phẩm, [work-model](../../.ai/guide/work-model.md)), có ưu tiên. Không chứa Task: Task ở [task-backlog](task-backlog.md); Task và Plan ghi User Story mà chúng phục vụ, backlog này không ghi ngược.
>
> **Người quyết định:** PO quyết nội dung và ưu tiên.

## 1. Epic

Nhóm chức năng/công việc lớn theo phạm vi sản phẩm hoặc lộ trình. Mã `EPIC-<NN>`. Một Epic có thể đáp ứng nhiều BRQ và đóng góp vào nhiều Goal (ghi danh sách mã); Epic không phải con của Goal.

| ID | Tên | Mô tả ngắn | BRQ | Goal | Mốc ([roadmap](roadmap.md)) | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| EPIC-<NN> |  |  | BRQ-<NN>, … | GOAL-<NN>, … | MS<N> | |

## 2. User Story

Nhu cầu của người dùng: ai muốn làm gì và vì sao. Mã `US-<MODULE>-<NN>`. Viết theo mẫu *Là `<vai>`, tôi muốn `<hành động>`, để `<giá trị>`*; vai dùng đúng tên ở [glossary](../00-project-overview/glossary.md). Một User Story có thể chạm nhiều Feature và cần nhiều FR; tiêu chí nghiệm thu gắn với FR ở [acceptance-criteria](../01-requirements/acceptance-criteria.md), không viết lại ở đây.

| ID | Là (vai) | Tôi muốn | Để | Epic | Feature | FR | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- | --- |
| US-<MODULE>-<NN> |  |  |  | EPIC-<NN> | FEAT-<NN>, … | FR-<MODULE>-<NN>, … | |

## 3. Quy tắc

- Ưu tiên theo MoSCoW, dùng chung với BRD, FR, NFR.
- Trạng thái hoàn thành không ghi ở đây: suy ra từ trạng thái FR ([FR](../01-requirements/FR/README.md)) và Task phục vụ ([task-backlog](task-backlog.md)), theo nguyên tắc một nơi.
- Epic và User Story phải truy về BRQ (Epic trực tiếp; User Story qua Epic, Feature hoặc FR). Không có BRQ thì ghi `OQ-<NN>` ([open-questions](../00-project-overview/open-questions.md)), không đoán.
- Thêm, bỏ hoặc đổi ưu tiên mục thuộc mốc đang chạy phải được PO duyệt.

## Lịch sử thay đổi
| Ngày | Mục | Thay đổi | Lý do | Người duyệt |
| --- | --- | --- | --- | --- |
