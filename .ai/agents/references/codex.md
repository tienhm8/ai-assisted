# Model và effort cho Codex (ChatGPT)

> Dùng khi phiên chạy trong OpenAI Codex (CLI, IDE extension, app, web), công cụ code của ChatGPT. **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu. Mức mặc định theo Skill nằm ở [model-effort.md](../../workflows/model-effort.md) §2.
> Phân hạng theo mô tả trong tài liệu models của Codex (learn.chatgpt.com/docs/models). Model và tên tham số đổi theo phiên bản Codex; kiểm tra lại trước khi áp dụng (cập nhật: 2026-11).

## 1. Ánh xạ hạng → model, mức → effort

| Hạng / mức khung | Model hoặc tham số thật |
| --- | --- |
| M1 · Nhẹ | `gpt-6-luna` (hiệu quả nhất, cho việc nhỏ, số lượng lớn) |
| M2 · Chuẩn | `gpt-6.1-terra` (nhanh, hiệu quả; cần Codex CLI 0.159.0 trở lên) |
| M3 · Mạnh | `gpt-6.1-sol` (gần Astra, chi phí thấp hơn, cho việc dài và lặp lại) |
| M3+ (tuỳ chọn, chi phí cao) | `gpt-6-astra`: chỉ cho việc rất khó khi Tech Lead cho phép |
| E1 · Thấp | `low` (giao diện: Light hoặc Low) |
| E2 · Trung bình | `medium` |
| E3 · Cao | `high` |
| E4 · Rất cao | Extra High (chọn qua `/model`; giá trị trong `config.toml` chưa xác nhận, thường là `xhigh`) |

Lưu ý:
- Max và Ultra (Ultra dùng subagent chạy song song) chỉ dành cho trường hợp đặc biệt, phải ghi lý do. `gpt-6-luna` hỗ trợ Max nhưng không hỗ trợ Ultra.
- Luôn khai báo model và effort tường minh, không dựa vào mặc định.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.
- Chưa kiểm chứng Terra ở M2 cho việc code thường ngày: tài liệu mô tả Terra mạnh ở viết, hiểu hình ảnh, computer use. Đo trên Task thật; nếu kém thì dùng `gpt-6.1-sol` với effort `medium`.

## 2. Phiên chính

```text
codex --model gpt-6.1-sol          # phiên Orchestrator, M3
/model                              # đổi model hoặc effort trong phiên; chọn "More reasoning…" cho Max/Ultra
```

Mỗi Run một phiên mới, chọn model, effort theo mức hiện tại của manifest (profile ở §3 giúp đổi nhanh, ví dụ một profile cho mỗi mức `m2-e1`, `m3-e3`).

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
