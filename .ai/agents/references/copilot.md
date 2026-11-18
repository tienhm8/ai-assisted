# Model và effort cho GitHub Copilot

> Dùng khi phiên chạy trong GitHub Copilot (Copilot CLI, VS Code, cloud agent). **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu. Mức mặc định theo Skill nằm ở [model-effort.md](../../workflows/model-effort.md) §2.
> Dùng họ GPT (OpenAI) của Copilot, như Claude Code dùng họ Claude. Phân hạng dựa trên mô tả trong tài liệu "Model comparison" của GitHub: Luna nhanh, chi phí thấp; Terra cân bằng cho việc hằng ngày; Sol cho tác vụ code phức tạp. Copilot cũng cung cấp họ Claude, Gemini, Grok; dự án đổi họ model thì đối chiếu bảng tương ứng ([claude-code.md](claude-code.md) §1).
> Đã kiểm chứng với Copilot CLI 1.0.112 (`copilot --help`, `copilot help config`, `copilot help commands`), 2026-11-17. Danh sách model phụ thuộc gói và thay đổi theo thời gian; VS Code và cloud agent chưa kiểm chứng.

## 1. Ánh xạ hạng → model, mức → effort

| Hạng / mức khung | Model hoặc tham số thật |
| --- | --- |
| M1 · Nhẹ | `gpt-6-luna` |
| M2 · Chuẩn | `gpt-6.1-terra` |
| M3 · Mạnh | `gpt-6.1-sol` |
| M3+ (tuỳ chọn, chi phí cao) | `gpt-6-astra`: chỉ cho việc rất khó khi Tech Lead cho phép |
| E1 · Thấp | `low` |
| E2 · Trung bình | `medium` |
| E3 · Cao | `high` |
| E4 · Rất cao | `xhigh` (dành `max` cho trường hợp đặc biệt, phải ghi lý do) |

Lưu ý:
- Effort chỉ xác nhận ở **Copilot CLI** (giá trị: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`; mức nào có tuỳ model). Không đặt thì dùng mặc định của model, thường là `medium`: **luôn khai báo tường minh**. VS Code và cloud agent chưa xác nhận có effort: ở đó chỉ áp dụng hạng M1–M3.
- Không dùng Auto (`auto`, hiển thị là Copilot Fusion) cho Task cần hạng tối thiểu: chọn model tường minh. Nơi không có model picker (một số điểm vào của cloud agent), Copilot tự dùng Auto; Task cần M3 thì không chạy ở đó.
- Không bật `continueOnAutoMode`: khi bị giới hạn tốc độ, Copilot tự chuyển sang Auto, tức tự hạ hạng.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Phiên chính (Copilot CLI)

```text
copilot --model gpt-6.1-sol --reasoning-effort high      # phiên Orchestrator, M3·E3
/model                                                    # đổi model trong phiên; mũi tên trái/phải đổi effort
copilot -p "<prompt>" --model gpt-6.1-terra --reasoning-effort medium   # chạy không tương tác
```

Mặc định cho repo: `/model --repo` ghi vào `.github/copilot/settings.json` (khoá `model`, `effortLevel`). Plan mode có model riêng: `planModel`, `planEffortLevel` (không kế thừa effort của phiên).

## 3. Agent theo vai và subagent

**Custom agent** (`.github/agents/*.agent.md`): frontmatter `model` nhận một tên hoặc một mảng ưu tiên (dùng model đầu tiên có sẵn). Bỏ trống thì dùng model đang chọn; cloud agent thì dùng model mặc định. Vì vậy **luôn khai báo `model`** cho agent vai Reviewer/Security. Nội dung chỉ trỏ về `.ai/`. Chọn trong CLI bằng `--agent <tên>` hoặc `/agent`.

```markdown
---
name: reviewer
description: Review độc lập diff của Task theo Skill code-review. Dùng sau khi Executor bàn giao.
model: gpt-6.1-sol
tools: ['read', 'search']
---

Bạn giữ vai Reviewer trong .ai/agents/README.md.
Nạp .ai/skills/code-review/SKILL.md và làm theo đúng quy trình trong đó.
Chỉ báo phát hiện có mức độ và file:dòng; không sửa code.
```

**Model và effort của subagent** (Copilot CLI): đặt qua `subagents.agents.<tên-agent>` với các trường `model`, `effortLevel`, `contextTier`; giá trị `inherit` lấy theo phiên cha. Cấu hình bằng `/subagents`. Chưa xác nhận frontmatter custom agent nhận trường effort, và chưa xác nhận khoá `subagents` có hiệu lực ở settings cấp repo.

Tên trường `tools` và định dạng khác nhau giữa VS Code và cloud agent; đối chiếu tài liệu "Custom agent file reference" trước khi áp dụng.

**Chạy Task theo manifest** (chỉ Task "Gửi đi", A3, A4; Task A2 trở xuống thì người mở phiên tương tác `copilot --model <model> --reasoning-effort <mức>` trong worktree của Task và duyệt từng bước): chưa xác nhận khoá `subagents.agents.*` có hiệu lực ở cấp repo, nên cách chắc chắn là mỗi Run một lệnh không tương tác, đặt model và effort theo mức hiện tại của manifest:

```text
copilot -p "Run Task WS-3 theo .ai/plans/GOAL-01-P2-dang-ky/tasks/WS-3.yaml. Làm theo AGENTS.md." --model gpt-6.1-terra --reasoning-effort low
```

Nâng mức: chạy lại với model, effort của bậc kế, kèm ghi chú lỗi của lần trước. Chưa xác nhận Copilot CLI có cờ chặn chi phí theo lần chạy: Orchestrator theo dõi `budget` và dừng khi vượt.
