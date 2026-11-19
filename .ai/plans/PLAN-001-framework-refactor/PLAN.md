# PLAN: PLAN-001 — Tái cấu trúc khung cho dễ hiểu, dễ dùng

> AI (Orchestrator) soạn; người phát triển khung (vai Tech Lead của khung) duyệt trước khi chạy Task. Duyệt Plan là duyệt từ vựng ở §6.1, định dạng `ai-config.yaml` ở §6.2, mức rủi ro, mức tự chủ, thứ tự thử model/effort, ngân sách, phạm vi của mọi Task.
> Plan này viết lựa chọn bằng chữ trước, mã cũ trong ngoặc, để người duyệt so được với khung hiện hành (`project-rules` 23).

| Mục | Giá trị |
| --- | --- |
| ID | `PLAN-001` |
| Nguồn (Source) | Yêu cầu độc lập của người phát triển khung, 2026-11-18 và 2026-11-19: rà soát và tái cấu trúc khung (5 vấn đề: nhiều file phân mảnh và ký hiệu khó hiểu; tổ chức lại file cấu hình; thư mục `.ai`; checklist áp dụng; file đặt sai thư mục con của `docs/`) |
| Goals (tuỳ chọn) | Không có (repo khung chưa có `goals.md` thật) |
| Trạng thái | Approved |
| Người duyệt · Ngày duyệt | Người phát triển khung (vai Tech Lead của khung) · 2026-11-19: duyệt từ vựng §6.1, `ai-config.yaml` §6.2, ngân sách, độ nghiêm ngặt chuẩn |
| Ngày tạo | 2026-11-19 |
| Branch · commit gốc | `refactor/AI-framework-refactor` · `a2181d9` |
| Model · Effort của Orchestrator | opus/high (M3·E3: model mạnh, effort cao) |
| Độ nghiêm ngặt | chuẩn (S2), người phát triển khung xác nhận 2026-11-19 |
| Ngân sách cả Plan | 15 USD (7 Task 9 · Review 3 · phiên điều phối 3), ước tính theo số Claude Code tự báo, không phải tiền thực trả qua proxy. Phiên điều phối mở mới, chỉ đọc PLAN và manifest. Chạm trần thì dừng, hỏi người |

## 1. Mục tiêu và phạm vi

**Đầu ra:** khung sau khi tái cấu trúc, gồm:
- `CHECKLIST.md`: một danh sách chung cho mọi dự án.
- `ai-config.yaml`: ghi thẳng model/effort theo loại việc, stack, lệnh kiểm tra, ngân sách.
- `PROJECT.md` điền sẵn giá trị khuyến nghị.
- `CLAUDE.md` một dòng.
- Tài liệu khung chuyển từ `docs/` sang `.ai/guide/`.
- Vùng đỏ khai theo thư mục con của `.ai/`.
- Mọi lựa chọn viết bằng chữ, trong cả file cho AI và file cho người.

**Làm:**
- 7 Task FW-1 đến FW-7 ở §5.
- Kiểm tra trên kết quả gộp.
- Review độc lập.
- Cập nhật nhật ký pilot.

**Không làm:**
- Điền nội dung Work study (đợt B của pilot).
- Dịch các file `.ai/agents/references/*.md` sang tiếng Anh. Mâu thuẫn với `project-rules` 22 được ghi ở §8 để làm Plan sau.
- Sửa Skill ngoài các mục nêu trong manifest.
- Merge vào `master` (người phát triển khung làm).

**Vì sao một Plan:** cùng một đầu ra, cùng chu kỳ duyệt, kết thúc ở một PR. Các Task phụ thuộc nhau theo chuỗi vì sửa chung nhiều file.

## 2. Tiêu chí hoàn thành

Chạy trên kết quả gộp, ở thư mục gốc repo:
- `python3 -I .ai/plans/PLAN-001-framework-refactor/check.py links` trả 0 link gãy. Mốc trước Plan: 0.
- `python3 -I .ai/plans/PLAN-001-framework-refactor/check.py codes .ai/rules .ai/skills .ai/workflows .ai/templates .ai/agents .ai/guide .ai/README.md docs README.md PROJECT.md CHECKLIST.md AGENTS.md CLAUDE.md ai-config.yaml` trả 0 mã lựa chọn. Mốc trước Plan: 683 mã trong 56 file.
- `ai-config.yaml` đọc được bằng YAML, mỗi Skill trong `.ai/skills/` có đúng một dòng mức.
- Lệnh lọc dòng loại việc trong `task-execution.md` trả đúng một dòng cho mỗi loại việc.
- Mọi AC của 7 Task đạt. Review ở bước 8 không còn phát hiện mức Critical hoặc High.
- Người phát triển khung duyệt diff cuối.

## 3. Yêu cầu và ngữ cảnh đã nạp

**Quyết định của người phát triển khung:**

| Ngày | Quyết định |
| --- | --- |
| 2026-11-19 | Tên file là `CHECKLIST.md`. Một danh sách chung, không chia cột dự án mới / dự án đang chạy. Cột cuối là "Điều kiện hoàn thành", viết ngắn, đúng ý |
| 2026-11-19 | `ai-config.yaml` ghi thẳng model/effort cho từng loại việc, không qua hạng trung gian |
| 2026-11-19 | Giữ `.ai/plans/` trong `.ai/`. Vùng đỏ khai theo thư mục con, trừ `plans/` |
| 2026-11-19 | Bỏ `.ai/worktrees/`. Worktree tạo trong `.claude/worktrees/`, chỗ mặc định của Claude Code; công cụ khác cũng dùng chỗ này |
| 2026-11-19 | Đổi mã thành chữ ở cả file cho AI và file cho người |
| 2026-11-19 | Làm xong trước khi pilot bắt đầu code |

**Bằng chứng từ rà soát** (chi tiết ở nhật ký pilot #18 đến #28; nhật ký không commit):
- Áp dụng khung phải mở 16 file, điền 13 file, quyết 24 việc.
- 683 mã lựa chọn trong 56 file.
- Cấu hình AI nằm ở 6 nơi. "Ngân sách mặc định của dự án" được nhắc ở `task-execution.md:90` nhưng chưa có chỗ khai báo.
- Ở mọi dòng của `model-effort.md` §2, `floor` bằng `start`.
- `glossary.md` §1 có 16 KB thuật ngữ khung, nạp vào 4 Skill.

**Đã thử trên Claude Code 2.1.326:**

| Thử nghiệm | Kết quả |
| --- | --- |
| Thư mục cha có `CLAUDE.md` | `AGENTS.md` bị bỏ qua |
| `CLAUDE.md` chỉ chứa `@AGENTS.md` | Nạp được |
| `.claude/rules/*.md` không có `paths` | Nạp vào mọi phiên |
| Symlink cả thư mục `.claude/skills` | Chạy được |
| Skill `code-review` của dự án | Che Skill có sẵn cùng tên |
| `.claude/worktrees` là symlink, đã commit hoặc chưa commit | `claude -w` từ chối tạo worktree (tài liệu Claude Code ghi rõ, mục Troubleshooting) |
| Hook `WorktreeCreate` tạo `git worktree add .ai/worktrees/<tên>` rồi in đường dẫn | Chạy được, nhưng không dùng: người phát triển khung chọn chỗ mặc định `.claude/worktrees/` |

**Điểm áp dụng:**
- `gates-and-rigor` §3 Áp dụng khung vào dự án → duyệt file khung bằng PR có người duyệt, không đổi dòng Trạng thái.
- `project-rules` 22 → file chỉ dẫn trong `.ai/` viết tiếng Anh. `.ai/guide/` là tài liệu cho người nên viết tiếng Việt; FW-4 sửa câu chữ rule 22 cho khớp.

## 4. Chiến lược

- **Thứ tự:**
  - FW-1: từ vựng, làm trước vì mọi Task sau viết bằng từ mới.
  - FW-2: điểm vào và vùng.
  - FW-3: `ai-config.yaml`.
  - ⏸ Người phát triển khung xem kết quả đợt 1 trước khi sửa hàng loạt.
  - FW-4: chuyển tài liệu khung.
  - FW-5: `CHECKLIST.md` và `PROJECT.md`.
  - FW-6 ∥ FW-7: đổi mã thành chữ, hai Task không chung file nên chạy song song.
- **Chuỗi Skill:** theo loại việc "đổi kiến trúc của khung" (T7). Bước thiết kế (`architecture-design`) đã làm trong Plan này, ở §6, nên các Task chỉ còn `documentation`.
- **Cách chạy:**
  - Mỗi Task chạy trong worktree riêng, tạo bằng `git worktree add .claude/worktrees/<Task> -b plan-001/<Task> <commit gốc>`. Dùng lệnh git thay `claude -w` để chọn đúng commit gốc, vì `.claude/settings.json` chỉ có từ FW-2.
  - Chạy bằng `claude -p --model --effort --max-budget-usd` (cách B ở reference Claude Code §3) trong thư mục worktree.
  - Task sau tạo worktree từ commit đã gộp kết quả Task trước.

## 5. Task

Mọi Task chạm file của khung ở vùng đỏ. Mức rủi ro đề xuất là **vừa (R2: ảnh hưởng nhiều file khung, gồm file Approved; không chạm phân quyền, tiền, dữ liệu cá nhân)**. Mức tự chủ đề xuất là **làm trọn Task (A3: người duyệt kết quả cuối)**, cách chạy Gửi đi, agent executor, Skill `documentation`.

| Task | Tên | Loại | Thứ tự thử model/effort | Ngân sách (USD) | Lệch mặc định | Phụ thuộc | Cổng | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FW-1 | Từ vựng: thang dùng chung, tên loại việc, bỏ rule 23 | đổi kiến trúc của khung (T7) | sonnet/low → sonnet/high (M2·E1 → M2·E3: model chuẩn, effort thấp → cao) | 1,5 | Không | — | — | New |
| FW-2 | Điểm vào `CLAUDE.md`; vùng theo thư mục con; bỏ `.ai/worktrees/`, chuyển worktree sang `.claude/worktrees/` (`.gitignore`, `.claude/settings.json`, sửa 6 chỗ nhắc) | đổi kiến trúc của khung (T7) | sonnet/low → sonnet/high (M2·E1 → M2·E3) | 1 | Không | FW-1 | — | New |
| FW-3 | `ai-config.yaml`; rút `model-effort` còn quy tắc; sửa mẫu manifest, runs, Plan; khối cấu hình mẫu theo công cụ; Skill chọn reference theo `stack` | đổi kiến trúc của khung (T7) | sonnet/high → opus/high (M2·E3 → M3·E3: chuẩn, cao → mạnh, cao) | 2 | **Có**: bắt đầu ở mức cao vì viết lại quy tắc nâng mức mà mọi Plan sau dựa vào | FW-2 | ⏸ Người phát triển khung xem đợt 1 | New |
| FW-4 | Chuyển tài liệu khung từ `docs/` sang `.ai/guide/`, tách glossary, task-breakdown, ai-tools; sửa link | chỉ sửa tài liệu (T12) | sonnet/low → sonnet/high (M2·E1 → M2·E3) | 1,5 | Không | FW-3 | — | New |
| FW-5 | `CHECKLIST.md`; `PROJECT.md` điền sẵn khuyến nghị; README trỏ checklist | chỉ sửa tài liệu (T12) | sonnet/low → sonnet/high (M2·E1 → M2·E3) | 1 | Không | FW-4 | — | New |
| FW-6 | Đổi mã thành chữ trong file cho AI (`.ai/` trừ `guide/`, `plans/`) | chỉ sửa tài liệu (T12) | sonnet/low → sonnet/high (M2·E1 → M2·E3) | 1 | Không | FW-5 | — | New |
| FW-7 | Đổi mã thành chữ trong file cho người (`.ai/guide/`, `docs/`, file gốc) | chỉ sửa tài liệu (T12) | sonnet/low → sonnet/high (M2·E1 → M2·E3) | 1 | Không | FW-5 | — | New |
| Review (bước 8) | Review độc lập toàn bộ diff | review Pull Request (T9) | opus/high → opus/xhigh (M3·E3 → M3·E4: mạnh, cao → rất cao); mức tự chủ chỉ đọc và báo cáo (A1) | 3 | Không | mọi Task | — | New |

Tổng: 7 Task 9 USD, Review 3 USD, phiên điều phối 3 USD, cộng 15 USD. Mỗi Run đặt `--max-budget-usd` bằng ngân sách còn lại của Task.

## 6. Thiết kế

### 6.1 Từ vựng thay cho mã

File cho AI dùng cột tiếng Anh, file cho người dùng cột tiếng Việt. Mã định danh đối tượng (`FR-`, `BR-`, `NFR-`, `OQ-`, `SRC-`, `BRQ-`, `EPIC-`, `FEAT-`, `US-`, `GOAL-`, `PLAN-`, `ADR-`, mã Task `<KEY>-<N>`) giữ nguyên. Mã chuẩn bên ngoài như OWASP `A01:2025` cũng giữ nguyên.

| Thang | Mã cũ | Tiếng Anh (AI) | Tiếng Việt (người) |
| --- | --- | --- | --- |
| Rủi ro của Task | R1 · R2 · R3 | `low` · `medium` · `high` | thấp · vừa · cao |
| Mức tự chủ | A0 · A1 · A2 · A3 · A4 | `answer-only` · `read-only` · `step-by-step` · `full-task` · `pre-approved` | chỉ trả lời · chỉ đọc · duyệt từng bước · làm trọn Task · miễn duyệt từng Task |
| Độ nghiêm ngặt | S1 · S2 · S3 | `lean` · `standard` · `strict` | gọn · chuẩn · nghiêm ngặt |
| Mức dữ liệu | D0 · D1 · D2 · D3 | `public` · `internal` · `sensitive` · `secret` | công khai · nội bộ · nhạy cảm · bí mật (gồm dữ liệu cá nhân) |
| Cổng duyệt | G0 · G1 · G2 · G3 · G4 · G5 · G6 · G7 | `setup` · `scope` · `requirements` · `design` · `task-ready` · `code-complete` · `release-ready` · `operations` | Khai báo dự án · Phạm vi · Yêu cầu · Thiết kế · Sẵn sàng giao việc · Code xong · Sẵn sàng phát hành · Vận hành |
| Giai đoạn | [01] … [08] | `discovery` · `requirements` · `design` · `ai-context` · `implementation` · `testing` · `release` · `improvement` | Khám phá sản phẩm · Yêu cầu · Thiết kế · Chuẩn bị ngữ cảnh AI · Lập trình · Kiểm thử · Phát hành và vận hành · Cải tiến |
| Loại việc | T1 … T15 | `new-feature` · `feature` · `bug-fix` · `refactor` · `schema-change` · `requirement-change` · `architecture-change` · `requirement-review` · `pr-review` · `security-check` · `tests-only` · `docs-only` · `release` · `incident` · `periodic-review` | tính năng mới · làm tính năng · sửa lỗi · refactor · đổi schema · đổi yêu cầu · đổi kiến trúc · rà soát yêu cầu · review PR · kiểm tra bảo mật · chỉ viết test · chỉ sửa tài liệu · phát hành · sự cố production · rà soát định kỳ |
| Mức model·effort | M1–M3 · E1–E4 | Bỏ hạng. Ghi thẳng `model/effort` từ `ai-config.yaml`; văn bản chung nói "mức bắt đầu", "mức kế tiếp", "mức tối đa" | như cột trái |
| Vùng file | 🟢 · 🟡 · 🔴 | `green` · `yellow` · `red` | vùng xanh · vùng vàng · vùng đỏ (giữ biểu tượng màu cạnh chữ) |

Rule 23 thay bằng một câu: viết lựa chọn bằng từ của các thang trên; mã chỉ dùng cho định danh đối tượng; lần đầu nhắc một mã định danh với người thì nói nó là loại gì.

### 6.2 `ai-config.yaml` (gốc repo)

- Lập Plan chỉ đọc file này, không mở file khác.
- `try` là thứ tự thử: phần tử đầu là mức bắt đầu, phần tử cuối là mức tối đa. Bỏ `floor`, `ladder`, `start`, `ceiling`.
- `high_risk_min` giữ sàn cứng cho việc rủi ro cao.
- Mỗi `.ai/agents/references/<công-cụ>.md` có sẵn khối `sessions`/`tasks` đã điền model của công cụ đó. Đổi công cụ thì chép khối sang.
- Skill có `references/` theo công nghệ chọn file theo `stack`.

```yaml
tool: claude-code
sessions:
  orchestrator: opus/high      # Plan có đổi kiến trúc: opus/xhigh
  review:       opus/high
tasks:
  - for: [lookup]
    try: [haiku/low, sonnet/medium]
  - for: [documentation]
    try: [sonnet/low, sonnet/high]
  - for: [unit-testing, integration-testing, e2e-testing]
    try: [sonnet/low, sonnet/high, opus/high]
  - for: [backend-development, api-development, frontend-development]
    try: [sonnet/low, sonnet/high, opus/high]
  - for: [refactoring, caching, deployment, requirement-review, continuous-improvement]
    try: [sonnet/medium, opus/medium, opus/high]
  - for: [bug-fixing]
    try: [sonnet/medium, opus/high, opus/xhigh]
  - for: [product-discovery, requirement-analysis, architecture-design, database-design, task-planning, incident-analysis, code-review]
    try: [opus/high, opus/xhigh]
  - for: [authentication-rbac, security-review]
    try: [opus/high, opus/xhigh]
high_risk_min: opus/high
budget_usd_per_task: 2
stack: {}        # ví dụ backend: nestjs@11, orm: prisma@6, database: postgresql@17
commands: {}     # ví dụ test: npm test, lint: npm run lint, typecheck: npm run typecheck
```

### 6.3 Vùng file trong `.ai/`

| Đường dẫn | Vùng |
| --- | --- |
| `.ai/rules/`, `skills/`, `workflows/`, `templates/`, `agents/`, `guide/`, các `README.md` | đỏ: sửa cần Task riêng và người duyệt |
| `.ai/plans/` | xanh: AI tạo Plan, Plan có bước duyệt riêng |


**Worktree ở `.claude/worktrees/` cho mọi công cụ** (quyết định 2026-11-19):
- **Xoá** `.ai/worktrees/` (chỉ có `.gitkeep`).
- **`.gitignore`** thay hai dòng `.ai/worktrees/` bằng `.claude/worktrees/`. Phần còn lại của `.claude/` vẫn commit.
- **Claude Code:** dùng `claude -w <mã Task>`, không cần hook.
  - Commit `.claude/settings.json` với `"worktree": {"baseRef": "head"}`.
  - Lý do: mặc định (`fresh`) tạo worktree từ nhánh mặc định trên remote, còn quy trình cần worktree tạo từ commit đã gộp kết quả các Task phụ thuộc (`task-execution`, "Isolation and merging").
  - `.worktreeinclude` vẫn dùng được nếu dự án cần chép `.env` vào worktree.
- **Công cụ khác:** `git worktree add .claude/worktrees/<mã Task> -b <nhánh> <commit gốc>`.
- **Vùng:** worktree không xếp vùng, không commit. File sửa trong đó theo vùng của đường dẫn gốc.
- **Chỗ phải sửa:** `README.md:34`, `.ai/README.md:13`, `.gitignore:2-3`, `task-execution.md:33`, `agents/references/claude-code.md:70`, `glossary.md:73` (dòng này chuyển sang `.ai/guide/` ở FW-4).

### 6.4 Chuyển file

| Từ | Sang |
| --- | --- |
| `docs/getting-started.md` | `.ai/guide/getting-started.md`; các bước khai báo rút gọn, trỏ `CHECKLIST.md` |
| `docs/04-project-management/gates-and-rigor.md`, `work-model.md` | `.ai/guide/` |
| `docs/04-project-management/task-breakdown.md` | `.ai/guide/task-breakdown.md`; bảng Task mẫu bỏ, Task của dự án ở `task-backlog.md` |
| `docs/03-engineering/ai-governance.md`, `external-skills.md` | `.ai/guide/` |
| `docs/03-engineering/ai-tools.md` §1–§2 | `.ai/guide/ai-tools.md` |
| `docs/03-engineering/ai-tools.md` §3–§4 | Mục mới "Công cụ AI" trong `PROJECT.md` (quyền, MCP). Tên công cụ, model ở `ai-config.yaml` |
| `docs/00-project-overview/glossary.md` §1 | `.ai/guide/glossary.md`. Glossary của dự án chỉ còn thuật ngữ nghiệp vụ |

## 7. Kế hoạch kiểm thử

Mỗi AC có lệnh kiểm trong manifest. Bước 6 chạy trên kết quả gộp:
- `check.py links` và `check.py codes` (lệnh ở §2).
- Đọc `ai-config.yaml` bằng YAML.
- Lệnh lọc loại việc.

Không có code nên không có test đơn vị. Phần nội dung do người phát triển khung xem ở cổng sau FW-3 và khi duyệt diff cuối.

## 8. Rủi ro và điểm cần người quyết

| Rủi ro | Xử lý |
| --- | --- |
| Sót chỗ khi thay mã hàng loạt, sai nghĩa khi viết lại rule | `check.py codes` bắt mã sót. Review bước 8 so nội dung rule trước và sau. Người duyệt xem đợt 1 trước khi sửa hàng loạt |
| Gãy khoảng 190 link khi chuyển file | `check.py links` là AC của FW-4 và tiêu chí §2 |
| Worktree nằm trong repo nên thấy `CLAUDE.md` của repo chính (thư mục cha) | Prompt của mỗi Run dùng đường dẫn tương đối trong worktree. Tiêu chí Hợp lệ kiểm mọi file sửa nằm trong worktree |
| Dự án đã áp dụng khung bản cũ không đọc được bản mới | Ghi bảng ánh xạ §6.1 vào ghi chú phát hành của PR |
| `.ai/agents/references/*.md` viết tiếng Việt, trái `project-rules` 22 | Ngoài phạm vi; ghi nhật ký pilot, làm ở Plan sau |

Điểm người phát triển khung đã quyết khi duyệt Plan (2026-11-19):
1. Từ vựng §6.1, nhất là tên tiếng Anh của mức tự chủ và loại việc.
2. Định dạng `ai-config.yaml` §6.2.
3. Ngân sách 15 USD.
4. Độ nghiêm ngặt "chuẩn".

Cả bốn điểm đã duyệt.

## 9. Kết quả (điền sau khi xong)
