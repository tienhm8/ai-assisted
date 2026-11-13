# 03-engineering

> **Mục đích:** Hướng dẫn sử dụng, phạm vi và quy tắc áp dụng Engineering Standards
>
> **Người quyết: Tech Lead** (thêm Security nếu quy chuẩn đụng tới xác thực, phân quyền, dữ liệu nhạy cảm).
>
> **Điều kiện áp dụng:** mọi code mới và mọi lần review đều phải tuân thủ các quy chuẩn trong thư mục này. Ngoại lệ phải được ghi lại và được Tech Lead chấp thuận.

## Cấu trúc

```text
03-engineering/
├── README.md
├── coding-standards.md
├── security-standards.md
├── error-handling.md
├── testing-strategy.md
├── ai-governance.md
└── external-skills.md
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và quy tắc áp dụng Engineering Standards |
| [coding-standards.md](coding-standards.md) | Quy chuẩn viết code, cấu trúc source code, naming, design principles |
| [security-standards.md](security-standards.md) | Quy tắc bảo mật khi phát triển và review code |
| [error-handling.md](error-handling.md) | Quy chuẩn xử lý exception, error, logging và phản hồi lỗi |
| [testing-strategy.md](testing-strategy.md) | Chiến lược kiểm thử, loại test, coverage và điều kiện chất lượng |
| [ai-governance.md](ai-governance.md) | Giải thích kiểm soát AI: việc cần duyệt, năm rủi ro |
| [external-skills.md](external-skills.md) | Quy trình tiếp nhận Skill bên ngoài (cộng đồng, package) |

## Thứ tự đọc và quan hệ

`coding-standards` → `error-handling` / `security-standards` → `testing-strategy` (kiểm chứng việc tuân thủ các quy chuẩn trước đó).

Đầu vào: [02-architecture](../02-architecture/) (kiến trúc, module, API, ADR). Quy chuẩn phải nhất quán với các quyết định kiến trúc; nếu mâu thuẫn thì xử lý bằng cách cập nhật quy chuẩn hoặc tạo ADR mới, không tự bỏ qua.

Khi review, dùng cả ba checklist: [coding-standards](coding-standards.md) §9.1, [error-handling](error-handling.md) §11 và [security-standards](security-standards.md) §11.
