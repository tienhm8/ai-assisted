# Model và effort cho GitHub Copilot

> Dùng khi phiên chạy trong GitHub Copilot (VS Code, cloud agent). **§1 là bảng ánh xạ** mà [model-effort.md](../../workflows/model-effort.md) tham chiếu. Cột "Model · Effort" theo loại Task nằm ở [task-types.md](../../workflows/task-types.md) §1.
> Dùng họ GPT (OpenAI) của Copilot, như Claude Code dùng họ Claude. Phân hạng dựa trên mô tả trong tài liệu "Model comparison" của GitHub: Luna nhanh, chi phí thấp; Terra cân bằng cho việc hằng ngày; Sol cho tác vụ code phức tạp. Danh sách model phụ thuộc gói và thay đổi theo thời gian; đối chiếu "Supported models" trước khi áp dụng (cập nhật: 2026-11).

## 1. Ánh xạ hạng → model, mức → effort

| Hạng / mức khung | Model hoặc tham số thật |
| --- | --- |
| M1 · Nhẹ | GPT-6 Luna |
| M2 · Chuẩn | GPT-6.1 Terra |
| M3 · Mạnh | GPT-6.1 Sol |
| E1–E4 | Không áp dụng: chỉ chọn model theo hạng M1–M3, bỏ qua mức effort |

Lưu ý:
- Không dùng Auto cho Task cần hạng tối thiểu: chọn model tường minh. Nơi không có model picker (một số điểm vào của cloud agent), Copilot tự dùng Auto; Task cần M3 thì không chạy ở đó.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Agent theo vai (`.github/agents/*.agent.md`)

Frontmatter `model` nhận một tên hoặc một mảng ưu tiên (dùng model đầu tiên có sẵn). Bỏ trống thì dùng model đang chọn; cloud agent thì dùng model mặc định. Vì vậy **luôn khai báo `model`** cho agent vai Reviewer/Security. Nội dung chỉ trỏ về `.ai/`.

```markdown
---
name: reviewer
description: Review độc lập diff của Task theo Skill code-review. Dùng sau khi Executor bàn giao.
model: GPT-6.1 Sol
tools: ['read', 'search']
---

Bạn giữ vai Reviewer trong .ai/agents/README.md.
Nạp .ai/skills/code-review/SKILL.md và làm theo đúng quy trình trong đó.
Chỉ báo phát hiện có mức độ và file:dòng; không sửa code.
```

Tên trường `tools` và định dạng khác nhau giữa VS Code và cloud agent; đối chiếu tài liệu "Custom agent file reference" trước khi áp dụng.
