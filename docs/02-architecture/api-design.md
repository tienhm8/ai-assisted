# API Design

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt (dự án) | Kiến trúc sư |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | system-architecture.md, module-design.md, database-design.md, ADR/, ../01-requirements/FR/, ../01-requirements/business-rules.md, ../03-engineering/coding-standards.md, ../03-engineering/error-handling.md, ../03-engineering/security-standards.md, ../05-operations/deployment.md, ../../.ai/rules/architecture-rules.md, ../../.ai/skills/api-development/SKILL.md |

> **Mục đích.** API Specification và Integration Specification: route, request/response, mã lỗi, quyền, tương thích ngược, tích hợp hệ thống ngoài.

## 1. API Specification

### 1.1 Danh mục API
| Method · Route | Module | Mục đích | Quyền | Request | Response | Mã lỗi | FR |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | | |

Mỗi API truy vết được về `FR-<MODULE>-<NN>`. Thay đổi phá vỡ tương thích phải có ADR mới và thông báo bên tiêu thụ.

### 1.2 Chi tiết API
Chỉ mô tả API phức tạp hoặc có quy tắc đặc biệt; API đơn giản để danh mục §1.1 và đặc tả OpenAPI (§6) làm nguồn chuẩn. Lặp lại mẫu cho từng API.

#### [Method · Route]
| Hạng mục | Nội dung |
| --- | --- |
| Mô tả · Module · FR |  |
| Xác thực · Quyền cần có |  |
| Request (header, path, query, body) |  |
| Response thành công |  |
| Response lỗi · Mã lỗi |  |
| Validation |  |
| Business rule áp dụng | `BR-<MODULE>-<NN>`, nội dung ở [business-rules](../01-requirements/business-rules.md) |
| Idempotency (thao tác ghi có thể bị gọi lặp) |  |
| Rate limit |  |

## 2. Integration Specification (hệ thống ngoài / liên module)
| Hệ thống | Hướng | Giao thức · định dạng | Xác thực | Xử lý lỗi/retry | Chủ sở hữu | FR |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |

Danh sách hệ thống ngoài mức tổng thể ở [system-architecture](system-architecture.md) §5.1.

## 3. Tổng quan và quy ước API

### 3.1 Tổng quan
| Hạng mục | Nội dung |
| --- | --- |
| Kiểu API (REST, GraphQL, gRPC…) |  |
| Bên tiêu thụ (web, mobile, hệ thống ngoài) |  |
| Base URL | Theo từng môi trường: xem [deployment](../05-operations/deployment.md) §3 |

### 3.2 Quy ước chung
Quy ước đặt tên chung cho mã nguồn ở [coding-standards](../03-engineering/coding-standards.md) §4. Quy ước đặt tên route và các quy ước riêng cho API do mục này sở hữu.

| Hạng mục | Quy ước |
| --- | --- |
| Đặt tên route (danh từ, số nhiều, kebab-case…) |  |
| HTTP method (ý nghĩa từng method) |  |
| HTTP status code | Ánh xạ theo [error-handling](../03-engineering/error-handling.md) §5.2; chỉ ghi ngoại lệ của API nếu có |
| Định dạng request / response thành công (envelope, tên trường) | Định dạng phản hồi lỗi: [error-handling](../03-engineering/error-handling.md) §5.1 |
| Phân trang |  |
| Lọc và sắp xếp |  |
| Phiên bản (URL, header) và chính sách ngừng hỗ trợ |  |
| Định dạng ngày giờ, múi giờ | Thống nhất với [database-design](database-design.md) §2 |

### 3.3 Thành phần dùng chung
| Hạng mục | Nội dung |
| --- | --- |
| Header chung (correlation/request ID, ngôn ngữ…) |  |
| Cấu trúc response chung |  |
| Cấu trúc response lỗi và mã lỗi | Nguồn duy nhất ở [error-handling](../03-engineering/error-handling.md) §3, §5 (mã riêng của module ở [module-design](module-design.md)); không định nghĩa lại ở đây. Cột "Mã lỗi" của từng API chỉ liệt kê mã đã có |
| Quy tắc validation chung |  |

## 4. Authentication & Authorization
Thiết kế cơ chế xác thực, phân quyền, vòng đời token ở [system-architecture](system-architecture.md) §6, không lặp lại. Mục này chỉ ghi cách áp dụng ở tầng API:

| Hạng mục | Nội dung |
| --- | --- |
| Cách client gửi thông tin xác thực (header, cookie) |  |
| API công khai (không cần xác thực) |  |
| Cách khai báo quyền cần có trên từng API | Cột "Quyền" ở §1.1 |
| Phản hồi khi thiếu xác thực / thiếu quyền (401/403) | Theo [error-handling](../03-engineering/error-handling.md) §5.2 |

## 5. Bảo mật API
Quy tắc bắt buộc ở [security-standards](../03-engineering/security-standards.md). Ghi phần áp dụng riêng cho API: giới hạn tần suất, kích thước request, CORS, chống lạm dụng, dữ liệu nhạy cảm không đưa vào URL/log.
<!-- Điền theo từng dự án -->

## 6. Đặc tả và tài liệu API
Công cụ và vị trí đặc tả máy đọc được (OpenAPI/Swagger…), cách sinh và cập nhật, ai chịu trách nhiệm đồng bộ với mã nguồn.
<!-- Điền theo từng dự án -->
