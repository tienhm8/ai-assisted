# Model và effort cho Codex (ChatGPT)

> Dùng khi phiên chạy trong OpenAI Codex (CLI, IDE extension, app, web), công cụ code của ChatGPT. **§1 là khối `sessions`/`tasks`** của Codex: đổi công cụ sang Codex thì chép khối này vào [ai-config.yaml](../../../ai-config.yaml); quy tắc chọn mức nằm ở [model-effort.md](../../workflows/model-effort.md).
> Phân hạng theo mô tả trong tài liệu models của Codex (learn.chatgpt.com/docs/models). Model và tên tham số đổi theo phiên bản Codex; kiểm tra lại trước khi áp dụng (cập nhật: 2026-11).

## 1. Model và effort theo loại việc

Model: `gpt-6-luna` (hiệu quả nhất, cho việc nhỏ, số lượng lớn) thay cho `haiku`; `gpt-6.1-terra` (nhanh, hiệu quả; cần Codex CLI 0.159.0 trở lên) thay cho `sonnet`; `gpt-6.1-sol` (gần Astra, chi phí thấp hơn, cho việc dài và lặp lại) thay cho `opus`. Effort: `low` (giao diện: Light hoặc Low), `medium`, `high`, `xhigh` (giao diện: Extra High; chọn qua `/model`, giá trị trong `config.toml` chưa xác nhận, thường là `xhigh`).

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
- `gpt-6-astra` (chi phí cao) chỉ cho việc rất khó khi người phát triển khung hoặc Tech Lead cho phép; không nằm trong khối.
- Max và Ultra (Ultra dùng subagent chạy song song) chỉ dành cho trường hợp đặc biệt, phải ghi lý do. `gpt-6-luna` hỗ trợ Max nhưng không hỗ trợ Ultra.
- Luôn khai báo model và effort tường minh, không dựa vào mặc định.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.
- Chưa kiểm chứng Terra ở vai `sonnet` (model chuẩn) cho việc code thường ngày: tài liệu mô tả Terra mạnh ở viết, hiểu hình ảnh, computer use. Đo trên Task thật; nếu kém thì dùng `gpt-6.1-sol` với effort `medium`.

## 2. Phiên chính

```text
codex --model gpt-6.1-sol          # phiên Orchestrator
/model                              # đổi model hoặc effort trong phiên; chọn "More reasoning…" cho Max/Ultra
```

Mỗi Run một phiên mới, chọn model, effort theo mức hiện tại của manifest (profile ở §3 giúp đổi nhanh, ví dụ một profile cho mỗi mức dùng trong `try`, như `terra-low`, `sol-high`).

Mặc định cho repo trong `.codex/config.toml` (chỉ nạp với project đã tin cậy):

```toml
model = "gpt-6.1-terra"
model_reasoning_effort = "medium"
```

## 3. Vai theo profile

Profile đọc từ `~/.codex/<tên>.config.toml` và chọn bằng `--profile <tên>`; chỉ đặt giá trị khác mặc định. Ví dụ `~/.codex/reviewer.config.toml`:

```toml
model = "gpt-6.1-sol"
model_reasoning_effort = "high"
```

```text
codex --profile reviewer
```

Mở đầu phiên: "Bạn giữ vai Reviewer trong .ai/agents/README.md. Nạp .ai/skills/code-review/SKILL.md." (tương tự Security với `security-review`). Chưa xác nhận Codex có file subagent khai báo theo repo như `.claude/agents`; không giả định có.

**Chạy Task theo manifest:** chưa xác nhận Codex có subagent khai báo được model theo repo, nên Orchestrator không tự gửi Task. Orchestrator soạn manifest và câu mở phiên cho từng Run; người mở phiên mới, chọn model theo mức hiện tại của manifest, dán câu mở phiên, rồi đưa báo cáo bàn giao về phiên Orchestrator để đánh giá. Nâng mức: mở phiên mới ở bậc kế.
