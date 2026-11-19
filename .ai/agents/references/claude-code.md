# Model và effort cho Claude Code

> Dùng khi dự án chọn Claude Code ([ai-tools.md](../../../docs/03-engineering/ai-tools.md) §3). **§1 là khối `sessions`/`tasks`** của Claude Code: đổi công cụ sang Claude Code thì chép khối này vào [ai-config.yaml](../../../ai-config.yaml); quy tắc chọn mức nằm ở [model-effort.md](../../workflows/model-effort.md). Các mục còn lại (§2–§4) là cách cấu hình; §3 ghi điều đã kiểm chứng.
> Tên model và tham số thay đổi theo phiên bản Claude Code. Kiểm tra lại tài liệu chính thức trước khi áp dụng (cập nhật: 2026-11).

## 1. Model và effort theo loại việc

Mỗi mức viết `model/effort`: `haiku` = `claude-haiku-5-5`, `sonnet` = `claude-sonnet-5-5`, `opus` = `claude-opus-5-5`; effort là `low`, `medium`, `high`, `xhigh`.

```yaml
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
```

Lưu ý:
- Mỗi model có effort mặc định riêng; ví dụ Opus 5.5 mặc định `medium`. Vì vậy **luôn khai báo `effort` tường minh**, không dựa vào mặc định.
- Hạ effort trên model mạnh thường tốt hơn chuyển xuống model yếu với effort cao. Hãy đo trên Task thật trước khi đổi khối.
- `max` dành cho trường hợp đặc biệt, phải ghi lý do. `claude-fable-5-2` (chi phí cao) chỉ cho việc rất khó (kiến trúc lớn, sự cố phức tạp) khi người phát triển khung hoặc Tech Lead cho phép; không nằm trong khối.

## 2. Phiên Orchestrator

Mở phiên chính ở mức `sessions.orchestrator` của `ai-config.yaml` ([model-effort](../../workflows/model-effort.md) §1):

```text
/model opus
/effort high       # xhigh nếu Plan có Task loại architecture-change (đổi kiến trúc hoặc API contract)
```

Fast lane (một Task rủi ro thấp): mở phiên ở mức bắt đầu của Task theo Skill chính (phần tử đầu của `try`), ví dụ `documentation` → `/model sonnet` + `/effort low`.

Lệnh `/effort` và trường `effort` phụ thuộc phiên bản Claude Code; bản không hỗ trợ thì chỉnh qua `/model` hoặc `/config`.

## 3. Chạy Task theo manifest

Đã kiểm chứng trên Claude Code 2.1.326 (2026-11-18, chạy thử bằng `claude -p`):
- `claude -p` (không tương tác) nhận `--model`, `--effort`, `--output-format json`. Kết quả JSON có `total_cost_usd`, `modelUsage` (model thật đã dùng, token, chi phí): đủ để ghi `runs.md`.
- `--max-budget-usd` chặn chi phí **chỉ khi chạy với `-p`/`--print`**, và tính cho một lần gọi. Đặt bằng ngân sách còn lại của Task (model-effort §3 quy tắc 6), không phải cả ngân sách.
- `--agents '<json>'` khai báo subagent ngay khi gọi. Đã xác nhận trường `model`: subagent `model: haiku` dưới phiên Opus, `modelUsage` ghi cả hai model. **Chưa xác nhận trường `effort`** trong JSON này có được áp dụng không (JSON trả về không ghi effort).
- Không có cờ giới hạn token đầu ra: `max_output_tokens` của manifest ghi "không áp dụng" trong Run.
- Chưa xác nhận: gọi công cụ Agent từ phiên tương tác có đổi được model, effort cho từng lần gọi không. Vì vậy cách chắc chắn là một trong hai cách dưới.
- Chỉ dùng cho Task "Gửi đi" (mức tự chủ `full-task`, `pre-approved`). Task `step-by-step` trở xuống chạy "Có người": người mở phiên tương tác bằng `claude --model <model> --effort <mức>` theo manifest, phiên dừng sau mỗi bước chờ duyệt.

**Cách A: subagent theo vai × mức** (`.claude/agents/<vai>-<mức>.md`), Orchestrator gọi trong phiên tương tác. Mỗi mức dùng trong `try` cần một file; tên file ghép model và effort: `executor-sonnet-low`. Cách này không có cờ chặn chi phí: Orchestrator đọc chi phí sau mỗi lần chạy và dừng khi chạm ngân sách. Trường `effort` trong frontmatter phụ thuộc phiên bản; kiểm tra trước khi dùng. Chạy song song nhiều subagent thì mỗi subagent làm trong worktree riêng của Task.

`.claude/agents/executor-sonnet-low.md`:

```markdown
---
name: executor-sonnet-low
description: Chạy một Task vai Executor ở mức sonnet/low theo Task Manifest. Chỉ dùng khi manifest ghi agent executor và mức hiện tại sonnet/low.
model: sonnet
effort: low
tools: Read, Edit, Write, Grep, Glob, Bash
---

Bạn giữ vai Executor trong .ai/agents/README.md.
Đọc Task Manifest được giao; chỉ nạp Rule, Skill, mục tài liệu manifest liệt kê.
Làm từng Skill theo thứ tự; trả báo cáo bàn giao có bằng chứng cho từng AC, giả định, điểm chưa chắc.
Gặp thiếu đầu vào, mâu thuẫn, ngoài allowed_paths, phát hiện bảo mật: dừng và báo, không tự xử lý.
```

Các mức khác chỉ khác `name`, `description`, `model`, `effort`.

**Cách B: phiên không tương tác cho mỗi Run.** Orchestrator (hoặc người) chạy từ thư mục worktree của Task:

```sh
cd .claude/worktrees/WS-3      # worktree riêng của Task, tạo từ commit base
claude -p --model sonnet --effort low --max-budget-usd 2 --output-format json \
  --permission-mode acceptEdits \
  --allowedTools "Read Grep Glob Edit Write Bash(npm test *) Bash(npm run lint) Bash(npm run typecheck) Bash(git diff *) Bash(git status)" \
  -- "Run Task WS-3 theo .ai/plans/PLAN-002-dang-ky/tasks/WS-3.yaml. Làm theo AGENTS.md." > run-WS-3-1.json
```

- `--permission-mode acceptEdits` cho phép sửa file không hỏi; `--allowedTools` chỉ mở các lệnh có trong `acceptance_criteria[].check` của manifest và lệnh git chỉ đọc. Không dùng `bypassPermissions`.
- Đã chạy thử (2.1.326): `--allowedTools` nhận một chuỗi ngăn bằng dấu cách, kể cả mục có dấu cách bên trong như `Bash(echo *)`; lệnh ngoài danh sách bị chặn và ghi ở `permission_denials` của JSON. **Prompt phải đặt sau `--`**, nếu không bị đọc thành giá trị của `--allowedTools`.
- `permission_denials` khác rỗng: ghi `permission_denied` vào Run.
- `allowed_paths` không có cờ tương ứng: Orchestrator kiểm ở tiêu chí "Hợp lệ" (file thay đổi phải nằm trong `allowed_paths`).
- Lần chạy bị từ chối quyền là `permission_denied` trong `stop_on`: dừng, không nâng mức.
- Lấy `result`, `total_cost_usd`, `modelUsage` từ file JSON ghi vào `runs.md`. Nâng mức thì đưa worktree về commit `base`, chạy lại với `--model`, `--effort` của bậc kế, `--max-budget-usd` bằng ngân sách còn lại, kèm ghi chú lỗi của lần trước trong prompt.

## 4. Subagent vai cố định

Vai không cần nâng mức (Reviewer, Security, tra cứu) dùng một file mỗi vai, mức theo `sessions.review` hoặc dòng `tasks` của Skill trong `ai-config.yaml`. Nội dung file chỉ trỏ về `.ai/`, không chép Rule hay Skill vào.

`.claude/agents/reviewer.md`:

```markdown
---
name: reviewer
description: Review độc lập diff của Task theo Skill code-review. Dùng sau khi Executor bàn giao; không dùng trong phiên vừa viết code.
model: opus
effort: high
tools: Read, Grep, Glob, Bash
---

Bạn giữ vai Reviewer trong .ai/agents/README.md.
Nạp .ai/skills/code-review/SKILL.md và làm theo đúng quy trình trong đó.
Chỉ báo phát hiện có mức độ và file:dòng; không sửa code.
```

`.claude/agents/security.md`:

```markdown
---
name: security
description: Rà soát bảo mật theo Skill security-review; chỉ khuyến nghị, không sửa code.
model: opus
effort: high
tools: Read, Grep, Glob
---

Bạn giữ vai Security trong .ai/agents/README.md.
Nạp .ai/skills/security-review/SKILL.md. Không đưa secret hoặc dữ liệu `secret` vào ngữ cảnh.
```

`.claude/agents/explorer.md` (tra cứu, chỉ đọc):

```markdown
---
name: explorer
description: Tìm file, đọc nhiều file và trả kết luận ngắn. Không quyết định thiết kế.
model: haiku
effort: low
tools: Read, Grep, Glob
---

Chỉ đọc và báo cáo (mức tự chủ `read-only`). Trả về đường dẫn file:dòng và kết luận; không dán nguyên nội dung file.
```
