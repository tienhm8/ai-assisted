# Công cụ AI

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người duyệt (dự án) | Tech Lead |
| Tài liệu liên quan | ../../AGENTS.md, ../../.ai/rules/security-rules.md, external-skills.md |

> **Mục đích.** Cách nối công cụ AI với `.ai/` và khai báo công cụ dự án dùng. AI không nạp file này khi làm Task.

## 1. Tích hợp

`.ai/` là nguồn duy nhất. Mỗi công cụ chỉ có file vào trỏ về `.ai/`, không chép nội dung. Đổi công cụ hoặc phiên bản thì chạy thử một Task.

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

Không đưa Rule vào `.claude/rules/`, `.cursor/rules/`: Rule không có `paths` nạp từ đầu mọi phiên; `paths` chỉ lọc theo file đang sửa, không theo loại Task như [task-execution](../../.ai/workflows/task-execution.md). Trên Windows cần `git config core.symlinks true`.

## 3. Công cụ dự án dùng

| Công cụ | Vai trò (chính / phụ) | Phiên bản | Dùng cho việc | Quyền được cấp (terminal, Git, browser, ...) |
| --- | --- | --- | --- | --- |
|  | | | | |

## 4. Công cụ cấp cho AI (MCP server, plugin)

Công cụ mà AI gọi được, ví dụ MCP server của Laravel Boost. Guideline đi kèm tiếp nhận theo [external-skills.md](external-skills.md). Tính năng ghi dữ liệu hoặc chạy code tuỳ ý (ví dụ tinker, câu query ghi) xếp vào vùng 🟡/🔴 ở [PROJECT.md](../../PROJECT.md) §2.2.

| Công cụ · phiên bản | Tính năng được dùng | Môi trường kết nối | Tính năng bị tắt / giới hạn | Người duyệt |
| --- | --- | --- | --- | --- |
|  | | | | |
