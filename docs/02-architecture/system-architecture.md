# System Architecture

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | module-design.md, ADR/, ../03-engineering/security-standards.md |

> **Mục đích.** Kiến trúc tổng thể, ranh giới, chiều phụ thuộc, tích hợp ngoài, thiết kế Authentication & Authorization. **Người quyết: Kiến trúc sư (thêm Security nếu rủi ro R3).** Điều kiện sẵn sàng build: thiết kế Approved, có ADR cho quyết định lớn. **Chưa đạt thì không code tính năng.**

## 1. Bối cảnh hệ thống (actor, hệ thống ngoài)
<!-- Điền theo từng dự án -->

## 2. Thành phần chính và ranh giới
<!-- Điền theo từng dự án -->

## 3. Stack và phiên bản
| Lớp | Công nghệ | Phiên bản |
| --- | --- | --- |
|  | | |

## 4. Luồng dữ liệu chính
<!-- Điền theo từng dự án -->

## 5. Threat model (bắt buộc khi có R3 / S3)
Ai làm được gì, lạm dụng thế nào, chặn bằng gì.

## 6. Authentication & Authorization (thiết kế)
Cơ chế xác thực, mô hình phân quyền (vai trò, quyền, phạm vi dữ liệu), vòng đời phiên/token. Quy tắc bắt buộc ở [security-standards](../03-engineering/security-standards.md) §2.
<!-- Điền theo từng dự án -->

## 7. Quyết định liên quan
Liệt kê `ADR-<NNNN>` tại [ADR/](ADR/).
