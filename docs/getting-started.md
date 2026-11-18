# Hướng dẫn sử dụng khung

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày | 0.1 · 2026-11-16 |
| Tài liệu liên quan | ../README.md, ../PROJECT.md, 04-project-management/gates-and-rigor.md, 04-project-management/task-breakdown.md, 03-engineering/ai-tools.md |

> **Mục đích.** Hướng dẫn từng bước cho người áp dụng khung vào một **dự án mới** hoặc một **dự án cũ đang chạy**. File chỉ nói làm gì, theo thứ tự nào, ai duyệt; định nghĩa và điều kiện nằm ở tài liệu được trỏ tới. AI không nạp file này khi làm Task.

## 1. Chọn lối vào

| Bạn đang… | Đọc |
| --- | --- |
| Bắt đầu một dự án chưa có code | §2, rồi §3 |
| Đưa khung vào một dự án đã có code, đang chạy hoặc đang bảo trì | §2, rồi §4 |
| Đã áp dụng xong, cần giao việc cho AI hằng ngày | §5 |
| Gặp tình huống lạ | §6 |
| Gặp ký hiệu không hiểu (T12, R1, A2, G3…) | §2, bảng tra ký hiệu |
| Cần biết mỗi giai đoạn nhận gì, ra gì, ai kiểm soát | §3.4 |
| Chọn model, effort trước khi mở phiên AI | §5.2 |
| Cần mẫu prompt cho một tình huống | §5.3 |
| Nhận tài liệu, hỏi lại khách hàng | [sources](00-project-overview/sources/README.md), [open-questions](00-project-overview/open-questions.md) mục "Hỏi khách hàng qua đầu mối" |
| Chọn công cụ AI | [ai-tools](03-engineering/ai-tools.md) §1 |
| Tạo symlink cho công cụ AI | [ai-tools](03-engineering/ai-tools.md) §2 |
| Khai báo giá trị riêng của dự án | [PROJECT.md](../PROJECT.md) |
| Cần biết AI làm một Task qua những bước nào | [task-execution](../.ai/workflows/task-execution.md), [task-types](../.ai/workflows/task-types.md) |
| Cần hiểu vì sao AI bị kiểm soát | [ai-governance](03-engineering/ai-governance.md) |
| Cần điều kiện duyệt | [gates-and-rigor](04-project-management/gates-and-rigor.md) |

## 2. Sáu khái niệm cần biết trước

| Khái niệm | Nói ngắn | Định nghĩa |
| --- | --- | --- |
| Draft / Approved | AI chỉ soạn `Draft`; chỉ người có thẩm quyền đổi sang `Approved`. AI chỉ dựa vào tài liệu `Approved` | [project-rules](../.ai/rules/project-rules.md) 4, 14 |
| Cổng G0–G7 | Điều kiện phải đạt để sang giai đoạn sau, qua bằng bằng chứng | [gates-and-rigor](04-project-management/gates-and-rigor.md) §1 |
| Độ nghiêm ngặt S1–S3 | Chọn một lần cho cả dự án | [gates-and-rigor](04-project-management/gates-and-rigor.md) §2 |
| Task với R và A | Mỗi Task có mức rủi ro R1–R3 và mức tự chủ A0–A4; thiếu thì AI dừng và hỏi | [project-rules](../.ai/rules/project-rules.md), mục "Thang dùng chung" |
| Vùng 🟢🟡🔴 | Đường dẫn AI được sửa tự do, sửa khi plan đã duyệt, hay cần Task riêng | [PROJECT.md](../PROJECT.md) §2.2 |
| Goal → Plan → Task → Run | Muốn đạt gì → làm thế nào (nhiều Task) → việc cụ thể (mỗi Task một mức model·effort) → một lần chạy (nâng mức khi không đạt) | [goals](04-project-management/goals.md), [task-execution](../.ai/workflows/task-execution.md) |

### Bảng tra ký hiệu

AI phải ghi nghĩa bằng lời ở lần đầu nhắc một ký hiệu trong câu trả lời, câu hỏi, plan, báo cáo ([project-rules](../.ai/rules/project-rules.md) 23). Gặp ký hiệu không hiểu thì tra ở đây.

| Ký hiệu | Nghĩa |
| --- | --- |
| `[01]`–`[08]` | Giai đoạn: Khám phá sản phẩm · Yêu cầu · Thiết kế · Chuẩn bị ngữ cảnh AI · Lập trình · Kiểm thử · Phát hành và vận hành · Cải tiến |
| G0–G7 | Cổng duyệt: G0 khai báo dự án · G1 vision, phạm vi · G2 yêu cầu · G3 thiết kế · G4 sẵn sàng giao Task · G5 code xong · G6 sẵn sàng phát hành · G7 vận hành ổn |
| S1 · S2 · S3 | Độ nghiêm ngặt cả dự án: gọn · chuẩn · nghiêm ngặt (kiểm toán được) |
| R1 · R2 · R3 | Rủi ro của Task: thấp, dễ hoàn tác · ảnh hưởng nhiều module hoặc API nội bộ · đụng phân quyền, tiền, dữ liệu cá nhân, migration, bảo mật (cần 2 reviewer) |
| A0 · A1 · A2 · A3 · A4 | Mức tự chủ của AI: chỉ trả lời · chỉ đọc và báo cáo · làm từng bước, người duyệt từng bước · làm trọn Task, người duyệt kết quả cuối · như A3 nhưng không cần duyệt từng Task (chỉ việc hẹp đã cho phép) |
| D0 · D1 · D2 · D3 | Mức dữ liệu: công khai · nội bộ · nhạy cảm · bí mật và dữ liệu cá nhân (không bao giờ đưa vào AI) |
| 🟢 · 🟡 · 🔴 | Vùng file: sửa trong phạm vi Task · sửa khi plan đã duyệt · cần Task riêng và người duyệt |
| T1 | Tính năng mới, chưa có yêu cầu (soạn yêu cầu, thiết kế) |
| T2 | Làm tính năng đã có yêu cầu, tiêu chí nghiệm thu, thiết kế |
| T3 · T4 · T5 | Sửa lỗi · Refactor · Đổi schema |
| T6 · T7 · T8 | Đổi yêu cầu · Đổi kiến trúc hoặc API contract · Rà soát tài liệu yêu cầu |
| T9 · T10 · T11 | Review Pull Request · Kiểm tra bảo mật · Chỉ viết test |
| T12 · T13 · T14 · T15 | Chỉ sửa tài liệu · Phát hành · Sự cố production · Rà soát định kỳ |
| `SRC-<NN>` | Tài liệu nguồn từ khách hàng hoặc PO ([sources](00-project-overview/sources/README.md)) |
| `OQ-<NN>` | Câu hỏi mở, giả định, đầu vào còn thiếu ([open-questions](00-project-overview/open-questions.md)) |
| `OUT-<NN>` · `BRQ-<NN>` | Kết quả đo được của dự án (vision) · Yêu cầu nghiệp vụ (BRD) |
| `FR-<MODULE>-<NN>` · `BR-…` · `NFR-<NN>` | Yêu cầu chức năng · Quy tắc nghiệp vụ · Yêu cầu phi chức năng |
| `<FR>-AC<N>` | Tiêu chí nghiệm thu (AC) của một FR |
| `ADR-<NNNN>` | Bản ghi quyết định kiến trúc |
| `GOAL-<NN>` · `<GOAL>-P<N>` · `<KEY>-<N>#<n>` | Goal (kết quả muốn đạt) · Plan của Goal · lần chạy thứ n của Task |
| M1 · M2 · M3 | Hạng model: nhẹ · chuẩn · mạnh |
| E1 · E2 · E3 · E4 | Mức effort: thấp · trung bình · cao · rất cao; viết gộp `M2·E1` (model chuẩn, effort thấp) |

Repo này là **repo cha** của một dự án: giữ hồ sơ (`docs/`), khai báo (`PROJECT.md`) và chỉ dẫn AI (`.ai/`). Mã nguồn nằm ở `project/<repo>/`, mỗi repo con có Git riêng ([README](../README.md), mục Cấu trúc). Phiên AI luôn mở ở thư mục gốc repo cha để công cụ đọc được `AGENTS.md`.

## 3. Dự án mới

### 3.1 Tạo repo cha cho dự án
1. Tạo một repo mới từ repo khung này (fork, template hoặc clone rồi đổi remote). Mỗi dự án một repo cha, vì `PROJECT.md` và `docs/` là của riêng dự án.
2. Tạo hoặc clone các repo mã nguồn vào `project/` (ví dụ `project/api`, `project/web`).

### 3.2 Khai báo dự án (cổng G0)
1. Yêu cầu AI: *"Tạo PROJECT.md cho dự án …"* và kèm thông tin bạn có (loại dự án, quy mô, dữ liệu xử lý). AI điền bản `Draft`; mục nào AI không biết thì để trống hoặc ghi câu hỏi.
2. Bạn tự quyết và điền: độ nghiêm ngặt S (§4), mức dữ liệu D0–D3 (§3), vùng 🟢🟡🔴 (§2.2), vai trò (§5).
3. Tech Lead duyệt thì đổi trạng thái sang `Approved`, ghi người duyệt và ngày. Như vậy là qua G0.

### 3.3 Nối công cụ AI
Chọn công cụ và tạo symlink theo [ai-tools](03-engineering/ai-tools.md) §1–§2, rồi khai báo ở §3–§4 của file đó. Chạy thử một Task nhỏ (ví dụ một Task T12) để chắc công cụ đã đọc `AGENTS.md`.

### 3.4 Đi qua các giai đoạn trước khi code

Mỗi dòng là một hoặc nhiều Task; AI soạn `Draft`, người ở cột "Duyệt" chuyển `Approved`. Đầu ra của bước trước là đầu vào của bước sau; AI chỉ dùng đầu vào đã `Approved` (bước 0 không cần duyệt, chỉ cần đã ẩn danh).

| Bước | Đầu vào (người cung cấp) | Loại Task giao AI | Đầu ra AI soạn (`Draft`) | Duyệt | Cổng |
| --- | --- | --- | --- | --- | --- |
| 0 | Tài liệu của khách hàng, PO: quy trình nghiệp vụ, biểu mẫu, biên bản (Đầu mối lưu, ẩn danh) | T12 (chỉ sửa tài liệu) | Danh mục [sources](00-project-overview/sources/README.md) `SRC-<NN>`; câu hỏi `Input` cho phần còn thiếu | Đầu mối với khách hàng | — |
| 1 | `SRC-<NN>`; câu trả lời của khách hàng | T1 (tính năng mới, Skill `product-discovery`) hoặc T12 | [00-project-overview](00-project-overview/README.md): vision, scope, glossary, open-questions; gói câu hỏi gửi khách hàng | PO | G1 (vision, phạm vi) |
| 2 | Bước 1 `Approved`; `SRC-<NN>`; OQ đã `Closed` | T1 (phần yêu cầu), rà bằng T8 (rà soát yêu cầu) | [01-requirements](01-requirements/README.md): BRD, FR, NFR, BR, AC; báo cáo rà soát | PO/BA, QA rà | G2 (yêu cầu) |
| 3 | Bước 2 `Approved`; code hiện có (dự án cũ, nền sẵn có) | T1 (phần thiết kế) hoặc T7 (đổi kiến trúc) | [02-architecture](02-architecture/README.md): kiến trúc, module, DB, API, ADR | Kiến trúc sư (+ Security nếu có tiền, phân quyền, dữ liệu cá nhân, migration) | G3 (thiết kế) |
| 4 | Chuẩn của công ty; công cụ AI được phép | T12 | [03-engineering](03-engineering/README.md): chuẩn code, bảo mật, lỗi, test, [ai-tools](03-engineering/ai-tools.md) | Tech Lead | G4 (sẵn sàng giao Task) |
| 5 | Bước 2–3 `Approved`; ưu tiên của PO | T1 (Skill `task-planning`) | [04-project-management](04-project-management/README.md): roadmap, backlog, Task (mẫu [task-breakdown](04-project-management/task-breakdown.md) §4) | Tech Lead; PO quyết ưu tiên | G4 |
| 6 | Hạ tầng, quy định vận hành (DevOps) | T12, có thể làm song song từ bước 3 | [05-operations](05-operations/README.md): deployment, monitoring, backup | Owner, tham khảo Tech Lead | trước G7 |

Từ bước 5 trở đi, công việc đi qua [task-execution](../.ai/workflows/task-execution.md) theo mô hình **Goal → Plan → Task → Run** ([goals](04-project-management/goals.md)): Goal là kết quả muốn đạt; Plan là cách đạt, gồm nhiều Task; mỗi Task chạy trong một phiên hoặc subagent riêng với model·effort riêng; mỗi lần chạy là một Run. Đầu vào và đầu ra:

| Bước | Đầu vào | Đầu ra | Người kiểm soát |
| --- | --- | --- | --- |
| Lập Plan | Goal; FR/BR/AC, thiết kế `Approved` | Plan theo [PLAN-TEMPLATE](../.ai/templates/PLAN-TEMPLATE.md) và một Task Manifest cho mỗi Task ([mẫu](../.ai/templates/TASK-MANIFEST-TEMPLATE.yaml)) ở `.ai/plans/<plan>/` | Tech Lead duyệt Plan: R, A, khoảng model·effort, ngân sách, phạm vi của từng Task |
| Chạy Task | Plan đã duyệt | Diff hoặc tài liệu; `runs.md` ghi từng lần chạy, nâng mức, chi phí; kết quả test thật ([TEST-REPORT](../.ai/templates/TEST-REPORT-TEMPLATE.md)) | Orchestrator đánh giá bằng lệnh kiểm; cổng tự động (lint, test, build) |
| Bàn giao | Diff, kết quả test | [DELIVERY-REPORT](../.ai/templates/DELIVERY-REPORT-TEMPLATE.md); PR theo [PR-TEMPLATE](../.ai/templates/PR-TEMPLATE.md) | Reviewer (phiên AI khác hoặc người); R3 thêm reviewer độc lập |
| Phát hành | PR đã merge | [RELEASE-REPORT](../.ai/templates/RELEASE-REPORT-TEMPLATE.md) nháp | Owner quyết; DevOps thực hiện; AI không deploy |

Bạn không cần viết kín mọi tài liệu cho cả dự án trước khi code. Cổng G2, G3 chỉ xét **phạm vi đang làm**: viết đủ cho mốc đầu tiên của roadmap, làm xong mốc đó rồi mở rộng.

### 3.5 Task đầu tiên
Khi qua G4, giao Task theo §5. Thường bắt đầu bằng một Task T2 nhỏ, R1 hoặc R2, để cả nhóm quen các điểm dừng.

## 4. Dự án cũ

### 4.1 Khác dự án mới ở đâu
- **Code đang chạy chưa phải là yêu cầu.** AI viết lại hồ sơ từ code (hiện trạng, *as-is*), nhưng một hành vi chỉ thành FR, BR khi PO/BA xác nhận đó là hành vi mong muốn ([documentation](../.ai/skills/documentation/SKILL.md), bước 2). Hành vi đáng ngờ được ghi thành câu hỏi mở hoặc bug, không tự sửa.
- **Lập hồ sơ theo phần cần, không lập hết một lần.** Trước khi giao Task vào một module, hồ sơ của module đó phải có và đã `Approved`; các module chưa đụng tới thì chưa cần.
- **An toàn trước tốc độ.** Hệ thống có người dùng thật, dữ liệu thật: lập lưới test trước khi sửa, khoanh vùng code nhạy cảm, không cho AI chạm production ([project-rules](../.ai/rules/project-rules.md) 13).

### 4.2 Đưa mã vào repo cha
1. Tạo repo cha như §3.1.
2. Clone các repo đang có vào `project/<repo>/`, giữ nguyên lịch sử Git và remote của chúng. Repo cha không theo dõi `project/` ([.gitignore](../.gitignore)).
3. Ghi đường dẫn repo vào [PROJECT.md](../PROJECT.md) §1, dòng Repository.

### 4.3 Rà chỉ dẫn AI có sẵn trong repo cũ
Repo cũ có thể đã có `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.cursor/rules/`, `.github/copilot-instructions.md`. Công cụ AI có thể tự nạp các file này khi làm việc trong thư mục con, và chúng có thể trái với `.ai/`.

| Nội dung trong file cũ | Xử lý |
| --- | --- |
| Lệnh build, test, chạy app; cấu trúc thư mục | Chuyển vào chuẩn ở [03-engineering](03-engineering/README.md) (ví dụ [coding-standards](03-engineering/coding-standards.md), [testing-strategy](03-engineering/testing-strategy.md) §8–§9) |
| Quy tắc nghiệp vụ | Chuyển vào [business-rules](01-requirements/business-rules.md) dạng `Draft` cho PO/BA xác nhận |
| Quy tắc trùng hoặc trái `.ai/` | Bỏ; nếu dự án thật sự cần giữ khác đi, ghi ở [PROJECT.md](../PROJECT.md) §6 kèm lý do |

Sau khi chuyển xong, xoá file cũ hoặc thu lại thành một dòng trỏ về repo cha. Đây là thay đổi trong repo con, cần một Task T12 riêng.

### 4.4 Khai báo PROJECT.md cho dự án cũ
Làm như §3.2, với các điểm riêng sau:

| Mục PROJECT.md | Gợi ý cho dự án cũ |
| --- | --- |
| §1 Giai đoạn hiện tại | Ghi rõ: đang vận hành, bảo trì hay phát triển tiếp |
| §2.2 Vùng | 🔴 cho xác thực, phân quyền, thanh toán, migration, cấu hình CI/hạ tầng; 🟡 cho module chưa có test hoặc chưa có hồ sơ; 🟢 cho phần còn lại |
| §3 Dữ liệu | Liệt kê dữ liệu thật đang có. D3 không bao giờ đưa vào AI: không dán log production, dump DB, `.env` vào phiên AI |
| §4 Độ nghiêm ngặt | Dự án bảo trì gợi ý S1–S2 ([gates-and-rigor](04-project-management/gates-and-rigor.md) §2); có hợp đồng hoặc pháp lý thì theo yêu cầu đó |
| §6 Tailoring | Ghi cách lập hồ sơ theo phần (§4.1); ghi phiên bản thư viện thực tế nếu cũ hơn phiên bản mà reference của Skill nhắm tới (AI dùng theo phiên bản của codebase, [project-rules](../.ai/rules/project-rules.md) 16) |
| §7 Miễn trừ | Ghi những gì khung yêu cầu mà dự án chưa có, kèm hạn và kế hoạch khắc phục. Thường gặp: chưa có CI (chạy cổng tự động cục bộ), chưa có cơ chế chặn commit message sai chuẩn ([git-workflow-rules](../.ai/rules/git-workflow-rules.md) 3), nhánh chưa theo Gitflow (rule 2), độ phủ test dưới ngưỡng ([testing-strategy](03-engineering/testing-strategy.md) §9) |

Không có miễn trừ thì AI sẽ dừng ở yêu cầu đó và xin miễn trừ ([project-rules](../.ai/rules/project-rules.md) 12). Khai báo trước giúp tránh việc này.

### 4.5 Lập hồ sơ hiện trạng
Mỗi dòng là một Task T12 (R1, A3 là đủ vì chỉ viết tài liệu, không sửa code). Làm cho **module sắp có việc trước**, không cần theo thứ tự cả hệ thống.

| Thứ tự | Tài liệu | AI đọc gì | Ai xác nhận |
| --- | --- | --- | --- |
| 1 | [system-architecture](02-architecture/system-architecture.md), [module-design](02-architecture/module-design.md) | Cấu trúc thư mục, điểm vào, cấu hình, phụ thuộc giữa module | Kiến trúc sư |
| 2 | [database-design](02-architecture/database-design.md) | Schema, migration hiện có (không đọc dữ liệu thật) | Kiến trúc sư (+ Security nếu có dữ liệu cá nhân) |
| 3 | [api-design](02-architecture/api-design.md) | Route, controller, DTO, middleware phân quyền | Kiến trúc sư |
| 4 | [FR](01-requirements/FR/README.md), [business-rules](01-requirements/business-rules.md), [acceptance-criteria](01-requirements/acceptance-criteria.md) của module | Hồ sơ 1–3 đã duyệt và code của module | PO/BA |
| 5 | [glossary](00-project-overview/glossary.md), [scope](00-project-overview/scope.md) | Hồ sơ đã có, tài liệu cũ (wiki, Confluence) bạn cung cấp | PO |
| 6 | [03-engineering](03-engineering/README.md), [05-operations](05-operations/README.md) | Lệnh build/test, CI, cách deploy hiện tại | Tech Lead; Owner cho phần vận hành |

Yêu cầu chung cho Task lập hồ sơ:
- Mỗi điều mô tả ghi nguồn `file:line` để người duyệt kiểm được.
- Chỗ code và tài liệu cũ mâu thuẫn, hành vi trông như lỗi, logic không rõ lý do: ghi `OQ-<NN>` vào [open-questions](00-project-overview/open-questions.md), không đoán.
- Lỗi đã chắc chắn: lập bug theo [BUG-TEMPLATE](../.ai/templates/BUG-TEMPLATE.md) để sửa ở Task T3 riêng, không sửa trong Task tài liệu.

Mẫu Task (điền vào mẫu đầy đủ ở [task-breakdown](04-project-management/task-breakdown.md) §4):

```markdown
# TASK: PRJ-3 - Lập hồ sơ hiện trạng module Đơn hàng

## 1. Objective
Mô tả hiện trạng module Đơn hàng ở project/api vào module-design và api-design, trạng thái Draft.

## 2. Business Context
- Phân loại: T12 · rủi ro R1 (chỉ viết tài liệu) · mức tự chủ A3

## 6. Scope
### In Scope
docs/02-architecture/module-design.md, docs/02-architecture/api-design.md: phần Đơn hàng.
### Out of Scope
Sửa code; tạo FR, BR; đổi trạng thái sang Approved.

## 7. Acceptance Criteria
- [ ] Mỗi endpoint của module có trong api-design, ghi nguồn file:line.
- [ ] Điểm chưa rõ ghi OQ-<NN>, lỗi nghi ngờ lập bug riêng.
```

### 4.6 Lập lưới an toàn trước khi sửa
Module chưa có test thì Task đầu tiên vào module đó nên là **T11** (chỉ viết test): viết test ghi lại hành vi hiện tại, kể cả hành vi đang bị nghi là sai (ghi chú `OQ-<NN>` trong test). T4 (refactor) bắt buộc có test nền trước ([task-types](../.ai/workflows/task-types.md), dòng T4). Có lưới test rồi, Tech Lead có thể hạ module từ 🟡 xuống 🟢 trong [PROJECT.md](../PROJECT.md) §2.2.

### 4.7 Chọn loại Task cho việc thường gặp

| Việc | Loại Task | Điều kiện trước |
| --- | --- | --- |
| Sửa lỗi | T3 | Có bug report; module có hồ sơ đủ để hiểu hành vi đúng |
| Thêm tính năng chưa có yêu cầu | T1, rồi T2 | Hồ sơ hiện trạng của module liên quan đã `Approved` (§4.5) |
| Làm tính năng đã có FR, AC, thiết kế | T2 | Như dự án mới |
| Dọn code, tách module | T4 | Có test nền (§4.6) |
| Đổi schema | T5 | database-design của phần liên quan đã `Approved` |
| Viết thêm test | T11 | — |
| Viết hoặc sửa tài liệu | T12 | — |
| Sự cố production | T14 | — |

## 5. Giao việc hằng ngày (dùng chung)

### 5.1 Viết Goal hoặc Task
- **Việc lớn:** nêu Goal (kết quả muốn đạt, tiêu chí hoàn thành, căn cứ FR/thiết kế). AI chia thành Plan và Task, đề xuất R, A, mức model·effort cho từng Task; bạn duyệt Plan là cấp các giá trị đó.
- **Việc nhỏ:** viết một Task theo mẫu ở [task-breakdown](04-project-management/task-breakdown.md) §4; Task chỉ giao AI khi đạt điều kiện sẵn sàng ở §7 của file đó. Ghi đủ: loại Task (T1–T15, danh sách ở [task-types](../.ai/workflows/task-types.md) §1), rủi ro R, mức tự chủ A. Task R1 đủ điều kiện fast lane thì chạy ngay, không cần Plan.
- Một Task một việc: không gộp sửa lỗi với refactor lớn.

### 5.2 Mở phiên AI
Mở phiên ở thư mục gốc repo cha. Chọn model, effort **trước khi gõ câu mở đầu**:

| Phiên | Mức | Nghĩa |
| --- | --- | --- |
| Orchestrator (lập Plan, gửi Task, đánh giá) | M3·E3; M3·E4 nếu Goal có đổi kiến trúc hoặc API contract (T7) | Model mạnh · effort cao / rất cao |
| Fast lane (một Task R1) | Mức bắt đầu của Skill chính ([model-effort](../.ai/workflows/model-effort.md) §2), ví dụ sửa tài liệu M2·E1 | Model chuẩn · effort thấp |
| Từng Task (Run) | Orchestrator tự chọn theo manifest; Task A2 trở xuống hoặc công cụ không có subagent thì bạn mở phiên mới theo mức Orchestrator báo | — |
| Review (bước 8) | M3·E3, phiên mới, không dùng lịch sử phiên viết code | Model mạnh · effort cao |

- **Mức theo Task, không theo cả phiên:** mỗi Task có mức bắt đầu, sàn, trần trong manifest. Task chạy thấp trước; kết quả không đạt vì năng lực thì Orchestrator tự nâng một bậc, tối đa tới trần bạn đã duyệt; thiếu đầu vào, yêu cầu mâu thuẫn, bị từ chối quyền thì dừng hỏi bạn ([model-effort](../.ai/workflows/model-effort.md) §3).
- **Task mức tự chủ A2 trở xuống** (duyệt từng bước, gồm mọi Task code R3) không gửi cho subagent: Orchestrator đưa bạn manifest, đường dẫn worktree của Task và câu mở phiên; bạn mở phiên tương tác **trong worktree đó**, ở mức ghi trong manifest, duyệt từng bước, khi trả báo cáo thì kèm chi phí nếu công cụ hiển thị.
- Task R3 (đụng phân quyền, tiền, dữ liệu cá nhân, migration, bảo mật): sàn M3·E3.
- Đổi M1–M3, E1–E4 sang model thật: §1 của file công cụ trong [references/](../.ai/agents/references/); cách chạy Task theo manifest ở mục kế tiếp của file đó. Công cụ không có effort thì chỉ chọn model theo hạng M.

Câu mở đầu:

```text
Goal GOAL-03: <kết quả muốn đạt>. Căn cứ: <FR, thiết kế>. Làm theo AGENTS.md.
```

hoặc với một Task:

```text
Task PRJ-12 (T3 · R1 · A3). Làm theo AGENTS.md.
<dán Task Specification hoặc link tới Task>
```

**Nguyên tắc viết prompt.** Prompt chỉ mang **việc gì** (Task, đầu vào, điều kiện riêng của lần này). **Làm thế nào** đã nằm trong Rule, Skill, workflow; không chép lại vào prompt, không viết "hãy cẩn thận", "đừng bịa". Muốn AI làm khác đi thì sửa Rule hoặc Skill bằng Task riêng, không vá bằng prompt. Không dán dữ liệu D3 (bí mật, dữ liệu cá nhân) vào prompt.

### 5.3 Mẫu prompt theo tình huống

Thay phần `<...>`. Mã Task, loại, R, A lấy từ Task đã viết theo §5.1.

| Tình huống | Prompt |
| --- | --- |
| Khai báo dự án (G0) | `Tạo PROJECT.md cho dự án <tên>. Loại: <nội bộ / gia công / bảo trì>. Quy mô: <số người, thời gian>. Dữ liệu xử lý: <mô tả>. Khách hàng: <có / không; đại diện là ai, đầu mối là ai>. Mục nào bạn không biết thì để trống và hỏi.` |
| Nhận tài liệu từ khách hàng | `Task <KEY>-<N> (T12 · R1 · A2). Đăng ký tài liệu nguồn vào docs/00-project-overview/sources/: <đường dẫn các file đã ẩn danh>. Người cung cấp: <tên>, ngày nhận: <ngày>. Liệt kê tài liệu còn thiếu thành OQ loại Input.` |
| Khám phá sản phẩm từ tài liệu nguồn | `Task <KEY>-<N> (T1 · R<N> · A2). Soạn vision, scope, glossary cho module <tên> từ SRC-<NN>, SRC-<NN>. Soạn gói câu hỏi gửi khách hàng cho các điểm chưa rõ.` |
| Phân tích yêu cầu | `Task <KEY>-<N> (T1 · R<N> · A2). Viết BRD, FR, BR, AC cho module <tên>. Căn cứ: vision, scope đã Approved; SRC-<NN>; OQ đã Closed.` |
| Khách hàng đã trả lời | `Khách hàng trả lời các câu hỏi OQ-<NN>, OQ-<NN> (đã lưu SRC-<NN>). Cập nhật open-questions và các tài liệu bị ảnh hưởng; câu trả lời sinh câu hỏi mới thì mở OQ mới.` |
| Rà soát yêu cầu | `Task <KEY>-<N> (T8 · R1 · A1). Rà soát FR-<MODULE>-* và AC trước khi trình PO duyệt.` |
| Thiết kế | `Task <KEY>-<N> (T1 · R<N> · A2). Thiết kế module <tên> trên nền <hệ thống sẵn có, đường dẫn code>. Căn cứ: FR-<MODULE>-* đã Approved.` |
| Lập Plan cho Goal | `Goal GOAL-<NN>: <kết quả muốn đạt>. Căn cứ FR-<MODULE>-*, thiết kế đã Approved. Chia thành Plan và Task kèm manifest; đề xuất R, A, mức model·effort cho từng Task.` |
| Chạy Plan đã duyệt | `Plan <GOAL>-P<N> đã duyệt. Chạy các Task theo manifest, ghi runs.md.` |
| Làm tính năng | `Task <KEY>-<N> (T2 · R<N> · A<N>). Làm theo AGENTS.md.` + dán Task |
| Sửa lỗi | `Task <KEY>-<N> (T3 · R<N> · A<N>). Làm theo AGENTS.md.` + dán bug report theo BUG-TEMPLATE |
| Review PR (phiên mới) | `Task <KEY>-<N> (T9 · R<N> · A1). Review PR <link/số> của Task <KEY>-<M>. Không dùng lịch sử phiên viết code.` |
| Tiếp tục phiên bị ngắt | `Tiếp tục Plan <GOAL>-P<N> từ .ai/plans/<thư mục>. Đọc bảng Task trong PLAN.md và runs.md để biết đã làm tới đâu.` |
| Duyệt tài liệu | `<Vai> <tên> duyệt, chuyển <file> sang Approved.` |
| Trả lời câu hỏi cần quyết | `OQ-<NN>: chọn phương án <A/B>, lý do <...>.` hoặc `Chưa quyết OQ-<NN>, làm tiếp phần không bị chặn.` |

### 5.4 Việc của bạn ở từng điểm dừng
Các bước AI thực hiện ở [task-execution](../.ai/workflows/task-execution.md).

| Khi AI… | Bạn làm |
| --- | --- |
| Hỏi R, A, S hoặc loại Task | Trả lời; AI không tự gán |
| Gửi câu hỏi cần quyết (có Vấn đề, Phương án, Đề xuất) | Chọn phương án; muốn quyết sau thì nói rõ phần nào được làm tiếp |
| Gửi Plan và các Task Manifest | Duyệt hoặc yêu cầu sửa: R, A, mức bắt đầu và trần, ngân sách, phạm vi từng Task. AI chưa chạy Task nào trước khi bạn duyệt |
| Dừng vì vượt trần, hết lượt hoặc hết ngân sách | Đọc các mức đã thử và lỗi; nâng trần, sửa manifest, hoặc tự làm |
| Bàn giao (báo cáo bàn giao, kết quả test thật) | Đọc phần giả định, câu hỏi còn mở, phần chưa kiểm |
| Mở PR | Review bằng **một phiên AI khác** (Task T9) hoặc người khác; Task R3 cần thêm một reviewer độc lập |
| Chờ merge, phát hành | Người merge; AI không tự merge, tag hay deploy |

### 5.5 Duyệt tài liệu
Chỉ người có thẩm quyền (cột "Người duyệt" ở [README](../README.md), mục Giai đoạn và người duyệt) đổi `Draft` sang `Approved`, ghi tên và ngày vào bảng thuộc tính của tài liệu. Có thể tự sửa tay hoặc bảo AI: *"Tech Lead duyệt, chuyển … sang Approved"*. AI không tự chuyển.

Tài liệu cần khách hàng duyệt: Đầu mối gửi khách hàng → khách hàng duyệt, báo Đầu mối → Đầu mối lưu kết quả thành `SRC-<NN>` ([sources](00-project-overview/sources/README.md)) → mới chuyển `Approved`, ghi mã `SRC` cạnh tên người duyệt. Khách hàng yêu cầu sửa: ghi thành OQ, AI sửa bản `Draft`, gửi lại.

## 6. Tình huống thường gặp

| Tình huống | Nguyên nhân | Xử lý |
| --- | --- | --- |
| AI dừng, báo thiếu spec, AC hoặc thiết kế | Task không đạt điều kiện sẵn sàng ([project-rules](../.ai/rules/project-rules.md) 2) | Bổ sung tài liệu và duyệt, hoặc đổi Task sang T1/T12 để soạn chúng trước |
| AI dừng, xin miễn trừ | Một yêu cầu của khung chưa đáp ứng được | Duyệt miễn trừ ở [PROJECT.md](../PROJECT.md) §7, hoặc bổ sung cái còn thiếu |
| AI nói hành vi cũ "có thể là lỗi" | Code và tài liệu, hoặc code và câu trả lời của PO, không khớp | PO/BA quyết: giữ (ghi BR) hay sửa (lập bug, Task T3) |
| AI không theo `.ai/`, làm theo chỉ dẫn khác | Repo con còn file chỉ dẫn AI cũ, hoặc phiên mở sai thư mục | Rà theo §4.3; mở phiên ở gốc repo cha |
| AI dùng API không có ở phiên bản thư viện đang chạy | Reference của Skill viết cho bản mới hơn | Ghi phiên bản thực tế ở [PROJECT.md](../PROJECT.md) §6; nhắc phiên bản trong Task |
| Muốn sửa Rule, Skill trong `.ai/` | `.ai/` là vùng 🔴 | Mở Task riêng, Tech Lead duyệt ([.ai/README](../.ai/README.md)) |
