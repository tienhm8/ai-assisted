# Model và effort cho Claude Code

> Dùng khi dự án chọn Claude Code ([ai-tools.md](../../../docs/03-engineering/ai-tools.md) §3). **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu khi phiên chạy trong Claude Code: hạng M1–M3 → model, mức E1–E4 → `effort`. Mức mặc định theo Skill nằm ở [model-effort.md](../../workflows/model-effort.md) §2. Các mục còn lại (§2–§4) là cách cấu hình; §3 ghi điều đã kiểm chứng.
> Tên model và tham số thay đổi theo phiên bản Claude Code. Kiểm tra lại tài liệu chính thức trước khi áp dụng (cập nhật: 2026-11).

## 1. Ánh xạ hạng → model, mức → effort

| Hạng / mức khung | Model hoặc tham số thật |
| --- | --- |
| M1 · Nhẹ | `haiku` · `claude-haiku-5-5` |
| M2 · Chuẩn | `sonnet` · `claude-sonnet-5-5` |
| M3 · Mạnh | `opus` · `claude-opus-5-5` |
| M3+ (tuỳ chọn, chi phí cao) | `claude-fable-5-2`: chỉ cho việc rất khó (kiến trúc lớn, sự cố phức tạp) khi Tech Lead cho phép |
| E1 · Thấp | `low` |
| E2 · Trung bình | `medium` |
| E3 · Cao | `high` |
| E4 · Rất cao | `xhigh` (dành `max` cho trường hợp đặc biệt, phải ghi lý do) |

Lưu ý:
- Mỗi model có effort mặc định riêng; ví dụ Opus 5.5 mặc định `medium`. Vì vậy **luôn khai báo `effort` tường minh**, không dựa vào mặc định.
- Hạ effort trên model mạnh thường tốt hơn chuyển xuống model yếu với effort cao. Hãy đo trên Task thật trước khi đổi bảng.

## 2. Phiên Orchestrator

Mở phiên chính ở mức của Orchestrator ([model-effort](../../workflows/model-effort.md) §1):

```text
/model opus
/effort high       # xhigh nếu Plan có Task T7 (đổi kiến trúc hoặc API contract)
```

Fast lane (một Task R1): mở phiên ở mức bắt đầu của Task theo Skill chính (model-effort §2), ví dụ `documentation` → `/model sonnet` + `/effort low`.

Lệnh `/effort` và trường `effort` phụ thuộc phiên bản Claude Code; bản không hỗ trợ thì chỉnh qua `/model` hoặc `/config`.

## 3. Chạy Task theo manifest

Đã kiểm chứng trên Claude Code 2.1.326 (2026-11-18, chạy thử bằng `claude -p`):
- `claude -p` (không tương tác) nhận `--model`, `--effort`, `--output-format json`. Kết quả JSON có `total_cost_usd`, `modelUsage` (model thật đã dùng, token, chi phí): đủ để ghi `runs.md`.
- `--max-budget-usd` chặn chi phí **chỉ khi chạy với `-p`/`--print`**, và tính cho một lần gọi. Đặt bằng ngân sách còn lại của Task (model-effort §3 quy tắc 6), không phải cả ngân sách.
- `--agents '<json>'` khai báo subagent ngay khi gọi. Đã xác nhận trường `model`: subagent `model: haiku` dưới phiên Opus, `modelUsage` ghi cả hai model. **Chưa xác nhận trường `effort`** trong JSON này có được áp dụng không (JSON trả về không ghi effort).
- Không có cờ giới hạn token đầu ra: `max_output_tokens` của manifest ghi "không áp dụng" trong Run.
- Chưa xác nhận: gọi công cụ Agent từ phiên tương tác có đổi được model, effort cho từng lần gọi không. Vì vậy cách chắc chắn là một trong hai cách dưới.
- Chỉ dùng cho Task "Gửi đi" (A3, A4). Task A2 trở xuống chạy "Có người": người mở phiên tương tác bằng `claude --model <model> --effort <mức>` theo manifest, phiên dừng sau mỗi bước chờ duyệt.

**Cách A: subagent theo vai × mức** (`.claude/agents/<vai>-<mức>.md`), Orchestrator gọi trong phiên tương tác. Mỗi mức dùng trong thang nâng cấp cần một file; tên mức viết thường không dấu chấm: `m2-e1`. Cách này không có cờ chặn chi phí: Orchestrator đọc chi phí sau mỗi lần chạy và dừng khi chạm ngân sách. Trường `effort` trong frontmatter phụ thuộc phiên bản; kiểm tra trước khi dùng. Chạy song song nhiều subagent thì mỗi subagent làm trong worktree riêng của Task.

`.claude/agents/executor-m2-e1.md`:

```markdown
---
name: executor-m2-e1
description: Chạy một Task vai Executor ở mức M2·E1 theo Task Manifest. Chỉ dùng khi manifest ghi agent executor và mức hiện tại M2·E1.
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

Vai không cần nâng mức (Reviewer, Security, tra cứu) dùng một file mỗi vai, mức theo model-effort §2. Nội dung file chỉ trỏ về `.ai/`, không chép Rule hay Skill vào.

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
Nạp .ai/skills/security-review/SKILL.md. Không đưa secret hoặc dữ liệu D3 vào ngữ cảnh.
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

Chỉ đọc và báo cáo (A1). Trả về đường dẫn file:dòng và kết luận; không dán nguyên nội dung file.
```
