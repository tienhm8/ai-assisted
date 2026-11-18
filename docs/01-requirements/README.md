# 01-requirements

> **Mục đích:** Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu
>
> **Người quyết: PO/BA** (QA rà khả năng kiểm thử).
>
> **Điều kiện duyệt:** mọi FR trong phạm vi có AC kiểm thử được; QA đã rà; điểm chưa rõ ghi vào [open-questions](../00-project-overview/open-questions.md). **Chưa đạt thì không sang thiết kế/code.**

## Cấu trúc

```text
01-requirements/
├── README.md
├── BRD.md
├── features.md
├── NFR.md
├── business-rules.md
├── acceptance-criteria.md
└── FR/
    └── README.md
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu |
| [BRD.md](BRD.md) | Yêu cầu nghiệp vụ ở mức mục tiêu và giá trị (`BRQ-<NN>`) |
| [features.md](features.md) | Function/Feature: hệ thống cần có chức năng gì (`FEAT-<NN>`); chi tiết hoá bằng FR |
| [FR/](FR/README.md) | Yêu cầu chức năng, mỗi module một file `FR-<MODULE>.md`; nguồn chính của truy vết và trạng thái hoàn thành |
| [NFR.md](NFR.md) | Yêu cầu phi chức năng đo được (`NFR-<NN>`) |
| [business-rules.md](business-rules.md) | Quy tắc nghiệp vụ (`BR-<MODULE>-<NN>`); AI không tự tạo hay chốt |
| [acceptance-criteria.md](acceptance-criteria.md) | Định nghĩa "làm xong" của từng FR, dạng Given / When / Then |

## Thứ tự đọc và quan hệ

`BRD` (BRQ) → `features` → `FR` / `NFR` / `business-rules` → `acceptance-criteria`.

Thư mục này giữ phần đặc tả của nhóm A, định nghĩa nghiệp vụ và sản phẩm: BRD, BRQ, Function/Feature và FR, NFR, BR, AC chi tiết hoá chúng. Goal, Epic, User Story cũng thuộc nhóm A nhưng là mục quản lý ưu tiên, nằm ở [04-project-management](../04-project-management/README.md) (goals, product-backlog). Ba nhóm và cách liên kết: [work-model](../04-project-management/work-model.md). Tài liệu ở đây không ghi Goal, Epic, User Story, Plan, Task; các đối tượng đó trỏ về đây.

Truy vết: Feature ghi BRQ (nhiều-nhiều); bảng FR giữ liên kết FR → BRQ, FR → Feature và FR → BR; BRD và business-rules chỉ tham chiếu ngược. AC trỏ tới FR (và BR kiểm chứng). Trạng thái hoàn thành FR chỉ nằm ở bảng FR.

Đầu vào: [00-project-overview](../00-project-overview/) (vision, scope, glossary). Đầu ra: là đầu vào của [02-architecture](../02-architecture/).
