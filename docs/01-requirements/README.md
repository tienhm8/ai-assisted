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
| [FR/](FR/README.md) | Yêu cầu chức năng, mỗi module một file `FR-<MODULE>.md`; nguồn chính của truy vết và trạng thái hoàn thành |
| [NFR.md](NFR.md) | Yêu cầu phi chức năng đo được (`NFR-<NN>`) |
| [business-rules.md](business-rules.md) | Quy tắc nghiệp vụ (`BR-<MODULE>-<NN>`); AI không tự tạo hay chốt |
| [acceptance-criteria.md](acceptance-criteria.md) | Định nghĩa "làm xong" của từng FR, dạng Given / When / Then |

## Thứ tự đọc và quan hệ

`BRD` → `FR` / `NFR` / `business-rules` → `acceptance-criteria`.

Truy vết: bảng FR giữ liên kết FR → BRQ và FR → BR; BRD và business-rules chỉ tham chiếu ngược. AC trỏ tới FR (và BR kiểm chứng). Trạng thái hoàn thành FR chỉ nằm ở bảng FR.

Đầu vào: [00-project-overview](../00-project-overview/) (vision, scope, glossary). Đầu ra: là đầu vào của [02-architecture](../02-architecture/).
