# rules

Bộ quy tắc **bắt buộc** AI phải tuân thủ khi làm việc trong dự án. Rule không phải câu prompt viết tùy hứng: đó là tiêu chuẩn kỹ thuật và nghiệp vụ ổn định, có người phụ trách và trạng thái.

## Bảy nhóm Rule

| Nhóm | Nội dung | File dự kiến | Nguồn chính (docs) |
| --- | --- | --- | --- |
| Project Rules | Quy tắc chung của dự án | [project-rules.md](project-rules.md) | [vision](../../docs/00-project-overview/vision.md), [scope](../../docs/00-project-overview/scope.md), [business-rules](../../docs/01-requirements/business-rules.md) |
| Architecture Rules | Quy tắc kiến trúc | [architecture-rules.md](architecture-rules.md) | [system-architecture](../../docs/02-architecture/system-architecture.md), [module-design](../../docs/02-architecture/module-design.md), [ADR](../../docs/02-architecture/ADR/) |
| Coding Rules | Quy tắc viết code | [coding-rules.md](coding-rules.md) | [coding-standards](../../docs/03-engineering/coding-standards.md), [error-handling](../../docs/03-engineering/error-handling.md) |
| Database Rules | Quy tắc thiết kế và thao tác dữ liệu | [database-rules.md](database-rules.md) | [database-design](../../docs/02-architecture/database-design.md) |
| Security Rules | Quy tắc bảo mật | [security-rules.md](security-rules.md) | [security-standards](../../docs/03-engineering/security-standards.md) |
| Testing Rules | Quy tắc kiểm thử | [testing-rules.md](testing-rules.md) | [testing-strategy](../../docs/03-engineering/testing-strategy.md), [acceptance-criteria](../../docs/01-requirements/acceptance-criteria.md) |
| Git Workflow Rules | Quy tắc nhánh, commit, PR, merge | [git-workflow-rules.md](git-workflow-rules.md) | [coding-standards](../../docs/03-engineering/coding-standards.md) §5.1 |

Cả 7 file đã tạo. Nội dung là rule do chủ dự án ban hành.

## Nguyên tắc

- **Rule trỏ về tài liệu, không chép lại.** Tài liệu trong `docs/` là nguồn sự thật; rule chỉ nêu điều AI phải làm/không được làm và dẫn tới mục tương ứng. Nhờ vậy tài liệu và rule không thành hai nguồn mâu thuẫn.
- **Rule càng cụ thể, có thể kiểm chứng tự động càng tốt.** Ưu tiên viết rule thành điều kiện đo được (ví dụ: file đổi nằm trong path của task, có quét secret trước khi commit) để hook, linter hoặc branch protection kiểm tra thay con người. Rule chưa kiểm chứng tự động được vẫn giữ, nhưng phải ghi rõ là cần người review.
- Core Rules lấy từ tổ chức; thư mục này chỉ chứa phần **riêng của dự án**.
- Chỉ được cụ thể hoá hoặc siết chặt, không hạ sàn bảo mật/governance.
- AI không tự suy diễn quy tắc nghiệp vụ, không tự đổi kiến trúc khi chưa được phê duyệt.
- Sửa rules thuộc vùng 🔴: cần Task riêng và người duyệt.
