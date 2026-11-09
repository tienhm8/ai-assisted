# Authentication & RBAC – Examples

> Bản nháp (Draft). Đây là **ví dụ minh hoạ**, không phải ma trận phân quyền chính thức. AI phải đọc RBAC specification và FR/BR trong `docs/` trước; ví dụ ở đây không được dùng làm nghiệp vụ.

Bối cảnh ví dụ: hệ thống có **Web** (khách truy cập, người dùng) và **ERP** (nội bộ), với các vai Owner, Admin, CTV, Sale, Customer.

## Ranh giới ứng dụng (Web và ERP)

- Giữ nguyên ranh giới truy cập giữa Web và ERP.
- Áp chính sách phiên độc lập cho từng ứng dụng khi spec quy định.
- Chặn truy cập chéo ứng dụng trái phép.
- Mọi ERP API phải được kiểm tra ở backend (khớp [security-rules.md](../../rules/security-rules.md)).

## Truy cập theo tài nguyên

- Người dùng chỉ truy cập tài nguyên được phép.
- **CTV** chỉ truy cập tài nguyên trong phạm vi được duyệt.
- **Sale** chỉ truy cập dữ liệu được phân công khi yêu cầu như vậy.
- Quyền quản trị theo quyền được cấp rõ ràng; không mặc định Admin được phép mọi thứ.

## Ví dụ ca test ranh giới quyền

| Tình huống | Kết quả mong đợi |
| --- | --- |
| Chưa đăng nhập gọi ERP API | 401 |
| Customer gọi ERP API | 403 |
| CTV truy cập tài nguyên ngoài phạm vi | 403 hoặc 404 theo quy ước của API |
| Sale truy cập dữ liệu không được phân công | 403 hoặc 404 theo quy ước của API |
| Client gửi role giả trong request | Bỏ qua; backend lấy role từ phiên |
| Phiên Web dùng cho ERP | Từ chối |
| Phiên đã bị thu hồi hoặc hết hạn | 401 |

Ghi chú khi áp dụng cho dự án: thay bằng ma trận quyền thật khi `docs/` có RBAC và business rule được duyệt.
