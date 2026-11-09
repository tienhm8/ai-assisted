# Chọn Skill theo loại Task

> Trạng thái: **Draft**. Chuỗi Skill là **mặc định đề xuất**; plan của từng Task có thể bỏ hoặc thêm Skill nhưng phải nêu lý do. Quy trình điều phối: [skill-orchestration.md](skill-orchestration.md).

## 1. Công việc → Skill chính

Không yêu cầu AI đọc cả 17 Skill. Chọn theo loại công việc:

| Công việc | Skill chính |
| --- | --- |
| Phân tích chức năng mới | [requirement-analysis](../skills/requirement-analysis/SKILL.md) |
| Kiểm tra tài liệu FR/BR | [requirement-review](../skills/requirement-review/SKILL.md) |
| Thiết kế hệ thống | [architecture-design](../skills/architecture-design/SKILL.md) |
| Thiết kế bảng dữ liệu | [database-design](../skills/database-design/SKILL.md) |
| Xây dựng API | [api-development](../skills/api-development/SKILL.md) |
| Xây dựng giao diện | [frontend-development](../skills/frontend-development/SKILL.md) |
| Xây dựng business logic | [backend-development](../skills/backend-development/SKILL.md) |
| Đăng nhập, phân quyền | [authentication-rbac](../skills/authentication-rbac/SKILL.md) |
| Kiểm thử hàm | [unit-testing](../skills/unit-testing/SKILL.md) |
| Kiểm thử tích hợp | [integration-testing](../skills/integration-testing/SKILL.md) |
| Kiểm thử hành trình người dùng | [e2e-testing](../skills/e2e-testing/SKILL.md) |
| Review Pull Request | [code-review](../skills/code-review/SKILL.md) |
| Kiểm tra bảo mật | [security-review](../skills/security-review/SKILL.md) |
| Sửa lỗi | [bug-fixing](../skills/bug-fixing/SKILL.md) |
| Tối ưu cấu trúc code | [refactoring](../skills/refactoring/SKILL.md) |
| Cập nhật tài liệu | [documentation](../skills/documentation/SKILL.md) |
| Triển khai hệ thống | [deployment](../skills/deployment/SKILL.md) |

## 2. Loại Task → chuỗi Skill

Ký hiệu: `→` tuần tự · `∥` có thể chạy song song · `[ ]` có điều kiện.

| # | Loại Task | Chuỗi Skill mặc định |
| --- | --- | --- |
| T1 | **Tính năng mới** (chưa có FR/AC) | requirement-analysis → requirement-review → *(chờ PO/BA duyệt: mọi FR có AC)* → architecture-design ∥ database-design → *(chờ Kiến trúc sư duyệt: thiết kế Approved)* → T2 |
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
