# Loại Task: nạp Rule nào, dùng Skill nào

> Trạng thái: **Approved**. Sửa file này cần Task riêng và người duyệt.

## 1. Bảng định tuyến

AI chỉ đọc dòng của loại Task đang làm (lệnh lọc ở [task-execution.md](task-execution.md)). `project-rules` luôn nạp nên không ghi. Tên Rule viết gọn: `git` là `git-workflow-rules`, còn lại là `<tên>-rules`. `cache`, `document-database` nạp theo điều kiện với mọi loại Task.

Ký hiệu chuỗi Skill: `→` tuần tự · `∥` song song được · `[ ]` có điều kiện (load-conditions §2) · `⏸` chờ người duyệt.

| # | Loại Task | Rule luôn nạp | Rule theo điều kiện (load-conditions §1) | Chuỗi Skill | Template | Model · Effort (plan / thực thi) |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Tính năng mới (chưa có FR, AC) | architecture | database, security, git | [product-discovery] → requirement-analysis → requirement-review → ⏸ PO/BA → architecture-design ∥ database-design → [caching] → ⏸ Kiến trúc sư → task-planning → ⏸ Tech Lead → các Task T2 | PLAN, ADR | M3·E3 / — |
| T2 | Cài đặt tính năng (đã có FR, AC, thiết kế) | git, coding, architecture, testing | database, security | [authentication-rbac] → backend-development → [caching] → api-development ∥ frontend-development → unit-testing → [integration-testing] → [e2e-testing] → [security-review] → code-review → [documentation] | PLAN, TEST-REPORT, DELIVERY-REPORT | M3·E3 / M2·E2 |
| T3 | Sửa lỗi | git, coding, testing | architecture, database, security | bug-fixing → [caching] → [integration-testing / e2e-testing] → [security-review] → code-review → [documentation] | BUG (đầu vào), DELIVERY-REPORT | M2·E3 / M2·E3 |
| T4 | Refactor | git, coding, architecture, testing | database | unit-testing (baseline) → refactoring → unit-testing / integration-testing (so sánh) → code-review | PLAN, DELIVERY-REPORT | M2·E3 / M2·E2 |
| T5 | Thay đổi schema | git, database, architecture, testing | security, coding | database-design → [caching] → integration-testing → code-review → documentation | PLAN, DELIVERY-REPORT | M3·E3 / M2·E3 |
| T6 | Thay đổi yêu cầu | — | architecture, git | requirement-analysis → requirement-review → ⏸ PO/BA → các Task T2/T5 bị ảnh hưởng | — | M2·E3 / — |
| T7 | Thay đổi kiến trúc hoặc contract | architecture | database, security, git | architecture-design → ⏸ Kiến trúc sư (ADR) → các Task T2/T5 bị ảnh hưởng → documentation | ADR, PLAN | M3·E4 / — |
| T8 | Rà soát tài liệu yêu cầu | — | — | requirement-review | — | M2·E2 / — |
| T9 | Review Pull Request | coding, architecture, testing | database, security, git | code-review → [security-review] | PR (đầu vào), DELIVERY-REPORT | M3·E3 / — |
| T10 | Kiểm tra bảo mật | security, coding | database, architecture | security-review → bug-fixing (finding Critical/High) → security-review (kiểm lại) | DELIVERY-REPORT | M3·E3 / M2·E3 |
| T11 | Chỉ viết test | git, coding, testing | database, security | unit-testing / integration-testing / e2e-testing (theo tầng) | TEST-REPORT, DELIVERY-REPORT | M2·E2 / M2·E2 |
| T12 | Chỉ cập nhật tài liệu | git | architecture | documentation | DELIVERY-REPORT | M2·E2 / M2·E1 |
| T13 | Phát hành | git, security, testing | database | [security-review nếu chưa có] → deployment (chuẩn bị) → ⏸ Owner → người thực thi → documentation | TEST-REPORT, RELEASE-REPORT | M2·E2 / M2·E2 |
| T14 | Sự cố production | security | database, architecture | incident-analysis → Task T3 riêng để sửa → continuous-improvement | BUG | M3·E3 / theo T3 |
| T15 | Rà soát định kỳ | — | — | continuous-improvement → Task riêng cho từng đề xuất sửa Rule, Skill | — | M2·E2 / — |

Chuỗi Skill là mặc định; plan được bỏ hoặc thêm Skill, phải nêu lý do.

- **Thứ tự:** phân tích và thiết kế trước code; test cùng hoặc ngay sau code; `code-review`, `security-review` sau khi có diff và kết quả test; `documentation` khi hành vi đã ổn định.
- **T1 → T2 không tự chuyển:** cần PO/BA duyệt (mọi FR có AC) và Kiến trúc sư duyệt (thiết kế Approved).
- **T2:** `backend-development` làm service, logic nghiệp vụ; `api-development` làm contract, validation, handler. API chỉ chuyển tiếp tới service sẵn có thì chỉ dùng `api-development`. `api-development` ∥ `frontend-development` chỉ khi API contract đã Approved.
- **`code-review`** không bị bỏ khi Task có diff.
