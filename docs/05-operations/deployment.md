# Deployment

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | monitoring.md, backup-recovery.md |

> **Mục đích.** Environment Configuration, CI/CD, phát hành, rollback. **Người quyết phát hành: Owner (tham khảo Tech Lead).** Điều kiện: smoke test đạt, không có sự cố nghiêm trọng trong khung theo dõi, rollback dùng được. AI không tự deploy production.

## 1. Environment Configuration
| Môi trường | Mục đích | Dữ liệu | Truy cập | Cấu hình/biến môi trường (không ghi giá trị secret) |
| --- | --- | --- | --- | --- |
|  | | | | |

## 2. CI/CD
- Pipeline: các bước build · lint · type-check · test · security scan · deploy:
- Cổng bắt buộc và bảo vệ nhánh:

## 3. Quy trình phát hành
Luồng chuẩn: merge vào main → Staging → UAT / Regression → Production. AI không tự merge, không tự deploy production, không truy cập production database nếu chưa có cơ chế được phê duyệt (xem [coding-standards](../03-engineering/coding-standards.md) §5.1).

Chi tiết từng bước:

## 4. Rollback
<!-- Điền theo từng dự án -->

## 5. Người quyết phát hành
AI không tự deploy production.
