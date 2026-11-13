# Error Handling

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | coding-standards.md, security-standards.md, testing-strategy.md, ../02-architecture/api-design.md, ../02-architecture/database-design.md, ../05-operations/monitoring.md, ../../.ai/rules/coding-rules.md |

> **Mục đích.** Error handling và Logging: nguyên tắc, phân loại và mã lỗi, xử lý exception, phản hồi lỗi API, quy ước ghi log (không ghi dữ liệu nhạy cảm), retry, nhất quán dữ liệu khi lỗi.

## 1. Nguyên tắc xử lý lỗi

| Nguyên tắc | Quy tắc áp dụng |
| --- | --- |
| Nhất quán | Cùng một loại lỗi được xử lý và phản hồi theo cùng một cách trên toàn hệ thống. |
| Fail Fast | Phát hiện và dừng sớm khi đầu vào hoặc trạng thái không hợp lệ. |
| Fail Safely | Khi lỗi, hệ thống ở trạng thái an toàn: không mở quyền, không để dữ liệu dở dang ([security-standards](security-standards.md) §2). |
| Không nuốt lỗi | Cấm `catch` rỗng; mọi lỗi phải được xử lý, ghi log hoặc ném tiếp. |
| Minh bạch có kiểm soát | Người dùng thấy thông điệp dễ hiểu; chi tiết kỹ thuật chỉ ghi trong log, không trả ra ngoài. |

## 2. Phân loại lỗi

| Loại | Mô tả | Xử lý chính |
| --- | --- | --- |
| Nghiệp vụ | Vi phạm business rule (`BR-<MODULE>-<NN>`) | Báo người dùng, không retry |
| Validation | Dữ liệu đầu vào sai định dạng, thiếu, ngoài miền giá trị | Báo rõ trường sai, không retry |
| Xác thực | Chưa đăng nhập, token sai/hết hạn | Yêu cầu xác thực lại |
| Phân quyền | Không đủ quyền | Từ chối, ghi log bảo mật |
| Hệ thống | Lỗi không lường trước trong code | Ghi log đầy đủ, trả thông điệp chung |
| Hạ tầng | DB, cache, queue, mạng không sẵn sàng | Retry/fallback theo §8 |
| Tích hợp | Hệ thống ngoài lỗi hoặc trả dữ liệu sai | Retry/fallback theo §8, ghi log |

Bảng trên là mặc định khung; dự án chỉnh tại đây.

## 3. Mã lỗi

### 3.1 Định dạng và cách đặt tên
Định dạng mã lỗi, quy tắc đặt tên, cách nhóm theo loại/module.
<!-- Điền theo từng dự án -->

### 3.2 Danh mục mã lỗi
Mã lỗi gắn với module ở [module-design](../02-architecture/module-design.md); mã dùng chung do tài liệu này sở hữu.
| Mã | Loại | Ý nghĩa | HTTP / kênh | Người dùng thấy gì |
| --- | --- | --- | --- | --- |
|  | | | | |

## 4. Xử lý exception

| Hạng mục | Quy tắc |
| --- | --- |
| Hệ thống phân cấp exception | Exception riêng của dự án theo loại ở §2, kế thừa từ một lớp gốc chung. |
| Lan truyền | Chỉ bắt lỗi ở tầng có thể xử lý được; không bắt rồi ném lại mà không thêm thông tin. |
| Chuyển đổi (mapping) | Lỗi tầng thấp (DB, thư viện) được chuyển thành exception của dự án trước khi lên tầng cao; giữ nguyên nguyên nhân gốc. |
| Global exception handler | Một điểm tập trung chuyển exception thành phản hồi lỗi theo §5 và ghi log theo §7. |
| Giải phóng tài nguyên | Luôn đóng kết nối, file, lock kể cả khi lỗi ([coding-standards](coding-standards.md) §6). |

<!-- Điền theo từng dự án: chi tiết theo ngôn ngữ, framework -->

## 5. Phản hồi lỗi API
Hợp đồng API ở [api-design](../02-architecture/api-design.md); mục này quy định cấu trúc lỗi dùng chung.

### 5.1 Cấu trúc phản hồi
Các trường bắt buộc (mã lỗi, thông điệp, correlation ID, chi tiết theo trường nếu có).
<!-- Điền theo từng dự án -->

### 5.2 Ánh xạ HTTP status
| Loại lỗi | HTTP status |
| --- | --- |
| Validation | |
| Nghiệp vụ | |
| Xác thực | |
| Phân quyền | |
| Hệ thống / hạ tầng | |
| Tích hợp | |

### 5.3 Phản hồi theo loại
- **Validation:** liệt kê từng trường sai kèm lý do.
- **Nghiệp vụ:** mã lỗi và thông điệp nghiệp vụ, không lộ cấu trúc nội bộ.
- **Hệ thống:** thông điệp chung và correlation ID; không trả stack trace, câu truy vấn, đường dẫn nội bộ.

## 6. Thông điệp lỗi cho người dùng
Thông điệp rõ ràng, nói được người dùng cần làm gì tiếp; không chứa dữ liệu nhạy cảm hay chi tiết kỹ thuật.
<!-- Điền theo từng dự án: ngôn ngữ, nơi quản lý thông điệp -->

## 7. Logging
| Nội dung | Quy định |
| --- | --- |
| Mức log (debug/info/warn/error) và khi nào dùng |  |
| Định dạng log (khuyến nghị có cấu trúc) |  |
| Trường bắt buộc (thời gian, mức, module, mã lỗi, ...) |  |
| Correlation/request ID | Sinh ở điểm vào, truyền xuyên suốt các module và hệ thống ngoài |
| **Không ghi** secret, token, dữ liệu cá nhân (D3) | Bắt buộc; yêu cầu bảo mật thêm ở [security-standards](security-standards.md) §9 |
| Nơi lưu, thời hạn lưu |  |

Giám sát và cảnh báo dựa trên log: xem [monitoring](../05-operations/monitoring.md).

## 8. Retry, timeout, fallback

| Hạng mục | Quy tắc |
| --- | --- |
| Chính sách retry | Chỉ retry lỗi tạm thời (hạ tầng, tích hợp) và thao tác idempotent; số lần tối đa. |
| Exponential backoff | Giãn cách tăng dần kèm jitter để tránh dồn tải. |
| Timeout | Mọi lời gọi ra ngoài (DB, API, queue) phải có timeout; không chờ vô hạn. |
| Circuit breaker | Ngắt tạm khi hệ thống phụ thuộc lỗi liên tục; điều kiện mở/đóng. |
| Fallback | Hành vi suy giảm chấp nhận được khi không retry được (dữ liệu cache, thông báo thử lại sau). |

<!-- Điền theo từng dự án: giá trị -->

## 9. Transaction và nhất quán dữ liệu
Thiết kế transaction ở [database-design](../02-architecture/database-design.md) §6; mục này nêu cách xử lý khi lỗi.

- **Rollback:** lỗi trong transaction phải rollback toàn bộ; không commit dở dang.
- **Giao dịch phân tán:** hạn chế; nếu cần, nêu cơ chế bù trừ (saga, outbox) và ghi ADR.
- **Lỗi một phần:** với xử lý nhiều bước/nhiều bản ghi, nêu cách báo kết quả từng phần và cách thử lại không gây trùng.
<!-- Điền theo từng dự án -->

## 10. Giám sát và cảnh báo lỗi
Cấu hình chi tiết ở [monitoring](../05-operations/monitoring.md); mục này nêu yêu cầu từ phía xử lý lỗi.

- **Chỉ số lỗi:** tỷ lệ lỗi theo loại, theo module, theo endpoint.
- **Điều kiện cảnh báo:** ngưỡng và loại lỗi phải báo ngay (hệ thống, hạ tầng, tích hợp).
- **Error tracking:** công cụ gom lỗi, gắn correlation ID để truy vết.
<!-- Điền theo từng dự án -->

## 11. Checklist xử lý lỗi
Dùng khi tự kiểm và review ([coding-standards](coding-standards.md) §9.1).
- [ ] Không có `catch` rỗng hoặc nuốt lỗi.
- [ ] Lỗi được phân loại và dùng đúng mã lỗi trong §3.2.
- [ ] Phản hồi lỗi không lộ stack trace, câu truy vấn hay thông tin nội bộ.
- [ ] Log có correlation ID, không chứa dữ liệu nhạy cảm.
- [ ] Mọi lời gọi ra ngoài có timeout; retry chỉ áp dụng cho thao tác idempotent.
- [ ] Transaction rollback đúng khi lỗi; tài nguyên được giải phóng.
- [ ] Có test cho các nhánh lỗi chính ([testing-strategy](testing-strategy.md)).

## 12. Tham khảo
Quy chuẩn lỗi của framework/giao thức được dùng (ví dụ RFC 9457 Problem Details cho API HTTP).
<!-- Điền theo từng dự án -->
