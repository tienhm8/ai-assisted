# Model và effort cho Gemini CLI

> Dùng khi phiên chạy trong Gemini CLI. **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu. Cột "Model · Effort" theo loại Task nằm ở [task-types.md](../../workflows/task-types.md) §1.
> Tên model theo tài liệu geminicli.com (cập nhật: 2026-11). Tài liệu đó chỉ nêu hai dòng Pro và Flash nên Gemini CLI chỉ có hai hạng thật: M1 và M2 dùng chung Flash. Tài liệu cũng ghi Gemini CLI đã được thay bằng Antigravity CLI từ 2026-06-18 và chưa tối ưu cho Gemini 4; nếu dự án dùng Antigravity CLI hoặc Gemini 4, đối chiếu lại bảng này.

## 1. Ánh xạ hạng → model, mức → effort

| Hạng / mức khung | Model hoặc tham số thật |
| --- | --- |
| M1 · Nhẹ | `gemini-3-flash-preview` |
| M2 · Chuẩn | `gemini-3-flash-preview` |
| M3 · Mạnh | `gemini-3-pro-preview` |
| E1–E4 | Không áp dụng: chỉ chọn model theo hạng M1–M3, bỏ qua mức effort |

Lưu ý:
- Thứ tự ưu tiên chọn model: cờ `--model` > biến môi trường `GEMINI_MODEL` > `model.name` trong `settings.json` > mặc định (Auto). **Không dùng Auto** cho Task cần hạng tối thiểu: đặt model tường minh.
- Đổi trong phiên bằng `/model`.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Mặc định cho repo

`.gemini/settings.json` (định dạng lồng nhau ở bản mới; bản cũ dùng chuỗi phẳng, kiểm tra theo phiên bản):

```json
{
  "model": { "name": "gemini-3-flash-preview" }
}
```

## 3. Vai (agent)

Mở phiên mới cho Reviewer/Security, chọn hạng theo dòng T9, mở đầu bằng "Bạn giữ vai Reviewer trong .ai/agents/README.md. Nạp .ai/skills/code-review/SKILL.md." (tương tự Security với `security-review`).
