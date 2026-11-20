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
├── open-questions.md
└── sources/          tài liệu đầu vào từ khách hàng, PO (SRC-<NN>)
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu |
| [vision.md](vision.md) | Vấn đề cần giải quyết, đối tượng dùng, đầu ra giai đoạn 1 |
| [scope.md](scope.md) | Ranh giới dự án: trong phạm vi, ngoài phạm vi, ràng buộc |
| [glossary.md](glossary.md) | Thuật ngữ thống nhất cho người và AI; AI không tự đặt nghĩa mới |
| [open-questions.md](open-questions.md) | Sổ chung: câu hỏi cấp dự án và mục lục mọi câu hỏi mở, giả định, đầu vào còn thiếu (`OQ-<NN>`); câu hỏi của Module, Feature nằm ở sổ con trong `01-requirements/FR/`; tài liệu khác chỉ trỏ tới mã |
| [sources/](sources/README.md) | Tài liệu đầu vào từ khách hàng, PO, bên liên quan (`SRC-<NN>`), đã ẩn danh; câu trả lời làm rõ cũng lưu ở đây |

## Thứ tự đọc và quan hệ

`sources` → `vision` → `scope` → `glossary` → `open-questions` (cập nhật xuyên suốt khi phát sinh điểm chưa rõ).

Đầu ra: là đầu vào của [01-requirements](../01-requirements/) (BRD, Epic/Feature, User Story, FR, NFR, business rules). Điểm chưa rõ ghi vào đúng sổ (xem `open-questions.md`), không tự đoán.
