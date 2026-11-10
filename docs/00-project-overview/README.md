# 00-project-overview

> **Mục đích:** Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu
>
> **Người quyết: PO** (phần khung do Tech Lead).
>
> **Điều kiện sang 01-requirements:** vision, scope trạng thái Approved; câu hỏi mở chặn phạm vi đã được xử lý.

## Cấu trúc

```text
00-project-overview/
├── README.md
├── vision.md
├── scope.md
├── glossary.md
└── open-questions.md
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu |
| [vision.md](vision.md) | Vấn đề cần giải quyết, đối tượng dùng, đầu ra giai đoạn 1 |
| [scope.md](scope.md) | Ranh giới dự án: trong phạm vi, ngoài phạm vi, ràng buộc |
| [glossary.md](glossary.md) | Thuật ngữ thống nhất cho người và AI; AI không tự đặt nghĩa mới |
| [open-questions.md](open-questions.md) | Nơi duy nhất ghi câu hỏi mở và giả định (`OQ-<NN>`); tài liệu khác chỉ trỏ tới mã |

## Thứ tự đọc và quan hệ

`vision` → `scope` → `glossary` → `open-questions` (cập nhật xuyên suốt khi phát sinh điểm chưa rõ).

Đầu ra: là đầu vào của [01-requirements](../01-requirements/) (BRD, FR, NFR, business rules). Điểm chưa rõ ở mọi tài liệu ghi vào `open-questions.md`, không tự đoán.
