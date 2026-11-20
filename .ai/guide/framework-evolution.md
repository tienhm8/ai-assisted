# Quan hệ hai chiều: Project, Framework và bên ngoài

> Dành cho người; AI không nạp khi làm Task. Skill `continuous-improvement` là nơi AI thực hiện các bước dưới đây.

Framework quy định cách làm, trung lập công nghệ. Project (ví dụ `project/aisoft-backend`) cung cấp chuẩn và nền tảng kỹ thuật để thực hiện cách làm đó. Hai luồng giữ cho Framework tiến hoá mà không bị gắn vào một công nghệ.

```text
Bên ngoài (công nghệ, model AI, skill, tool, thư viện, pattern)
      │ N2: đánh giá định kỳ
      ▼
Framework  ◄── N1: đề xuất, qua cổng duyệt ──  Project (aisoft-backend, project tiếp theo)
      │ áp dụng                                    ▲
      └────────────────────────────────────────────┘
```

## N1. Project đề xuất lên Framework

Mọi Project ghi nhận bài học khi triển khai và đề xuất cải tiến Framework. Project không tự sửa lõi Framework.

1. **Ghi nhận:** bài học ghi vào bảng "Hành động cải tiến" của [ai-kpi](../../docs/04-project-management/ai-kpi.md) §6, cột "Cấp" chọn `Framework` hoặc `Project`. Mỗi dòng có bằng chứng (Run, báo cáo bàn giao, lỗi, review).
2. **Phân loại** (làm ở Skill `continuous-improvement`, bước 6):

   | Bài học | Cấp | Đưa vào |
   | --- | --- | --- |
   | Đúng cho mọi project, không nhắc tên công nghệ | `Framework` | Rule, Skill (`SKILL.md`), workflow, template, guide |
   | Riêng một công nghệ hoặc phiên bản | `Project` | `references/<công-nghệ>.md`, chuẩn của project ở `docs/`, `ai-config.yaml` |
   | Điều bắt buộc của project | `Project` | `docs/03-engineering/` |

3. **Cổng duyệt** trước khi một dòng cấp `Framework` thành thay đổi: (a) trung lập công nghệ? (b) có bằng chứng? (c) người duyệt vùng `.ai/` chốt (Tech Lead, CHECKLIST mục 11). Thiếu một điều thì giữ ở cấp `Project`.
4. **Thực hiện:** mỗi đề xuất đã duyệt là một Task riêng sửa `.ai/` (vùng 🔴, cần reviewer), theo loại `periodic-review` ở [task-types](../workflows/task-types.md).

## N2. Bên ngoài vào Framework và Project

Framework và Project định kỳ đánh giá thứ mới từ bên ngoài. Thứ bên ngoài chỉ là tài liệu tham khảo.

- **Kỳ đánh giá:** cuối mỗi Plan, và khi có thay đổi lớn (ví dụ model AI mới, nâng phiên bản chính của framework hay ORM project đang dùng).
- **Đối tượng:** công nghệ và phiên bản trong `stack`; model và effort trong `ai-config.yaml`; skill và guideline bên ngoài; tool; pattern.
- **Cách làm:** ghi kết quả vào bảng "Đánh giá bên ngoài" ở [ai-kpi](../../docs/04-project-management/ai-kpi.md) §6. Thử trong **một Project** trước. Có bằng chứng thì đưa lên Framework qua N1.
- **Skill bên ngoài:** tiếp nhận theo [external-skills.md](external-skills.md). Rà lại reference với phiên bản đang dùng theo bước 6 của file đó.
- **Reference theo phiên bản:** đầu file ghi "Áp dụng cho" (nguồn ghi ở PR). Nếu công nghệ có nhiều phiên bản chính mà project dùng một, ghi một mục "Version notes" (§0) nêu điều không áp dụng cho phiên bản đó; xem `nestjs-11.md`, `redis.md`, `postgresql.md` trong `.ai/skills/*/references/`.
