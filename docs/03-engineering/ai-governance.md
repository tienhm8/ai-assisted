# AI Governance

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người duyệt (dự án) | Tech Lead |
| Tài liệu liên quan | ../../.ai/rules/project-rules.md, ../../PROJECT.md §2, ../04-project-management/gates-and-rigor.md |

> **Mục đích.** Giải thích vì sao và ở mức nào AI bị kiểm soát: việc cần người duyệt, năm rủi ro cần quản lý. Điều bắt buộc với AI nằm ở [project-rules](../../.ai/rules/project-rules.md); file này chỉ là phần giải thích cho người đọc.

## 1. Nguyên tắc

AI không tự suy diễn quy tắc nghiệp vụ và không tự ý đổi kiến trúc khi chưa được phê duyệt. Định nghĩa mức tự chủ A0–A4, trần mặc định và nghĩa của vùng 🟢🟡🔴 ở [project-rules](../../.ai/rules/project-rules.md); dự án khai báo phần siết thêm và bản đồ vùng trong [PROJECT.md](../../PROJECT.md) §2 (vai ở [.ai/agents/](../../.ai/agents/README.md) không có mức riêng).

## 2. Việc cần người duyệt hoặc kiểm soát đặc biệt

| Hành động | Mức kiểm soát |
| --- | --- |
| Thay đổi kiến trúc, thay đổi RBAC | Phải được duyệt |
| Migration dữ liệu production | Phải được duyệt |
| Deploy production | Có approval, AI không tự deploy (project-rules 13) |
| Quản lý secrets | Không giao AI tùy ý |
| Xóa dữ liệu | Cần kiểm soát đặc biệt |

Các việc còn lại (đọc code, phân tích yêu cầu, viết code, viết test, sửa lỗi) AI làm trong phạm vi Task theo mức tự chủ được cấp.

## 3. Năm rủi ro cần quản lý

| # | Rủi ro | Biểu hiện | Chặn bởi ([project-rules](../../.ai/rules/project-rules.md)) |
| --- | --- | --- | --- |
| 1 | Hallucination | AI tự tạo ra nghiệp vụ, API hoặc thư viện không tồn tại | Rule 3 (không tự nghĩ ra nghiệp vụ, ghi `OQ`), Rule 16 (xác minh API, thư viện, lệnh tồn tại trước khi dùng) |
| 2 | Context Drift | AI làm theo quyết định cũ hoặc tài liệu không còn hiệu lực | Rule 14 (chỉ dùng tài liệu Approved), Rule 1 (chỉ nạp tài liệu Task chỉ tới), Rule 9 (cập nhật tài liệu cùng thay đổi) |
| 3 | Security Vulnerability | Code chạy được nhưng có lỗ hổng | Rule 19 (cổng tự động và review R3), Rule 13 và Rule 17 (không đụng production, không xoá không hoàn tác); `security-rules.md` |
| 4 | Overengineering | AI xây dựng phức tạp hơn yêu cầu | Rule 7 (chỉ sửa trong phạm vi Task), Rule 5 và Rule 6 (không tự đổi kiến trúc, không tự thêm dependency) |
| 5 | False Confidence | AI báo hoàn thành nhưng chưa chạy test hoặc chưa kiểm tra hết trường hợp | Rule 10 (báo kết quả kiểm tra thật và nêu rõ phần chưa kiểm tra), Rule 18 (tối đa 3 vòng sửa), Rule 20 (không tự coi cổng đã qua) |

Cách khắc phục không phải chỉ viết Prompt tốt hơn, mà phải có **tài liệu chuẩn** (`docs/`), **Rule** và **Skill** (`.ai/`), **CI/CD**, **Test** và **quyền hạn rõ ràng** (mức tự chủ ở Rule, bản đồ vùng trong `PROJECT.md`).
