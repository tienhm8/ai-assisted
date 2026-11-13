# Coding Standards

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | security-standards.md, error-handling.md, testing-strategy.md, ../02-architecture/system-architecture.md, ../02-architecture/module-design.md, ../../.ai/rules/coding-rules.md |

> **Mục đích.** Convention code của dự án: cấu trúc source code, naming, format, lint, thực hành lập trình, ngưỡng review. Cụ thể hoá các quy tắc ở [.ai/rules/coding-rules.md](../../.ai/rules/coding-rules.md), không trái chúng.

## 1. Ngôn ngữ, framework, phiên bản
Stack và phiên bản chính thức ở [system-architecture](../02-architecture/system-architecture.md) §4; mục này chỉ ghi phiên bản ngôn ngữ/runtime bắt buộc khi viết code.

| Hạng mục | Giá trị |
| --- | --- |
| Ngôn ngữ / runtime và phiên bản |  |
| Chế độ kiểm tra kiểu (ví dụ TypeScript `strict`) |  |
| Kiểu thoát khỏi hệ thống kiểu (ví dụ `any`) | Chỉ dùng khi có lý do ghi rõ |
<!-- Điền theo từng dự án -->

## 2. Nguyên tắc chung
Clean Code, SOLID, DRY, KISS, YAGNI và Separation of Concerns áp dụng cho mọi dự án, là điều bắt buộc ở [coding-rules](../../.ai/rules/coding-rules.md) mục "Nguyên tắc thiết kế". Mục này chỉ ghi nguyên tắc dự án bổ sung.
<!-- Điền theo từng dự án: để trống nếu không có -->

## 3. Cấu trúc dự án

### 3.1 Cây thư mục
Cây thư mục mã nguồn và quy tắc đặt file vào đâu.
<!-- Điền theo từng dự án -->

### 3.2 Tổ chức file
Một file một trách nhiệm chính; giới hạn kích thước file theo §8 (dòng "Kích thước file"); vị trí đặt test, config, hằng số.
<!-- Điền theo từng dự án -->

### 3.3 Tổ chức module
Cấu trúc bên trong một module, khớp với phân rã ở [module-design](../02-architecture/module-design.md). Chỉ truy cập module khác qua interface công khai của module đó.
<!-- Điền theo từng dự án -->

### 3.4 Quản lý dependency
Quy tắc thêm/nâng cấp thư viện, ghim phiên bản, kiểm tra license và lỗ hổng. Quy tắc bảo mật chuỗi cung ứng ở [security-standards](security-standards.md).
<!-- Điền theo từng dự án -->

## 4. Naming Convention

| Đối tượng | Quy ước | Ví dụ |
| --- | --- | --- |
| Biến |  | |
| Hằng số |  | |
| Hàm / method |  | |
| Class / interface |  | |
| File / thư mục |  | |
| Bảng / cột DB |  | |
| Route API |  | |

Quy ước riêng cho database ở [database-design](../02-architecture/database-design.md) §2; cho API ở [api-design](../02-architecture/api-design.md) §3.2. Mục này là quy ước chung cho mã nguồn.

## 5. Format và công cụ

### 5.1 Quy tắc format
Indentation, độ dài dòng tối đa, thứ tự và nhóm import.
<!-- Điền theo từng dự án -->

### 5.2 Comment và tài liệu code
Comment giải thích *vì sao*, không lặp lại *cái gì*. Quy định khi nào bắt buộc docblock (API công khai, logic phức tạp).
<!-- Điền theo từng dự án -->

### 5.3 Công cụ format · lint · type-check
| Việc | Lệnh |
| --- | --- |
| format |  |
| lint |  |
| type-check |  |
| static analysis |  |

## 6. Thực hành lập trình

| Hạng mục | Quy tắc |
| --- | --- |
| Thiết kế hàm | Ngắn, một việc, ít tham số; tránh side effect ẩn. |
| Thiết kế class | Trách nhiệm đơn, ưu tiên composition hơn kế thừa. |
| Thiết kế interface | Nhỏ, tập trung theo nhu cầu của bên dùng. |
| Immutability | Ưu tiên dữ liệu bất biến; chỉ cho phép thay đổi khi có lý do. |
| Xử lý null | Quy ước chung cho null/undefined/giá trị rỗng; không trả null khi có thể dùng kiểu rõ nghĩa hơn. |
| Lập trình bất đồng bộ | Quy ước async/await, timeout, huỷ tác vụ, xử lý song song. |
| Quản lý tài nguyên | Luôn giải phóng kết nối, file, lock; dùng cơ chế tự đóng của ngôn ngữ. |

Xử lý exception và logging theo [error-handling](error-handling.md); bảo mật khi code theo [security-standards](security-standards.md).
<!-- Điền theo từng dự án: chi tiết theo ngôn ngữ -->

## 7. Kiến trúc và thiết kế trong code
Mục này chỉ nêu quy tắc khi viết code; thiết kế chính thức ở [system-architecture](../02-architecture/system-architecture.md) §3 và [module-design](../02-architecture/module-design.md) §3.

- **Tách tầng:** mỗi tầng chỉ làm đúng trách nhiệm đã định ở system-architecture §3.3.
- **Chiều phụ thuộc:** chỉ phụ thuộc theo chiều đã cho phép; cấm vòng phụ thuộc.
- **Design pattern:** chỉ dùng khi giải quyết vấn đề cụ thể; pattern được chuẩn hoá của dự án liệt kê tại đây.
- **Tránh coupling chặt:** phụ thuộc qua interface, inject dependency, không truy cập trực tiếp dữ liệu của module khác.

## 8. Chất lượng code

| Hạng mục | Quy tắc |
| --- | --- |
| Static analysis | Công cụ và mức cảnh báo chấp nhận được. |
| Lint | Ruleset dùng chung; không tắt rule nếu không có lý do ghi rõ. |
| Format | Tự động bằng công cụ, không tranh luận thủ công. |
| Kích thước file | Sàn ở [coding-rules](../../.ai/rules/coding-rules.md) 15. Dự án chỉ ghi ngưỡng thấp hơn tại đây, nên kiểm bằng linter (ví dụ rule `max-lines`). |
| Độ phức tạp | Ngưỡng cyclomatic/cognitive complexity tối đa cho hàm. |
| Trùng lặp code | Ngưỡng trùng lặp cho phép. |

Lệnh chạy ở §5.3; điều kiện chất lượng để qua CI ở [testing-strategy](testing-strategy.md).
<!-- Điền theo từng dự án: ngưỡng -->

## 9. Code Review

### 9.1 Thứ tự ưu tiên khi review
Quy trình chi tiết ở Skill [code-review](../../.ai/skills/code-review/SKILL.md). Thứ tự ưu tiên:

1. Đúng việc: đáp ứng FR/Task và Acceptance Criteria liên kết.
2. Có test chứng minh theo [testing-strategy](testing-strategy.md).
3. Đặt đúng chỗ theo tầng ở [system-architecture](../02-architecture/system-architecture.md) §3.3 và §7 ở trên.
4. Đúng khi chạy đồng thời và chạy lại (race condition, idempotent).
5. Hiệu năng, dữ liệu, cache.
6. Bảo mật theo [security-standards](security-standards.md).
7. Vận hành: log, alert, rollback; xử lý lỗi theo [error-handling](error-handling.md).
8. Clean code và style theo §4–§6, §8.

Logic sai thì không duyệt; code xấu thì comment, không chặn PR. Những gì formatter/linter bắt được thì không comment tay.

### 9.2 Yêu cầu với Pull Request
- Mô tả theo [PR-TEMPLATE](../../.ai/templates/PR-TEMPLATE.md); thiếu mục bắt buộc thì bị trả về trước khi review.
- PR nhỏ, một mục đích; CI phải xanh trước khi review.

| Ngưỡng | Giá trị | Ghi chú |
| --- | --- | --- |
| Kích thước PR tối đa (dòng thay đổi, không tính code sinh tự động, lockfile) |  | Ví dụ: 400; vượt ngưỡng thì tách hoặc ghi lý do |
| Độ dài hàm / method |  | Dấu hiệu cần xem xét, không phải luật |
| Độ dài lớp nhận yêu cầu (controller, handler) |  | Ví dụ: 50 dòng; vượt thường là đang chứa nghiệp vụ |
| Độ dài lớp nghiệp vụ (service, use case) |  | Ví dụ: 200 dòng; vượt thì cân nhắc tách theo nghiệp vụ |
| Số dependency inject vào một lớp |  | Ví dụ: 5–6 |
<!-- Điền theo từng dự án: ngưỡng theo ngôn ngữ -->

### 9.3 Phê duyệt
Số người duyệt và người có quyền duyệt theo mức rủi ro. AI không tự phê duyệt hoặc tự merge.
<!-- Điền theo từng dự án -->

## 10. Git Workflow và Branching Strategy
- Mô hình nhánh (Gitflow), tên nhánh, commit message và các điều cấm: [git-workflow-rules](../../.ai/rules/git-workflow-rules.md).
- Lệnh cắt release, phát hành, hotfix: [gitflow-release](../../.ai/skills/deployment/references/gitflow-release.md).
- Nhịp phát hành và cấu hình bảo vệ nhánh của dự án: [deployment](../05-operations/deployment.md) §6.

## 11. Quy chuẩn theo công nghệ
Chỉ giữ các mục dự án có dùng; quy chuẩn bổ sung này không được trái các mục trên.

### 11.1 Backend
<!-- Điền theo từng dự án -->

### 11.2 Frontend
<!-- Điền theo từng dự án -->

### 11.3 Mobile
<!-- Điền theo từng dự án -->

### 11.4 Database
Quy ước truy vấn, migration trong code. Thiết kế dữ liệu ở [database-design](../02-architecture/database-design.md).
<!-- Điền theo từng dự án -->

## 12. Tham khảo
Tài liệu, style guide chính thức của ngôn ngữ/framework được áp dụng.
<!-- Điền theo từng dự án -->
