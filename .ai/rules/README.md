# rules

Bộ quy tắc **bắt buộc** AI phải tuân thủ khi làm việc trong dự án. Rule không phải câu prompt viết tùy hứng: đó là tiêu chuẩn ổn định, có người phụ trách và trạng thái.

## Các nhóm Rule

| Nhóm | Nội dung | File |
| --- | --- | --- |
| Project Rules | Quy tắc chung của dự án | project-rules.md |
| Architecture Rules | Quy tắc kiến trúc | architecture-rules.md |
| Coding Rules | Quy tắc viết code và xử lý lỗi | coding-rules.md |
| Database Rules | Quy tắc thiết kế và thao tác dữ liệu | database-rules.md |
| Cache Rules | Quy tắc dùng cache | cache-rules.md |
| Document Database Rules | Quy tắc riêng cho CSDL tài liệu | document-database-rules.md |
| Security Rules | Quy tắc bảo mật | security-rules.md |
| Testing Rules | Quy tắc kiểm thử | testing-rules.md |
| Git Workflow Rules | Quy tắc nhánh, commit, PR, merge | git-workflow-rules.md |

## Nguyên tắc

- **Rule tự đủ nghĩa, ngắn gọn, không tham chiếu đi đâu.** Rule không trỏ sang tài liệu hay thành phần khác.
- **Phân vai:** giá trị riêng của dự án (ngưỡng, công cụ, mã lỗi, ngôn ngữ, kiến trúc) nằm trong tài liệu dự án; rule chỉ giữ điều AI phải làm hoặc không được làm.
- **Phép thử:** chép rule sang dự án dùng stack khác mà vẫn đúng thì giữ ở đây; nếu không thì chuyển sang tài liệu dự án.
- **Một câu cấm, một nơi:** không lặp cùng một điều ở hai rule.
- **Kiểm chứng được:** ưu tiên viết thành điều kiện đo được để hook, linter hoặc branch protection kiểm tra; rule chưa tự động hoá được thì cần người review.
- Chỉ được cụ thể hoá hoặc siết chặt, không hạ sàn bảo mật hay governance.
- **Ngôn ngữ:** nội dung rule viết bằng tiếng Anh để tiết kiệm token; đầu ra cho người vẫn bằng tiếng Việt (`project-rules` 22).
- Sửa rules thuộc vùng 🔴: cần Task riêng và người duyệt.
