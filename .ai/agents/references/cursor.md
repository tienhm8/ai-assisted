# Model và effort cho Cursor

> Dùng khi phiên chạy trong Cursor. **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu. Cột "Model · Effort" theo loại Task nằm ở [task-types.md](../../workflows/task-types.md) §1.
> Dùng model do Cursor cung cấp (Composer, Grok), như Claude Code dùng họ Claude. Tài liệu cursor.com/docs/models không xếp hạng chất lượng; phân hạng dưới đây suy từ giá theo token (Composer 2.5 rẻ nhất, Grok 4.7 đắt nhất), nên Tech Lead đo trên Task thật trước khi chốt. Model đổi thường xuyên, kiểm tra lại trước khi áp dụng (cập nhật: 2026-11).

## 1. Ánh xạ hạng → model, mức → effort

| Hạng / mức khung | Model hoặc tham số thật |
| --- | --- |
| M1 · Nhẹ | Composer 2.5 |
| M2 · Chuẩn | Grok 4.6 |
| M3 · Mạnh | Grok 4.7 |
| E1–E4 | Không áp dụng: chỉ chọn model theo hạng M1–M3, bỏ qua mức effort |

Lưu ý:
- Chọn model **thủ công** trong model picker của chat/agent trước khi bắt đầu phiên; không dùng chế độ tự chọn (Auto) cho Task cần hạng tối thiểu theo [model-effort.md](../../workflows/model-effort.md).
- Chưa xác nhận được cách đặt model hay effort mặc định cho repo qua `.cursor/rules`. Không giả định có.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Vai (agent)

Cursor không dùng `.claude/agents`. Vai Reviewer, Security: mở phiên mới, chọn hạng theo dòng T9, mở đầu bằng "Bạn giữ vai Reviewer trong .ai/agents/README.md. Nạp .ai/skills/code-review/SKILL.md." (tương tự cho Security với `security-review`).
