# Monitoring

| Thuộc tính | Giá trị |
| --- | --- |
| Người duyệt | Owner |
| Tài liệu liên quan | deployment.md, backup-recovery.md, ../01-requirements/NFR.md, ../02-architecture/system-architecture.md, ../03-engineering/error-handling.md, ../03-engineering/security-standards.md, ../../.ai/workflows/release-workflow.md |

> **Mục đích.** Giám sát, log, cảnh báo và ngưỡng sự cố.
>
> Template dùng chung cho mọi dự án: điền công cụ, endpoint, ngưỡng, lịch và người phụ trách khi áp dụng. Không ghi giá trị secret.

## 1. Purpose
Phạm vi và đối tượng của tài liệu: giám sát cái gì, để phát hiện vấn đề nào, ai đọc và dùng khi nào.

## 2. Monitoring Overview
Tóm tắt cách giám sát: công cụ sử dụng, luồng thu thập dữ liệu (metrics, log, trace) → lưu trữ → cảnh báo → xử lý.

## 3. Monitoring Scope
| Thành phần / dịch vụ | Môi trường | Loại giám sát (metrics/log/trace/health) | Mức ưu tiên |
| --- | --- | --- | --- |
|  | | | |

Đối chiếu thành phần trong [system-architecture](../02-architecture/system-architecture.md).

## 4. Metrics
| Chỉ số | Nguồn | Ngưỡng cảnh báo | Người nhận | Hành động |
| --- | --- | --- | --- | --- |
|  | | | | |

Nhóm chỉ số thường gặp: hạ tầng (CPU, RAM, đĩa, mạng), ứng dụng (latency, error rate, throughput), nghiệp vụ. Ngưỡng lấy từ [NFR](../01-requirements/NFR.md).

## 5. Logging
- Mức log, định dạng, trường bắt buộc (correlation/request ID, thời gian, môi trường):
- Nơi lưu trữ, thời gian lưu giữ, truy vấn:
- Quy tắc không ghi dữ liệu nhạy cảm vào log (xem [error-handling](../03-engineering/error-handling.md) §7, [security-standards](../03-engineering/security-standards.md) §9 và §9.2):

## 6. Distributed Tracing
Áp dụng khi hệ thống có nhiều dịch vụ/module gọi nhau; nếu không thì ghi "Không áp dụng".
- Công cụ và cách truyền trace/correlation ID giữa các thành phần:
- Tỷ lệ lấy mẫu, thời gian lưu giữ:

## 7. Health Checks
| Thành phần | Endpoint/cách kiểm tra | Tần suất | Tiêu chí khỏe/không khỏe |
| --- | --- | --- | --- |
|  | | | |

## 8. Alerting
- Mức độ cảnh báo (Critical/Warning/Info) và tiêu chí:
- Kênh gửi, người nhận, lịch trực (on-call):
- Quy tắc giảm nhiễu, leo thang khi không phản hồi:

## 9. Dashboards
| Dashboard | Mục đích | Đối tượng xem | Liên kết |
| --- | --- | --- | --- |
|  | | | |

## 10. Incident Detection and Response
- Cách phát hiện sự cố (cảnh báo, người dùng báo, kiểm tra định kỳ):
- Phân loại mức độ sự cố và thời gian phản hồi/xử lý mục tiêu:
- Quy trình xử lý: tiếp nhận → xác định ảnh hưởng → khắc phục/rollback (xem [deployment](deployment.md) §10) → khôi phục dữ liệu nếu cần (xem [backup-recovery](backup-recovery.md)) → thông báo:
- Post-mortem và hành động phòng ngừa:

## 11. Monitoring Security
- Quyền truy cập công cụ giám sát, dashboard và log (tối thiểu cần thiết; xem [security-standards](../03-engineering/security-standards.md) §9):
- Bảo vệ log và metrics chứa dữ liệu nhạy cảm, mã hóa khi lưu/truyền:
- Ghi dấu vết kiểm toán thay đổi cấu hình cảnh báo:

## 12. Operational Review
- Chu kỳ rà soát ngưỡng, cảnh báo và dashboard:
- Rà soát cảnh báo nhiễu/bỏ sót, cập nhật sau mỗi sự cố:
- Người chịu trách nhiệm rà soát:

## 13. References
- [deployment.md](deployment.md)
- [backup-recovery.md](backup-recovery.md)
- [NFR](../01-requirements/NFR.md)
- [system-architecture](../02-architecture/system-architecture.md)
- [error-handling](../03-engineering/error-handling.md)
- [security-standards](../03-engineering/security-standards.md)
