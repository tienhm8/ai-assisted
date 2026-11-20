# 01-requirements

> **Mục đích:** Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu
>
> **Người quyết: PO/BA** (QA rà khả năng kiểm thử).
>
> **Điều kiện duyệt:** mọi FR trong phạm vi có AC kiểm thử được; QA đã rà; điểm chưa rõ ghi vào đúng sổ OQ theo cấp (xem [FR/README](FR/README.md)). **Chưa đạt thì không sang thiết kế/code.**

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
    ├── README.md
    └── <MODULE>/                                  # tạo khi có FEAT-<NN> thuộc Module
        ├── open-questions.md                      # câu hỏi chung của Module
        └── <FEAT-NN>-<tên>/                       # tạo khi Feature có mã FEAT-<NN>
            ├── FR.md                              # thêm khi Feature có FR
            └── open-questions.md                  # câu hỏi của Feature, FR, BR, AC
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu |
| [BRD.md](BRD.md) | Yêu cầu nghiệp vụ ở mức mục tiêu và giá trị (`BRQ-<NN>`) |
| [features.md](features.md) | Function/Feature: hệ thống cần có chức năng gì (`FEAT-<NN>`); chi tiết hoá bằng FR |
| [FR/](FR/README.md) | Yêu cầu chức năng, mỗi Feature một thư mục có `FR.md` và sổ câu hỏi; nguồn chính của truy vết và trạng thái hoàn thành |
| [NFR.md](NFR.md) | Yêu cầu phi chức năng đo được (`NFR-<NN>`) |
| [business-rules.md](business-rules.md) | Quy tắc nghiệp vụ (`BR-<MODULE>-<NN>`); AI không tự tạo hay chốt |
| [acceptance-criteria.md](acceptance-criteria.md) | Định nghĩa "làm xong" của từng FR, dạng Given / When / Then |

## Thứ tự đọc và quan hệ

`BRD` (BRQ) → `features` → `FR` / `NFR` / `business-rules` → `acceptance-criteria`.

Thư mục này giữ phần đặc tả của nhóm A, định nghĩa nghiệp vụ và sản phẩm: BRD, BRQ, Function/Feature và FR, NFR, BR, AC chi tiết hoá chúng. Goal, Epic, User Story cũng thuộc nhóm A nhưng là mục quản lý ưu tiên, nằm ở [04-project-management](../04-project-management/README.md) (goals, product-backlog). Ba nhóm và cách liên kết: [work-model](../../.ai/guide/work-model.md). Tài liệu ở đây không ghi Goal, Epic, User Story, Plan, Task; các đối tượng đó trỏ về đây.

Truy vết: Feature ghi BRQ (nhiều-nhiều); bảng FR giữ liên kết FR → BRQ, FR → Feature và FR → BR; BRD và business-rules chỉ tham chiếu ngược. AC trỏ tới FR (và BR kiểm chứng). Trạng thái hoàn thành FR chỉ nằm ở bảng FR.

Đầu vào: [00-project-overview](../00-project-overview/) (vision, scope, glossary). Đầu ra: là đầu vào của [02-architecture](../02-architecture/).

## Câu hỏi làm rõ với BA

Câu hỏi mở chia theo cấp: sổ Module `FR/<MODULE>/open-questions.md`; sổ Feature `FR/<MODULE>/<FEAT-NN>-<tên>/open-questions.md`. Câu hỏi cấp dự án (vision, scope, BRQ, BRD, NFR, Epic, Goal): sổ [00-project-overview/open-questions.md](../00-project-overview/open-questions.md). Tra sổ con trước khi hỏi; OQ đã `Closed` thì áp dụng quyết định. Mã `OQ-<NN>` duy nhất toàn dự án.
