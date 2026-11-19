# Công cụ AI

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người duyệt (dự án) | Tech Lead |
| Tài liệu liên quan | ../../AGENTS.md, ../../.ai/rules/security-rules.md, external-skills.md |

> **Mục đích.** Cách nối công cụ AI với `.ai/`. AI không nạp file này khi làm Task.

## 1. Tích hợp

`.ai/` là nguồn duy nhất. Mỗi công cụ chỉ có file vào trỏ về `.ai/`, không chép nội dung. Quy định tên công cụ, tên model và effort ở [ai-config.yaml](../../ai-config.yaml).

| Công cụ | File vào | Skill tự kích hoạt |
| --- | --- | --- |
| Claude Code | `AGENTS.md` (từ v2.1.277 tự đọc khi repo không có `CLAUDE.md`; có `CLAUDE.md` thì thêm dòng `@AGENTS.md`) | `.claude/skills` |
| Cursor | `AGENTS.md` | Đọc `.claude/skills/` hoặc `.agents/skills/` |
| Antigravity CLI (thay Gemini CLI) | `AGENTS.md` hoặc `GEMINI.md` | `.agents/skills` |
| Codex | `AGENTS.md` | Skills tương thích |
| GitHub Copilot | `.github/copilot-instructions.md` | — |

## 2. Tạo symlink

Chỉ symlink thư mục Skill, chạy ở thư mục gốc repo, cho công cụ dự án dùng:

```bash
mkdir -p .claude && ln -s ../.ai/skills .claude/skills   # Claude Code (Cursor cũng đọc)
mkdir -p .agents && ln -s ../.ai/skills .agents/skills   # Antigravity
```

Không đưa Rule vào `.claude/rules/`, `.cursor/rules/`: Rule không có `paths` nạp từ đầu mọi phiên; `paths` chỉ lọc theo file đang sửa, không theo loại Task như [task-execution](../../.ai/workflows/task-execution.md).

## 3. Chạy Task với Claude Code

> Dành cho người vận hành; Orchestrator đọc mục này khi `auto_runs: true` và `tool: claude-code`; Run của Task không nạp. Chỉ ghi điều đã kiểm chứng trên Claude Code 2.1.326 (2026-11). Model và effort lấy từ [ai-config.yaml](../../ai-config.yaml); đổi phiên bản Claude Code thì kiểm lại.

- **Một Run không tương tác cho mỗi Task**, chạy trong worktree của Task, prompt đặt sau `--`:

  ```sh
  claude -p --model <model> --effort <effort> --max-budget-usd <ngân-sách-còn-lại> \
    --output-format json --permission-mode acceptEdits \
    --allowedTools "<danh-sách>" -- "<prompt>"
  ```

- **`--allowedTools` là một chuỗi ngăn bằng dấu cách.** Lệnh ngoài danh sách bị chặn và ghi vào `permission_denials` của JSON. Lệnh nối (`;`, `&&`, `cd`) và script phụ trợ cũng bị chặn, nên prompt yêu cầu mỗi lệnh Bash chạy riêng một lệnh và sửa file bằng Edit/Write.
- **Ghi file dưới `.claude/` bị chặn** ở chế độ này dù đã cho phép theo tên: người tạo các file đó.
- **`--allowedTools` chỉ mở lệnh có trong `acceptance_criteria[].check` và lệnh git chỉ đọc.**
- **Không dùng `bypassPermissions`.**
- **`allowed_paths` không có cờ tương ứng:** Orchestrator kiểm file đổi ở tiêu chí Hợp lệ.
- **`permission_denials` chặn bước bắt buộc** thì là `permission_denied`: dừng, không nâng mức.
- **Đọc từ JSON để ghi `runs.md`:** `is_error` (lỗi API có thể kết thúc Run với `subtype: success`), `total_cost_usd`, `modelUsage`, `permission_denials`. `--max-budget-usd` chỉ có tác dụng với `-p` và tính cho từng lần gọi: đặt bằng ngân sách còn lại của Task.
- **Không có cờ giới hạn token đầu ra:** Run ghi "không áp dụng: max_output_tokens".
- **Task `step-by-step`:** người mở phiên tương tác `claude --model <model> --effort <effort>` trong worktree của Task.
- **Phiên Orchestrator:** dùng `/model` và `/effort` theo `sessions.orchestrator`.
- **Subagent Reviewer/Security:** một file mỗi vai trong `.claude/agents/`, model và effort theo `sessions.review`; nội dung chỉ trỏ về `.ai/`. Ví dụ `.claude/agents/reviewer.md`:

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
