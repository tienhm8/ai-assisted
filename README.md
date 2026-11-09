# AI-Assisted Software Engineering System

Hệ thống kỹ nghệ phần mềm có AI tham gia xuyên suốt vòng đời phát triển.

README là **bản đồ** của repo: nói hệ thống làm gì, tài liệu nằm ở đâu, ai quyết gì. Không chứa quy tắc chi tiết, chi tiết nằm ở file được trỏ tới. Khung (`docs/`, `.ai/`) dùng chung cho mọi dự án; phần riêng của từng dự án nằm ở [PROJECT.md](PROJECT.md).

| Bạn đang… | Đọc |
| --- | --- |
| Mới vào repo, muốn hiểu tổng thể | Vòng đời phát triển có AI, Cấu trúc tài liệu |
| Áp dụng cho dự án mới hoặc đã có | Bắt đầu từ đâu, [PROJECT.md](PROJECT.md) |
| Giao việc cho AI | Các thành phần để AI làm việc, Kiểm soát AI |
| Tìm người duyệt và điều kiện duyệt | Mục đích từng nhóm tài liệu |
| Chọn hoặc đổi công cụ AI | Công cụ AI |

## Cấu trúc tài liệu

```text
project/
├── README.md
├── PROJECT.md                   hồ sơ riêng của dự án (công cụ AI, mức dữ liệu, mức tự chủ)
├── docs/
│   ├── 00-project-overview/     vision.md · scope.md · glossary.md
│   ├── 01-requirements/         BRD.md · FR/ · NFR.md · business-rules.md · acceptance-criteria.md
│   ├── 02-architecture/         system-architecture.md · module-design.md · database-design.md · api-design.md · ADR/
│   ├── 03-engineering/          coding-standards.md · security-standards.md · error-handling.md · testing-strategy.md
│   ├── 04-project-management/   roadmap.md · backlog.md · task-breakdown.md · ai-kpi.md
│   └── 05-operations/           deployment.md · monitoring.md · backup-recovery.md
├── .ai/                         rules/ · skills/ · agents/ · workflows/ · templates/ · plans/ · worktrees/   (nguồn chuẩn, độc lập công cụ)
└── AGENTS.md · CLAUDE.md · .github/copilot-instructions.md   (điểm tích hợp, chỉ tham chiếu .ai/)
```

## Vòng đời phát triển có AI

AI tham gia ở từng giai đoạn, nhưng con người vẫn chịu trách nhiệm về quyết định nghiệp vụ, kiến trúc, bảo mật và vận hành.

| # | Giai đoạn | Nội dung | Tài liệu đầu ra |
| --- | --- | --- | --- |
| 01 | Product Discovery | Business requirements, vision, scope, stakeholders | [00-project-overview](docs/00-project-overview/) |
| 02 | Requirements Engineering | BRD, FR, NFR, user story, acceptance criteria | [01-requirements](docs/01-requirements/) |
| 03 | System Design | Kiến trúc, database, API, security, ADR | [02-architecture](docs/02-architecture/) |
| 04 | AI Context & Governance | Rules, skills, agents, context, knowledge base | [PROJECT.md](PROJECT.md); [03-engineering](docs/03-engineering/); [.ai](.ai/) |
| 05 | Implementation | AI: lên plan + coding worktree, human review, Git | [04-project-management](docs/04-project-management/); [.ai/plans](.ai/plans/); [.ai/worktrees](.ai/worktrees/) |
| 06 | Quality Engineering | Unit, integration, E2E, security, regression | [testing-strategy](docs/03-engineering/testing-strategy.md) |
| 07 | Delivery & Operations | CI/CD, deploy, monitoring, logging, rollback | [05-operations](docs/05-operations/) |
| 08 | Continuous Improvement | Feedback, phân tích lỗi, cập nhật rule/skill | [ai-kpi.md](docs/04-project-management/ai-kpi.md) (số liệu); cập nhật [.ai/](.ai/) |

## Mục đích từng nhóm tài liệu

AI tham gia xuyên suốt: ở mỗi nhóm AI soạn nháp, phân tích hoặc thực hiện, còn người quyết duyệt rồi mới sang nhóm sau. Làm theo thứ tự từ trên xuống; mỗi thư mục ứng với giai đoạn ở bảng "Vòng đời phát triển có AI".

| Thư mục | Trả lời câu hỏi | AI làm | Người quyết và điều kiện duyệt |
| --- | --- | --- | --- |
| [PROJECT.md](PROJECT.md) | Dự án này dùng công cụ AI nào, mức dữ liệu và mức tự chủ ra sao? | Soạn nháp khi được yêu cầu "tạo/cập nhật PROJECT.md" | Tech Lead: thông tin dự án, công cụ AI đã điền |
| `00-project-overview` | Làm gì, cho ai, ranh giới ở đâu, dùng thuật ngữ nào? | Soạn nháp vision, scope, thuật ngữ | PO: Vision và Scope ở trạng thái Approved, câu hỏi mở được ghi |
| `01-requirements` | Hệ thống phải làm gì, theo quy tắc nào, nghiệm thu ra sao? | Phân tích yêu cầu, phát hiện chỗ thiếu | PO/BA: mọi yêu cầu chức năng (FR) trong phạm vi có tiêu chí nghiệm thu (AC) kiểm thử được |
| `02-architecture` | Xây thế nào, quyết định kiến trúc nào đã chốt? | Đề xuất phương án, soạn ADR và thiết kế | Kiến trúc sư (thêm Security nếu thiết kế đụng tới tiền, phân quyền, dữ liệu cá nhân, migration): thiết kế Approved, có ADR cho quyết định lớn. |
| `03-engineering` + [.ai/](.ai/README.md) | Code, bảo mật, lỗi, test theo chuẩn nào? AI phải tuân thủ gì? | Tuân thủ Rules, dùng Skills; viết và chạy test | Tech Lead: các chuẩn code, bảo mật, lỗi, test đã được điền cho dự án trước khi giao Task đầu tiên |
| `04-project-management` | Làm gì trước, chia Task ra sao? Có tốt lên không? | Chia Task từ plan đã duyệt (plan nằm ở [.ai/plans/](.ai/plans/)); tổng hợp số liệu, đề xuất sửa rule/skill | Tech Lead: mỗi Task có mục tiêu, phạm vi làm/không làm, tiêu chí nghiệm thu, mức rủi ro, mức tự chủ của AI |
| `05-operations` | Phát hành, giám sát, khôi phục thế nào? | Soạn release note, phân tích log và sự cố; không tự deploy | Owner (tham khảo Tech Lead; DevOps thực hiện): smoke test đạt, không có sự cố nghiêm trọng, rollback dùng được |

Lưu ý khi áp dụng:
- Dự án đã có code: AI chỉ mô tả hiện trạng (trạng thái `Draft`), người xác nhận mới `Approved`; Task mới có thể bắt đầu ngay khi nhóm `04` sẵn sàng.
- Mặc định dùng một AI Coding Agent nhiều mũ; chỉ tách thành nhiều agent riêng khi vai trò và bàn giao đã ổn định (xem [.ai/agents/](.ai/agents/README.md)).
- Chưa có nơi chạy CI/CD thì chạy kiểm tra tự động cục bộ và ghi miễn trừ có thời hạn trong `PROJECT.md`, không bỏ qua âm thầm.
- Thời gian tuỳ quy mô codebase và nhân sự. Khác với `docs/04-project-management/roadmap.md` (lộ trình sản phẩm theo FR).

## Các thành phần để AI làm việc

Kiến thức về dự án nằm ở `docs/`; kiểm thử và CI/CD ở [testing-strategy.md](docs/03-engineering/testing-strategy.md) và [deployment.md](docs/05-operations/deployment.md). Phần dành riêng cho AI:

| Thành phần | Mục đích | Ví dụ | Nằm ở |
| --- | --- | --- | --- |
| Rules | Quy tắc bắt buộc | Coding conventions | `.ai/rules/` |
| Skills | Quy trình chuyên môn | API development | `.ai/skills/` |
| Agents | Vai trò thực hiện | Backend Developer | `.ai/agents/` |
| Workflows | Điều phối nhiều bước | Chọn Skill theo Task, phát hành | `.ai/workflows/` |
| Context | Đúng tài liệu, đúng phạm vi; không bắt AI đọc cả dự án | Module đang làm | Task, [plan](.ai/plans/); thứ tự nạp: [skill-orchestration.md](.ai/workflows/skill-orchestration.md) §2 |
| Plans | Cầu nối từ đặc tả sang Task; lưu kế hoạch và kết quả; AI soạn, Tech Lead duyệt | Chia tính năng thành Task, kế hoạch kiểm chứng | `.ai/plans/` (được commit) |
| Worktrees | Môi trường cô lập, mỗi Task một nơi; AI code và test ở đây theo plan, bàn giao kèm bằng chứng test thật | Nhánh riêng cho từng Task | `.ai/worktrees/` (không commit) |
| Tools | Công cụ thực thi | Terminal, Git, Browser | Khai báo và cấp quyền trong `PROJECT.md` |

Rule, Skill và Agent khác nhau: Rule là **điều bắt buộc**, Skill là **cách làm một loại việc**, Agent là **vai thực hiện**. Skill cũng không phải Prompt: Prompt là yêu cầu một lần, Skill là quy trình tái sử dụng (danh mục và ví dụ: [.ai/skills/](.ai/skills/README.md)).

## Kiểm soát AI

**Nguyên tắc:** AI không tự suy diễn quy tắc nghiệp vụ và không tự ý đổi kiến trúc khi chưa được phê duyệt. Mức tự chủ và bản đồ vùng 🟢🟡🔴 của dự án ghi trong `PROJECT.md`; mức tối đa theo loại việc ở [.ai/agents/](.ai/agents/README.md).

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
- **Kiểm chứng:** sau mỗi lần đổi công cụ hoặc phiên bản, chạy một Task thử để chắc công cụ nạp đúng hướng dẫn.

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
- **Mã định danh:** `FR-<MODULE>-<NN>` · `BR-<MODULE>-<NN>` · `NFR-<NN>` · `<FR>-AC<N>` · `ADR-<NNNN>` · Task `<KEY>-<N>`.
- **Một nơi duy nhất:** mỗi quy tắc, quyết định hoặc trạng thái chỉ có một nơi quản lý chính thức; nơi khác chỉ tham chiếu. Không để hai tài liệu quy định cùng nội dung nhưng mâu thuẫn.
- **Chưa có đặc tả và tiêu chí nghiệm thu (AC) thì chưa code.** AC là điều kiện kiểm thử được để biết một yêu cầu chức năng đã làm đúng hay chưa. Chưa có thiết kế Approved thì không triển khai tính năng.
- **Thay đổi có lý do:** đổi Rule phải có lý do, đổi Skill phải có lịch sử, quyết định kiến trúc ghi thành ADR ([docs/02-architecture/ADR/](docs/02-architecture/ADR/README.md)). AI không tự đổi Rule cấp dự án khi làm Task thông thường.
- **Cập nhật tài liệu khi hệ thống thay đổi.**
- Tài liệu hoá tương xứng với rủi ro: gộp hoặc bỏ file không cần cho quy mô dự án, ghi lý do trong `PROJECT.md`.

## Bắt đầu từ đâu

1. Yêu cầu AI "tạo/cập nhật PROJECT.md cho dự án …": [PROJECT.md](PROJECT.md) là mẫu trống, chỉ điền khi có yêu cầu này. Dự án đã có: điền theo hiện trạng, AI chỉ mô tả (`Draft`), người xác nhận mới `Approved`.
2. Chọn công cụ AI, tạo file tích hợp mỏng (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, …) trỏ về `.ai/`.
3. Điền `docs/00-project-overview/` để PO duyệt, rồi đi tiếp `01-requirements` → `02-architecture` → lập plan và Task.
