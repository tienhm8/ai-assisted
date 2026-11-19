# DELIVERY REPORT: PLAN-002

> AI (Orchestrator) soạn khi bàn giao Plan, theo [DELIVERY-REPORT-TEMPLATE](../../templates/DELIVERY-REPORT-TEMPLATE.md). Số đo lấy từ [runs.md](runs.md) và JSON của từng Run. Review bước 8 đọc báo cáo này cùng `git diff 135fe14..HEAD`.

## 1. Kết quả

PLAN-002 thêm quy tắc xử lý Task thiếu ngân sách: cảnh báo, đánh giá lại, cấp thêm từ quỹ dự phòng có giữ chỗ, đồng bộ manifest, thu hồi, và sổ ghi mọi điều chỉnh. Cả hai Task được nhận. Mọi tiêu chí dạng lệnh đạt khi Orchestrator chạy lại nguyên văn trên kết quả gộp. Review bước 8 chưa chạy khi soạn báo cáo này.

| Task | Kết quả | Tiêu chí còn chờ người |
| --- | --- | --- |
| BG-1 quy tắc và mẫu cho AI | Đạt | BG-1-AC6: người phát triển khung đối chiếu quy tắc 9 đến 13 với PLAN §6.1 và thử hai ví dụ số ở PLAN §7 |
| BG-2 hướng dẫn cho người | Đạt | BG-2-AC5: hướng dẫn khớp quy tắc 9 đến 13, không thêm quy tắc mới |

## Mô tả thay đổi (đầu vào của review)

- **Vấn đề đang giải quyết:** Task thiếu ngân sách so với thực tế chạy thì khung chỉ có "dừng, hỏi người" (`model-effort` quy tắc 6 và 7 cũ). PLAN-002 (yêu cầu độc lập của người phát triển khung, 2026-11-19) thêm cách xử lý có kiểm soát. BG-1 nhận quy tắc và mẫu cho AI; BG-2 nhận hướng dẫn cho người.
- **Đổi hành vi hay chỉ refactor:** đổi hành vi của khung. Quy tắc mới: cảnh báo ở 80% ngân sách hiện hành; Orchestrator tự cấp thêm từ quỹ dự phòng khi đủ bốn điều kiện (Task không phải rủi ro cao, số thiếu không vượt số dư quỹ, tổng cấp thêm của Task không vượt 50% ngân sách ban đầu, ghi được giữ chỗ vào sổ); giữ chỗ tuần tự; sửa `budget.max_cost_usd` trong manifest, không sửa `initial_cost_usd`; thu hồi phần dư khi Task xong; ngân sách tối đa của Plan không tự tăng.
- **Phạm vi ảnh hưởng:**
  - Cấu hình: thêm ba khoá vào `ai-config.yaml`; thêm khoá `initial_cost_usd` vào mẫu manifest (manifest đã có không bị sửa).
  - Quy tắc và workflow: `model-effort` quy tắc 5, 6, 7 sửa và thêm quy tắc 9 đến 13; `task-execution` ở "Plan approval", ngoại lệ, "Re-approval", danh sách dừng, bước 5 và bước 7.
  - Mẫu: Plan (ngân sách tối đa, quỹ dự phòng), `runs.md` (bảng "Điều chỉnh ngân sách", dòng Phiên điều phối), manifest, Skill `task-planning`.
  - Hướng dẫn: `getting-started`, `glossary`, `ai-tools`.
  - Không đụng: API, dữ liệu, quyền truy cập, `project-rules`, thứ tự thử model/effort, số lượt chạy lại, tiêu chí Đạt/Không đạt.
- **Ngoài phạm vi:** không sửa `project-rules` (PLAN §6.3); không tự động hoá việc cộng chi phí; không sửa PLAN-001 và `check.py`; chưa có script đọc transcript. PLAN-002 chưa có quỹ dự phòng, nên các quy tắc mới chưa có hiệu lực với chính nó.
- **Kiểm thử thế nào, bằng chứng ở đâu:** mục 3 và `runs.md`.
- **Thay đổi dữ liệu:** không áp dụng: không có dữ liệu hay schema.
- **Thay đổi phá tương thích:** không áp dụng cờ tính năng. Manifest cũ không có `initial_cost_usd`: quy tắc 6 coi `max_cost_usd` là ngân sách ban đầu, nên Plan cũ vẫn dùng được; Plan mới ghi cả hai khoá. Hoàn tác: `git revert` hai commit gộp `61c584b` và `a6bca49` (và `3bf126e`).

## 2. Thay đổi

**Nguồn đã gộp**

| Task | Worktree / nhánh | Lần chạy được nhận | Commit |
| --- | --- | --- | --- |
| BG-1 | `.claude/worktrees/BG-1`, `plan-002/BG-1` | BG-1#1 | `77001f5`, gộp nhánh chính vào nhánh Task `ff35f44`, gộp vào nhánh chính `61c584b` |
| BG-2 | `.claude/worktrees/BG-2`, `plan-002/BG-2` | BG-2#1 | `080f88e`, gộp `a6bca49` |
| BG-2 (sửa) | `.claude/worktrees/BG-2b`, `plan-002/BG-2b` | BG-2#2 | `60ec1c9`, gộp `3bf126e` |

Ba worktree còn tồn tại ở `.claude/worktrees/` (BG-1, BG-2, BG-2b); không nằm trong diff.

**Tóm tắt triển khai:** khung có quy tắc ngân sách đầy đủ: cảnh báo, đánh giá lại, cấp thêm, giữ chỗ, đồng bộ manifest, thu hồi và sổ. Mọi giá trị mặc định nằm trong `ai-config.yaml`.

**Thay đổi theo nghiệp vụ**

| # | Nghiệp vụ | File:dòng | Loại | Nội dung thay đổi | Đề xuất tốt hơn |
| --- | --- | --- | --- | --- | --- |
| 1 | Giá trị ngân sách | `ai-config.yaml:30-32` | Thêm | `budget_warn_pct: 80`, `budget_topup_max_pct: 50`, `budget_pool_pct: 20` | |
| 2 | Quy tắc cấp thêm | `.ai/workflows/model-effort.md:7, 62-70` | Sửa, Thêm | Quy tắc 5, 6, 7 sửa; quy tắc 9 đến 13 mới | |
| 3 | Duyệt và dừng | `.ai/workflows/task-execution.md:65, 67, 88, 90, 92, 124` | Sửa | Bước 5 và 7 trỏ quy tắc 9 đến 13, thêm quy trình transcript và USD; "Plan approval", ngoại lệ, "Re-approval", danh sách dừng | Ô bước 7 rất dài; có thể tách thành đoạn riêng (agent cũng nêu) |
| 4 | Khai báo ở Plan | `.ai/templates/PLAN-TEMPLATE.md:15-16, 56` | Sửa, Thêm | Ngân sách tối đa kèm công thức; dòng Quỹ dự phòng; dòng Kết quả về cấp thêm | |
| 5 | Sổ điều chỉnh | `.ai/templates/RUNS-TEMPLATE.md:12-13, 17-` | Sửa, Thêm | Dòng Phiên điều phối; bảng "Điều chỉnh ngân sách" | |
| 6 | Manifest | `.ai/templates/TASK-MANIFEST-TEMPLATE.yaml:56-57` | Sửa, Thêm | `initial_cost_usd`; chú thích `max_cost_usd` | |
| 7 | Lập Plan | `.ai/skills/task-planning/SKILL.md:23, 25, 36` | Sửa, Thêm | Ghi cả hai khoá; khai báo công thức và quỹ | |
| 8 | Hướng dẫn người | `.ai/guide/getting-started.md:260-263` | Sửa, Thêm | Bốn dòng trong bảng "Khi AI… / Bạn làm" | |
| 9 | Thuật ngữ | `.ai/guide/glossary.md:70-74` | Thêm | Năm thuật ngữ ngân sách | |
| 10 | Công cụ | `.ai/guide/ai-tools.md:53` | Thêm | Ngân sách còn lại bằng ngân sách hiện hành trừ chi phí đã dùng | |

**Điểm reviewer nên xem kỹ:**
- **`model-effort` quy tắc 10 và 11:** công thức số thiếu và giữ chỗ tuần tự. Thử hai ví dụ số ở PLAN §7: ngân sách hiện hành 2, đã dùng 1,7, `DuKienTong` 2,6 hoặc `DuKienThem` 0,9 đều cho thiếu 0,6; hai Task cùng thiếu 0,8 khi quỹ còn 0,8 thì chỉ một Task được cấp.
- **Quy tắc 6 với manifest cũ:** manifest không có `initial_cost_usd`. Quy tắc 10 tính hạn mức trên `initial_cost_usd`; chưa viết rõ trường hợp này (xem mục 7).
- **Mâu thuẫn tiềm ẩn:** `project-rules` 8 và 20 nói AI không tự nâng quyền; PLAN §6.3 lập luận cấp thêm trong Plan đã duyệt không vi phạm. Cần người duyệt đồng ý lập luận này.
- **Hai Run nâng mức của BG-2:** lỗi do chọn `sonnet/low` rồi tìm ra hai chỗ sai nội dung.

## 3. Kiểm thử

Orchestrator chạy lại nguyên văn trên kết quả gộp, đều đạt:

| Kiểm tra | Lệnh | Kết quả |
| --- | --- | --- |
| BG-1-AC1 | đọc `ai-config.yaml` bằng YAML, so 80/50/20 và `budget_usd_per_task` bằng 2 | đạt |
| BG-1-AC2, AC3 | chuỗi `grep` trong `model-effort`, `task-execution`, ba mẫu, Skill | đạt |
| BG-1-AC4 và BG-2-AC3 | `check.py` `links`, `config`, `vocab`, `types`, `tree`, `codes` | 0 lỗi mỗi lệnh |
| BG-1-AC5, BG-2-AC4 | `git diff --name-only <base>` | mọi file nằm trong `allowed_paths` |
| BG-2-AC1, AC2 | `grep` glossary và getting-started | đạt |
| So bước 5 và 7 của `task-execution` với bản gốc | so từng ký tự | chỉ chèn thêm, không mất chữ |

`check.py codes` báo 0, đã thử trên một file mẫu có 2 mã cũ thì báo đúng 2 mã, nên 0 là kết quả quét thật.

**Chưa kiểm tra:**
- BG-1-AC6 và BG-2-AC5 (kiểm bằng người): chờ người phát triển khung.
- Hai ví dụ số ở PLAN §7: agent BG-1 và BG-2 chưa đọc §7; chưa có ai tính thử bằng tay.
- Quy tắc mới chưa chạy với Plan thật: chưa có Plan nào có quỹ dự phòng để thử cấp thêm, giữ chỗ, thu hồi.
- Hai khoá USD: `/cost` và Account & Usage là thông tin người phát triển khung nêu, chưa kiểm.

## 4. Giả định, quyết định, câu hỏi mở

- **Giả định:** ba giá trị 80, 50, 20 là điểm bắt đầu, chưa đo; người phát triển khung xác nhận 2026-11-19 và nói sẽ đo ở Plan kế tiếp.
- **Quyết định đã đưa ra (người phát triển khung):** ngân sách tối đa là trần của cả Plan (phương án A); Orchestrator tự cấp thêm trong hạn mức, rủi ro cao hỏi người (phương án C); Orchestrator tự đánh giá lại từ `runs.md`; rủi ro vừa; hai tên ước tính `DuKienTong`, `DuKienThem`; người đọc USD từ `/cost` hoặc Account & Usage cùng với transcript; gộp BG-1, chạy BG-2, sửa glossary rồi chạy review.
- **Quyết định tôi tự đưa ra:** xử lý xung đột một dòng bước 7 của `task-execution` bằng cách giữ cả quy tắc `Done` và quy tắc ngân sách; BG-2#2 giữ diff BG-2#1, không đưa về commit gốc.
- **Câu hỏi mở:** không có `OQ` nào chưa giải quyết.

## 5. Hành động cần người thực hiện

1. Làm BG-1-AC6 và BG-2-AC5.
2. Đưa transcript của phiên điều phối và số USD từ `/cost` hoặc Account & Usage, để ghi dòng `PLAN-002-ĐIỀU-PHỐI#1` (hiện "chưa đo").
3. Duyệt diff cuối: `git diff 135fe14..HEAD -- . ':!.ai/plans'`.
4. Mở PR (nhánh `refactor/AI-framework-refactor` vào `master`) hoặc quyết cách gộp.
5. Quyết về ba worktree còn lại ở `.claude/worktrees/` (BG-1, BG-2, BG-2b), xoá hay giữ.

## 6. Quy trình đã dùng

- Chuỗi Skill: `documentation` cho cả hai Task. Không dùng `architecture-design` vì thiết kế đã nằm ở PLAN §6.
- Tài liệu đã đọc: PLAN-002 §6; `model-effort.md`, `task-execution.md`, `ai-tools.md`, `getting-started.md`, `glossary.md`, ba mẫu, Skill `task-planning`; `runs.md` và báo cáo bàn giao của PLAN-001.
- Cách chạy: `claude -p --model --effort --max-budget-usd --output-format json`, worktree riêng, nhánh `plan-002/<Task>`.

## 7. Hạn chế và rủi ro còn lại

- **Manifest cũ không có `initial_cost_usd`:** chưa có quy tắc viết rõ cho trường hợp này. Plan mới không bị ảnh hưởng.
- **Cảnh báo giữa các Run, không giữa một Run:** một Run có thể đi từ dưới 80% thẳng đến trần (PLAN §6.4).
- **Quy tắc phụ thuộc người nhớ đưa transcript và USD** sau mỗi Task; chưa có công cụ tự động.
- **PLAN-002 chưa chạy dưới quy tắc mới:** quỹ dự phòng bằng 0, nên cấp thêm, giữ chỗ, thu hồi chưa được thử thật.
- **Ô bước 7 của `task-execution` rất dài** (nhận xét của agent BG-1).
- **Thư mục `.ai/plans/PLAN-001-framework-refactor/check.py`** vẫn là nơi duy nhất có các lệnh kiểm; PLAN-002 phụ thuộc nó như PLAN-001.
- **Ba worktree còn trên đĩa.**

## 8. Số đo

Số lấy từ `runs.md` và JSON của từng Run (`total_cost_usd`, `duration_ms`, `modelUsage`).

| Chỉ số | Giá trị | Nguồn |
| --- | --- | --- |
| Giờ người | không đo: chưa có công cụ ghi giờ người | — |
| Thời gian AI chạy | 159,9 giây (BG-1#1 79,0; BG-2#1 43,5; BG-2#2 37,3; tổng `duration_ms` trong JSON) | JSON từng Run |
| Chi phí AI của các Run | 0,701 USD (0,305 + 0,204 + 0,192), 25.975 token ra | `runs.md` |
| Chi phí phiên điều phối | không đo: chờ transcript và số USD từ người | người chạy `/cost` |
| Số vòng sửa | 1: BG-2#2 sửa hai phát hiện sau BG-2#1; chưa có review nên chưa tính vòng review | `runs.md` |
| Số lần người sửa lại bản AI soạn; số lần AI sai phải quay lại | 2 lần AI viết thiếu hoặc sai nội dung phải quay lại ở BG-2 (định nghĩa thiếu hai phần; phần thêm nằm sai ô) | `runs.md` |

**Chi phí và số lần chạy từng Task:**

| Task | Số Run | Chi phí (USD) | Mức cuối | Run không được nhận |
| --- | --- | --- | --- | --- |
| BG-1 | 1 | 0,305 | `sonnet/high` | không |
| BG-2 | 2 | 0,396 | `sonnet/high` | không (BG-2#1 được nhận, BG-2#2 sửa chồng lên) |
| Review (bước 8) | 0 | 0 | chưa chạy | — |
| **Tổng** | **3** | **0,701** | | không |

So với ngân sách đã duyệt (Task 4 USD, Review 2 USD, phiên điều phối 1,5 USD, tổng 7,5 USD): Task 0,701 USD; Review và phiên điều phối chưa tính. Số lần nâng mức: 1 (BG-2#2 từ `sonnet/low` lên `sonnet/high`).
