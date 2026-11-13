# Loại Task: nạp Rule nào, dùng Skill nào

> Trạng thái: **Approved**. Sửa file này cần Task riêng và người duyệt.

Nguồn duy nhất cho câu hỏi: một loại Task nạp Rule nào, đi qua Skill nào, dùng template nào, chạy bằng hạng model và effort nào. Nạp ở bước nào xem [task-execution.md](task-execution.md).

## 1. Bảng định tuyến

`project-rules` luôn nạp cho mọi Task nên không ghi trong bảng. Tên Rule viết gọn: `git` là `git-workflow-rules`, các tên khác là `<tên>-rules`. `cache` và `document-database` nạp theo điều kiện ở mục 2 với mọi loại Task.

Ký hiệu chuỗi Skill: `→` tuần tự · `∥` song song được · `[ ]` có điều kiện (mục 3) · `⏸` chờ người duyệt.

| # | Loại Task | Rule luôn nạp | Rule theo điều kiện (mục 2) | Chuỗi Skill | Template | Model · Effort (plan / thực thi) |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Tính năng mới (chưa có FR, AC) | architecture | database, security, git | [product-discovery] → requirement-analysis → requirement-review → ⏸ PO/BA → architecture-design ∥ database-design → ⏸ Kiến trúc sư → task-planning → ⏸ Tech Lead → các Task T2 | PLAN, ADR | M3·E3 / — |
| T2 | Cài đặt tính năng (đã có FR, AC, thiết kế) | git, coding, architecture, testing | database, security | [authentication-rbac] → backend-development → api-development ∥ frontend-development → unit-testing → [integration-testing] → [e2e-testing] → [security-review] → code-review → [documentation] | PLAN, TEST-REPORT, DELIVERY-REPORT | M3·E3 / M2·E2 |
| T3 | Sửa lỗi | git, coding, testing | architecture, database, security | bug-fixing → [integration-testing / e2e-testing] → [security-review] → code-review → [documentation] | BUG (đầu vào), DELIVERY-REPORT | M2·E3 / M2·E3 |
| T4 | Refactor | git, coding, architecture, testing | database | unit-testing (baseline) → refactoring → unit-testing / integration-testing (so sánh) → code-review | PLAN, DELIVERY-REPORT | M2·E3 / M2·E2 |
| T5 | Thay đổi schema | git, database, architecture, testing | security, coding | database-design → integration-testing → code-review → documentation | PLAN, DELIVERY-REPORT | M3·E3 / M2·E3 |
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

Chuỗi Skill là mặc định; plan được bỏ hoặc thêm Skill nhưng phải nêu lý do. Ghi chú:

- **Task lai** tách thành Task con theo loại; không gộp sửa lỗi với refactor lớn.
- **Thứ tự:** phân tích và thiết kế trước code; test cùng hoặc ngay sau code; `code-review` và `security-review` sau khi có diff và kết quả test; `documentation` khi hành vi đã ổn định.
- **T1 → T2 không tự chuyển:** cần PO/BA duyệt (mọi FR có AC) và Kiến trúc sư duyệt (thiết kế Approved).
- **T2:** `backend-development` làm service và logic nghiệp vụ; `api-development` làm contract, validation, handler. API chỉ chuyển tiếp tới service sẵn có thì dùng riêng `api-development`. `api-development` ∥ `frontend-development` chỉ khi API contract đã Approved.
- **`code-review`** chạy ở phiên khác phiên viết code và không bị bỏ khi Task có diff.

## 2. Điều kiện nạp Rule

| Rule | Nạp khi |
| --- | --- |
| git | Task có commit hoặc PR |
| coding | Có sửa code, kể cả code test |
| testing | Có sửa code, viết hoặc chạy test, hoặc phải báo kết quả kiểm tra |
| architecture | Thiết kế; chạm ranh giới module, tầng, API contract; thêm module hoặc dependency; ảnh hưởng NFR |
| database | Chạm schema, migration, query, transaction, seed hoặc dữ liệu test trong CSDL, xoá dữ liệu |
| cache | Thêm, sửa hoặc đọc cache; đổi dữ liệu đang được cache |
| document-database | Rule `database` đã thoả và hệ quản trị là CSDL tài liệu (MongoDB, NoSQL) |
| security | Task R3; chạm xác thực, phiên, phân quyền; dữ liệu D2/D3; input từ ngoài, upload; tích hợp bên thứ ba; thêm hoặc đổi dependency; secret, cấu hình bảo mật; phát hành |

Rule đã thoả điều kiện thì không bỏ, kể cả với Task R1. Mức rủi ro chỉ đổi độ sâu kiểm tra, không đổi bộ Rule.

## 3. Điều kiện dùng Skill có điều kiện

| Skill | Dùng khi |
| --- | --- |
| product-discovery | Chưa có vision, scope |
| authentication-rbac | Task có đăng nhập, phiên, vai trò, quyền hoặc truy cập theo tài nguyên. Làm xong luôn kèm `security-review` và `integration-testing` |
| integration-testing | Chạm CSDL, giao tiếp giữa module, API hoặc dịch vụ ngoài |
| e2e-testing | Có hành trình người dùng quan trọng hoặc đổi luồng nhiều màn hình |
| security-review | Thoả điều kiện nạp Rule `security` ở mục 2. Bắt buộc với Task R3 |
| documentation | Đổi hành vi, API, schema, kiến trúc hoặc cách vận hành |
| architecture-design (soạn ADR) | Thiết kế dữ liệu cần partition, sharding, tách CSDL, đổi hệ quản trị hoặc chọn mẫu đa tenant |


## 4. Model và effort

Tra cột cuối của dòng loại Task ở §1; hạng, mức và ánh xạ sang công cụ thật ở [model-effort.md](model-effort.md).
