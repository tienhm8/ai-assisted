# 05-operations

> **Mục đích:** Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu Operations (triển khai, giám sát, sao lưu/khôi phục)
>
> **Người quyết phát hành: Owner** (tham khảo Tech Lead; thêm Security nếu đụng tới secret, phân quyền, dữ liệu cá nhân, backup dữ liệu).
>
> **Điều kiện phát hành:** smoke test đạt, không có sự cố nghiêm trọng trong khung theo dõi, rollback dùng được. **AI không tự deploy production.**

## Cấu trúc

```text
05-operations/
├── README.md
├── deployment.md
├── gitflow.md
├── monitoring.md
└── backup-recovery.md
```

## Vai trò từng file

| File | Mục đích |
| --- | --- |
| `README.md` | Hướng dẫn sử dụng, phạm vi và mối quan hệ giữa các tài liệu |
| [deployment.md](deployment.md) | Triển khai hệ thống: môi trường, CI/CD, quy trình phát hành, rollback |
| [gitflow.md](gitflow.md) | Quy trình nhánh Gitflow (nvie): nhánh, nhịp phát hành, luồng ví dụ release/hotfix |
| [monitoring.md](monitoring.md) | Giám sát, log, cảnh báo và ngưỡng sự cố |
| [backup-recovery.md](backup-recovery.md) | Sao lưu, khôi phục, RPO/RTO, diễn tập |

## Nguyên tắc sử dụng

Các file là **template dùng chung cho mọi dự án**: nội dung mô tả cấu trúc, yêu cầu và quy tắc cần có. Khi áp dụng vào một dự án cụ thể, điền công nghệ, môi trường, endpoint, lịch chạy, thông số và người phụ trách. Không ghi giá trị secret vào tài liệu.

## Thứ tự đọc và quan hệ

`deployment` → `monitoring` → `backup-recovery` (sau khi triển khai thì theo dõi, rồi bảo vệ và khôi phục dữ liệu).

Đầu vào: [NFR](../01-requirements/NFR.md) (ngưỡng hiệu năng, sẵn sàng, RPO/RTO), [system-architecture](../02-architecture/system-architecture.md) và [database-design](../02-architecture/database-design.md) (thành phần và dữ liệu cần triển khai/sao lưu), [coding-standards](../03-engineering/coding-standards.md) và [security-standards](../03-engineering/security-standards.md) (quy tắc AI và bảo mật khi deploy).
