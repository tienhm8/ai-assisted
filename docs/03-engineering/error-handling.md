# Error Handling

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | api-design.md (../02-architecture/api-design.md), security-standards.md |

> **Mục đích.** Error handling và Logging: mã lỗi, thông điệp, retry, quy ước ghi log (không ghi dữ liệu nhạy cảm).

## 1. Phân loại lỗi
<!-- Điền theo từng dự án -->

## 2. Mã lỗi và định dạng phản hồi
| Mã | Ý nghĩa | HTTP / kênh | Người dùng thấy gì |
| --- | --- | --- | --- |
|  | | | |

## 3. Retry, timeout, fallback
<!-- Điền theo từng dự án -->

## 4. Logging
| Nội dung | Quy định |
| --- | --- |
| Mức log (debug/info/warn/error) và khi nào dùng |  |
| Định dạng, correlation/request ID |  |
| **Không ghi** secret, token, dữ liệu cá nhân (D3) | Bắt buộc |
| Nơi lưu, thời hạn lưu |  |

Giám sát và cảnh báo dựa trên log: xem [monitoring](../05-operations/monitoring.md).
