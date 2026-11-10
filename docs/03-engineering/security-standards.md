# Security Standards

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | coding-standards.md, error-handling.md, testing-strategy.md, ../02-architecture/system-architecture.md, ../02-architecture/api-design.md, ../02-architecture/database-design.md, ../../.ai/rules/security-rules.md, ../../.ai/skills/security-review/SKILL.md, ../../.ai/skills/authentication-rbac/SKILL.md |

> **Mục đích.** Chuẩn bảo mật: nguyên tắc, Authentication & Authorization (quy tắc), kiểm tra đầu vào, bảo vệ dữ liệu, secret, API, logging, dependency. Sàn không hạ được.

## 1. Mức dữ liệu dự án (D0–D3) và quy tắc đưa vào AI
Định nghĩa D0–D3 xem [glossary](../00-project-overview/glossary.md); mức dữ liệu của dự án khai báo ở [PROJECT.md](../../PROJECT.md). Với mỗi mức, ghi loại dữ liệu của dự án và việc được/không được đưa vào AI, log, môi trường không phải production.
| Mức | Dữ liệu của dự án | Được đưa vào AI | Được ghi log |
| --- | --- | --- | --- |
| D0 | | | |
| D1 | | | |
| D2 | | | |
| D3 | | Không | Không |

<!-- Điền theo từng dự án -->

## 2. Nguyên tắc bảo mật

| Nguyên tắc | Quy tắc áp dụng |
| --- | --- |
| Secure by Default | Cấu hình mặc định phải an toàn; tính năng rủi ro phải bật chủ động. |
| Least Privilege | Người dùng, service, tài khoản DB chỉ có quyền tối thiểu cần để làm việc. |
| Defense in Depth | Không dựa vào một lớp bảo vệ duy nhất; kiểm tra ở nhiều tầng. |
| Fail Securely | Khi lỗi thì từ chối truy cập, không mở quyền; thông báo lỗi không lộ chi tiết nội bộ. |

## 3. Authentication
Thiết kế cụ thể ở [system-architecture](../02-architecture/system-architecture.md) §6; mục này là quy tắc bắt buộc.

### 3.1 Xử lý mật khẩu
Thuật toán băm, độ mạnh tối thiểu, đặt lại mật khẩu. Không lưu hay log mật khẩu dạng rõ.
<!-- Điền theo từng dự án -->

### 3.2 Kiểm tra token
Quy tắc xác minh chữ ký, thời hạn, audience/issuer; thu hồi token.
<!-- Điền theo từng dự án -->

### 3.3 Quản lý phiên
Thời hạn phiên, làm mới, đăng xuất, cookie flag (`HttpOnly`, `Secure`, `SameSite`).
<!-- Điền theo từng dự án -->

### 3.4 Luồng xác thực
Các luồng được phép (đăng nhập, MFA, SSO); chống brute-force, khoá tài khoản.
<!-- Điền theo từng dự án -->

## 4. Authorization

### 4.1 Kiểm tra quyền
Mọi thao tác phải kiểm tra quyền ở phía server; không tin dữ liệu quyền do client gửi.

### 4.2 Phân quyền theo vai trò
Mô hình vai trò (RBAC) và nguyên tắc quyền tối thiểu. Danh sách vai trò, quyền ở [system-architecture](../02-architecture/system-architecture.md) §6.
<!-- Điền theo từng dự án -->

### 4.3 Phân quyền theo tài nguyên
Kiểm tra người dùng có quyền với *chính bản ghi đó* (chống truy cập trái phép theo ID, IDOR), không chỉ kiểm tra vai trò.

### 4.4 Phân quyền cho API
Mỗi endpoint khai báo quyền yêu cầu ([api-design](../02-architecture/api-design.md)); mặc định từ chối nếu chưa khai báo.

## 5. Kiểm tra đầu vào

| Hạng mục | Quy tắc |
| --- | --- |
| Validate request | Validate kiểu, độ dài, định dạng, giá trị cho phép ở biên hệ thống (allow-list); không tin đầu vào từ client. |
| SQL Injection | Dùng truy vấn tham số hoá/ORM; cấm nối chuỗi vào câu truy vấn. |
| XSS | Mã hoá đầu ra theo ngữ cảnh; không render HTML thô từ dữ liệu người dùng. |
| CSRF | Dùng token CSRF hoặc `SameSite` cho các request thay đổi dữ liệu dựa trên cookie. |
| Upload file | Kiểm tra loại thật, kích thước, đổi tên file, lưu ngoài thư mục thực thi, quét mã độc nếu cần. |

<!-- Bổ sung chi tiết theo công nghệ của dự án -->

## 6. Bảo vệ dữ liệu
Mức dữ liệu ở §1; thiết kế bảo mật cho từng bảng/cột ở [database-design](../02-architecture/database-design.md) §5.

### 6.1 Xử lý dữ liệu nhạy cảm
Chỉ thu thập và lưu dữ liệu cần thiết; không đưa dữ liệu D3 vào log, URL, thông báo lỗi.

### 6.2 Mã hoá
Mã hoá khi truyền (TLS) và khi lưu; thuật toán, độ dài khoá, nơi quản lý khoá.
<!-- Điền theo từng dự án -->

### 6.3 Che dữ liệu (masking)
Trường nào che khi hiển thị, khi xuất, khi dùng ở môi trường không phải production.
<!-- Điền theo từng dự án -->

### 6.4 Bảo vệ dữ liệu cá nhân
Căn cứ pháp lý, thời hạn lưu, quyền của chủ thể dữ liệu. Ràng buộc pháp lý khai báo ở [scope](../00-project-overview/scope.md).
<!-- Điền theo từng dự án -->

## 7. Quản lý secret (CẤM commit secret, CẤM đưa vào AI)

| Hạng mục | Quy tắc |
| --- | --- |
| Không hardcode | Cấm đặt secret, key, token, mật khẩu trong code, test, tài liệu, prompt gửi AI. |
| Cấu hình môi trường | Secret lấy từ biến môi trường hoặc secret manager; file mẫu (`.env.example`) chỉ chứa giá trị giả. |
| Xoay vòng | Chu kỳ đổi secret; quy trình thu hồi và thay ngay khi nghi ngờ lộ. |
| Kiểm soát truy cập | Ai được đọc secret từng môi trường; secret production tách biệt các môi trường khác. |

Secret đã lộ (kể cả trong lịch sử Git) coi như bị xâm phạm: phải thu hồi và thay mới.
<!-- Điền công cụ và quy trình theo từng dự án -->

## 8. Bảo mật API
Thiết kế và giá trị cụ thể ở [api-design](../02-architecture/api-design.md) §5; mục này là quy tắc bắt buộc.

| Hạng mục | Quy tắc |
| --- | --- |
| Rate limiting | Bắt buộc với endpoint xác thực và endpoint tốn tài nguyên. |
| CORS | Chỉ cho phép origin được khai báo; không dùng `*` với request có thông tin xác thực. |
| Giới hạn kích thước request | Đặt giới hạn body, upload, số phần tử/trang. |
| Security headers | Các header bắt buộc (HSTS, `Content-Security-Policy`, `X-Content-Type-Options`, ...). |

<!-- Điền giá trị theo từng dự án -->

## 9. Logging và Audit
Quy định chung ở [error-handling](error-handling.md) §7; mục này chỉ bổ sung yêu cầu bảo mật.

### 9.1 Ghi sự kiện bảo mật
Đăng nhập thành công/thất bại, đổi quyền, truy cập bị từ chối, thay đổi cấu hình bảo mật.

### 9.2 Che dữ liệu nhạy cảm trong log
Không ghi dữ liệu D3, mật khẩu, token; che hoặc băm dữ liệu cá nhân. Kiểm soát truy cập log.

### 9.3 Yêu cầu audit
Hành động cần audit trail (ai, làm gì, khi nào, trên đối tượng nào); thời hạn lưu; chống sửa/xoá log.
<!-- Điền theo từng dự án -->

## 10. Dependency và license

### 10.1 Quét dependency
Công cụ và thời điểm quét (CI, định kỳ).

### 10.2 Quản lý lỗ hổng
Thời hạn xử lý theo mức độ nghiêm trọng (Critical, High, Medium, Low).

### 10.3 Cập nhật dependency
Chu kỳ cập nhật, quy tắc ghim phiên bản, kiểm tra license được phép dùng.
<!-- Điền theo từng dự án -->

## 11. Checklist phát triển an toàn
Dùng khi tự kiểm và review ([coding-standards](coding-standards.md) §9.1).
- [ ] Mọi thao tác có kiểm tra xác thực và quyền ở server.
- [ ] Đầu vào được validate; truy vấn được tham số hoá.
- [ ] Không có secret, dữ liệu D3 trong code, log, prompt.
- [ ] Lỗi không lộ thông tin nội bộ.
- [ ] Dependency mới đã qua quét lỗ hổng và kiểm tra license.
- [ ] Thay đổi chạm tiền, phân quyền, dữ liệu cá nhân, migration có Security duyệt.

## 12. Quản lý ngoại lệ bảo mật
Sàn bảo mật không hạ được; chỉ cho phép ngoại lệ tạm thời có:
- Lý do, phạm vi, rủi ro còn lại và biện pháp bù.
- Người đề xuất và người duyệt (Tech Lead; thêm Security nếu đụng tới xác thực, phân quyền, dữ liệu cá nhân, secret).
- Thời hạn hết hiệu lực và kế hoạch khắc phục.

Ngoại lệ được ghi lại tại đây hoặc trong ADR ([ADR/](../02-architecture/ADR/README.md)).
<!-- Danh sách ngoại lệ đang hiệu lực -->

## 13. Tham khảo
OWASP ASVS, OWASP Top 10, hướng dẫn bảo mật của framework được dùng, quy định pháp lý về dữ liệu áp dụng cho dự án.
<!-- Điền theo từng dự án -->
