# PLAN: AI-10 — Mô hình Goal → Plan → Task → Run và điều phối nhiều phiên

> Trạng thái: **Draft**, đã triển khai theo quyết định 2026-11-18 (§6) và sửa theo review độc lập (§7); chờ người phát triển khung (Tech Lead của khung) review diff.
> **Nguồn đúng là các file của khung**, không phải bản đề xuất này: mô hình ở `task-execution.md`, mức và nâng mức ở `model-effort.md`, manifest ở `TASK-MANIFEST-TEMPLATE.yaml`. §2–§4 dưới đây đã sửa cho khớp, chỉ còn tóm tắt.
> Nguồn: yêu cầu của người phát triển khung trong pilot AI-10, 2026-11-18; nhật ký pilot #10.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Loại Task | T7 (đổi kiến trúc của khung) + T12 (sửa tài liệu) |
| Mức rủi ro · Mức tự chủ | R2 (ảnh hưởng nhiều file của khung) · A2 (duyệt từng bước) — đề xuất, chờ xác nhận |
| Model · Effort | Soạn đề xuất: M3·E4 · Sửa file sau khi duyệt: M2·E2 |

## 1. Vấn đề

Hiện 1 Task = 1 plan = 1 cặp model·effort cho cả phiên.
- Task lớn có bước cần model mạnh (thiết kế, phân quyền) lẫn bước chỉ cần model nhẹ (tra cứu, viết tài liệu): phải chọn mức cao nhất cho cả phiên, tốn token; hoặc chọn thấp thì bước khó bị làm kém.
- Đổi model, effort giữa chừng trong một phiên không đáng tin: context cũ vẫn mang theo, công cụ nào cũng có giới hạn riêng.
- "Plan" đang mang 2 nghĩa: plan của Skill `task-planning` (sinh nhiều Task, `task-planning/SKILL.md` bước 5) và plan của 1 Task (`task-execution.md` bước 3).

## 2. Mô hình đề xuất

```text
Goal (1) ──< Plan (N) ──< Task (N) ──< Run (N)
 WHAT         HOW          WHAT TO DO    DO
```

| Cấp | Trả lời | Ví dụ | Mã | Nơi lưu |
| --- | --- | --- | --- | --- |
| Goal | Cuối cùng muốn đạt kết quả gì? | Triển khai module Work study trên DigiUni | `GOAL-<NN>` (không dùng `G<N>` để khỏi trùng cổng G0–G7) | `docs/04-project-management/goals.md` (mới) |
| Plan | Đạt Goal bằng cách nào? AI suy nghĩ, chia nhỏ | Phân tích yêu cầu; Thiết kế; Làm tính năng Đăng ký | `<GOAL>-P<N>` | `.ai/plans/<GOAL>-P<N>-<slug>/PLAN.md` |
| Task | Công việc cụ thể, có đầu vào, đầu ra, trạng thái | Thiết kế bảng hồ sơ sinh viên | `<KEY>-<N>` (giữ nguyên) | Manifest `tasks/<KEY>-<N>.yaml` trong thư mục Plan; backlog, task-breakdown |
| Run | Thực thi Task thế nào? Agent nào, model·effort nào, kết quả | Run 1 của WS-3: Executor, sonnet·low, test đạt | `<KEY>-<N>#<n>` | `runs.md` trong thư mục Plan |

Ranh giới: **Plan ≠ Task ≠ Agent.** Plan là cách chia; Task là đơn vị việc; Agent là chủ thể thực thi Task (vai Planner/Executor/Tester/Reviewer/Security ở `.ai/agents/README.md`); Tool là công cụ Agent dùng.

### 2.1 Trường dữ liệu

**Goal:** id · tên · kết quả mong đợi (đo được) · truy vết (OUT, BRQ, FR nếu có) · tiêu chí hoàn thành · người sở hữu · trạng thái · ngày tạo.

**Plan:** id · goal · mô tả · chiến lược (vì sao chia như vậy, thứ tự) · tiêu chí hoàn thành · người duyệt · trạng thái · ngày tạo.

**Task:** khai báo bằng Task Manifest (§3.1). Plan chỉ giữ bảng tóm tắt: id · tên · loại T · R · A · cách chạy · agent · Skill · thang mức · lệch mặc định · phụ thuộc · cổng · trạng thái; thêm một dòng "Review" cho bước 8.

**Run:** task_id · lần · agent · model·effort thật · lý do chạy (lần đầu / nâng cấp / chạy lại sau khi sửa môi trường) · bắt đầu/kết thúc · kết quả đánh giá (Đạt / Không đạt / Dừng) và tiêu chí không đạt · bằng chứng · token/chi phí (nối với số đo ở DELIVERY-REPORT §8).

### 2.2 Khi nào tạo Plan mới (thay vì thêm Task vào Plan cũ)

Tạo Plan mới khi có ít nhất một điều:
- Mục tiêu đầu ra khác nhau.
- Thực hiện độc lập được.
- Có vòng đời và tiêu chí hoàn thành riêng.
- Cần quản lý tiến độ hoặc quyền truy cập riêng.

Mặc định gợi ý: mỗi chặng có cổng duyệt riêng (phân tích → G2, thiết kế → G3, làm tính năng → G5) là một Plan.

### 2.3 Trạng thái

- Goal: `Open` → `In Progress` → `Achieved` / `Dropped`.
- Plan: `Draft` → `Approved` → `In Progress` → `Done` / `Cancelled`.
- Task: giữ nguyên backlog §5 (`New` → `Ready` → `In Progress` → `In Review` → `Done`, hoặc `Blocked` / `Cancelled`).
- Run: `Đạt` / `Không đạt` / `Dừng` (đạt một phần AC là `Không đạt`). Mỗi lỗi tối đa 3 Run, kể cả nâng mức; lỗi mới sau test hoặc review có 3 Run riêng; ngân sách cộng dồn của Task là trần cứng (`project-rules` 18).

## 3. Điều phối: Model-Aware Task Orchestration

Tách 3 việc độc lập: **lập Plan** · **phân loại Task** (gán loại T, R, A, agent, model·effort) · **thực thi Task**. Không đổi model trong một phiên; mỗi Task chạy trong một phiên/subagent riêng, khởi tạo với cấu hình riêng.

**Master Orchestrator** = phiên chính, model M3 (lập Plan và phân loại cần suy luận tốt). Trách nhiệm:
1. Tạo Plan và Task từ Goal.
2. Xác định model·effort cho từng Task (mặc định theo Skill ở `model-effort` §2; R3 hoặc Skill bảo mật: ít nhất M3·E3).
3. Gửi Task tới subagent đúng vai và cấu hình.
4. Nhận kết quả (báo cáo bàn giao + bằng chứng), ghi Run.
5. Kiểm tra phụ thuộc trước khi gửi Task kế; chạy song song chỉ khi không chung file, schema, contract.
6. Tổng hợp output, cập nhật trạng thái Plan, Goal.

Orchestrator **không tự viết code** của Task và không duyệt thay người. Các điểm ⏸ (cổng duyệt) vẫn dừng chờ người.

**Subagent** nhận đúng: manifest, ghi chú lỗi của lần trước (nếu có), `project-rules`, Rule, Skill, mục tài liệu manifest liệt kê. Không nhận lịch sử phiên Orchestrator (giữ context nhỏ, review độc lập).

**Cách chạy theo mức tự chủ:** Task A3, A4 "Gửi đi" (subagent hoặc phiên không tương tác). Task A2 trở xuống "Có người": người mở phiên tương tác ở mức của manifest, duyệt từng bước (quyết định Q2). Mỗi Task một worktree; Orchestrator gộp nhánh theo thứ tự phụ thuộc trước bước 6.

**Theo công cụ:**
- Claude Code: subagent theo vai × mức (`executor-m2-e1`…) hoặc `claude -p` mỗi Run (chi tiết `references/claude-code.md` §3). Copilot CLI: `copilot -p` mỗi Run.
- Cursor, Gemini CLI, Codex: mọi Run đều "Có người"; Orchestrator soạn manifest và câu mở phiên.

### 3.1 Task Manifest

Mỗi Task có một manifest tách 3 câu hỏi: **làm gì** (mục tiêu, đầu vào, đầu ra, phạm vi) · **chạy bằng cấu hình nào** (agent, model·effort, ngân sách, nâng cấp) · **làm sao biết xong đúng** (AC kèm cách kiểm).

**Manifest chỉ là metadata.** Nó không tự đổi model, effort. Chỉ có tác dụng khi bên thực thi đọc và áp dụng: Orchestrator chọn subagent hoặc tham số tương ứng; với công cụ không có subagent thì người mở phiên theo manifest. Bên thực thi nào không áp được một trường thì ghi vào Run ("không áp dụng: max_output_tokens"), không im lặng bỏ qua.

Chỗ khác bản tham khảo:
- Dùng hạng của khung (`M2·E1`), không dùng tên model thật: manifest không phụ thuộc công cụ; đổi sang model thật theo `references/<công cụ>.md` §1.
- Thay một mức `effort` bằng **mức bắt đầu, mức sàn, mức trần, thang nâng cấp**.
- Mỗi AC có **cách kiểm** (lệnh, file, người duyệt). AC không kiểm được bằng công cụ thì ghi rõ người kiểm.
- Thêm phạm vi file được sửa (khớp vùng 🟢🟡🔴), Rule, Skill, đầu vào cần nạp (nạp đúng lúc), điều kiện dừng thay vì nâng cấp.
- Định dạng YAML, không dùng JSON: người đọc dễ hơn, ít token hơn, vẫn đọc được bằng máy.

Mẫu chính thức: [TASK-MANIFEST-TEMPLATE.yaml](../templates/TASK-MANIFEST-TEMPLATE.yaml). Không chép lại ở đây để chỉ có một nguồn.

Manifest được duyệt cùng Plan. Sau khi duyệt, nâng cấp trong thang không cần duyệt lại; đổi `start`, `floor`, `ceiling`, `ladder`, `budget`, `scope`, AC, R, A thì phải duyệt lại. Kết quả từng lần chạy ghi ở `runs.md` cùng thư mục, không ghi vào manifest: tách cấu hình đã duyệt khỏi dữ liệu lúc chạy.

### 3.2 Nâng cấp động (Dynamic Escalation)

Không phải lúc nào cũng phân loại đúng Task ngay từ đầu. Vì vậy Task chạy ở mức bắt đầu, đánh giá kết quả, chỉ nâng khi không đạt. Cách này rẻ hơn chạy mức cao cho cả quy trình.

```text
Run ở mức start ──► Đánh giá ──► Đạt ──► nhận kết quả, sang Task kế
                       │
                       └─► Không đạt ──► lỗi thuộc stop_on? ──có──► Dừng, hỏi người
                                              │
                                              └─không─► còn bậc và còn lượt? ──không──► Dừng, hỏi người
                                                              │
                                                              └─có─► Run mới ở bậc kế trong ladder
```

**Đánh giá và quy tắc nâng mức:** ở `model-effort.md` §3. Tóm tắt:
- Đạt cần đủ ba tiêu chí Đầy đủ, Đúng, Hợp lệ; đạt một phần là không đạt.
- Độ tin cậy do agent tự báo không làm Đạt và không gây nâng mức; lần chạy đạt nhưng agent không chắc thì đưa người xem.
- Chỉ nâng khi lỗi do năng lực; `stop_on` (thiếu đầu vào, mâu thuẫn, ngoài phạm vi, môi trường, bảo mật, bị từ chối quyền) thì dừng.
- Thang kết thúc ở trần và không nhiều bậc hơn `max_attempts`, nên trần luôn tới được.
- Mỗi lần nâng đưa worktree về commit `base`, làm lại từ đầu với context mới.
- Ngân sách cộng dồn theo Task, gồm cả chi phí Orchestrator ở cấp Plan.
- Task chỉ có người kiểm (thiết kế, phân tích) bắt đầu ở mức mặc định, không bắt đầu thấp.

## 4. Thay đổi quy trình `task-execution`

| Hiện tại | Đề xuất |
| --- | --- |
| Bước 1–4: 1 phiên plan cho 1 Task | **Giai đoạn Plan** (Orchestrator): nhận Goal → tạo/chọn Plan → chia Task, phân loại → người duyệt Plan (gồm R, A từng Task, Tech Lead xác nhận một lần cho cả Plan) |
| Bước 3: plan file riêng cho mỗi Task | Nội dung đó thành Task Manifest (§3.1); Plan giữ chiến lược và bảng tóm tắt Task |
| Bước 5–7: 1 phiên thực thi | **Giai đoạn Run**: mỗi Task chạy ở subagent/phiên mới theo manifest, có đánh giá và nâng cấp động (§3.2) |
| Bước 8 review: phiên khác | `code-review`, `security-review` không chia thành Task ở bước 3; chạy ở bước 8 sau khi có kết quả test, agent Reviewer/Security, context mới, mức theo `model-effort` §2 |
| Fast lane R1 | Giữ: 1 Task, chạy ngay trong phiên chính ở mức bắt đầu của Skill chính; 3 vòng mỗi lỗi; review ở phiên mới do người mở; ghi mã Goal ở commit và báo cáo bàn giao |

Chuỗi Skill trong `task-types` §1 trở thành **mẫu chia Task**: mỗi Skill (hoặc nhóm Skill liền nhau cùng mức mặc định) là một Task, trừ Skill review. Ví dụ T1: Task phân tích (M3·E3) → Task rà soát (M2·E2) → ⏸ → Task thiết kế (M3·E3) → ⏸ → Task chia việc.

## 5. File dự kiến thay đổi

| File | Thay đổi |
| --- | --- |
| `docs/04-project-management/goals.md` (mới) | Bảng Goal, trạng thái, truy vết |
| `.ai/templates/PLAN-TEMPLATE.md` | Viết lại: Goal, chiến lược, tiêu chí hoàn thành, bảng tóm tắt Task, Kết quả |
| `.ai/templates/TASK-MANIFEST-TEMPLATE.yaml` (mới) | Mẫu manifest §3.1, chú thích từng trường |
| `.ai/templates/RUNS-TEMPLATE.md` (mới) | Bảng Run: lần, mức, lý do, kết quả đánh giá, bằng chứng, chi phí |
| `.ai/workflows/model-effort.md` §3 | Quy tắc đánh giá và nâng mức (không tạo file `escalation.md`) |
| `.ai/workflows/task-execution.md` | Giai đoạn Plan / Run, vai Orchestrator, quy tắc chuyển |
| `.ai/workflows/task-types.md` §1 | Bỏ cột model·effort (mức theo Skill ở `model-effort` §2); chuỗi Skill là mẫu chia Task |
| `.ai/workflows/model-effort.md` §1–§2, §4 | Mức Orchestrator; mức mặc định, sàn, trần, thang theo Skill; ánh xạ công cụ |
| `.ai/agents/README.md` | Thêm vai Orchestrator; subagent theo vai × hạng |
| `.ai/agents/references/*.md` | Claude Code, Copilot: subagent theo hạng; Cursor, Gemini, Codex: cách mở phiên theo Task |
| `.ai/skills/task-planning/SKILL.md` | Tạo Plan theo Goal, áp tiêu chí tạo Plan mới §2.2 |
| `docs/04-project-management/task-breakdown.md` §2, `backlog.md` §2 | Phân cấp Goal → Plan → Task → Run; bỏ "Subtask không ID" |
| `docs/00-project-overview/glossary.md` | Goal, Plan (sửa), Run, Orchestrator |
| `docs/getting-started.md` §2, §5.2, §5.3 | Mở phiên Orchestrator; mẫu prompt mới |
| `DELIVERY-REPORT-TEMPLATE.md` §8 | Số đo lấy theo Run |

## 6. Điểm cần người quyết

**Đã quyết (2026-11-18, người phát triển khung): cả OQ-A … OQ-D theo đề xuất.** OQ-E đã kiểm chứng, kết quả ở §7.

**Đã quyết sau review (2026-11-18): Q1, Q2 theo đề xuất.**
- Q1: `project-rules` 18 đếm theo từng lỗi; nâng mức tính vào 3 vòng của lỗi đó; lỗi mới sau test, review có 3 vòng riêng; ngân sách cộng dồn của Task là trần cứng.
- Q2: Task A2 trở xuống chạy "Có người" trong phiên tương tác, duyệt từng bước; Orchestrator không gửi cho subagent.

- **OQ-A (vị trí Goal):** đặt Goal ở file mới `goals.md` (đề xuất: tách khỏi backlog vì Goal có vòng đời riêng) hay thêm loại "Goal" vào backlog §2 (ít file hơn, nhưng backlog sẽ trộn kết quả và việc). Còn quan hệ với Epic: đề xuất Epic giữ nghĩa nhóm theo mốc roadmap, một Goal có thể thuộc một Epic.
- **OQ-B (ai gán R, A cho nhiều Task):** đề xuất Orchestrator đề xuất R, A cho từng Task trong Plan; Tech Lead duyệt cả Plan là xác nhận R, A. Ngược lại, nếu Tech Lead gán từng Task thì chậm hơn nhưng giữ đúng câu chữ hiện tại của `project-rules` 8 ("autonomy level granted by the Task").
- **OQ-C (model của Orchestrator):** đề xuất M3·E3 cố định; Goal có Plan kiến trúc thì M3·E4.

- **OQ-D (nâng cấp có cần người duyệt không):** đề xuất Orchestrator tự nâng trong thang `ladder` đến `ceiling` đã duyệt cùng Plan, ghi vào `runs.md`; vượt trần mới hỏi. Được: không chờ người ở mỗi lần nâng. Mất: chi phí có thể lên tới mức trần mà không ai xem trước; giới hạn bằng `budget`. Cách khác: mỗi lần nâng đều hỏi, an toàn chi phí nhưng chậm, mất ý nghĩa tự động.
- **OQ-E (cần kiểm chứng trên công cụ, không phải quyết định):** Claude Code có đặt được model, effort cho **từng lần gọi** subagent không, hay chỉ cố định trong frontmatter `.claude/agents/*.md`? Nếu chỉ có frontmatter thì phải tạo một file subagent cho mỗi tổ hợp vai × bậc (ví dụ `executor-m2-e1`, `executor-m2-e3`, `executor-m3-e3`). Theo `project-rules` 16, mình sẽ đọc tài liệu và chạy thử trên bản Claude Code đang dùng trước khi viết vào `references/claude-code.md`. Copilot CLI tương tự với `subagents.agents.*`.

Nếu chưa quyết: viết được glossary, PLAN-TEMPLATE, mẫu manifest, phân cấp ở task-breakdown; chưa sửa `task-execution`, `project-rules`, quy tắc nâng cấp.

## 7. Kết quả (điền sau khi xong)

**Kiểm chứng OQ-E** (Claude Code 2.1.326, chạy thử `claude -p`): có `--model`, `--effort`, `--max-budget-usd`, `--output-format json` (trả `total_cost_usd`, `modelUsage`); `--agents '<json>'` nhận `model` cho subagent (chạy thử subagent haiku dưới phiên Opus, `modelUsage` thấy cả hai model); trường `effort` trong JSON này chưa xác nhận được áp dụng. `--allowedTools` nhận một chuỗi ngăn bằng dấu cách, prompt phải đặt sau `--`. Không có cờ giới hạn token đầu ra. Chưa xác nhận đổi model cho từng lần gọi công cụ Agent trong phiên tương tác → khung dùng subagent theo vai × mức hoặc `claude -p` mỗi Run.

**Lệch so với đề xuất:**
- Cột model·effort ở `task-types` §1 bị bỏ; mức mặc định chuyển sang theo **Skill** (`model-effort` §2), vì một Task giờ ứng với một hoặc vài Skill, không còn ứng với cả loại Task.
- Escalation viết thành §3 của `model-effort.md`, không tạo file `escalation.md` (tránh thêm file workflow, theo `workflows/README`).
- Plan lưu thành thư mục `.ai/plans/<GOAL>-P<N>-<slug>/` (PLAN.md, tasks/, runs.md). File đề xuất này giữ dạng cũ vì soạn trước quy ước.
- Fast lane giữ cho một Task R1: 3 vòng mỗi lỗi, không nâng mức trong phiên; review ở phiên mới do người mở.

**File đã sửa:** workflow (`task-execution`, `model-effort`, `task-types`, README); rule (`project-rules` 8, 18, 23); mẫu (PLAN, TASK-MANIFEST mới, RUNS mới, DELIVERY-REPORT §8, README); agents (README, 5 file references); Skill `task-planning` và dòng ghi test case của 4 Skill code; `docs/` (goals mới, task-breakdown, backlog, PM README, glossary, getting-started); README gốc.

**Sửa theo review độc lập (14 phát hiện, 2026-11-18):**
- High: thang mặc định nhảy bậc, tối đa 3 bậc, trần luôn tới được (#1); điều 18 theo Q1 (#2); Task A2 chạy "Có người" theo Q2 (#3); `code-review`, `security-review` chỉ chạy ở bước 8 (#4); miễn duyệt Plan chỉ khi mọi mức đúng mặc định và ngân sách trong mức mặc định của dự án (#5).
- Medium: đưa worktree về commit `base` trước mỗi lần nâng, ghi `base` trong `runs.md`; đạt một phần là không đạt (#6); bỏ `low_confidence` khỏi `escalate_on` (#7); ngân sách cộng dồn, `--max-budget-usd` bằng ngân sách còn lại, tính cả Orchestrator (#8); lệnh `claude -p` có `--permission-mode acceptEdits` và `--allowedTools`, thêm `permission_denied` vào `stop_on` (#9); fast lane: 3 vòng mỗi lỗi, review ở phiên mới, mã Goal ở commit (#10); đổi bất kỳ trường mức nào đều phải duyệt lại (#11).
- Low: DELIVERY-REPORT, TEST-REPORT, 6 Skill code/test, task-breakdown §4 chuyển sang Plan và manifest (#12); thứ tự mức có thêm M3·E1, M3·E2, số bước của Orchestrator khớp nhau, sàn R3 kéo cả `start` (#13); ghi rõ `effort` của `--agents` chưa kiểm chứng, `--max-budget-usd` chỉ chạy với `-p` (#14).

**Sửa theo review lần hai (2026-11-18):**
- High: mỗi lỗi có commit gốc riêng, nâng mức không xoá kết quả đã nhận; lỗi mới chạy từ mức của lần chạy được nhận gần nhất. Đang ở trần mà còn lượt thì chạy lại cùng mức (Task R3 không còn bị giới hạn 1 lần chạy).
- Medium: Plan luôn có dòng "Review" cho bước 8, mức và ngân sách duyệt cùng Plan, ghi `runs.md` dạng `<GOAL>-P<N>-REVIEW#<n>`.
- Low: Copilot, agents README nói rõ Task "Có người"; Run "Có người" mở trong worktree của Task, người báo chi phí; chạy thử `--allowedTools`, thêm `--` trước prompt.
- Review lần ba (không còn High): worktree của Task tách từ commit chứa kết quả được nhận của mọi Task nó phụ thuộc; sau mỗi bản sửa ở bước 6, 8 thì rebase Task phụ thuộc, gộp lại và chạy lại bước 6; không xác định được Task gây lỗi thì dừng hỏi người. Mọi lần chạy lại của một lỗi đều đưa worktree về commit gốc của lỗi. Dòng Review có cột ngân sách và tiêu chí trượt riêng.
- Ngân sách mặc định (2026-11-18, người phát triển khung chọn B): để sang đợt B, điền khi làm `PROJECT.md` cho Work study theo số đo thật. Đã kiểm trên Claude Code 2.1.326: `claude -p` trả `total_cost_usd` và chặn được bằng `--max-budget-usd`; phiên tương tác chỉ có token trong transcript, không có số tiền, không có cờ chặn; không thấy trần ngân sách cho cả team trong cấu hình máy.
- Còn treo: điều kiện miễn duyệt cần "ngân sách mặc định của dự án" chưa có chỗ khai báo (đợt B).

**Chưa kiểm:** chưa chạy thử một Plan thật từ đầu tới cuối; mức mặc định theo Skill ở `model-effort` §2 là ước đoán, cần đo trên Work study (đợt B). "Ngân sách mặc định của dự án" (điều kiện miễn duyệt) chưa có chỗ khai báo trong `PROJECT.md`: hiện coi như không có, nên Plan luôn chờ duyệt.
