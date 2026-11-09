# skills

Skill là **kỹ năng chuyên môn và quy trình làm việc của AI**. Khác với Rule:

- **Rule** trả lời: AI phải tuân thủ điều gì?
- **Skill** trả lời: AI phải thực hiện một loại công việc như thế nào?

Ví dụ, khi yêu cầu AI tạo API, không nên chỉ nói "hãy code API". Phải có Skill hướng dẫn AI từng bước:

1. Đọc yêu cầu nghiệp vụ.
2. Kiểm tra API specification.
3. Kiểm tra database schema.
4. Xác định quyền truy cập.
5. Thiết kế request/response.
6. Viết validation.
7. Viết service.
8. Viết API handler/controller.
9. Viết test.
10. Cập nhật tài liệu.
11. Báo cáo kết quả.

## Danh mục Skill nên xây dựng

| Skill | Nhiệm vụ |
| --- | --- |
| requirement-analysis | Phân tích yêu cầu |
| requirement-review | Kiểm tra tính đầy đủ của yêu cầu |
| architecture-design | Thiết kế kiến trúc |
| database-design | Thiết kế database |
| api-development | Phát triển API |
| frontend-development | Phát triển giao diện |
| backend-development | Phát triển backend |
| authentication-rbac | Xây dựng phân quyền |
| unit-testing | Viết unit test |
| integration-testing | Viết integration test |
| e2e-testing | Kiểm thử end-to-end |
| code-review | Review code |
| security-review | Kiểm tra bảo mật |
| bug-fixing | Điều tra và sửa lỗi |
| refactoring | Tái cấu trúc |
| documentation | Cập nhật tài liệu |
| deployment | Triển khai hệ thống |

Không cần xây dựng tất cả ngay lập tức. Nên xây dựng các Skill phục vụ công việc thực tế trước.

Đã tạo đủ 17 Skill trong danh mục (bản nháp, làm rõ dần theo Task thật): [requirement-analysis](requirement-analysis/SKILL.md), [requirement-review](requirement-review/SKILL.md), [architecture-design](architecture-design/SKILL.md), [database-design](database-design/SKILL.md), [api-development](api-development/SKILL.md), [frontend-development](frontend-development/SKILL.md), [backend-development](backend-development/SKILL.md), [authentication-rbac](authentication-rbac/SKILL.md), [unit-testing](unit-testing/SKILL.md), [integration-testing](integration-testing/SKILL.md), [e2e-testing](e2e-testing/SKILL.md), [code-review](code-review/SKILL.md), [security-review](security-review/SKILL.md), [bug-fixing](bug-fixing/SKILL.md), [refactoring](refactoring/SKILL.md), [documentation](documentation/SKILL.md), [deployment](deployment/SKILL.md).

## Cách tổ chức

- **Mỗi Skill một thư mục riêng**, `SKILL.md` là file bắt buộc. Không gộp nhiều Skill vào một file lớn.
- Khi cần, bổ sung vào thư mục của Skill đó: `checklist.md`, `examples.md`, `references/` (tài liệu tham chiếu), `scripts/` (script hỗ trợ). Chỉ thêm khi thực sự dùng.
- `SKILL.md` giữ quy trình **tổng quát**. Ví dụ và chi tiết gắn với dự án (vai trò, thực thể, công cụ cụ thể) nằm trong `examples.md`; ví dụ không phải nghiệp vụ chính thức.
- `SKILL.md` là nguồn chính của quy trình; file bổ sung không được mâu thuẫn với nó.
- Việc chọn và phối hợp nhiều Skill nằm ở [workflows/](../workflows/README.md), không nằm trong từng Skill.

## Ví dụ cấu trúc Skill

Một Skill có thể được lưu dưới dạng thư mục chứa `SKILL.md` và các tài liệu tham chiếu.

```text
.ai/
└── skills/
    ├── api-development/
    │   ├── SKILL.md
    │   ├── checklist.md
    │   └── examples.md
    │
    ├── database-design/
    │   ├── SKILL.md
    │   └── checklist.md
    │
    └── code-review/
        ├── SKILL.md
        └── review-checklist.md
```

Cấu trúc trên đã được tạo ở dạng bản nháp (Draft); nội dung sẽ được làm rõ dần theo Task thật.

## Một Skill tốt phải có đủ

> Lưu ý: thiếu bất kỳ mục nào dưới đây thì Skill chưa đạt, chưa được chuyển sang Approved.

- Mục tiêu.
- Điều kiện đầu vào.
- Điều kiện đầu ra.
- Quy trình thực hiện.
- Checklist.
- Tiêu chí hoàn thành.
- Những việc không được phép làm.

## Skill không đồng nghĩa với Prompt

- **Prompt** là yêu cầu cụ thể trong một lần làm việc.
- **Skill** là quy trình có thể tái sử dụng nhiều lần.

| Thành phần | Ví dụ |
| --- | --- |
| Prompt | Tạo API đăng tin bất động sản. |
| Skill | Quy trình chuẩn để phát triển API. |
| Rule | API phải kiểm tra quyền ở backend. |
| Documentation | Mô tả nghiệp vụ đăng tin và phân quyền. |

Bốn thành phần này phối hợp với nhau để tạo ra kết quả nhất quán.

## Quy chuẩn sử dụng Skill

### Chọn và phối hợp Skill

Không yêu cầu AI đọc và dùng cả 17 Skill trong mọi Task; chọn theo loại công việc. Một Task có thể cần nhiều Skill phối hợp: có Skill chạy song song, có Skill được kích hoạt lặp lại khi phát hiện lỗi.

Quy trình chi tiết nằm ở [.ai/workflows/](../workflows/README.md):

- [skill-selection.md](../workflows/skill-selection.md): bảng "công việc → Skill" và chuỗi Skill theo loại Task (T1–T13).
- [skill-orchestration.md](../workflows/skill-orchestration.md): nhận diện Task, lập chuỗi Skill, cổng vào/ra, vòng lặp khi lỗi, bàn giao.

### Năm nguyên tắc kỹ thuật khi đưa Skill vào thực tế

1. **Skill không thay thế Rule.**
   - `authentication-rbac` hướng dẫn cách triển khai phân quyền.
   - [security-rules.md](../rules/security-rules.md) quy định mọi ERP API phải được bảo vệ ở backend.
2. **Skill không thay thế tài liệu nghiệp vụ.** AI phải đọc FR/BR trước khi triển khai. Không được lấy ví dụ trong Skill làm nghiệp vụ chính thức.
3. **Skill phải có phiên bản và được kiểm thử.** Khi cập nhật Skill, kiểm tra bằng một số Task thực tế để xác định AI có làm đúng hướng dẫn không.
4. **Skill có thể gọi Skill khác.** Ví dụ `backend-development` có thể yêu cầu sử dụng `unit-testing` và `security-review` khi cần. Quan hệ này được khai báo trong [skill-orchestration.md](../workflows/skill-orchestration.md) (mục "Skill gọi Skill khác"), không chép vào từng `SKILL.md`.
5. **Không phải Skill nào cũng được phép tự thực hiện hành động.**
   - `deployment` chỉ chuẩn bị và kiểm tra release; deploy production vẫn phải có phê duyệt.
   - `database-design` được tạo migration; chạy migration trên production phải tuân thủ quy trình phê duyệt.

## Nguyên tắc tạo Skill

- Chỉ tạo khi quy trình đã ổn định; không tạo skill chỉ để đặt tên cho một prompt ngắn.
- Skill mới phải chạy thử trên Task thật trước khi chuyển Approved.
- Sửa skill thuộc vùng 🔴: cần Task riêng và người duyệt.
