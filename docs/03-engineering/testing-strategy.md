# Testing Strategy

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | ../01-requirements/acceptance-criteria.md, coding-standards.md |

> **Mục đích.** Chiến lược kiểm thử và cổng chất lượng tự động. Test ghi ID AC.

## 1. Các tầng test
| Tầng | Phạm vi | Công cụ | Khi chạy |
| --- | --- | --- | --- |
| Unit | | | |
| Integration | | | |
| E2E | | | |
| Security | | | |
| Regression | | | |

## 2. Cổng tự động
Áp dụng như nhau cho code người và code AI. Công cụ và ngưỡng do từng dự án chọn (ví dụ ở cuối mục này).

| Cổng | Nội dung | Chặn khi |
| --- | --- | --- |
| Build | Build thành công | Lỗi |
| Format/lint | Theo cấu hình của dự án | Lỗi mức error |
| Kiểm tra kiểu | Nếu ngôn ngữ hỗ trợ, bật chế độ nghiêm ngặt | Có lỗi |
| Unit test + coverage | Ngưỡng theo module/rủi ro | Fail hoặc dưới ngưỡng |
| Integration/E2E | Theo rủi ro | Test bắt buộc fail |
| Secret scanning | Mọi commit | Phát hiện secret |
| Dependency/SCA, license | Khi đổi dependency | Lỗ hổng high/critical, license cấm |
| SAST | Mức nghiêm ngặt S2 trở lên | Phát hiện high |
| Migration check | Khi có migration | Không chạy được trên DB sạch, thiếu cách khôi phục |
| Truy vết | PR có ID Task/FR | Thiếu liên kết |
| Đối chiếu phiếu ↔ diff | S2 trở lên | File vùng 🟡/🔴, test bị xoá, xoá cột/bảng không có trong phiếu |

**Luật chung**
- **Cấm** tắt lint/kiểm tra kiểu/test, hạ ngưỡng coverage, xoá hoặc làm yếu assertion, bỏ hook (`--no-verify`) để qua cổng.
- Bỏ một kiểm tra thường lệ phải giải thích trong báo cáo bàn giao.
- Sửa cổng và ngưỡng thuộc vùng 🔴, cần Task riêng.
- Chưa có CI thì chạy cổng **cục bộ** (hook hoặc lệnh tay), ghi kết quả thật vào báo cáo bàn giao; ghi miễn trừ có thời hạn thay vì bỏ qua âm thầm. Khi có CI, CI là nguồn kết quả chính thức.

**Review theo rủi ro.** Mức R1–R3; cách review ở Skill [code-review](../../.ai/skills/code-review/SKILL.md). R3 cần hai người, một người độc lập; nếu thiếu người thì ghi miễn trừ.

**Ví dụ chọn công cụ** (không bắt buộc): dự án TypeScript dùng ESLint + Prettier, `tsc --strict`, Vitest/Jest, Playwright, gitleaks, `npm audit`; dự án Python dùng ruff, mypy, pytest.

## 3. Dữ liệu test (giả/ẩn danh)
<!-- Điền theo từng dự án -->

## 4. Quy ước báo kết quả
Phân biệt rõ pass / fail / skipped / not-run, kèm output thật làm bằng chứng.

## 5. Nguyên tắc: không chỉ để AI viết code, phải để AI kiểm tra code
AI viết code không đồng nghĩa AI đã chứng minh code đúng. Phải có hệ thống kiểm thử độc lập với việc sinh code.

### 5.1. Các tầng kiểm thử
| Loại kiểm thử | Mục đích | AI hỗ trợ |
| --- | --- | --- |
| Static Analysis | Phát hiện lỗi tĩnh | Phân tích cảnh báo |
| Type Checking | Kiểm tra kiểu dữ liệu | Phát hiện lỗi type |
| Unit Test | Kiểm tra hàm/module | Sinh test cases |
| Integration Test | Kiểm tra tích hợp | Tạo kịch bản |
| API Test | Kiểm tra API | Test request/response |
| E2E Test | Kiểm tra hành trình người dùng | Viết Playwright tests |
| Security Test | Kiểm tra bảo mật | Phân tích lỗ hổng |
| Performance Test | Kiểm tra tải | Phân tích bottleneck |
| Regression Test | Tránh lỗi tái phát | Bổ sung test tự động |
| UAT | Kiểm tra nghiệp vụ | Hỗ trợ tạo test scenarios |

### 5.2. Ví dụ kiểm thử chức năng phân quyền
Giả sử hệ thống có các vai trò: Owner, Admin, CTV, Sale, Customer, Visitor.

Không được chỉ kiểm tra trường hợp người dùng có quyền truy cập. Phải kiểm tra cả trường hợp không có quyền.

| Tình huống | Kết quả mong đợi |
| --- | --- |
| Admin truy cập API quản trị theo quyền được cấp | Cho phép |
| Customer truy cập ERP API | Từ chối |
| Visitor gọi API yêu cầu đăng nhập | Từ chối |
| CTV xem tài nguyên ngoài phạm vi được cấp | Từ chối |
| Người dùng giả mạo role ở frontend | Backend vẫn từ chối |
| Tài khoản bị thu hồi phiên | Không tiếp tục sử dụng phiên đó |

Đây là cách dùng AI rất hiệu quả: yêu cầu AI tạo ma trận kiểm thử dựa trên Business Rules và RBAC Specification.

### 5.3. Testing Pyramid
```text
        /\          E2E          Ít hơn · Chi phí cao
       /  \
      /----\        Integration  Mức trung bình
     /      \
    /--------\      Unit Tests   Nhiều nhất · Chạy nhanh
```
Không nên chỉ tập trung vào E2E vì kiểm thử này thường chậm và khó bảo trì. Cần kết hợp nhiều tầng.

### 5.4. Definition of Done: điều kiện hoàn thành
Mỗi Task chỉ được đánh dấu hoàn thành khi:

- [ ] Đúng yêu cầu nghiệp vụ.
- [ ] Không vi phạm kiến trúc.
- [ ] Không vi phạm Coding Rules.
- [ ] Không vi phạm Security Rules.
- [ ] Typecheck thành công.
- [ ] Lint thành công.
- [ ] Unit tests thành công.
- [ ] Integration tests thành công nếu có liên quan.
- [ ] E2E tests thành công nếu có liên quan.
- [ ] Không có lỗi nghiêm trọng chưa xử lý.
- [ ] Code review được chấp thuận.
- [ ] Tài liệu được cập nhật.
- [ ] Có bằng chứng kiểm thử.

Không nên áp một con số coverage duy nhất cho tất cả module. Có thể đặt mục tiêu riêng cho logic nghiệp vụ, bảo mật, tiện ích và những phần ít rủi ro hơn.
