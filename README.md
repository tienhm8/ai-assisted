# AI-Assisted Software Engineering System

Hệ thống kỹ nghệ phần mềm có AI tham gia xuyên suốt vòng đời phát triển.

README là **bản đồ** của repo: nói hệ thống làm gì, tài liệu nằm ở đâu, ai quyết gì.

| Bạn đang… | Đọc |
| --- | --- |
| Tổng quan | Cấu trúc tài liệu |
| Áp dụng dự án | [PROJECT.md](PROJECT.md) |
| Giao việc cho AI | Cấu trúc tài liệu (`.ai/`), Kiểm soát AI |
| Điều kiện duyệt | Cấu trúc tài liệu (danh sách giai đoạn và người duyệt) |
| Công cụ AI | Công cụ AI |

## Cấu trúc tài liệu
Nguyên tắc chung: **AI soạn nháp (`Draft`), người có thẩm quyền duyệt (`Approved`)**; chỉ sang giai đoạn sau khi giai đoạn trước đã được duyệt.

Ký hiệu `[01]`–`[08]` trong cây là giai đoạn của vòng đời (kèm người duyệt):

- `[01]` Product Discovery, duyệt: PO
- `[02]` Requirements Engineering, duyệt: PO/BA (QA rà khả năng kiểm thử)
- `[03]` System Design, duyệt: Kiến trúc sư (thêm Security nếu đụng tới tiền, phân quyền, dữ liệu cá nhân, migration)
- `[04]` AI Context & Governance, duyệt: Tech Lead
- `[05]` Implementation, duyệt: Tech Lead
- `[06]` Quality Engineering, duyệt: Tech Lead
- `[07]` Delivery & Operations, duyệt: Owner (tham khảo Tech Lead; DevOps thực hiện; AI không tự deploy)
- `[08]` Continuous Improvement, duyệt: Tech Lead

```text
project/
├── README.md                          bản đồ của repo
├── PROJECT.md                         [04] công cụ AI, mức dữ liệu, mức tự chủ, bản đồ vùng 🟢🟡🔴
│
├── docs/                              hồ sơ dự án (mỗi dự án viết riêng)
│   │
│   ├── 00-project-overview/           [01] làm gì, cho ai, ranh giới ở đâu?
│   │   ├── vision.md                  vấn đề cần giải quyết, đối tượng dùng, kết quả đo được
│   │   ├── scope.md                   trong phạm vi, ngoài phạm vi, ràng buộc
│   │   ├── glossary.md                thuật ngữ thống nhất cho người và AI
│   │   └── open-questions.md          câu hỏi mở và giả định (OQ-NN)
│   │
│   ├── 01-requirements/               [02] phải làm gì, nghiệm thu ra sao?
│   │   ├── BRD.md                     yêu cầu nghiệp vụ (BRQ-NN)
│   │   ├── FR/                        yêu cầu chức năng, mỗi module một file (FR-MODULE-NN)
│   │   ├── NFR.md                     yêu cầu phi chức năng, đo được
│   │   ├── business-rules.md          quy tắc nghiệp vụ (BR-MODULE-NN)
│   │   └── acceptance-criteria.md     tiêu chí nghiệm thu (FR-AC)
│   │
│   ├── 02-architecture/               [03] xây thế nào, đã chốt quyết định nào?
│   │   ├── system-architecture.md     kiến trúc tổng thể, công nghệ, xác thực và phân quyền
│   │   ├── module-design.md           module, trách nhiệm, phụ thuộc
│   │   ├── database-design.md         lược đồ dữ liệu, ràng buộc, migration
│   │   ├── api-design.md              hợp đồng API
│   │   └── ADR/                       mỗi quyết định kiến trúc lớn một file (ADR-NNNN)
│   │
│   ├── 03-engineering/                [04] chuẩn code, bảo mật, lỗi, test
│   │   ├── coding-standards.md        ngôn ngữ, naming, cấu trúc code, Git
│   │   ├── security-standards.md      bảo mật, mức dữ liệu D0-D3, secret
│   │   ├── error-handling.md          phân loại lỗi, mã lỗi, log
│   │   └── testing-strategy.md        [06] các tầng test, cổng chất lượng
│   │
│   ├── 04-project-management/         [05] làm gì trước, chia Task ra sao?
│   │   ├── roadmap.md                 lộ trình theo mốc
│   │   ├── backlog.md                 danh sách việc, ưu tiên, rủi ro
│   │   ├── task-breakdown.md          cách chia Task, mẫu Task giao cho AI
│   │   └── ai-kpi.md                  [08] đo hiệu quả AI
│   │
│   └── 05-operations/                 [07] phát hành, giám sát, khôi phục
│       ├── deployment.md              môi trường, CI/CD, phát hành, rollback
│       ├── monitoring.md              giám sát, cảnh báo
│       └── backup-recovery.md         sao lưu, khôi phục (RPO/RTO)
│
├── .ai/                               quy trình AI làm việc
│   ├── rules/                         BẮT BUỘC: AI phải / không được làm gì?
│   │   └── project · architecture · coding · database · security · testing · git-workflow  (-rules.md)
│   ├── skills/                        CÁCH LÀM: làm một loại việc thì làm thế nào?
│   │   ├── [01] product-discovery
│   │   ├── [02] requirement-analysis · requirement-review
│   │   ├── [03] architecture-design · database-design
│   │   ├── [05] task-planning · api-development · backend-development · frontend-development
│   │   │        authentication-rbac · bug-fixing · refactoring
│   │   ├── [06] unit-testing · integration-testing · e2e-testing · code-review · security-review
│   │   ├── [07] deployment · incident-analysis · documentation
│   │   └── [08] continuous-improvement
│   ├── agents/                        VAI: ai làm, với quyền gì? (mặc định một AI Coding Agent)
│   ├── workflows/                     ĐIỀU PHỐI: chọn Skill, xếp thứ tự, dừng ở đâu?
│   │   └── task-execution · skill-selection · skill-orchestration · release-workflow
│   ├── templates/                     MẪU: kết quả trình bày dưới dạng nào?
│   │   └── PLAN · BUG · PR · DELIVERY-REPORT · TEST-REPORT · RELEASE-REPORT  (-TEMPLATE.md)
│   ├── plans/                         [05] kế hoạch do AI soạn, Tech Lead duyệt (được commit)
│   └── worktrees/                     [05] môi trường cô lập, mỗi Task một nơi (không commit)
│
└── AGENTS.md · CLAUDE.md · .github/copilot-instructions.md   điểm tích hợp công cụ, chỉ trỏ về .ai/
```

Lưu ý khi áp dụng:
- Task mới bắt đầu khi giai đoạn `[04]` sẵn sàng.
- Mặc định dùng một AI Coding Agent; chỉ tách thành nhiều agent riêng khi vai trò và bàn giao đã ổn định (xem [.ai/agents/](.ai/agents/README.md)).
- Chưa có CI/CD: chạy kiểm tra tự động tại máy và ghi miễn trừ có thời hạn vào `PROJECT.md` (không bỏ qua âm thầm).
- **Context:** chỉ nạp đúng tài liệu cho Task, không bắt AI đọc cả dự án; nạp gì theo loại Task ở [context-loading.md](.ai/workflows/context-loading.md), thứ tự nạp ở [skill-orchestration.md](.ai/workflows/skill-orchestration.md) §2.
- **Tools** (Terminal, Git, Browser): khai báo và cấp quyền trong `PROJECT.md`.

## Kiểm soát AI

**Nguyên tắc:** AI không tự suy diễn quy tắc nghiệp vụ và không tự ý đổi kiến trúc khi chưa được phê duyệt. Mức tự chủ và bản đồ vùng 🟢🟡🔴 của dự án ghi trong `PROJECT.md`; mức tối đa (trần) theo loại việc × rủi ro ở `PROJECT.md` §3.1 (vai ở [.ai/agents/](.ai/agents/README.md) không có mức riêng).

### Việc cần người duyệt hoặc kiểm soát đặc biệt

| Hành động | Mức kiểm soát |
| --- | --- |
| Thay đổi kiến trúc, thay đổi RBAC | Phải được duyệt |
| Migration dữ liệu production | Phải được duyệt |
| Deploy production | Có approval, AI không tự deploy |
| Quản lý secrets | Không giao AI tùy ý |
| Xóa dữ liệu | Cần kiểm soát đặc biệt |

Các việc còn lại (đọc code, phân tích yêu cầu, viết code, viết test, sửa lỗi) AI làm trong phạm vi Task theo mức tự chủ được cấp.

### Năm rủi ro cần quản lý

| # | Rủi ro | Biểu hiện |
| --- | --- | --- |
| 1 | Hallucination | AI tự tạo ra nghiệp vụ, API hoặc thư viện không tồn tại |
| 2 | Context Drift | AI làm theo quyết định cũ hoặc tài liệu không còn hiệu lực |
| 3 | Security Vulnerability | Code chạy được nhưng có lỗ hổng |
| 4 | Overengineering | AI xây dựng phức tạp hơn yêu cầu |
| 5 | False Confidence | AI báo hoàn thành nhưng chưa chạy test hoặc chưa kiểm tra hết trường hợp |

Cách khắc phục không phải chỉ viết Prompt tốt hơn, mà phải có **tài liệu chuẩn** (`docs/`), **Rule** và **Skill** (`.ai/`), **CI/CD**, **Test** và **quyền hạn rõ ràng** (mức tự chủ và bản đồ vùng trong `PROJECT.md`).

## Công cụ AI

Không cần dùng nhiều công cụ; quan trọng là phối hợp tốt. Mỗi công cụ có cấu trúc file riêng và có thể đổi theo phiên bản, nên:

- **Một nguồn chuẩn:** Rule và Skill nằm ở `.ai/`, độc lập công cụ (đổi tên thư mục theo công cụ).
- **File tích hợp mỏng:** mỗi công cụ chỉ có file trỏ về `.ai/`, không chép lại nội dung. Cần vị trí riêng thì dùng symlink hoặc script đồng bộ.
- **Công cụ chính:** chọn một, ghi trong `PROJECT.md`; công cụ khác dùng cho việc chuyên biệt.
- **Kiểm chứng:** sau mỗi lần đổi công cụ hoặc phiên bản, chạy thử một Task để chắc chắn đúng hướng dẫn.

Ví dụ (không bắt buộc):

| Công cụ | Cách cấu hình thường dùng |
| --- | --- |
| Cursor | `.cursor/rules/` |
| Claude Code | `CLAUDE.md`, `.claude/skills/` |
| Codex | `AGENTS.md`, cấu hình và Skills tương thích |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/` |

Nhóm công cụ cần có: AI Coding IDE hoặc Agent, quản lý source (Git), kiểm thử, CI/CD, giám sát chất lượng và runtime. Công cụ cụ thể do từng dự án chọn.

## Quy ước làm việc với tài liệu

- **Trạng thái tài liệu:** Draft → In Review → Approved → Deprecated. Chỉ người có thẩm quyền chuyển sang Approved; AI không tự chốt.
- **Mã định danh:** `FR-<MODULE>-<NN>` · `BRQ-<NN>` · `BR-<MODULE>-<NN>` · `NFR-<NN>` · `OUT-<NN>` · `OQ-<NN>` · `<FR>-AC<N>` · `ADR-<NNNN>` · Task `<KEY>-<N>`.
- **Truy vết một chiều khai báo:** FR giữ liên kết tới BRQ và BR (bảng FR); AC trỏ tới FR (và BR); BRD, business-rules chỉ tham chiếu ngược.
- **Một nơi duy nhất:** mỗi quy tắc, quyết định hoặc trạng thái chỉ có một nơi quản lý chính thức; nơi khác chỉ tham chiếu. Không để hai tài liệu quy định cùng nội dung nhưng mâu thuẫn.
- **Chưa có đặc tả và tiêu chí nghiệm thu (AC) thì chưa code.** AC là điều kiện kiểm thử được để biết một yêu cầu chức năng đã làm đúng hay chưa. Chưa có thiết kế Approved thì không triển khai tính năng.
- **Thay đổi có lý do:** đổi Rule phải có lý do, đổi Skill phải có lịch sử, quyết định kiến trúc ghi thành ADR ([docs/02-architecture/ADR/](docs/02-architecture/ADR/README.md)). AI không tự đổi Rule cấp dự án khi làm Task thông thường.
- **Cập nhật tài liệu khi hệ thống thay đổi.**
- Tài liệu hoá tương xứng với rủi ro: gộp hoặc bỏ file không cần cho quy mô dự án, ghi lý do trong `PROJECT.md`.

## Bắt đầu từ đâu

1. Yêu cầu AI "tạo/cập nhật PROJECT.md cho dự án …": [PROJECT.md](PROJECT.md) là mẫu trống, chỉ điền khi có yêu cầu này. Dự án đã có: điền theo hiện trạng, AI chỉ mô tả (`Draft`), người xác nhận mới `Approved`.
2. Chọn công cụ AI, tạo file tích hợp mỏng (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, …) trỏ về `.ai/`.
3. Điền `docs/00-project-overview/` để PO duyệt, rồi đi tiếp `01-requirements` → `02-architecture` → lập plan và Task.
