# .ai — Nguồn chuẩn Rule và Skill

Đây là **nguồn chuẩn, độc lập công cụ** cho Rule, Skill, Agent và Workflow. Không đổi tên theo công cụ. Mỗi công cụ có file tích hợp mỏng (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, …) chỉ tham chiếu tới đây, không chép lại nội dung. Công cụ cần vị trí riêng (`.claude/skills/`, `.cursor/rules/`) thì dùng symlink hoặc script đồng bộ sinh từ thư mục này. Xem README gốc, mục "Công cụ AI".

| Thư mục | Nội dung |
| --- | --- |
| [rules/](rules/) | Quy tắc AI phải tuân thủ (Core, Project) |
| [skills/](skills/) | 17 Skill, mỗi Skill một thư mục có `SKILL.md` |
| [agents/](agents/) | Định nghĩa vai/agent (Planner, Executor, Tester, Reviewer…) |
| [workflows/](workflows/) | Điều phối Skill (chọn Skill theo Task, cổng vào/ra, bàn giao) và quy trình nhiều bước |
| [templates/](templates/) | Mẫu Bug, Code Review, Test Report, Release Report |
| [plans/](plans/) | Lưu các plan; file plan mới được commit (giữ thư mục bằng `.gitkeep`) |
| [worktrees/](worktrees/) | Git worktree của AI; nội dung **không** commit (đã ignore trong `.gitignore`, chỉ giữ `.gitkeep`) |

Ghi chú:
- **Kiểm soát thay đổi:** sửa `.ai/` cần Task riêng và người duyệt; AI chỉ đề xuất qua kênh đề xuất riêng. Mức tự chủ, bản đồ vùng và dữ liệu D0–D3 được định nghĩa trong [PROJECT.md](../PROJECT.md) mục 3–4.
- Bản ghim từ tổ chức (`core/`, `packs/`, `adapters/`) thuộc vùng 🔴, không sửa tay; chưa tạo vì chưa chọn stack.
- `plans/` được commit; `worktrees/` **không** commit, đã khai báo trong `.gitignore` gốc.
