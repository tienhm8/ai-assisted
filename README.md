# AI-Assisted Software Engineering System

Hệ thống kỹ nghệ phần mềm có AI tham gia xuyên suốt vòng đời phát triển. Nguyên tắc chung: **AI soạn nháp (`Draft`), người có thẩm quyền duyệt (`Approved`)**; chỉ sang giai đoạn sau khi giai đoạn trước đã được duyệt.

README là **bản đồ** của repo: nói hệ thống làm gì, tài liệu nằm ở đâu, ai quyết gì.

## Cấu trúc

Mỗi thư mục có README riêng ghi người quyết và điều kiện sang bước sau. Tên giai đoạn vòng đời ghi cạnh thư mục.

```text
project/
├── README.md                    bản đồ của repo
├── CHECKLIST.md                 việc cần làm khi áp dụng khung
├── PROJECT.md                   (Chuẩn bị ngữ cảnh AI) khai báo giá trị riêng của dự án (mức tự chủ, vùng, dữ liệu, S, vai trò, miễn trừ)
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
│   ├── 00-project-overview/     (Khám phá sản phẩm) làm gì, cho ai, ranh giới ở đâu?
│   ├── 01-requirements/         (Yêu cầu) phải làm gì, nghiệm thu ra sao?
│   ├── 02-architecture/         (Thiết kế) xây thế nào, đã chốt quyết định nào?
│   ├── 03-engineering/          (Chuẩn bị ngữ cảnh AI, Kiểm thử) code, bảo mật, lỗi, test theo chuẩn nào? kiểm soát AI ra sao?
│   ├── 04-project-management/   (Chuẩn bị ngữ cảnh AI, Cải tiến) làm gì trước, chia Task ra sao, qua cổng nào?
│   └── 05-operations/           (Phát hành và vận hành) phát hành, giám sát, khôi phục thế nào?
│
└── .ai/                         AI làm gì, làm thế nào (dạng mệnh lệnh, không chứa giá trị riêng của dự án)
    ├── README.md                bản đồ của .ai/
    ├── guide/                   tài liệu khung cho người
    ├── rules/                   BẮT BUỘC: AI phải / không được làm gì?
    ├── skills/                  CÁCH LÀM: làm một loại việc thì làm thế nào?
    ├── agents/                  VAI: ai làm, với quyền gì? (mặc định một AI Coding Agent)
    ├── workflows/               ĐIỀU PHỐI: chọn Skill, xếp thứ tự, dừng ở đâu?
    ├── templates/               MẪU: kết quả trình bày dưới dạng nào?
    ├── plans/                   Plan do AI soạn, Tech Lead duyệt: mỗi Plan một thư mục (PLAN.md, tasks/*.yaml, runs.md), được commit
```

Danh mục Rule và Skill: [rules/](.ai/rules/README.md), [skills/](.ai/skills/README.md).

## Giai đoạn và người duyệt

Tám cổng duyệt giữa các giai đoạn (Khai báo dự án, Phạm vi, Yêu cầu, Thiết kế, Sẵn sàng giao việc, Code xong, Sẵn sàng phát hành, Vận hành) và ba độ nghiêm ngặt (gọn, chuẩn, nghiêm ngặt): [gates-and-rigor.md](.ai/guide/gates-and-rigor.md).

| Giai đoạn | Người duyệt |
| --- | --- |
| Khám phá sản phẩm (Product Discovery) | PO (Đại diện khách hàng cung cấp nguồn, duyệt phạm vi qua Đầu mối) |
| Yêu cầu (Requirements Engineering) | PO/BA (QA rà khả năng kiểm thử; Đại diện khách hàng trả lời câu hỏi, duyệt yêu cầu qua Đầu mối) |
| Thiết kế (System Design) | Kiến trúc sư (thêm Security nếu đụng tới tiền, phân quyền, dữ liệu cá nhân, migration) |
| Chuẩn bị ngữ cảnh AI (AI Context & Governance) | Tech Lead |
| Lập trình (Implementation) | Tech Lead |
| Kiểm thử (Quality Engineering) | Tech Lead |
| Phát hành và vận hành (Delivery & Operations) | Owner (tham khảo Tech Lead; DevOps thực hiện; AI không tự deploy) |
| Cải tiến (Continuous Improvement) | Tech Lead |

## Bắt đầu

Làm theo [CHECKLIST.md](CHECKLIST.md) trước, rồi đọc [.ai/guide/getting-started.md](.ai/guide/getting-started.md).