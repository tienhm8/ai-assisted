# AI-Assisted Software Engineering System

Hệ thống kỹ nghệ phần mềm có AI tham gia xuyên suốt vòng đời phát triển. Nguyên tắc chung: **AI soạn nháp (`Draft`), người có thẩm quyền duyệt (`Approved`)**; chỉ sang giai đoạn sau khi giai đoạn trước đã được duyệt.

README là **bản đồ** của repo: nói hệ thống làm gì, tài liệu nằm ở đâu, ai quyết gì.

## Cấu trúc

Mỗi thư mục có README riêng ghi người quyết và điều kiện sang bước sau. `[01]`–`[08]` là giai đoạn vòng đời.

```text
project/
├── README.md                    bản đồ của repo
├── PROJECT.md                   [04] khai báo giá trị riêng của dự án (mức tự chủ, vùng, dữ liệu, S, vai trò, miễn trừ)
├── AGENTS.md                    điểm vào cho AI, chỉ trỏ về .ai/
├── CLAUDE.md                    chỉ chứa @AGENTS.md cho Claude Code
├── ai-config.yaml               model/effort theo loại việc, ngân sách, stack, lệnh kiểm
├── project/                     mã nguồn các repo con; mỗi repo tự commit, repo cha không theo dõi (.gitignore)
│
├── .claude/                     cấu hình Claude Code
│   ├── settings.json            cấu hình worktree
│   └── worktrees/               worktree của AI (không commit)
│
├── docs/                        hồ sơ dự án cho cả người và AI; người không dùng AI chỉ đọc docs/
│   ├── getting-started.md       hướng dẫn áp dụng khung cho dự án mới và dự án cũ
│   ├── 00-project-overview/     [01] làm gì, cho ai, ranh giới ở đâu?
│   ├── 01-requirements/         [02] phải làm gì, nghiệm thu ra sao?
│   ├── 02-architecture/         [03] xây thế nào, đã chốt quyết định nào?
│   ├── 03-engineering/          [04][06] code, bảo mật, lỗi, test theo chuẩn nào? kiểm soát AI ra sao?
│   ├── 04-project-management/   [04][08] làm gì trước, chia Task ra sao, qua cổng nào?
│   └── 05-operations/           [07] phát hành, giám sát, khôi phục thế nào?
│
└── .ai/                         AI làm gì, làm thế nào (dạng mệnh lệnh, không chứa giá trị riêng của dự án)
    ├── README.md                bản đồ của .ai/
    ├── rules/                   BẮT BUỘC: AI phải / không được làm gì?
    ├── skills/                  CÁCH LÀM: làm một loại việc thì làm thế nào?
    ├── agents/                  VAI: ai làm, với quyền gì? (mặc định một AI Coding Agent)
    ├── workflows/               ĐIỀU PHỐI: chọn Skill, xếp thứ tự, dừng ở đâu?
    ├── templates/               MẪU: kết quả trình bày dưới dạng nào?
    ├── plans/                   Plan do AI soạn, Tech Lead duyệt: mỗi Plan một thư mục (PLAN.md, tasks/*.yaml, runs.md), được commit
```

Danh mục Rule và Skill: [rules/](.ai/rules/README.md), [skills/](.ai/skills/README.md).

## Giai đoạn và người duyệt

Cổng G0–G7 giữa các giai đoạn và độ nghiêm ngặt S1–S3: [gates-and-rigor.md](docs/04-project-management/gates-and-rigor.md).

| Giai đoạn | Người duyệt |
| --- | --- |
| `[01]` Product Discovery | PO (Đại diện khách hàng cung cấp nguồn, duyệt phạm vi qua Đầu mối) |
| `[02]` Requirements Engineering | PO/BA (QA rà khả năng kiểm thử; Đại diện khách hàng trả lời câu hỏi, duyệt yêu cầu qua Đầu mối) |
| `[03]` System Design | Kiến trúc sư (thêm Security nếu đụng tới tiền, phân quyền, dữ liệu cá nhân, migration) |
| `[04]` AI Context & Governance | Tech Lead |
| `[05]` Implementation | Tech Lead |
| `[06]` Quality Engineering | Tech Lead |
| `[07]` Delivery & Operations | Owner (tham khảo Tech Lead; DevOps thực hiện; AI không tự deploy) |
| `[08]` Continuous Improvement | Tech Lead |

## Bắt đầu

Xem [docs/getting-started.md](docs/getting-started.md)