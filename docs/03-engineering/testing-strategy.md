# Testing Strategy

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | ../01-requirements/acceptance-criteria.md, ../01-requirements/NFR.md, coding-standards.md, security-standards.md, error-handling.md, ../05-operations/deployment.md, ../../.ai/skills/unit-testing/SKILL.md, ../../.ai/skills/integration-testing/SKILL.md, ../../.ai/skills/e2e-testing/SKILL.md |

> **Mục đích.** Chiến lược kiểm thử và cổng chất lượng tự động: mục tiêu, phạm vi, các tầng test, thiết kế test, dữ liệu test, tự động hoá, quality gate, Definition of Done. Test ghi ID AC.

## 1. Mục tiêu kiểm thử
- Chứng minh code đáp ứng FR và Acceptance Criteria ([acceptance-criteria](../01-requirements/acceptance-criteria.md)); mỗi test truy vết về ID AC.
- Chứng minh đáp ứng NFR ([NFR](../01-requirements/NFR.md)) và không vi phạm [security-standards](security-standards.md).
- Phát hiện lỗi sớm, ngăn lỗi cũ tái phát.

**Không chỉ để AI viết code, phải để AI kiểm tra code.** AI viết code không đồng nghĩa AI đã chứng minh code đúng. Phải có hệ thống kiểm thử độc lập với việc sinh code.

## 2. Nguyên tắc kiểm thử

| Nguyên tắc | Quy tắc áp dụng |
| --- | --- |
| Test sớm | Viết và chạy test ngay trong Task, không dồn về cuối. |
| Ưu tiên tự động | Việc lặp lại được thì tự động hoá; test thủ công chỉ cho phần chưa tự động được. |
| Theo rủi ro | Mức độ kiểm thử tăng theo mức rủi ro R1–R3 và mức dữ liệu D0–D3. |
| Độc lập | Test không phụ thuộc thứ tự chạy và không do chính cơ chế sinh code tự xác nhận. |
| Lặp lại được | Cùng đầu vào cho cùng kết quả; không phụ thuộc thời gian, mạng ngoài, dữ liệu may rủi. |

## 3. Phạm vi kiểm thử

### 3.1 Trong phạm vi
Các module và FR thuộc phạm vi ở [scope](../00-project-overview/scope.md).
<!-- Điền theo từng dự án -->

### 3.2 Ngoài phạm vi
Phần không kiểm thử (hệ thống ngoài, thư viện bên thứ ba) và lý do.
<!-- Điền theo từng dự án -->

## 4. Các tầng test

| Tầng | Phạm vi và mục đích | Công cụ | Khi chạy | AI hỗ trợ |
| --- | --- | --- | --- | --- |
| Static Analysis | Phát hiện lỗi tĩnh | | | Phân tích cảnh báo |
| Type Checking | Kiểm tra kiểu dữ liệu | | | Phát hiện lỗi type |
| Unit | Kiểm tra hàm/module | | | Sinh test cases |
| Integration | Kiểm tra tích hợp giữa module, DB, hệ thống ngoài | | | Tạo kịch bản |
| API | Kiểm tra request/response, mã lỗi theo [api-design](../02-architecture/api-design.md) | | | Test request/response |
| System | Kiểm tra toàn hệ thống trong môi trường gần thật | | | |
| E2E | Kiểm tra hành trình người dùng | Playwright ([testing-rules](../../.ai/rules/testing-rules.md) 9) | | Viết Playwright tests |
| Acceptance (UAT) | Kiểm tra nghiệp vụ với người dùng/nghiệp vụ | | | Hỗ trợ tạo test scenarios |
| Security | Kiểm tra bảo mật | | | Phân tích lỗ hổng |
| Regression | Tránh lỗi tái phát | | | Bổ sung test tự động |

```text
        /\          E2E          Ít hơn · Chi phí cao
       /  \
      /----\        Integration  Mức trung bình
     /      \
    /--------\      Unit Tests   Nhiều nhất · Chạy nhanh
```
Không nên chỉ tập trung vào E2E vì kiểm thử này thường chậm và khó bảo trì. Cần kết hợp nhiều tầng.

## 5. Kiểm thử phi chức năng
Chỉ tiêu cụ thể lấy từ [NFR](../01-requirements/NFR.md); mục này nêu cách kiểm chứng.

| Loại | Nội dung | Khi áp dụng |
| --- | --- | --- |
| Performance | Thời gian phản hồi, thông lượng so với chỉ tiêu NFR | |
| Load | Tải dự kiến theo kịch bản sử dụng thật | |
| Stress | Quá tải để tìm điểm giới hạn và cách hệ thống phục hồi | |
| Security | Kiểm thử lỗ hổng, phân quyền, theo [security-standards](security-standards.md) | |
| Compatibility | Trình duyệt, thiết bị, hệ điều hành hỗ trợ | |
| Accessibility | Tiêu chuẩn khả năng tiếp cận áp dụng | |

<!-- Điền theo từng dự án -->

## 6. Thiết kế test

| Kỹ thuật | Cách dùng |
| --- | --- |
| Thiết kế test case | Mỗi test case có điều kiện đầu, bước, kết quả mong đợi và ID AC. |
| Phân tích giá trị biên | Kiểm tra tại và quanh giá trị biên của mọi miền giá trị. |
| Phân vùng tương đương | Mỗi nhóm đầu vào tương đương chọn đại diện, không test thừa. |
| Negative testing | Kiểm tra đầu vào sai, thiếu, quá lớn, quyền không đủ và các nhánh lỗi ở [error-handling](error-handling.md). |
| Regression | Mỗi lỗi đã sửa có test chặn tái phát. |

### 6.1 Ví dụ: kiểm thử chức năng phân quyền
Ví dụ minh hoạ, vai trò thực tế của dự án theo [system-architecture](../02-architecture/system-architecture.md) §6. Giả sử hệ thống có các vai trò: Quản trị, Nhân viên, Khách hàng, Khách vãng lai (chưa đăng nhập).

Không được chỉ kiểm tra trường hợp người dùng có quyền truy cập. Phải kiểm tra cả trường hợp không có quyền.

| Tình huống | Kết quả mong đợi |
| --- | --- |
| Quản trị truy cập API quản trị theo quyền được cấp | Cho phép |
| Khách hàng truy cập API quản trị | Từ chối |
| Khách vãng lai gọi API yêu cầu đăng nhập | Từ chối |
| Nhân viên xem tài nguyên ngoài phạm vi được cấp | Từ chối |
| Người dùng giả mạo role ở frontend | Backend vẫn từ chối |
| Tài khoản bị thu hồi phiên | Không tiếp tục sử dụng phiên đó |

Đây là cách dùng AI rất hiệu quả: yêu cầu AI tạo ma trận kiểm thử dựa trên Business Rules và RBAC Specification.

## 7. Dữ liệu test (giả/ẩn danh)

| Hạng mục | Quy tắc |
| --- | --- |
| Chiến lược | Dùng dữ liệu giả hoặc sinh tự động; nguồn và cách tạo ghi tại đây. |
| Cô lập | Mỗi test tự tạo và không dùng chung dữ liệu với test khác; không chạm dữ liệu production. |
| Dữ liệu nhạy cảm | **Cấm** dùng dữ liệu thật mức D3 (secret, token, dữ liệu cá nhân) trong test; mức D1–D2 theo quy định ở [security-standards](security-standards.md) §1; nếu bắt buộc phải ẩn danh ([security-standards](security-standards.md) §6.3). |
| Dọn dẹp | Test dọn dữ liệu đã tạo hoặc chạy trên DB tạm có thể huỷ. |

<!-- Điền theo từng dự án -->

## 8. Tự động hoá test

| Hạng mục | Nội dung |
| --- | --- |
| Framework | Framework cho từng tầng ở §4. |
| Chuẩn viết test | Đặt tên, vị trí file, cấu trúc (arrange-act-assert); theo [coding-standards](coding-standards.md). |
| Tích hợp CI | Các cổng ở §9 chạy trong CI cho mọi PR. |
| Thực thi | Test nhanh chạy mỗi commit/PR; test chậm (E2E, performance) theo lịch hoặc trước phát hành. |

<!-- Điền theo từng dự án -->

## 9. Cổng chất lượng (Quality Gates)
Áp dụng như nhau cho code người và code AI. Công cụ và ngưỡng do từng dự án chọn (ví dụ ở cuối mục này).

| Cổng | Nội dung | Chặn khi |
| --- | --- | --- |
| Build | Build thành công | Lỗi |
| Format/lint | Theo cấu hình của dự án | Lỗi mức error |
| Kiểm tra kiểu | Nếu ngôn ngữ hỗ trợ, bật chế độ nghiêm ngặt | Có lỗi |
| Unit test + coverage | Ngưỡng theo module/rủi ro | Fail hoặc dưới ngưỡng |
| Integration/E2E | Theo rủi ro | Test bắt buộc fail |
| Commit message | Mọi commit, chạy ở hook `commit-msg` | Sai cú pháp Angular ([git-workflow-rules](../../.ai/rules/git-workflow-rules.md) mục 3) |
| Secret scanning | Mọi commit | Phát hiện secret |
| Dependency/SCA, license | Khi đổi dependency | Lỗ hổng high/critical, license cấm |
| SAST | Mức nghiêm ngặt S2 trở lên | Phát hiện high |
| Migration check | Khi có migration | Không chạy được trên DB sạch, thiếu cách khôi phục |
| Truy vết | PR có ID Task/FR | Thiếu liên kết |
| Đối chiếu phiếu ↔ diff | S2 trở lên | File vùng 🟡/🔴, test bị xoá, xoá cột/bảng không có trong phiếu |

**Luật chung**
- **Cấm** (xem [testing-rules](../../.ai/rules/testing-rules.md)) tắt lint/kiểm tra kiểu/test, hạ ngưỡng coverage, xoá hoặc làm yếu assertion, bỏ hook (`--no-verify`) để qua cổng.
- Bỏ một kiểm tra thường lệ phải giải thích trong báo cáo bàn giao.
- Sửa cổng và ngưỡng thuộc vùng 🔴, cần Task riêng.
- Chưa có CI thì chạy cổng **cục bộ** (hook hoặc lệnh tay), ghi kết quả thật vào báo cáo bàn giao; ghi miễn trừ có thời hạn thay vì bỏ qua âm thầm. Khi có CI, CI là nguồn kết quả chính thức.

**Coverage.** Không nên áp một con số coverage duy nhất cho tất cả module. Có thể đặt mục tiêu riêng cho logic nghiệp vụ, bảo mật, tiện ích và những phần ít rủi ro hơn.
<!-- Điền theo từng dự án: ngưỡng -->

**Review theo rủi ro.** Mức R1–R3; định nghĩa R1–R3 ở [project-rules](../../.ai/rules/project-rules.md) (Thang dùng chung), cách review ở Skill [code-review](../../.ai/skills/code-review/SKILL.md). R3 cần hai người, một người độc lập; nếu thiếu người thì ghi miễn trừ.

**Ví dụ chọn công cụ** (không bắt buộc, trừ E2E dùng Playwright cho mọi dự án): kiểm tra commit message dùng commitlint ở hook `commit-msg` của husky; dự án TypeScript dùng ESLint + Prettier, `tsc --strict`, Vitest/Jest, gitleaks, `npm audit`; dự án Python dùng ruff, mypy, pytest.

## 10. Môi trường test
Các môi trường dùng để test (local, CI, staging), cấu hình, dữ liệu và cách tạo/huỷ. Môi trường triển khai ở [deployment](../05-operations/deployment.md).
<!-- Điền theo từng dự án -->

## 11. Báo cáo kết quả
Phân biệt rõ pass / fail / skipped / not-run, kèm output thật làm bằng chứng. Báo cáo nêu số test, coverage, lỗi còn mở và test bị bỏ qua cùng lý do.

## 12. Definition of Done: điều kiện hoàn thành
Nguồn duy nhất của DoD; mẫu Task ([task-breakdown](../04-project-management/task-breakdown.md) mục 11) chỉ ghi thêm điều kiện riêng. Mỗi Task chỉ được đánh dấu hoàn thành khi:

- [ ] Đúng yêu cầu nghiệp vụ.
- [ ] Không vi phạm kiến trúc.
- [ ] Không vi phạm [coding-standards](coding-standards.md).
- [ ] Không vi phạm [security-standards](security-standards.md).
- [ ] Typecheck thành công (nếu ngôn ngữ hỗ trợ).
- [ ] Lint thành công.
- [ ] Unit tests thành công.
- [ ] Integration tests thành công nếu có liên quan.
- [ ] E2E tests thành công nếu có liên quan.
- [ ] Không có lỗi nghiêm trọng chưa xử lý.
- [ ] Code review được chấp thuận.
- [ ] Tài liệu được cập nhật.
- [ ] Có bằng chứng kiểm thử.

## 13. Tham khảo
Tài liệu về công cụ và chuẩn kiểm thử được dùng trong dự án.
<!-- Điền theo từng dự án -->
