# Skill Orchestration Workflow

> Trạng thái: **Draft**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.

Quy trình: **nhận diện loại Task → chọn Skill → xếp thứ tự → qua cổng → bàn giao**. Chi tiết từng việc nằm trong Skill; workflow này chỉ điều phối. Khi khác `task-execution.md` hoặc Rule thì hai bên đó thắng.

## Nguyên tắc

1. Chỉ nạp Skill cần cho Task, chọn theo `skill-selection.md`.
2. Skill không thay Rule, không thay tài liệu nghiệp vụ, không nâng mức tự chủ (A0–A4 do Task cấp).
3. Mỗi Skill có cổng vào và cổng ra (mục Definition of Done trong `SKILL.md`). Chưa qua cổng ra thì không chuyển Skill kế.
4. Qua cổng bằng bằng chứng (output test, diff, tài liệu Approved), không bằng lời khẳng định.
5. Yêu cầu, kiến trúc, quyền, bảo mật chưa được duyệt: ghi thành câu hỏi mở, không triển khai theo phỏng đoán.

## Sáu giai đoạn

1. **Intake:** đọc Task (mục tiêu, phạm vi, AC, R, A); xác định loại Task. Task lai thì tách thành Task con. Thiếu R hoặc A: hỏi, không tự gán.
2. **Nạp ngữ cảnh:** cấu hình dự án → Task/AC → ADR liên quan → FR/BR/contract/kiến trúc → Rules → Skill đã chọn → code, test → Git diff.
3. **Lập chuỗi Skill (plan):** Skill dùng theo thứ tự, Skill chạy song song, đầu vào/đầu ra mỗi Skill, file dự kiến đổi, kế hoạch test, Skill bỏ kèm lý do.
   - Phân tích và thiết kế trước code; test cùng hoặc ngay sau code.
   - `code-review` và `security-review` chạy sau khi có diff và kết quả test.
   - `documentation` chạy khi hành vi đã ổn định; `deployment` đứng cuối và là Task riêng khi chạm production (theo `release-workflow.md`).
   - Skill độc lập chạy song song được (ví dụ `api-development` ∥ `frontend-development` khi contract đã chốt).
4. **Chờ duyệt plan** khi: vượt phạm vi, đổi kiến trúc/contract/quyền/schema/dữ liệu; Task R3; mức tự chủ ≤ A2; chuỗi có hành động cần phê duyệt.
5. **Thực thi từng Skill:** cổng vào → làm theo `SKILL.md` → cổng ra, lưu bằng chứng → ghi đầu ra cho Skill kế.
6. **Bàn giao:** tự rà diff theo DoD của Task (đủ AC có bằng chứng, không ngoài phạm vi, đúng Rule, kết quả test pass/fail/skipped/not-run rõ ràng, tài liệu đã cập nhật, không blocker giấu). Báo cáo theo Delivery Report, thêm: chuỗi Skill thực tế, Skill đã bỏ, giả định, câu hỏi mở, hành động cần người làm (merge, migrate production, deploy). AI không tự chuyển tài liệu sang Approved.

## Vòng lặp khi có lỗi

| Phát hiện | Quay lại |
| --- | --- |
| Test fail do code | `bug-fixing` hoặc Skill đang code, rồi chạy lại test |
| Review nêu lỗi đúng/logic | Skill code tương ứng, rồi chạy lại test và review |
| Review thấy yêu cầu thiếu/mâu thuẫn | **Dừng**; `requirement-review`, chờ người quyết |
| Thiết kế không khả thi | `architecture-design` hoặc `database-design`; đổi kiến trúc cần duyệt |
| Security Critical/High | Skill code tương ứng; chạy lại `security-review` phần bị ảnh hưởng |
| Test fail do môi trường/dữ liệu test | Sửa môi trường; không nới assertion |

Tối đa **3 vòng** sửa–chạy cổng cho một lỗi. Quá giới hạn: dừng, báo điều đã thử và đề xuất hướng tiếp.

## Giới hạn hành động

| Skill | AI được làm | AI không tự làm |
| --- | --- | --- |
| `deployment` | Chuẩn bị, kiểm tra release, soạn release note, runbook | Deploy production, đổi secret, đổi dữ liệu production |
| `database-design` | Thiết kế, viết và chạy thử migration ngoài production | Chạy migration production |
| `architecture-design`, `requirement-*` | Đề xuất (Proposed/Draft) | Chuyển sang Approved |
| `authentication-rbac`, `security-review` | Triển khai và rà soát theo policy đã duyệt | Đổi role/policy, nới kiểm tra để test qua |
| `code-review` | Rà và khuyến nghị | Tự duyệt thay đổi do chính mình viết |
| `bug-fixing`, `refactoring` | Sửa trong phạm vi Task | Đổi business rule; trộn refactor lớn với sửa lỗi |

## Dừng và hỏi

Dừng phần bị ảnh hưởng (vẫn làm tiếp phần độc lập, an toàn) khi: tài liệu mâu thuẫn hoặc thiếu quyết định; cần đổi quyền, bảo mật, dữ liệu production hoặc vượt mức tự chủ; phát hiện secret hoặc lỗ hổng; không xác định được loại Task, môi trường hay lệnh chạy; không tìm ra nguyên nhân gốc của lỗi; vượt giới hạn vòng lặp. Khi dừng, nêu: đã làm gì, bị chặn ở đâu, cần ai quyết định gì.

## Skill kích hoạt Skill khác

| Skill | Kích hoạt thêm | Khi |
| --- | --- | --- |
| backend-development | unit-testing, integration-testing, security-review | Logic mới; chạm DB/tích hợp; chạm quyền hoặc dữ liệu nhạy cảm |
| api-development | authentication-rbac (chạy trước backend-development trong T2), unit-testing, integration-testing | Endpoint cần phân quyền; có validation, logic |
| frontend-development | unit-testing, e2e-testing | Có component, form, hành trình quan trọng |
| database-design | integration-testing, documentation | Đổi schema |
| authentication-rbac | security-review, integration-testing | Luôn, sau khi triển khai guard/policy |
| bug-fixing | unit-testing hoặc integration-testing | Viết regression test |
| refactoring | unit-testing | Baseline trước, kiểm tra sau |
| code-review | security-review | Diff chạm xác thực, phân quyền, dữ liệu nhạy cảm, input ngoài |
| requirement-analysis | requirement-review | Sau khi soạn, trước thiết kế |
| architecture-design | documentation | Ghi ADR, cập nhật kiến trúc |

Kích hoạt chéo phải ghi vào plan và báo cáo, không âm thầm mở rộng phạm vi.

## Cải tiến

Workflow và Skill được thử trên Task thật trước khi chuyển Approved. Sau mỗi Task đầu, ghi: chọn đúng Skill chưa, sót hay thừa bước nào, vòng lặp có hợp lý không. Đề xuất sửa Rule/Skill/workflow theo bước 10 của `task-execution.md`.
