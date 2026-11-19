# Security Standards

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | coding-standards.md, error-handling.md, testing-strategy.md, ../02-architecture/system-architecture.md, ../02-architecture/api-design.md, ../02-architecture/database-design.md, ../../.ai/rules/security-rules.md, ../../.ai/skills/security-review/SKILL.md, ../../.ai/skills/authentication-rbac/SKILL.md |

> **Mục đích.** Chuẩn bảo mật: nguyên tắc, Authentication & Authorization (quy tắc), kiểm tra đầu vào, bảo vệ dữ liệu, secret, API, logging, dependency, ánh xạ OWASP Top 10 và mức ASVS. Sàn không hạ được.

## 1. Xử lý dữ liệu theo mức
Định nghĩa bốn mức dữ liệu (công khai, nội bộ, nhạy cảm, bí mật) ở [project-rules](../../.ai/rules/project-rules.md); dữ liệu của dự án thuộc mức nào và mức nào được đưa vào AI khai báo ở [PROJECT.md](../../PROJECT.md) §3, không chép lại ở đây. Với mỗi mức, ghi việc được/không được ghi log và dùng ở môi trường không phải production.
| Mức | Được ghi log | Được dùng ở môi trường không phải production |
| --- | --- | --- |
| Công khai | | |
| Nội bộ | | |
| Nhạy cảm | | |
| Bí mật | Không | |

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
| SSRF | Server gọi URL lấy từ đầu vào thì dùng allow-list đích (host, scheme, port); chặn địa chỉ nội bộ, loopback, metadata cloud; không theo redirect tới đích ngoài danh sách. |
| Path traversal | Không ghép đường dẫn file từ đầu vào; chuẩn hoá đường dẫn và kiểm tra nằm trong thư mục cho phép. |
| Deserialization | Không giải tuần tự hoá dữ liệu không tin cậy bằng cơ chế cho phép tạo đối tượng tuỳ ý; chỉ dùng định dạng dữ liệu thuần (JSON) có schema. |

<!-- Điền theo từng dự án: chi tiết theo công nghệ -->

## 6. Bảo vệ dữ liệu
Dữ liệu của dự án theo mức ở [PROJECT.md](../../PROJECT.md) §3, cách xử lý ở §1; thiết kế bảo mật cho từng bảng/cột ở [database-design](../02-architecture/database-design.md) §5.

### 6.1 Xử lý dữ liệu nhạy cảm
Chỉ thu thập và lưu dữ liệu cần thiết; không đưa dữ liệu bí mật vào log, URL, thông báo lỗi.

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
<!-- Điền theo từng dự án: công cụ, quy trình -->

## 8. Bảo mật API
Thiết kế và giá trị cụ thể ở [api-design](../02-architecture/api-design.md) §5; mục này là quy tắc bắt buộc.

| Hạng mục | Quy tắc |
| --- | --- |
| Rate limiting | Bắt buộc với endpoint xác thực và endpoint tốn tài nguyên. |
| CORS | Chỉ cho phép origin được khai báo; không dùng `*` với request có thông tin xác thực. |
| Giới hạn kích thước request | Đặt giới hạn body, upload, số phần tử/trang. |
| Security headers | Các header bắt buộc (HSTS, `Content-Security-Policy`, `X-Content-Type-Options`, ...). |

<!-- Điền theo từng dự án: giá trị -->

## 9. Logging và Audit
Quy định chung ở [error-handling](error-handling.md) §7; mục này chỉ bổ sung yêu cầu bảo mật.

### 9.1 Ghi sự kiện bảo mật và cảnh báo
Đăng nhập thành công/thất bại, đổi quyền, truy cập bị từ chối, thay đổi cấu hình bảo mật.

Sự kiện bất thường (đăng nhập thất bại liên tiếp, truy cập bị từ chối tăng đột biến, đổi quyền quản trị) phải có cảnh báo tới người xử lý; ngưỡng và người nhận khai báo ở [monitoring](../05-operations/monitoring.md) §8. Chỉ ghi log mà không có cảnh báo thì chưa đạt.

### 9.2 Che dữ liệu nhạy cảm trong log
Không ghi dữ liệu bí mật, mật khẩu, token; che hoặc băm dữ liệu cá nhân. Kiểm soát truy cập log.

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

### 10.4 Chuỗi cung ứng và toàn vẹn
- Commit lockfile; build từ lockfile, không tự nâng phiên bản lúc build.
- Chỉ lấy gói từ registry được duyệt; cảnh báo gói mới, gói đổi chủ, tên gần giống gói phổ biến.
- Tạo danh sách thành phần (SBOM) cho mỗi bản phát hành.
- Pipeline CI/CD: quyền tối thiểu, secret theo môi trường, thay đổi pipeline cần duyệt (vùng 🔴).
- Artifact phát hành và bản cập nhật có kiểm tra toàn vẹn (checksum hoặc chữ ký) trước khi triển khai.
- Dữ liệu tin cậy (cookie, token, dữ liệu gửi qua client) có chữ ký hoặc kiểm tra toàn vẹn ở server.
<!-- Điền theo từng dự án: công cụ -->

## 11. Checklist phát triển an toàn
Dùng khi tự kiểm và review ([coding-standards](coding-standards.md) §9.1).
- [ ] Mọi thao tác có kiểm tra xác thực và quyền ở server.
- [ ] Đầu vào được validate; truy vấn được tham số hoá.
- [ ] Không có secret, dữ liệu bí mật trong code, log, prompt.
- [ ] Lỗi không lộ thông tin nội bộ; khi lỗi hoặc ngoại lệ thì từ chối (fail-closed), không bỏ qua kiểm tra.
- [ ] URL, đường dẫn file, dữ liệu tuần tự hoá từ đầu vào đã xử lý theo §5 (SSRF, path traversal, deserialization).
- [ ] Dependency mới đã qua quét lỗ hổng và kiểm tra license; lockfile được cập nhật.
- [ ] Sự kiện bảo mật mới có log và cảnh báo (§9.1).
- [ ] Đã đối chiếu thay đổi với các mục OWASP Top 10 và chương ASVS liên quan ở mức dự án đã khai báo (§13).
- [ ] Thay đổi chạm tiền, phân quyền, dữ liệu cá nhân, migration có Security duyệt.

## 12. Quản lý ngoại lệ bảo mật
Sàn bảo mật không hạ được; chỉ cho phép ngoại lệ tạm thời có:
- Lý do, phạm vi, rủi ro còn lại và biện pháp bù.
- Người đề xuất và người duyệt (Tech Lead; thêm Security nếu đụng tới xác thực, phân quyền, dữ liệu cá nhân, secret).
- Thời hạn hết hiệu lực và kế hoạch khắc phục.

Ngoại lệ được ghi lại tại đây hoặc trong ADR ([ADR/](../02-architecture/ADR/README.md)).
<!-- Điền theo từng dự án: danh sách ngoại lệ đang hiệu lực -->

## 13. OWASP Top 10 và ASVS
Phiên bản đang dùng (nguồn duy nhất; đổi phiên bản thì sửa tại đây và rà lại bảng): **OWASP Top 10:2025**, **OWASP ASVS 5.0**. Không chép nội dung OWASP vào repo; chỉ trỏ mã mục (`A01:2025`) và mã yêu cầu ASVS (`V8.2.1`).

### 13.1 Mức ASVS
Dự án khai báo mức ASVS mục tiêu ở [PROJECT.md](../../PROJECT.md) §4. Mức tối thiểu theo dữ liệu và rủi ro:

| Điều kiện | Mức tối thiểu |
| --- | --- |
| Chỉ có dữ liệu công khai hoặc nội bộ, không có tài khoản người dùng | L1 |
| Có dữ liệu nhạy cảm hoặc bí mật, có tài khoản người dùng hoặc phân quyền | L2 |
| Có tiền, y tế, hạ tầng trọng yếu hoặc bắt buộc theo hợp đồng/pháp lý | L3 |

Yêu cầu ASVS ở mức đã khai báo mà chưa đạt thì ghi ngoại lệ theo §12, không bỏ qua âm thầm.

### 13.2 Ánh xạ OWASP Top 10:2025
| Mã | Rủi ro | Quy định trong khung | Chương ASVS 5.0 liên quan |
| --- | --- | --- | --- |
| A01:2025 | Broken Access Control | §4; [security-rules](../../.ai/rules/security-rules.md) 1–2, 5; §5 (SSRF) | V8 Authorization |
| A02:2025 | Security Misconfiguration | §2 Secure by Default; §8 (CORS, headers); [deployment](../05-operations/deployment.md) | V13 Configuration, V3 Web Frontend Security |
| A03:2025 | Software Supply Chain Failures | §10; security-rules 7 | V15 Secure Coding and Architecture |
| A04:2025 | Cryptographic Failures | §3.1, §6.2; §7 | V11 Cryptography, V12 Secure Communication |
| A05:2025 | Injection | §5; security-rules 3 | V1 Encoding and Sanitization, V2 Validation and Business Logic, V5 File Handling |
| A06:2025 | Insecure Design | Threat model ở [system-architecture](../02-architecture/system-architecture.md) §8; §2 | V15 Secure Coding and Architecture, V2 Validation and Business Logic |
| A07:2025 | Authentication Failures | §3 | V6 Authentication, V7 Session Management, V9 Self-contained Tokens, V10 OAuth and OIDC |
| A08:2025 | Software or Data Integrity Failures | §10.4; §5 (Deserialization) | V15 Secure Coding and Architecture, V4 API and Web Service |
| A09:2025 | Security Logging and Alerting Failures | §9; security-rules 6 | V16 Security Logging and Error Handling |
| A10:2025 | Mishandling of Exceptional Conditions | §2 Fail Securely; [error-handling](error-handling.md) | V16 Security Logging and Error Handling |

Bảng này là danh mục để review; điểm còn trống của dự án (các mục `<!-- Điền theo từng dự án -->`) vẫn phải điền thì mới coi là phủ.

## 14. Tham khảo
OWASP Top 10:2025, OWASP ASVS 5.0 (phiên bản theo §13), hướng dẫn bảo mật của framework được dùng, quy định pháp lý về dữ liệu áp dụng cho dự án.
<!-- Điền theo từng dự án -->
