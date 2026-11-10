# 02-architecture

> **Mục đích:** Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu
>
> **Người quyết: Kiến trúc sư** (thêm Security nếu thiết kế đụng tới tiền, phân quyền, dữ liệu cá nhân, migration).
>
> **Điều kiện sẵn sàng build:** thiết kế Approved, có ADR cho quyết định lớn. **Chưa đạt thì không code tính năng.**

## Cấu trúc

```text
02-architecture/
├── README.md
├── system-architecture.md
├── module-design.md
├── database-design.md
├── api-design.md
└── ADR/
    ├── README.md
    └── _template.md
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu |
| [system-architecture.md](system-architecture.md) | Kiến trúc tổng thể, thành phần hệ thống, thiết kế Authentication & Authorization và threat model |
| [module-design.md](module-design.md) | Phân rã module, trách nhiệm và quan hệ phụ thuộc |
| [database-design.md](database-design.md) | Thiết kế dữ liệu, entity, schema, quan hệ, constraint, migration |
| [api-design.md](api-design.md) | Hợp đồng API (endpoint, request/response, quyền, mã lỗi) và tích hợp hệ thống ngoài / liên module |
| [ADR/](ADR/README.md) | Lưu các quyết định kiến trúc có ảnh hưởng lớn |

## Thứ tự đọc và quan hệ

`system-architecture` → `module-design` → `database-design` / `api-design` → `ADR/` (ghi lại quyết định phát sinh ở mọi bước).

Đầu vào: [01-requirements](../01-requirements/) (FR, NFR, business rules). Module ([module-design](module-design.md)) và API ([api-design](api-design.md)) ghi FR phục vụ ở cột FR của chính bảng đó.