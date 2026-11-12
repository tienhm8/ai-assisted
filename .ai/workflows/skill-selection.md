# Chọn Skill theo loại Task

> Trạng thái: **Approved**. Chuỗi Skill là **mặc định đề xuất**; plan của từng Task có thể bỏ hoặc thêm Skill nhưng phải nêu lý do. Quy trình điều phối: skill-orchestration.md.

## 1. Công việc → Skill chính

Không yêu cầu AI đọc toàn bộ Skill. Chọn theo loại công việc:

| Công việc | Skill chính |
| --- | --- |
| Làm rõ ý tưởng, tầm nhìn, phạm vi | product-discovery |
| Phân tích chức năng mới | requirement-analysis |
| Kiểm tra tài liệu FR/BR | requirement-review |
| Thiết kế hệ thống | architecture-design |
| Thiết kế bảng dữ liệu | database-design |
| Lập plan, chia Task | task-planning |
| Xây dựng API | api-development |
| Xây dựng giao diện | frontend-development |
| Xây dựng business logic | backend-development |
| Đăng nhập, phân quyền | authentication-rbac |
| Kiểm thử hàm | unit-testing |
| Kiểm thử tích hợp | integration-testing |
| Kiểm thử hành trình người dùng | e2e-testing |
| Review Pull Request | code-review |
| Kiểm tra bảo mật | security-review |
| Sửa lỗi | bug-fixing |
| Tối ưu cấu trúc code | refactoring |
| Cập nhật tài liệu | documentation |
| Chuẩn bị phát hành | deployment |
| Phân tích log, sự cố | incident-analysis |
| Tổng hợp KPI, cải tiến rule/skill | continuous-improvement |

## 2. Loại Task → chuỗi Skill

Ký hiệu: `→` tuần tự · `∥` có thể chạy song song · `[ ]` có điều kiện.

| # | Loại Task | Chuỗi Skill mặc định |
| --- | --- | --- |
| T1 | **Tính năng mới** (chưa có FR/AC) | [product-discovery nếu chưa có vision/scope] → requirement-analysis → requirement-review → *(chờ PO/BA duyệt: mọi FR có AC)* → architecture-design ∥ database-design → *(chờ Kiến trúc sư duyệt: thiết kế Approved)* → task-planning → *(Tech Lead duyệt plan)* → T2 |
| T2 | **Cài đặt tính năng** (đã có FR, AC, thiết kế) | [authentication-rbac] → backend-development → api-development ∥ frontend-development → unit-testing → integration-testing → [e2e-testing] → [security-review] → code-review → documentation |
| T3 | **Sửa lỗi** | bug-fixing (gồm regression test) → [integration-testing / e2e-testing] → [security-review nếu liên quan bảo mật] → code-review → [documentation] |
| T4 | **Refactor** | unit-testing (baseline) → refactoring → unit-testing / integration-testing (so sánh) → code-review |
| T5 | **Thay đổi schema dữ liệu** | database-design → integration-testing → code-review → documentation |
| T6 | **Thay đổi yêu cầu** | requirement-analysis → requirement-review → *(duyệt)* → các Task T2/T5 bị ảnh hưởng |
| T7 | **Thay đổi kiến trúc / contract** | architecture-design → *(duyệt, ADR)* → T2/T5 bị ảnh hưởng → documentation |
| T8 | **Rà soát tài liệu yêu cầu** | requirement-review |
| T9 | **Review Pull Request** | code-review → [security-review] |
| T10 | **Kiểm tra bảo mật** | security-review → (finding Critical/High) bug-fixing → security-review (retest) |
| T11 | **Chỉ viết test** | unit-testing / integration-testing / e2e-testing (theo tầng) |
| T12 | **Chỉ cập nhật tài liệu** | documentation |
| T13 | **Phát hành** | security-review (nếu chưa có) → deployment *(chuẩn bị)* → *(phê duyệt phát hành)* → deployment *(thực thi do người có quyền)* → documentation (release record) |
| T14 | **Sự cố production** | incident-analysis *(từ log do người xuất, đã che D3)* → bug-fixing / [security-review] → code-review → documentation → continuous-improvement |
| T15 | **Rà soát định kỳ** (theo mốc roadmap) | continuous-improvement → *(Task riêng cho đề xuất sửa rule/skill, vùng 🔴)* |

Ghi chú:

- **Task lai** tách thành Task con theo loại; không gộp sửa lỗi với refactor lớn.
- **T2:** `backend-development` sở hữu service và logic nghiệp vụ; `api-development` sở hữu contract, validation, handler. Khi API gần như chỉ chuyển tiếp tới service sẵn có, dùng riêng `api-development`.
- **T2 song song:** `api-development` ∥ `frontend-development` chỉ khi API contract đã chốt.
- **T1 → T2** không tự chuyển: cần PO/BA duyệt (mọi FR có AC) và Kiến trúc sư duyệt (thiết kế Approved, có ADR). Chưa có thiết kế Approved thì không code tính năng (P3).

## 3. Điều kiện kích hoạt các Skill có điều kiện

| Skill | Kích hoạt khi |
| --- | --- |
| authentication-rbac | Task có đăng nhập, phiên, vai trò, quyền, hoặc truy cập theo tài nguyên |
| security-review | Task R3; chạm xác thực/phân quyền, dữ liệu nhạy cảm, upload file, input từ ngoài, tích hợp bên thứ ba; trước phát hành |
| e2e-testing | Có hành trình người dùng quan trọng hoặc đổi luồng nhiều màn hình |
| integration-testing | Chạm DB, giao tiếp giữa module, API, hoặc dịch vụ ngoài |
| documentation | Đổi hành vi, API, schema, kiến trúc, cách vận hành |

## 4. Mức rủi ro ảnh hưởng chuỗi

| Mức | Ảnh hưởng |
| --- | --- |
| R1 (thấp) | Có thể bỏ `security-review`, `e2e-testing` nếu không chạm điều kiện kích hoạt; ghi lý do trong plan |
| R2 | Giữ `integration-testing`, `code-review`; cân nhắc `security-review` |
| R3 (cao) | Bắt buộc `security-review`; plan cần duyệt trước khi thực thi; mức tự chủ tối đa |

Mức tự chủ thực tế (A0–A4) vẫn do Task cấp; bảng trên chỉ gợi ý độ sâu kiểm tra.

Ghi chú khi áp dụng cho dự án: hiệu chỉnh chuỗi theo kết quả chạy thử Task thật; bổ sung loại Task nếu phát sinh.
