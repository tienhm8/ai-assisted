# Model và effort cho Claude Code

> Dùng khi dự án chọn Claude Code ([ai-tools.md](../../../docs/03-engineering/ai-tools.md) §3). **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu khi phiên chạy trong Claude Code: hạng M1–M3 → model, mức E1–E4 → `effort`. Cột "Model · Effort" theo loại Task nằm ở [task-types.md](../../workflows/task-types.md) §1. Các mục còn lại (§2–§3) chỉ là ví dụ cấu hình, không bắt buộc.
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

## 2. Phiên chính

Chọn theo cột "Model · Effort" của dòng loại Task (task-types §1). Lệnh cho phiên plan (bước 1–4):

| Model · Effort phiên plan | Lệnh trong Claude Code | Loại Task |
| --- | --- | --- |
| M3·E4 | `/model opus` + `/effort xhigh` | T7(Đổi kiến trúc hoặc API contract) |
| M3·E3 | `/model opus` + `/effort high` | T1(Tính năng mới), T2(Làm tính năng), T5(Đổi schema), T9(Review PR), T10(Kiểm tra bảo mật), T14(Sự cố production) |
| M2·E3 | `/model sonnet` + `/effort high` | T3(Sửa lỗi), T4(Refactor), T6(Đổi yêu cầu) |
| M2·E2 | `/model sonnet` + `/effort medium` | T8(Rà soát tài liệu yêu cầu), T11(Chỉ viết test), T12(Chỉ sửa tài liệu), T13(Phát hành), T15(Rà soát định kỳ) |

Ví dụ T2 (làm tính năng đã có yêu cầu, thiết kế): phiên plan M3·E3, phiên thực thi M2·E2:

```text
/model opus        # phiên plan (bước 1–4)
/effort high

/model sonnet      # phiên thực thi (bước 5–7), mở phiên mới với plan đã duyệt
/effort medium
```

Lệnh `/effort` và trường `effort` trong frontmatter phụ thuộc phiên bản Claude Code. Phiên bản không hỗ trợ thì chỉnh effort qua `/model` hoặc `/config`.

Đặt mặc định cho repo trong `.claude/settings.json`:

```json
{
  "model": "sonnet"
}
```

## 3. Subagent theo vai (`.claude/agents/*.md`)

Mỗi vai cần tách agent riêng (xem mục "Khi nào mới tách thành agent riêng" trong [README](../README.md)) được khai báo bằng một file. Frontmatter `model` và `effort` lấy theo hạng của bước mà subagent đảm nhiệm (ví dụ Reviewer = bước 8 = dòng T9). Nội dung file chỉ trỏ về `.ai/`, không chép Rule hay Skill vào.

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
