# Coding Standards

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | security-standards.md, testing-strategy.md |

> **Mục đích.** Convention code: folder structure, naming convention, format, lint, Git workflow, branching strategy. Cụ thể hoá, không hạ Core Rules.

## 1. Ngôn ngữ, framework, phiên bản
<!-- Điền theo từng dự án -->

## 2. Folder Structure
Cây thư mục mã nguồn và quy tắc đặt file vào đâu.
<!-- Điền theo từng dự án -->

## 3. Naming Convention
| Đối tượng | Quy ước | Ví dụ |
| --- | --- | --- |
| File / thư mục |  | |
| Class / hàm / biến | | |
| Bảng / cột DB | | |
| Route API | | |

## 4. Công cụ format · lint · type-check
| Việc | Lệnh |
| --- | --- |
| format |  |
| lint |  |
| type-check |  |

## 5. Git Workflow và Branching Strategy
- Mô hình nhánh, quy ước đặt tên nhánh, quy ước commit:
- Mọi PR liên kết ID Task và FR; quy tắc review và merge theo mức rủi ro.
- Cấu hình bảo vệ nhánh nằm ở [deployment](../05-operations/deployment.md).

### 5.1. AI làm việc với Git

AI **không** làm việc trực tiếp trên nhánh production/main. Mỗi Task làm trên nhánh riêng, đi qua PR và review của người trước khi merge.

```text
main
  |  create branch
  v
feature/TASK-ID
  |  AI implements
  v
Local Tests
  |  commit
  v
Pull Request
  |  CI/CD checks
  v
Human Code Review
  |  approve
  v
Merge
  v
Staging
  |  UAT / Regression
  v
Production
```

Quy tắc:

- Một Task tương ứng một branch hoặc một đơn vị thay đổi độc lập.
- Không cho AI tự merge vào main.
- Không cấp quyền deploy production mặc định.
- Không cho AI truy cập production database nếu không có cơ chế được phê duyệt.
- Mọi thay đổi phải có Git diff và lịch sử commit.

Các bước Staging, UAT/Regression, Production và người quyết phát hành khai báo ở [deployment](../05-operations/deployment.md).
