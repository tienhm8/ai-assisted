# DELIVERY REPORT: PLAN-001 — Tái cấu trúc khung cho dễ hiểu, dễ dùng

> Orchestrator soạn khi bàn giao Plan, theo [DELIVERY-REPORT-TEMPLATE](../../templates/DELIVERY-REPORT-TEMPLATE.md). Người duyệt: người phát triển khung. Nhánh `refactor/AI-framework-refactor`, commit gốc `226ad76`.

## 1. Kết quả

Khung đã được tái cấu trúc theo 5 vấn đề của yêu cầu. Cả 9 Task (FW-1 đến FW-9) được nhận. Mọi tiêu chí hoàn thành ở PLAN §2 đạt khi chạy trên kết quả gộp; mọi tiêu chí nghiệm thu dạng lệnh của 9 Task đạt. Review độc lập (bước 8) chạy 2 lần, kết luận cuối: có điều kiện, không còn lỗi mức Critical hay High. Các điều kiện đã sửa hoặc đã được người phát triển khung quyết (mục 4).

| Task | Kết quả | Tiêu chí còn chờ người |
| --- | --- | --- |
| FW-1 từ vựng thay mã | Đạt | FW-1-AC5: mọi rule giữ nghĩa (review đã trả lời, xem mục 4) |
| FW-2 điểm vào, vùng, worktree | Đạt | không |
| FW-3 `ai-config.yaml`, rút `model-effort` | Đạt | FW-3-AC4: người phát triển khung xem đợt 1 (đã duyệt) |
| FW-4 chuyển tài liệu sang `.ai/guide/` | Đạt | không |
| FW-5 `CHECKLIST.md`, `PROJECT.md` | Đạt | FW-5-AC4: checklist ngắn, đúng ý |
| FW-6 đổi mã thành chữ, file cho AI | Đạt | không |
| FW-7 đổi mã thành chữ, file cho người | Đạt | không |
| FW-8 review trên máy không cần PR | Đạt | FW-8-AC4: tiêu chí review giữ nguyên (review lần 2 đã trả lời) |
| FW-9 mẫu báo cáo có mục mô tả thay đổi | Đạt | không |

## Mô tả thay đổi (đầu vào của review)
Review trên máy đọc mục này thay cho mô tả PR.
- **Vấn đề đang giải quyết, gắn với Task và AC nào:** khung khó hiểu, khó dùng. Áp dụng khung phải mở 16 file, điền 13 file, quyết 24 việc; 775 mã lựa chọn trong 60 file; cấu hình AI nằm ở 6 nơi. Task và AC: FW-1 đến FW-9 và AC của từng Task.
- **Đổi hành vi hay chỉ refactor:** đổi cách viết và chỗ đặt, kèm vài quy tắc mới. Quy tắc mới (không chỉ đổi chữ): mức Task nhiều Skill; thứ tự mức; `auto_runs`; mức chỉ có model cho công cụ không có effort; review không cần PR. Còn lại giữ nghĩa theo review.
- **Phạm vi ảnh hưởng:** chỉ tài liệu, cấu hình khung và mẫu. Không có dữ liệu, schema, API, quyền, code chạy được.
- **Ngoài phạm vi:** điền nội dung Work study (đợt B của pilot); sửa Skill ngoài danh sách trong manifest; merge vào `master`.
- **Kiểm thử thế nào, bằng chứng ở đâu:** mục 3.
- **Thay đổi dữ liệu:** không áp dụng: không có dữ liệu.
- **Thay đổi phá tương thích, cờ tính năng, thứ tự triển khai, cách hoàn tác:** dự án đã áp dụng khung bản cũ không đọc được bản mới vì mã đã bỏ; ghi bảng ánh xạ PLAN §6.1 vào ghi chú phát hành của PR. Không cần cờ tính năng. Hoàn tác: revert nhánh.

## 2. Thay đổi

**Nguồn đã gộp**

| Task | Worktree / nhánh | Lần chạy được nhận | Commit |
| --- | --- | --- | --- |
| FW-1 | `plan-001/FW-1`, `plan-001/FW-1b` | FW-1#1, FW-1#2 | `8b07c11`, `54e10d1` |
| FW-2 | `plan-001/FW-2` | FW-2#2, FW-2#3 (`.claude/settings.json` do người tạo, `6ae1b90`) | `0126cff`, `acd8bff` |
| FW-3 | `plan-001/FW-3` | FW-3#1, #2, #3, #5 | `4e0ff2e`, `ec36514`, `aa9bab2`, `09670e5` |
| FW-4 | `plan-001/FW-4` | FW-4#1, #2 | `bde0c2f`, `c669351` |
| FW-5 | `plan-001/FW-5` | FW-5#1, #2 | `dba33c9`, `5f5e09d` |
| FW-6 | `plan-001/FW-6` | FW-6#1 | `3f6ba93` |
| FW-7 | `plan-001/FW-7` | FW-7#1, #3 | `49abdcb`, `e8b80e4` |
| FW-8 | `plan-001/FW-8` | FW-8#1 | `2813145` |
| FW-9 | `plan-001/FW-9` | FW-9#1 | `14a0602` |
| Sửa tay của người phát triển khung | nhánh chính | không qua Run | `aac519e`, `2b3277d`, `de835d6` |

Dải commit đầy đủ: `git diff 226ad76..HEAD -- . ':!.ai/plans'` (86 file, +951 −1.173). Với sửa tay, `CHECKLIST.md` và `PROJECT.md` trên nhánh chính là bản của người phát triển khung.

**Tóm tắt triển khai:** mã lựa chọn (R, A, S, D, G, T, M·E, số giai đoạn) thay bằng từ; cấu hình AI gom về `ai-config.yaml`; tài liệu khung chuyển sang `.ai/guide/`; thêm `CHECKLIST.md` và điểm vào `CLAUDE.md`; worktree chuyển sang `.claude/worktrees/`; review làm được trên máy khi chưa có PR.

**Thay đổi theo nghiệp vụ**

| # | Nghiệp vụ | File | Loại | Nội dung thay đổi |
| --- | --- | --- | --- | --- |
| 1 | Từ vựng thay mã (FW-1, FW-6, FW-7) | `.ai/rules/project-rules.md`, `.ai/workflows/task-types.md`, `task-execution.md`, 23 file trong `.ai/` ngoài `guide/`, 20 file `docs/`, `.ai/guide/` | Sửa | Mỗi thang định nghĩa bằng từ; rule 23 thành quy tắc dùng từ; loại việc có khoá như `bug-fix`; 775 mã về 0 |
| 2 | Cấu hình AI một chỗ (FW-3) | `ai-config.yaml` | Thêm | `tool`, `auto_runs`, `sessions`, `tasks` với `try`, `high_risk_min`, ngân sách, `stack`, `commands` |
| 3 | Quy tắc chọn mức (FW-3) | `.ai/workflows/model-effort.md` | Sửa | Chỉ còn quy tắc: thứ tự `try`, `high_risk_min`, Skill cùng dòng, thứ tự mức, nâng mức |
| 4 | Bỏ file reference theo công cụ (FW-3) | `.ai/agents/references/*.md` (5 file) | Xoá | Cách chạy Task bằng Claude Code chuyển vào `.ai/guide/ai-tools.md` §3 |
| 5 | Mẫu và Skill theo cấu hình (FW-3) | 3 mẫu, 5 Skill công nghệ, `task-planning`, `documentation` | Sửa | `execution.try` thay start/floor/ceiling/ladder; Skill chọn reference theo `stack` |
| 6 | Điểm vào và vùng (FW-2) | `CLAUDE.md`, `AGENTS.md`, `PROJECT.md`, `.gitignore`, `.claude/settings.json` | Thêm, sửa | `CLAUDE.md` một dòng `@AGENTS.md`; vùng đỏ theo thư mục con; worktree ở `.claude/worktrees/` |
| 7 | Tài liệu khung cho người (FW-4) | 7 file chuyển từ `docs/` sang `.ai/guide/`, `glossary.md`, `README.md` mới | Chuyển, thêm | `git mv` giữ lịch sử; glossary tách khung và dự án; `ai-tools` §3–§4 vào `PROJECT.md` |
| 8 | Checklist áp dụng (FW-5 và sửa tay) | `CHECKLIST.md`, `PROJECT.md` | Thêm | 12 việc, có "Điều kiện hoàn thành"; `PROJECT.md` điền sẵn giá trị khuyến nghị |
| 9 | Review trên máy (FW-8, FW-9) | `.ai/skills/code-review/SKILL.md`, `task-execution.md`, `DELIVERY-REPORT-TEMPLATE.md`, `getting-started.md` | Sửa | Đầu vào là mô tả PR hoặc báo cáo bàn giao kèm dải commit; mẫu báo cáo có mục "Mô tả thay đổi" |
| 10 | Cây "Cấu trúc" trong README (mọi Task) | `README.md` | Sửa | Khớp repo; quy tắc cập nhật cây ghi ở `task-execution`, Skill `documentation`, `task-planning` |

**Điểm reviewer nên xem kỹ:**
- Quy tắc mới trong `model-effort.md` §2 (Skill cùng dòng `tasks`, thứ tự mức).
- Định nghĩa `lean`/`standard`/`strict` và 8 cổng trong `project-rules` (agent viết từ `gates-and-rigor`).
- `ai-tools.md` §3 sau khi bỏ `references/`: đã thêm lại 4 ý về quyền (review lần 1), nhưng bỏ mẫu subagent "Cách A".
- Task phải nâng mức hay chạy lại nhiều lần: FW-2 (3 lần), FW-3 (5 lần, 2 lần dừng vì môi trường), FW-4 (1 lần nâng), FW-7 (3 lần).

## 3. Kiểm thử

Không có code chạy được nên không có test đơn vị. Kiểm bằng `check.py` của Plan và các lệnh trong manifest, chạy trên nhánh chính sau khi gộp:

| Kiểm | Kết quả |
| --- | --- |
| `check.py links` | pass: 0 link hỏng |
| `check.py codes` (lệnh đầy đủ ở PLAN §2) | pass: 0 mã (trước Plan: 775 mã trong 60 file) |
| `check.py config`, `tree`, `types`, `vocab` | pass: 0 lỗi |
| Mọi `acceptance_criteria` dạng lệnh của FW-1 đến FW-9, chạy lại hàng loạt | pass: 0 trượt |
| Quét đường dẫn trong dòng "Tài liệu liên quan" | pass: 0 sai (trước FW-4: 0; sau FW-4 lần 1: 21; lần 2: 0) |

Kiểm đối chứng: `check.py codes` trên file mẫu có mã `R3` và `A2` báo đúng 2 mã, nên kết quả 0 là thật.

**Chưa kiểm tra:**
- Nghĩa của rule trước và sau ở các file ngoài `project-rules`, `model-effort`, `task-execution`: review lần 1 chỉ đọc theo từ khoá các Skill do FW-6 sửa; review lần 2 không rà lại toàn bộ.
- Phát hiện 8 của review lần 1 ("§5" thành "§3") không được review lần 2 kiểm lại vì hết ngân sách; Orchestrator đã chạy `links` và quét chữ, kết quả đạt.
- `.ai/guide/glossary.md` §1 so từng dòng với bản gốc: chỉ so số dòng (75 = 75) và nội dung sau khi bỏ đích link, không đọc ngữ nghĩa từng dòng.
- Bốn file reference đã xoá của Codex, Copilot, Cursor, Gemini: chưa xem có điều đã kiểm chứng nào bị mất.
- Cách dùng thật của `auto_runs: false`: chưa chạy thử trên công cụ không có effort.
- Review lần 3 chưa chạy (ngân sách review đã dùng hết).

## 4. Giả định, quyết định, câu hỏi mở

- **Giả định:**
  - Mọi tên model trong `ai-config.yaml` là tên đã dùng thật trong Plan này (`haiku`, `sonnet`, `opus` của Claude Code 2.1.326).
  - Các giá trị `try`, `high_risk_min`, `budget_usd_per_task: 2` là điểm bắt đầu, không phải giá trị đã đo.
- **Quyết định đã đưa ra (người phát triển khung):**
  - Từ vựng §6.1, `ai-config.yaml` §6.2, ngân sách, độ nghiêm ngặt chuẩn (duyệt Plan).
  - Bỏ `.ai/agents/references/`; `ai-config.yaml` là nguồn duy nhất của model/effort; công cụ không có effort thì bậc kế là model mạnh hơn; khoá `auto_runs` (xem khoá cũ trùng tên `dispatch` của manifest).
  - Task nhiều Skill: cùng một dòng `tasks`; Skill dòng khác thêm giữa chừng thì lấy mức cao hơn từng vị trí và duyệt lại.
  - Review trên máy không cần PR (FW-8, FW-9).
  - Giữ bản sửa tay của `CHECKLIST.md` và `PROJECT.md` (bỏ dòng vùng xanh `.ai/plans/` và dòng `.claude/worktrees/`); FW-2-AC4 và FW-5-AC5 sửa theo.
  - Giữ chữ "sàn" (mức tối thiểu bắt buộc của khung) và tiêu đề "(Thang dùng chung)".
  - Nguồn mức của review: `sessions.review`; dòng `tasks` của `code-review`, `security-review` cùng mức.
- **Câu hỏi mở:** không có `OQ` nào chưa giải quyết.

## 5. Hành động cần người thực hiện

1. Xem `CHECKLIST.md` (FW-5-AC4): ngắn và đúng ý chưa.
2. Duyệt diff cuối: `git diff 226ad76..HEAD -- . ':!.ai/plans'`.
3. Mở PR vào `master`, kèm bảng ánh xạ PLAN §6.1 trong ghi chú phát hành.
4. Quyết thư mục chưa commit `.ai/plans/PLAN-002-budget-policy/` (không phải của Plan này).
5. Nhắc: file `pilot/AI-10-work-study.md` (không commit) có các dòng #30–#36 ghi phát hiện về quy trình trong Plan này.
6. Đo chi phí phiên điều phối bằng `/cost` rồi cộng vào mục 8.

## 6. Quy trình đã dùng

- **Chuỗi Skill:** theo loại việc `architecture-change` (T7). Bước thiết kế đã làm trong Plan (§6), nên mọi Task chỉ chạy Skill `documentation`. Review dùng Skill `code-review`; `security-review` không áp dụng (không chạm xác thực, phân quyền, dữ liệu).
- **Skill bỏ qua:** `security-review` vì diff chỉ là tài liệu; `unit-testing` và các testing Skill vì không có code.
- **Cách chạy:** mỗi Task một worktree ở `.claude/worktrees/<Task>`; mỗi Run một lần `claude -p` ở mức trong manifest; Task độc lập chạy song song (FW-3, FW-5, FW-7 sửa review; FW-6 với FW-7).
- **Tài liệu đã đọc:** `project-rules`, `task-execution`, `model-effort`, `PLAN.md` và manifest từng Task; Skill `code-review` cho review.
- **Điều đã lệch quy trình, có ghi:**
  - FW-4#2 giữ diff của lần 1 thay vì đưa worktree về commit gốc (ngoại lệ có lý do trong `runs.md`).
  - Các sửa tay của người phát triển khung trên nhánh chính được giữ khi xung đột, trước khi merge FW-5 và FW-7.
  - `.claude/settings.json` do người tạo vì Claude Code chặn Run ghi vào `.claude/`.
  - Khi soạn lần review đầu, thay mô tả PR bằng `REVIEW-INPUT.md` do Orchestrator soạn, vì Skill chưa hỗ trợ; FW-8 đã sửa Skill sau đó.

## 7. Hạn chế và rủi ro còn lại

- **Phụ thuộc `check.py`:** các kiểm của Plan nằm ở `.ai/plans/PLAN-001-framework-refactor/check.py`. Bước 6 của `task-execution` giờ không phụ thuộc script này (so cây bằng `git ls-files`), nhưng `tree`, `codes`, `links` chỉ có trong thư mục Plan. Cần một Task riêng để chuyển sang chỗ dùng chung nếu muốn tái dùng.
- **Hai bản của cùng việc:** bản `CHECKLIST.md` sửa tay thay bản FW-5 nên việc "duyệt `ai-config.yaml` qua PR" của review lần 1 không còn trong checklist; dòng duyệt ghi "Trạng thái Approved", trong khi `ai-config.yaml` không có dòng trạng thái.
- **Dự án đã áp dụng bản cũ** không đọc được bản mới (mã đã bỏ, file đã chuyển). Cần bảng ánh xạ ở ghi chú phát hành.
- **Chưa chạy thử với công cụ ngoài Claude Code:** các khối model của Cursor, Gemini, Codex, Copilot đã bị bỏ cùng file reference; `ai-config.yaml` chỉ có giá trị Claude Code. Người đổi công cụ phải tự điền tên model.
- **Skill `code-review` mới:** cổng vào theo báo cáo bàn giao chưa được dùng thử với một báo cáo thật ngoài báo cáo này.

## 8. Số đo

Số lấy từ `runs.md` của Plan và các file JSON của từng Run (`total_cost_usd`, `duration_ms`, `modelUsage`).

| Chỉ số | Giá trị | Nguồn |
| --- | --- | --- |
| Giờ người (soạn Task, trả lời câu hỏi, duyệt, review, sửa tay) | không đo: chưa có công cụ ghi giờ người | — |
| Thời gian AI chạy | 46,0 phút (tổng `duration_ms` của 22 Run) | JSON từng Run |
| Chi phí AI của các Run | 8,47 USD, 277.820 token ra | `runs.md` |
| Chi phí phiên điều phối | không đo: không đọc được từ trong phiên | người chạy `/cost` |
| Số vòng sửa (test fail, review trả về) | Review lần 1 trả về 7 Medium và 3 Low; lần 2 trả về 1 Medium và 2 Low; mỗi lần mở một đợt sửa | `runs.md`, `REVIEW-INPUT.md`, `REVIEW-2-INPUT.md` |
| Số lần người sửa lại bản AI soạn; số lần AI sai phải quay lại | người sửa tay 5 file trên nhánh chính (`aac519e`, `2b3277d`); 1 lần AI viết thiếu dòng `runs.md` (token Run review và 7 Run sửa) phải bổ sung; 1 lần Orchestrator ước token thay vì đọc JSON (FW-9#1) phải sửa | `git log`, hội thoại |

**Chi phí và số lần chạy từng Task** (Run không được nhận ghi riêng):

| Task | Số Run | Chi phí (USD) | Mức cuối | Run không được nhận |
| --- | --- | --- | --- | --- |
| FW-1 | 2 | 0,564 | `sonnet/low` | không |
| FW-2 | 3 | 0,368 | `sonnet/low` | FW-2#1 (dừng: API 503 và `.claude/` bị chặn) |
| FW-3 | 5 | 1,966 | `sonnet/high` | FW-3#4 (dừng: giới hạn tốc độ của gateway) |
| FW-4 | 2 | 0,806 | `sonnet/high` | FW-4#1 (không đạt: 21 đường dẫn sai) |
| FW-5 | 2 | 0,315 | `sonnet/low` | không |
| FW-6 | 1 | 0,294 | `sonnet/low` | không |
| FW-7 | 3 | 0,881 | `sonnet/low` | FW-7#2 (dừng: giới hạn tốc độ của gateway) |
| FW-8 | 1 | 0,201 | `sonnet/low` | không |
| FW-9 | 1 | 0,124 | `sonnet/low` | không |
| Review (bước 8) | 2 | 2,947 | `opus/high` | không |
| **Tổng** | **22** | **8,466** | | 4 Run |

So với ngân sách đã duyệt (Task 11 USD, review 3 USD): Task 5,52 USD; review 2,95 USD, sát trần. Chưa tính phiên điều phối (ngân sách 3 USD).
Số lần nâng mức: 1 (FW-4#2 từ `sonnet/low` lên `sonnet/high`). FW-3 bắt đầu ở `sonnet/high` theo manifest.
