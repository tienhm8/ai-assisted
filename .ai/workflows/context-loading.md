# Context Loading: nạp gì, ở bước nào

> Trạng thái: **Approved**. Sửa file này thuộc vùng 🔴: cần Task riêng và người duyệt.

Nguồn chuẩn duy nhất cho câu hỏi: **một Task nạp Rule, Skill, Vai, Workflow, Template nào, nạp ở bước nào, và chạy bằng hạng model, effort nào**. Các workflow khác chỉ trỏ tới đây.

**Nguyên tắc: nạp đúng lúc cần, không nạp trước.** Nạp thừa làm tốn context và khiến AI áp nhầm quy tắc của việc khác. Nạp thiếu khiến AI làm sai quy tắc. Mỗi bước chỉ nạp phần phục vụ quyết định của bước đó.

## 1. Ba mức nạp Skill

| Mức | Nạp phần nào của `SKILL.md` | Dùng để |
| --- | --- | --- |
| **S0 · Danh mục** | Chỉ `name` + `description` (frontmatter) | Chọn Skill, xếp chuỗi |
| **S1 · Cổng** | §2 Cổng vào + §6 Việc không được làm | Kiểm tra đủ điều kiện bắt đầu, đưa giới hạn vào plan |
| **S2 · Đầy đủ** | Toàn bộ `SKILL.md` | Thực thi Skill đó |

`examples.md` của Skill: không nạp, trừ khi cần ví dụ để làm đúng (ví dụ không phải nghiệp vụ chính thức).

`references/` của Skill: chỉ nạp cùng Skill ở mức S2. File theo chủ đề nạp khi `SKILL.md` chỉ tới; file theo công nghệ chỉ nạp file của công nghệ mà Task chạm tới. Ví dụ Task backend NestJS + Prisma nạp `backend-development/references/nestjs.md`, không nạp `references/laravel.md`. Ghi các file đã nạp vào PLAN §0.

## 2. Lịch nạp theo bước (task-execution)

| Bước | Nạp | Không nạp |
| --- | --- | --- |
| **1 · Intake** | Task; `PROJECT.md` (mức tự chủ, vùng 🟢🟡🔴); bảng ánh xạ ở §4 "Model và effort"; **dòng của loại Task** ở mục 4; Rule **P**; BUG-TEMPLATE nếu T3/T14 | Mọi Skill ở mức S2; Rule khác |
| **2 · Analyze** | FR/BR/AC, ADR mà Task chỉ tới; Skill trong chuỗi ở mức **S0**; Skill **đầu tiên** của chuỗi ở mức **S1** | Code ngoài phạm vi; tài liệu Task không chỉ tới |
| **3 · Plan** | PLAN-TEMPLATE; Rule ảnh hưởng **quyết định thiết kế**: **A**, **D**, **S** (nếu thoả điều kiện ở mục 3) và **T** (để lập kế hoạch AC → test); mọi Skill trong chuỗi ở mức **S1**; code liên quan để lập danh sách file | Skill mức S2; Rule **C**, **G** |
| **4 · Duyệt plan** | Không nạp thêm | — |
| **5 · Implement** | Plan đã duyệt; **chỉ Skill của bước con hiện tại** ở mức S2; Rule **C** (+ **A**, **D**, **S** như trong plan); Rule **G** khi commit | Skill của bước con khác; tài liệu đã tóm tắt trong plan |
| **6 · Run tests** | Skill testing tương ứng ở mức S2; Rule **T**; TEST-REPORT-TEMPLATE | Skill code |
| **7 · Self review** | §5 Checklist của các Skill đã dùng; DELIVERY-REPORT-TEMPLATE | — |
| **8 · Human review** | (phiên khác) theo dòng **T9** ở mục 4 | Lịch sử phiên viết code |
| **9 · Release** | `release-workflow.md`; Skill `deployment` S2; RELEASE-REPORT-TEMPLATE | — |
| **10 · Update knowledge** | Skill `documentation` S2 | — |

### Quy tắc chuyển bước

1. **Plan là ngữ cảnh nén.** Plan Approved phải đủ để thực thi: yêu cầu, quyết định thiết kế, file dự kiến đổi, AC → test, **lịch nạp** (PLAN §0). Từ bước 5, AI làm theo plan, không đọc lại toàn bộ tài liệu đã tóm tắt.
2. **Ưu tiên phiên mới khi sang bước 5.** Task R2/R3 hoặc chuỗi từ 3 Skill trở lên: kết thúc phiên lập plan, mở phiên thực thi chỉ với plan + Rule nền. Phiên review (bước 8) luôn là phiên khác.
3. **Mỗi bước con của bước 5 chỉ một Skill S2.** Xong cổng ra của Skill này, ghi đầu ra vào plan (mục Kết quả) rồi mới nạp Skill kế.
4. **Nạp bổ sung khi phát sinh điều kiện** (ví dụ fix bug hoá ra chạm phân quyền): nạp nhóm Rule/Skill tương ứng, ghi vào PLAN §0. Nếu làm đổi mức rủi ro, phạm vi hoặc cần Skill thiết kế: dừng và báo.
5. **Nghi ngờ chạm bảo mật hay dữ liệu thì nạp S, D.** Thừa một nhóm Rule rẻ hơn bỏ sót.

## 3. Rule: nhóm và điều kiện nạp

Ký hiệu: **P** project · **G** git-workflow · **A** architecture · **C** coding · **D** database · **S** security · **T** testing. Bước nạp xem mục 2.

| Nhóm | Điều kiện nạp |
| --- | --- |
| **P** | **Luôn luôn**, từ bước 1 (chứa thang R, D, severity mà nhóm khác dùng) |
| **G** | Task có commit hoặc PR. Task chỉ phân tích, đọc (A0–A1) không nạp |
| **C** | Có sửa code (kể cả code test) |
| **T** | Có sửa code, viết hoặc chạy test, hoặc phải báo kết quả kiểm tra |
| **A** | Thiết kế; chạm ranh giới module, tầng, API contract; thêm module/dependency; ảnh hưởng NFR |
| **D** | Chạm schema, migration, query, transaction, seed/dữ liệu test trong CSDL, xoá dữ liệu |
| **S** | Task **R3**; chạm xác thực, phiên, phân quyền; dữ liệu D2/D3; input từ ngoài, upload; tích hợp bên thứ ba; thêm/đổi dependency; secret, cấu hình bảo mật; phát hành |

Rule đã thoả điều kiện thì **không bỏ** kể cả với Task R1. Mức rủi ro chỉ đổi độ sâu kiểm tra, không đổi bộ Rule.

## 4. Bộ nạp theo loại Task

Mỗi Task chỉ nạp **dòng của mình**. `[ ]` = theo điều kiện ở mục 3. Vai: chỉ đọc dòng vai đó trong [agents/README.md](../agents/README.md), không đọc cả file. Thứ tự và điều kiện kích hoạt Skill theo [skill-selection.md](skill-selection.md) §2–§3 (chỉ đọc dòng của loại Task).

| # | Loại Task | Rule nền | Rule [ ] | Skill (thứ tự chuỗi) | Vai | Template | Model · Effort (plan / thực thi) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | Tính năng mới (phân tích → thiết kế → plan) | P, A | D, S, G | product-discovery, requirement-analysis, requirement-review, architecture-design, database-design, task-planning | Product Owner, Architect | PLAN; ADR (`docs/02-architecture/ADR/_template.md`) | M3·E3 / — |
| T2 | Cài đặt tính năng | P, G, C, A, T | D, S | authentication-rbac, backend-development, api-development, frontend-development, unit/integration/e2e-testing, security-review, code-review, documentation | Backend, Frontend, QA | PLAN, TEST-REPORT, DELIVERY-REPORT | M3·E3 / M2·E2 |
| T3 | Sửa lỗi | P, G, C, T | A, D, S | bug-fixing, integration/e2e-testing, security-review, code-review, documentation | Backend/Frontend, QA | BUG (đầu vào), DELIVERY-REPORT | M2·E3 / M2·E3 |
| T4 | Refactor | P, G, C, A, T | D | unit-testing, refactoring, integration-testing, code-review | Backend/Frontend | PLAN, DELIVERY-REPORT | M2·E3 / M2·E2 |
| T5 | Thay đổi schema | P, G, D, A, T | S, C | database-design, integration-testing, code-review, documentation | Architect, Backend | PLAN, DELIVERY-REPORT | M3·E3 / M2·E3 |
| T6 | Thay đổi yêu cầu | P | A, G | requirement-analysis, requirement-review | Product Owner | — | M2·E3 / — |
| T7 | Thay đổi kiến trúc / contract | P, A | D, S, G | architecture-design, documentation | Architect | ADR, PLAN | M3·E4 / — |
| T8 | Rà soát tài liệu yêu cầu | P | — | requirement-review | Product Owner | — | M2·E2 / — |
| T9 | Review Pull Request | P, C, A, T | D, S, G | code-review, security-review | Reviewer (phiên khác), Security | PR (đầu vào), DELIVERY-REPORT (kèm checklist code-review) | M3·E3 / — |
| T10 | Kiểm tra bảo mật | P, S, C | D, A | security-review, bug-fixing (khi Critical/High) | Security | DELIVERY-REPORT | M3·E3 / M2·E3 |
| T11 | Chỉ viết test | P, G, C, T | D, S | unit/integration/e2e-testing (theo tầng) | QA | TEST-REPORT, DELIVERY-REPORT | M2·E2 / M2·E2 |
| T12 | Chỉ cập nhật tài liệu | P, G | A | documentation | Executor | DELIVERY-REPORT | M2·E2 / M2·E1 |
| T13 | Phát hành | P, G, S, T | D | security-review, deployment, documentation | Release (người quyết) | TEST-REPORT, RELEASE-REPORT | M2·E2 / M2·E2 |
| T14 | Sự cố production | P, S | D, A | incident-analysis → chuyển T3 khi sửa → continuous-improvement | QA (A1, chỉ đọc), rồi theo T3 | BUG, rồi theo T3 | M3·E3 / theo T3 |
| T15 | Rà soát định kỳ | P | — | continuous-improvement | Planner | — | M2·E2 / — |

Task chỉ phân tích (T1, T6, T7, T8, T15) không có bước 5–6: Skill phân tích nạp mức S2 ở bước 2, đầu ra là tài liệu Draft.

### Model và effort

Cột cuối là **mặc định áp dụng** cho mọi Task cùng loại. Khung đề xuất sẵn; khi triển khai dự án, Tech Lead chốt bằng cách sửa trực tiếp cột này (nếu cần) và điền bảng ánh xạ bên dưới. Không khai báo ở nơi khác. "Plan" là phiên làm bước 1–4; "thực thi" là phiên làm bước 5–7 (quy tắc chuyển bước 2). Bước 8 dùng dòng T9.

- **Hạng model:** M1 nhẹ (tra cứu, tóm tắt, việc theo mẫu) · M2 chuẩn (code, test, tài liệu hằng ngày) · M3 mạnh (thiết kế, review, bảo mật, sự cố). **Effort:** E1 thấp · E2 trung bình · E3 cao · E4 rất cao.
- Task **R3**: tối thiểu M3·E3 ở mọi phiên. Bước con dùng `authentication-rbac` hoặc `security-review`: tối thiểu M3·E3.
- Bước 1 xác định loại Task. Nếu model của phiên hiện tại thấp hơn hạng ở cột "plan", AI dừng và đề nghị người đổi model. Plan ghi model và effort cho phiên thực thi (PLAN §0).
- Thiếu model đúng hạng hoặc hết hạn mức thì **dừng và hỏi**. Không tự hạ để chạy tiếp. Model mạnh hơn không thay cho bằng chứng kiểm chứng.

**Ánh xạ sang công cụ thật** (Tech Lead điền khi triển khai dự án; ví dụ Claude Code: [agents/examples/claude-code.md](../agents/examples/claude-code.md)):

| Hạng / mức | Model hoặc tham số thật (tên · phiên bản) |
| --- | --- |
| M1 · Nhẹ | |
| M2 · Chuẩn | |
| M3 · Mạnh | |
| E1 · Thấp | |
| E2 · Trung bình | |
| E3 · Cao | |
| E4 · Rất cao | |

## 5. Giai đoạn vòng đời → loại Task

| Giai đoạn (README) | Loại Task |
| --- | --- |
| 01 Product Discovery | T1 (phần product-discovery) |
| 02 Requirements Engineering | T1 (phần yêu cầu), T6, T8 |
| 03 System Design | T1 (phần thiết kế), T5, T7 |
| 04 AI Context & Governance | T12 (vùng 🔴: Task riêng, người duyệt) |
| 05 Implementation | T1 (task-planning), T2, T3, T4, T5 |
| 06 Quality Engineering | T9, T10, T11 |
| 07 Delivery & Operations | T13, T14 |
| 08 Continuous Improvement | T15 |

## 6. Ví dụ: T3 sửa lỗi, R2, chạm query

| Bước | Nạp |
| --- | --- |
| 1 | Task, BUG report, PROJECT.md, dòng T3 + bảng ánh xạ model (model plan M2·E3), Rule P, BUG-TEMPLATE |
| 2 | AC bị vi phạm; S0: bug-fixing, integration-testing, code-review; S1: bug-fixing |
| 3 | PLAN-TEMPLATE; Rule T, D (chạm query); code quanh lỗi |
| 5 | Phiên thực thi M2·E3 (theo plan); Plan; bug-fixing S2; Rule C, D; Rule G khi commit |
| 6 | integration-testing S2; Rule T |
| 7 | Checklist bug-fixing; DELIVERY-REPORT |
| 8 | Phiên khác, M3·E3: dòng T9 (code-review S2, Rule P, C, A, T, D) |

Không nạp lần nào: architecture-design, api-development, frontend-development, Rule S (trừ khi phát hiện chạm quyền).
