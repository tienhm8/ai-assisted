# Model và effort cho GitHub Copilot

> Dùng khi phiên chạy trong GitHub Copilot (Copilot CLI, VS Code, cloud agent). **§1 là khối `sessions`/`tasks`** của Copilot: đổi công cụ sang Copilot thì chép khối này vào [ai-config.yaml](../../../ai-config.yaml); quy tắc chọn mức nằm ở [model-effort.md](../../workflows/model-effort.md).
> Dùng họ GPT (OpenAI) của Copilot, như Claude Code dùng họ Claude. Phân hạng dựa trên mô tả trong tài liệu "Model comparison" của GitHub: Luna nhanh, chi phí thấp; Terra cân bằng cho việc hằng ngày; Sol cho tác vụ code phức tạp. Copilot cũng cung cấp họ Claude, Gemini, Grok; dự án đổi họ model thì đối chiếu bảng tương ứng ([claude-code.md](claude-code.md) §1).
> Đã kiểm chứng với Copilot CLI 1.0.112 (`copilot --help`, `copilot help config`, `copilot help commands`), 2026-11-17. Danh sách model phụ thuộc gói và thay đổi theo thời gian; VS Code và cloud agent chưa kiểm chứng.

## 1. Model và effort theo loại việc

Model: `gpt-6-luna` thay cho `haiku`; `gpt-6.1-terra` thay cho `sonnet`; `gpt-6.1-sol` thay cho `opus`. Effort: `low`, `medium`, `high`, `xhigh`.

```yaml
sessions:
  orchestrator: gpt-6.1-sol/high      # Plan có đổi kiến trúc: gpt-6.1-sol/xhigh
  review:       gpt-6.1-sol/high
tasks:
  - for: [lookup]
    try: [gpt-6-luna/low, gpt-6.1-terra/medium]
  - for: [documentation]
    try: [gpt-6.1-terra/low, gpt-6.1-terra/high]
  - for: [unit-testing, integration-testing, e2e-testing]
    try: [gpt-6.1-terra/low, gpt-6.1-terra/high, gpt-6.1-sol/high]
  - for: [backend-development, api-development, frontend-development]
    try: [gpt-6.1-terra/low, gpt-6.1-terra/high, gpt-6.1-sol/high]
  - for: [refactoring, caching, deployment, requirement-review, continuous-improvement]
    try: [gpt-6.1-terra/medium, gpt-6.1-sol/medium, gpt-6.1-sol/high]
  - for: [bug-fixing]
    try: [gpt-6.1-terra/medium, gpt-6.1-sol/high, gpt-6.1-sol/xhigh]
  - for: [product-discovery, requirement-analysis, architecture-design, database-design, task-planning, incident-analysis, code-review]
    try: [gpt-6.1-sol/high, gpt-6.1-sol/xhigh]
  - for: [authentication-rbac, security-review]
    try: [gpt-6.1-sol/high, gpt-6.1-sol/xhigh]
```

Lưu ý:
- `gpt-6-astra` (chi phí cao) chỉ cho việc rất khó khi người phát triển khung hoặc Tech Lead cho phép; không nằm trong khối. `max` dành cho trường hợp đặc biệt, phải ghi lý do.
- Effort chỉ xác nhận ở **Copilot CLI** (giá trị: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`; mức nào có tuỳ model). Không đặt thì dùng mặc định của model, thường là `medium`: **luôn khai báo tường minh**. VS Code và cloud agent chưa xác nhận có effort: ở đó chỉ áp dụng model, bỏ qua effort.
- Không dùng Auto (`auto`, hiển thị là Copilot Fusion) cho Task cần hạng tối thiểu: chọn model tường minh. Nơi không có model picker (một số điểm vào của cloud agent), Copilot tự dùng Auto; Task cần model mạnh (`gpt-6.1-sol`) thì không chạy ở đó.
- Không bật `continueOnAutoMode`: khi bị giới hạn tốc độ, Copilot tự chuyển sang Auto, tức tự hạ hạng.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Phiên chính (Copilot CLI)

```text
copilot --model gpt-6.1-sol --reasoning-effort high      # phiên Orchestrator
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

**Chạy Task theo manifest** (chỉ Task "Gửi đi", mức tự chủ `full-task`, `pre-approved`; Task `step-by-step` trở xuống thì người mở phiên tương tác `copilot --model <model> --reasoning-effort <mức>` trong worktree của Task và duyệt từng bước): chưa xác nhận khoá `subagents.agents.*` có hiệu lực ở cấp repo, nên cách chắc chắn là mỗi Run một lệnh không tương tác, đặt model và effort theo mức hiện tại của manifest:

```text
copilot -p "Run Task WS-3 theo .ai/plans/PLAN-002-dang-ky/tasks/WS-3.yaml. Làm theo AGENTS.md." --model gpt-6.1-terra --reasoning-effort low
```

Nâng mức: chạy lại với model, effort của bậc kế, kèm ghi chú lỗi của lần trước. Chưa xác nhận Copilot CLI có cờ chặn chi phí theo lần chạy: Orchestrator theo dõi `budget` và dừng khi vượt.
