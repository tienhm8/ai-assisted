# Deployment

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt | Owner |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | monitoring.md, backup-recovery.md, ../02-architecture/system-architecture.md, ../02-architecture/database-design.md, ../01-requirements/NFR.md, ../../.ai/workflows/release-workflow.md, ../../.ai/skills/deployment/SKILL.md |

> **Mục đích.** Triển khai hệ thống: môi trường, CI/CD, phát hành, rollback. **Người quyết phát hành: Owner (tham khảo Tech Lead).** Điều kiện: smoke test đạt, không có sự cố nghiêm trọng trong khung theo dõi, rollback dùng được. AI không tự deploy production.
>
> Template dùng chung cho mọi dự án: điền công nghệ, môi trường, thông số và người phụ trách khi áp dụng. Không ghi giá trị secret.

## 1. Purpose
Phạm vi và đối tượng của tài liệu: hệ thống/thành phần được triển khai, ai đọc, khi nào dùng.

## 2. Deployment Overview
Tóm tắt cách hệ thống được triển khai: các thành phần chính, môi trường, mô hình triển khai (VM, container, serverless...), tần suất phát hành.

## 3. Environment Configuration
| Môi trường | Mục đích | Dữ liệu | Truy cập | Cấu hình/biến môi trường (không ghi giá trị secret) |
| --- | --- | --- | --- | --- |
|  | | | | |

## 4. Infrastructure Requirements
| Thành phần | Yêu cầu (CPU/RAM/lưu trữ/phiên bản) | Môi trường áp dụng | Ghi chú |
| --- | --- | --- | --- |
|  | | | |

Nguồn: [NFR](../01-requirements/NFR.md) (hiệu năng, sẵn sàng, khả năng mở rộng).

## 5. Deployment Architecture
Sơ đồ/mô tả topology triển khai: thành phần, mạng, cổng, luồng truy cập, dịch vụ phụ thuộc. Đối chiếu [system-architecture](../02-architecture/system-architecture.md).

## 6. Build and Release Process
### 6.1 CI/CD
- Pipeline: các bước build · lint · type-check · test · security scan · deploy:
- Cổng bắt buộc và bảo vệ nhánh:

### 6.2 Quy trình phát hành
Luồng chuẩn theo Gitflow: `feature/*` → `develop` (Dev) → cắt `release/X.Y.0` (Staging) → UAT / Regression → merge `master` + tag `vX.Y.0` (Production) → merge ngược `develop`. Lỗi nghiêm trọng: `hotfix/X.Y.Z` từ `master`. Quy tắc nhánh ở [git-workflow-rules](../../.ai/rules/git-workflow-rules.md); lệnh từng bước ở [gitflow-release](../../.ai/skills/deployment/references/gitflow-release.md).

**Nhịp phát hành** (mặc định khung; dự án điều chỉnh tại đây). Release cắt theo thời điểm chốt sprint, không theo lịch cứng.

| Môi trường | Tần suất | Nguồn deploy | Mục đích |
| --- | --- | --- | --- |
| Dev | Hằng ngày | `develop` | Tích hợp code mới |
| Staging | 1–2 lần/tuần | `release/*` (hoặc `develop` tạm khi cần kiểm trước khi cắt release) | QA, UAT, regression |
| Prod | 2 tuần/lần theo sprint | `master` (tag) | Phát hành tính năng mới |
| Hotfix | Khi cần | `hotfix/*` → `master` | Xử lý lỗi nghiêm trọng |

**Hotfix khẩn cấp** (áp dụng [release-workflow](../../.ai/workflows/release-workflow.md); giá trị do dự án khai báo):

| Hạng mục | Giá trị |
| --- | --- |
| Thời hạn bổ sung hồ sơ sau hotfix | |
| Người duyệt hotfix | |

- Artifact và đánh phiên bản (tag/version):
- Quy tắc đặt tên bản phát hành, changelog:

## 7. Deployment Procedure
Chi tiết từng bước triển khai (trước · trong · sau), người thực hiện, người duyệt, khung thời gian:

## 8. Configuration and Secrets
- Nơi lưu cấu hình và secret, cách cấp phát và xoay vòng:
- Quy tắc: không commit secret vào repo, không ghi giá trị secret vào tài liệu (xem [security-standards](../03-engineering/security-standards.md) §7).

## 9. Database Deployment and Migration
- Quy trình chạy migration (thứ tự so với deploy ứng dụng, tương thích ngược):
- Sao lưu trước khi migrate: xem [backup-recovery](backup-recovery.md).
- Đối chiếu [database-design](../02-architecture/database-design.md) §7 (quy tắc migration; chạy migration production phải được duyệt).
- Cache (nếu có): bản phát hành đổi version key/value thì warm-up tầng T1 của nhóm mới trước khi bản mới nhận traffic. Mất key mốc epoch thì chạy warm-up. Cấu hình ở [database-design](../02-architecture/database-design.md) §3.7.

## 10. Rollback Strategy
- Điều kiện kích hoạt rollback:
- Cách rollback ứng dụng:
- Cách rollback dữ liệu/migration:
- Người quyết định rollback:

## 11. Post-deployment Verification
- Smoke test:
- Chỉ số cần theo dõi và khung thời gian theo dõi (xem [monitoring](monitoring.md)):
- Tiêu chí xác nhận phát hành thành công:

## 12. Deployment Security
- Quyền truy cập môi trường và pipeline (nguyên tắc tối thiểu):
- Quét bảo mật (dependency, image, cấu hình) trước khi deploy:
- Ghi log và dấu vết kiểm toán cho mỗi lần deploy:
- AI không tự deploy production, không truy cập production database nếu chưa có cơ chế được phê duyệt.

## 13. Deployment Checklist
- [ ] Thiết kế/PR đã duyệt, CI xanh
- [ ] Đã có bản sao lưu gần nhất (nếu có migration)
- [ ] Cấu hình và secret môi trường đích đã sẵn sàng
- [ ] Đã deploy và smoke test đạt trên Staging
- [ ] UAT / Regression đạt
- [ ] Kế hoạch rollback đã kiểm chứng
- [ ] Owner phê duyệt phát hành Production
- [ ] Smoke test sau deploy đạt, theo dõi trong khung thời gian quy định

## 14. References
- [monitoring.md](monitoring.md)
- [backup-recovery.md](backup-recovery.md)
- [system-architecture](../02-architecture/system-architecture.md)
- [database-design](../02-architecture/database-design.md)
- [NFR](../01-requirements/NFR.md)
- [coding-standards](../03-engineering/coding-standards.md)
- [security-standards](../03-engineering/security-standards.md) (§7 secret)
