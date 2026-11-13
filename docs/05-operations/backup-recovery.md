# Backup & Recovery

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt (dự án) | Owner |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | deployment.md, monitoring.md, ../01-requirements/NFR.md, ../02-architecture/database-design.md, ../03-engineering/security-standards.md, ../../.ai/rules/database-rules.md, ../../.ai/workflows/release-workflow.md |

> **Mục đích.** Sao lưu, khôi phục, RPO/RTO, diễn tập.
>
> Template dùng chung cho mọi dự án: điền công nghệ, lịch chạy, thông số và người phụ trách khi áp dụng. Không ghi giá trị secret (khóa mã hóa, mật khẩu, chuỗi kết nối).

## 1. Purpose
Phạm vi và đối tượng của tài liệu: bảo vệ dữ liệu/hệ thống nào, ai đọc, dùng khi nào (chuẩn bị, sự cố, diễn tập).

## 2. Scope
- Trong phạm vi (cơ sở dữ liệu, tệp, cấu hình, secret, hạ tầng...):
- Ngoài phạm vi:

## 3. Recovery Objectives
| Đối tượng | RPO (mất dữ liệu tối đa) | RTO (thời gian khôi phục tối đa) | Nguồn yêu cầu |
| --- | --- | --- | --- |
|  | | | |

Giá trị lấy từ [NFR](../01-requirements/NFR.md) (nhóm Sẵn sàng). Nếu NFR chưa có yêu cầu RPO/RTO thì bổ sung vào NFR trước, rồi mới điền bảng này.

## 4. Backup Strategy
Mô tả chiến lược: loại sao lưu (full / incremental / differential / snapshot / PITR), công cụ, nguyên tắc (ví dụ 3-2-1), tự động hóa.

## 5. Backup Scope
| Đối tượng | Loại | Nơi lưu nguồn | Phương thức sao lưu | Ghi chú |
| --- | --- | --- | --- | --- |
|  | | | | |

Đối chiếu dữ liệu cần bảo vệ trong [database-design](../02-architecture/database-design.md).

## 6. Backup Schedule
| Đối tượng | Tần suất | Thời điểm chạy | Lưu giữ | Người/cơ chế chạy |
| --- | --- | --- | --- | --- |
|  | | | | |

## 7. Backup Storage and Retention
- Nơi lưu (cùng/khác vùng, khác tài khoản), dung lượng:
- Chính sách lưu giữ và xóa bản sao lưu cũ:
- Yêu cầu pháp lý/tuân thủ về lưu giữ dữ liệu:

## 8. Backup Security
- Mã hóa khi lưu và khi truyền; quản lý khóa theo [security-standards](../03-engineering/security-standards.md) §7 (không ghi khóa vào tài liệu):
- Phân quyền truy cập bản sao lưu (tối thiểu cần thiết), tách biệt khỏi môi trường production:
- Bảo vệ chống xóa/ghi đè (immutable, versioning), dữ liệu cá nhân trong bản sao lưu (xem [security-standards](../03-engineering/security-standards.md) §6):
- Dữ liệu production không được dùng trực tiếp ở môi trường thấp hơn nếu chưa ẩn danh hóa.

## 9. Recovery Scenarios
| Kịch bản | Mức ảnh hưởng | Phương án khôi phục | Mục tiêu RTO/RPO |
| --- | --- | --- | --- |
| Xóa/sửa nhầm dữ liệu | | | |
| Lỗi migration/deploy | | | |
| Hỏng cơ sở dữ liệu / lưu trữ | | | |
| Mất máy chủ / dịch vụ | | | |
| Sự cố bảo mật (ransomware, xâm nhập) | | | |
| Mất cả site/vùng | | | |

## 10. Recovery Procedures
Từng bước khôi phục cho mỗi kịch bản: điều kiện kích hoạt, người quyết định, các bước thực hiện, cách xác nhận dữ liệu toàn vẹn, thông báo các bên liên quan. Rollback ứng dụng xem [deployment](deployment.md) §10.

## 11. Disaster Recovery
- Kịch bản thảm họa và tiêu chí tuyên bố:
- Site/vùng dự phòng, mô hình (cold / warm / hot standby):
- Quy trình chuyển đổi (failover) và quay lại (failback):
- Liên hệ và leo thang:

## 12. Backup Verification
- Cách kiểm tra bản sao lưu thành công và toàn vẹn (checksum, thử khôi phục mẫu):
- Giám sát và cảnh báo khi sao lưu thất bại (xem [monitoring](monitoring.md)):

## 13. Recovery Testing
| Hạng mục diễn tập | Chu kỳ | Lần diễn tập gần nhất | Kết quả | RTO/RPO thực tế | Việc cần xử lý |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |

## 14. Roles and Responsibilities
| Vai trò | Trách nhiệm |
| --- | --- |
| Owner | Phê duyệt RPO/RTO, quyết định khôi phục có ảnh hưởng lớn |
| Tech Lead | Chịu trách nhiệm chiến lược, quy trình sao lưu và khôi phục |
| DevOps | Thực hiện sao lưu, kiểm tra, khôi phục, diễn tập |
| Security | Rà soát mã hóa, phân quyền, dữ liệu nhạy cảm |

Quy tắc cho AI với production xem [deployment](deployment.md) §12.

## 15. References
- [deployment.md](deployment.md)
- [monitoring.md](monitoring.md)
- [NFR](../01-requirements/NFR.md)
- [database-design](../02-architecture/database-design.md)
- [security-standards](../03-engineering/security-standards.md)
