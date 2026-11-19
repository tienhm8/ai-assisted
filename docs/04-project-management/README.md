# 04-project-management

> **Mục đích:** Hướng dẫn quản lý kế hoạch và công việc: cách sử dụng, phạm vi và mối quan hệ giữa các tài liệu
>
> **Người quyết: Tech Lead** (chia Task, mức rủi ro, mức tự chủ AI); Product Owner quyết thứ tự ưu tiên và lộ trình.
>
> **Điều kiện giao việc cho AI:** Task có đủ Objective, Scope in/out, AC, mức rủi ro R1–R3 và mức tự chủ A0–A4, bám theo FR đã duyệt. **Chưa đạt thì không giao AI code.**

## Cấu trúc

```text
04-project-management/
├── README.md
├── roadmap.md
├── goals.md
├── product-backlog.md
├── task-backlog.md
└── ai-kpi.md
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn quản lý kế hoạch và công việc, phạm vi và mối quan hệ giữa các tài liệu |
| [roadmap.md](roadmap.md) | Lộ trình phát triển theo mốc: dự án sẽ phát triển những gì, theo thứ tự nào |
| [goals.md](goals.md) | Goal: kết quả muốn đạt (Desired Outcome) |
| [product-backlog.md](product-backlog.md) | Epic và User Story, kèm ưu tiên |
| [task-backlog.md](task-backlog.md) | Danh sách Task cần thực hiện, kèm ưu tiên và rủi ro |
| [ai-kpi.md](ai-kpi.md) | Chỉ số, baseline và kết quả đo hiệu quả của AI trong phát triển |

## Thứ tự đọc và quan hệ

`roadmap` → `goals` → `product-backlog` → `task-backlog` → `ai-kpi` (đo kết quả của toàn bộ chu trình).

Khái niệm, chia Task, cổng duyệt và độ nghiêm ngặt (`work-model`, `task-breakdown`, `gates-and-rigor`) nằm ở [.ai/guide/](../../.ai/guide/README.md).

Đầu vào: [01-requirements](../01-requirements/) (FR, business rules) và [scope](../00-project-overview/scope.md). Roadmap, product-backlog và task-backlog chỉ tham chiếu FR/BR, không chép trạng thái hoàn thành FR. Task truy vết về User Story/FR qua cột Phục vụ; thiết kế liên quan nằm ở [02-architecture](../02-architecture/). KPI đối chiếu với [testing-strategy](../03-engineering/testing-strategy.md) và [monitoring](../05-operations/monitoring.md).
