# .ai — Nguồn chuẩn Rule và Skill

Nguồn chuẩn, độc lập công cụ cho Rule, Skill, Agent, Workflow. Thư mục này đổi tên theo công cụ chính (ví dụ Claude Code: `.claude/`), xem [glossary](../docs/00-project-overview/glossary.md). File tích hợp của từng công cụ (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, …) chỉ trỏ về đây.

| Thư mục | Nội dung |
| --- | --- |
| [rules/](rules/) | Quy tắc AI phải tuân thủ |
| [skills/](skills/) | Mỗi Skill một thư mục có `SKILL.md` |
| [agents/](agents/) | Vai/agent (Planner, Executor, Tester, Reviewer…) |
| [workflows/](workflows/) | Chọn Skill theo Task, cổng vào/ra, bàn giao |
| [templates/](templates/) | Mẫu Plan, Bug, PR, các Report |
| [plans/](plans/) | Plan do AI soạn (commit) |
| [worktrees/](worktrees/) | Git worktree của AI (không commit) |

Sửa `.ai/` cần Task riêng và người duyệt; AI chỉ đề xuất, không tự sửa.
