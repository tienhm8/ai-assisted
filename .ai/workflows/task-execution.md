# Task Execution Workflow

> Trạng thái: **Approved**. Quy trình **bắt buộc** cho mọi Task. Sửa file này cần Task riêng và người duyệt.

**Nạp đúng lúc cần.** Mỗi bước chỉ nạp phần ở cột "Nạp". Từ [task-types.md](task-types.md) chỉ đọc dòng của loại Task đang làm:

```sh
awk -v t=T2 '!/^\| T[0-9]+ \|/ || index($0, "| " t " |")==1' .ai/workflows/task-types.md
```

Thay `T2` bằng loại Task. Task chưa ghi loại thì lấy danh sách loại để phân loại; vẫn không rõ thì dừng và hỏi:

```sh
awk -F' \\| ' '/^\| T[0-9]+ \|/{print $1" | "$2}' .ai/workflows/task-types.md
```

## Các bước

| Bước | Việc | Nạp | Đầu ra |
| --- | --- | --- | --- |
| 1 · Tiếp nhận | Đọc Task: mục tiêu, phạm vi, AC, mức rủi ro, mức tự chủ. Xác định loại Task; Task lai tách thành Task con, không gộp sửa lỗi với refactor lớn. Thiếu mức rủi ro, mức tự chủ hoặc độ nghiêm ngặt S: hỏi, không tự gán | Task; `project-rules`; `PROJECT.md` §2, §4; `gates-and-rigor.md` §2 khi cần áp S; dòng loại Task; [load-conditions.md](load-conditions.md) §1 | Loại Task, bộ nạp |
| 2 · Phân tích | Đọc yêu cầu, thiết kế, code liên quan; điểm chưa rõ ghi thành câu hỏi mở | FR/BR/AC, ADR, thiết kế Task chỉ tới; code trong phạm vi | Câu hỏi mở (nếu có) |
| 3 · Lập plan | File dự kiến đổi, quyết định thiết kế, AC → test, chuỗi Skill (bỏ hoặc thêm Skill phải nêu lý do), model và effort cho phiên thực thi | PLAN-TEMPLATE; [model-effort.md](model-effort.md); `load-conditions.md` §2 khi chuỗi có Skill `[ ]`; Rule `testing` và Rule `architecture`, `database`, `security` đã thoả điều kiện | Plan |
| 4 · Duyệt plan | Người duyệt, theo mục "Duyệt plan" | — | Plan Approved |
| 5 · Thực hiện | Làm lần lượt từng Skill: cổng vào → quy trình → kết quả cần kiểm. Ghi đầu ra vào plan rồi mới nạp Skill kế | Plan; `SKILL.md` của Skill đang làm và `references/` nó chỉ tới; Rule `coding`; Rule `git-workflow` khi commit | Diff |
| 6 · Kiểm thử | Chạy đủ cổng kiểm tra của dự án | Skill testing tương ứng; TEST-REPORT-TEMPLATE | Output thật |
| 7 · Tự rà | Rà diff theo AC, phạm vi và Rule đã nạp; soạn báo cáo bàn giao | DELIVERY-REPORT-TEMPLATE | Báo cáo bàn giao |
| 8 · Review | Phiên khác review theo dòng T9; người duyệt PR | Không dùng lịch sử phiên viết code | PR được duyệt |
| 9 · Phát hành | Người merge; AI chỉ chuẩn bị theo [release-workflow.md](release-workflow.md) | — | Bản phát hành |
| 10 · Cập nhật tri thức | Cập nhật tài liệu bị ảnh hưởng. Cần sửa Rule, Skill, workflow thì đề xuất Task riêng | Skill `documentation` | Tài liệu khớp hiện trạng |

Task chỉ phân tích hoặc thiết kế (T1, T6, T7, T8, T15) bỏ bước 5–6: Skill nạp ở bước 2, đầu ra là tài liệu Draft.

## Làn nhanh cho Task R1

Áp dụng khi đủ cả ba: Task R1; không thoả điều kiện nạp Rule `architecture`, `database`, `security`; không chạm vùng 🟡/🔴.

- Plan vài dòng ngay trong phiên (file dự kiến đổi, test sẽ chạy); không tạo file plan, không chờ duyệt.
- Một phiên, chỉ nạp Skill chính.
- Bước 6–8 giữ nguyên; báo cáo bàn giao chỉ điền mục có nội dung.

Phát sinh điều kiện ngoài làn nhanh: dừng, quay về bước 3.

## Duyệt plan

Chờ người duyệt trước bước 5 khi có một trong các điều kiện: Task R3; mức tự chủ ≤ A2; đổi kiến trúc, API contract, quyền, schema hoặc dữ liệu; chạm vùng 🟡; chuỗi có hành động cần phê duyệt. Còn lại làm tiếp, người duyệt kết quả cuối.

## Quy tắc chuyển bước

1. **Plan là ngữ cảnh nén:** đủ để thực thi (yêu cầu, quyết định thiết kế, file dự kiến đổi, AC → test, chuỗi Skill); từ bước 5 làm theo plan, không đọc lại tài liệu plan đã tóm tắt.
2. **Phiên mới cho bước 5** khi Task R2/R3 hoặc chuỗi từ 3 Skill: phiên thực thi chỉ nhận plan và Rule.
3. **Mỗi lúc một Skill:** chưa đạt "kết quả cần kiểm" thì không nạp Skill kế.
4. **Qua cổng bằng bằng chứng** (output test, diff, tài liệu Approved), không bằng lời khẳng định.
5. **Phát sinh điều kiện** (ví dụ sửa lỗi hoá ra chạm phân quyền): nạp Rule, Skill tương ứng, ghi vào plan; nghi ngờ chạm bảo mật hay dữ liệu thì nạp. Làm đổi mức rủi ro, phạm vi, hoặc cần Skill thiết kế: dừng và báo.

## Khi có lỗi

| Phát hiện | Quay lại |
| --- | --- |
| Test fail do code | Skill đang code hoặc `bug-fixing`, chạy lại test |
| Test fail do môi trường, dữ liệu test | Sửa môi trường; không nới assertion |
| Review nêu lỗi logic | Skill code tương ứng, chạy lại test và review |
| Finding bảo mật Critical/High | Skill code tương ứng, chạy lại `security-review` phần bị ảnh hưởng |
| Yêu cầu thiếu hoặc mâu thuẫn | **Dừng**; `requirement-review`, chờ người quyết |
| Thiết kế không khả thi | `architecture-design` hoặc `database-design`; đổi kiến trúc cần duyệt |

## Dừng và hỏi

Dừng phần bị ảnh hưởng, vẫn làm phần độc lập và an toàn, khi:

- tài liệu mâu thuẫn hoặc thiếu quyết định;
- gặp cổng duyệt chưa có người duyệt hoặc bằng chứng (cổng nào, người nào: `gates-and-rigor.md` §1);
- vượt phạm vi Task hoặc mức tự chủ; cần đổi quyền, bảo mật, dữ liệu production;
- phát hiện secret hoặc lỗ hổng;
- không xác định được loại Task, môi trường hay lệnh chạy;
- không tìm ra nguyên nhân gốc, hoặc đã hết 3 vòng sửa cho một lỗi.

Khi dừng, nêu: đã làm gì, bị chặn ở đâu, cần ai quyết gì.
