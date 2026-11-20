# Hướng dẫn sử dụng khung

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người duyệt | Tech Lead |
| Tài liệu liên quan | ../../README.md, ../../PROJECT.md, gates-and-rigor.md, task-breakdown.md, ai-tools.md |

> **Mục đích.** Tài liệu hướng dẫn sử dụng framework. AI không nạp file này khi làm Task.

## 1. Chọn lối vào

| Bạn đang… | Đọc |
| --- | --- |
| Bắt đầu một dự án chưa có code | §2, rồi §3 |
| Đưa khung vào một dự án đã có code, đang chạy hoặc đang bảo trì | §2, rồi §4 |
| Đã áp dụng xong, cần giao việc cho AI hằng ngày | §5 |
| Gặp tình huống lạ | §6 |
| Gặp mã định danh không hiểu (FR-, OQ-, SRC-…) | §2, mục "Mã định danh" |
| Cần biết mỗi giai đoạn nhận gì, ra gì, ai kiểm soát | §3.4 |
| Chọn model, effort trước khi mở phiên AI | §5.2 |
| Cần mẫu prompt cho một tình huống | §5.3 |
| Nhận tài liệu, hỏi lại khách hàng | [sources](../../docs/00-project-overview/sources/README.md), sổ OQ theo cấp ([open-questions](open-questions.md)) |
| Chọn công cụ AI | [ai-tools](ai-tools.md) §1 |
| Tạo symlink cho công cụ AI | [ai-tools](ai-tools.md) §2 |
| Khai báo giá trị riêng của dự án | [PROJECT.md](../../PROJECT.md) |
| Cần biết AI làm một Task qua những bước nào | [task-execution](../workflows/task-execution.md), [task-types](../workflows/task-types.md) |
| Cần hiểu vì sao AI bị kiểm soát | [ai-governance](ai-governance.md) |
| Cần điều kiện duyệt | [gates-and-rigor](gates-and-rigor.md) |

## 2. Bảy khái niệm cần biết trước

| Khái niệm | Nói ngắn | Định nghĩa |
| --- | --- | --- |
| Draft / Approved | AI chỉ soạn `Draft`; chỉ người có thẩm quyền đổi sang `Approved`. AI chỉ dựa vào tài liệu `Approved` | [project-rules](../rules/project-rules.md) 4, 14 |
| Tám cổng duyệt | Điều kiện phải đạt để sang giai đoạn sau, qua bằng bằng chứng | [gates-and-rigor](gates-and-rigor.md) §1 |
| Độ nghiêm ngặt | Gọn, chuẩn hoặc nghiêm ngặt; chọn một lần cho cả dự án | [gates-and-rigor](gates-and-rigor.md) §2 |
| Task với rủi ro và mức tự chủ | Mỗi Task có rủi ro (thấp, vừa, cao) và mức tự chủ (chỉ trả lời, chỉ đọc, duyệt từng bước, làm trọn Task, miễn duyệt từng Task); thiếu thì AI dừng và hỏi | [project-rules](../rules/project-rules.md), mục "Thang dùng chung" |
| Vùng 🟢🟡🔴 | Đường dẫn AI được sửa tự do, sửa khi plan đã duyệt, hay cần Task riêng | rule 8 của [project-rules](../rules/project-rules.md) |
| Ba nhóm khái niệm | A nghiệp vụ và sản phẩm (BRD, BRQ, Goal, Epic, Feature, User Story) · B lập kế hoạch và quản lý công việc (Plan, Task, Subtask, Dependency) · C thực thi bằng AI (Agent, Run, model·effort, Tool, Result, Review). Liên kết nhiều-nhiều, không phải cây cha-con | [work-model](work-model.md) |
| Plan → Task → Run | Kế hoạch (có Nguồn: Goal, Epic, User Story hoặc yêu cầu độc lập; Goals tuỳ chọn) → việc cụ thể (mỗi Task một mức model·effort) → một lần chạy (nâng mức khi không đạt) | [work-model](work-model.md), [task-execution](../workflows/task-execution.md) |

### Mã định danh

| Mã | Nghĩa |
| --- | --- |
| `SRC-<NN>` | Tài liệu nguồn từ khách hàng hoặc PO ([sources](../../docs/00-project-overview/sources/README.md)) |
| `OQ-<NN>` | Câu hỏi mở, giả định, đầu vào còn thiếu ([open-questions](open-questions.md)) |
| `OUT-<NN>` · `BRQ-<NN>` | Kết quả đo được của dự án (vision) · Yêu cầu nghiệp vụ (BRD) |
| `EPIC-<NN>` · `FEAT-<NN>` · `US-<MODULE>-<NN>` | Epic (nhóm công việc lớn) · Function/Feature (chức năng hệ thống) · User Story (nhu cầu người dùng) |
| `FR-<MODULE>-<NN>` · `BR-…` · `NFR-<NN>` | Yêu cầu chức năng · Quy tắc nghiệp vụ · Yêu cầu phi chức năng |
| `<FR>-AC<N>` | Tiêu chí nghiệm thu (AC) của một FR |
| `ADR-<NNNN>` | Bản ghi quyết định kiến trúc |
| `GOAL-<NN>` · `PLAN-<NNN>` · `<KEY>-<N>` · `<KEY>-<N>#<n>` | Goal (kết quả muốn đạt) · Plan (kế hoạch thực hiện) · Task · lần chạy thứ n của Task |

Repo này là **repo cha** của một dự án: giữ hồ sơ (`docs/`), khai báo (`PROJECT.md`) và chỉ dẫn AI (`.ai/`). Mã nguồn nằm ở `project/<repo>/`, mỗi repo con có Git riêng ([README](../../README.md), mục Cấu trúc). Phiên AI luôn mở ở thư mục gốc repo cha để công cụ đọc được `AGENTS.md`.

## 3. Dự án mới

### 3.1 Tạo repo cha cho dự án
1. Tạo một repo mới từ repo khung này (fork, template hoặc clone rồi đổi remote). Mỗi dự án một repo cha, vì `PROJECT.md` và `docs/` là của riêng dự án.
2. Tạo hoặc clone các repo mã nguồn vào `project/` (ví dụ `project/api`, `project/web`).

### 3.2 Khai báo dự án (cổng Khai báo dự án)
Làm theo [CHECKLIST.md](../../CHECKLIST.md) (từ việc 4 đến việc 12): [PROJECT.md](../../PROJECT.md) đã có giá trị khuyến nghị, mục nào đúng thì giữ. Tech Lead duyệt thì đổi trạng thái sang `Approved`, ghi người duyệt và ngày; như vậy là qua cổng Khai báo dự án.
Muốn AI điền giúp: yêu cầu *"Tạo PROJECT.md cho dự án …"* kèm thông tin bạn có (loại dự án, quy mô, dữ liệu xử lý); AI điền bản `Draft`, mục nào không biết thì để trống hoặc ghi câu hỏi.

### 3.3 Nối công cụ AI
Chọn công cụ và tạo symlink theo [ai-tools](ai-tools.md) §1–§2, rồi khai báo ở §3–§4 của file đó. Chạy thử một Task nhỏ (ví dụ một Task chỉ sửa tài liệu) để chắc công cụ đã đọc `AGENTS.md`.

### 3.4 Đi qua các giai đoạn trước khi code

Mỗi dòng là một hoặc nhiều Task; AI soạn `Draft`, người ở cột "Duyệt" chuyển `Approved`. Đầu ra của bước trước là đầu vào của bước sau; AI chỉ dùng đầu vào đã `Approved` (bước 0 không cần duyệt, chỉ cần đã ẩn danh).

| Bước | Đầu vào (người cung cấp) | Loại Task giao AI | Đầu ra AI soạn (`Draft`) | Duyệt | Cổng |
| --- | --- | --- | --- | --- | --- |
| 0 | Tài liệu của khách hàng, PO: quy trình nghiệp vụ, biểu mẫu, biên bản (Đầu mối lưu, ẩn danh) | chỉ sửa tài liệu | Danh mục [sources](../../docs/00-project-overview/sources/README.md) `SRC-<NN>`; câu hỏi `Input` cho phần còn thiếu | Đầu mối với khách hàng | — |
| 1 | `SRC-<NN>`; câu trả lời của khách hàng | tính năng mới (Skill `product-discovery`) hoặc chỉ sửa tài liệu | [00-project-overview](../../docs/00-project-overview/README.md): vision, scope, glossary; gói câu hỏi gửi khách hàng | PO | cổng Phạm vi |
| 2 | Bước 1 `Approved`; `SRC-<NN>`; OQ đã `Closed` | tính năng mới (phần yêu cầu), rà bằng rà soát yêu cầu | [01-requirements](../../docs/01-requirements/README.md): BRD, Feature, FR, NFR, BR, AC; Epic, User Story ở [product-backlog](../../docs/04-project-management/product-backlog.md); báo cáo rà soát | PO/BA, QA rà | cổng Yêu cầu |
| 3 | Bước 2 `Approved`; code hiện có (dự án cũ, nền sẵn có) | tính năng mới (phần thiết kế) hoặc đổi kiến trúc | [02-architecture](../../docs/02-architecture/README.md): kiến trúc, module, DB, API, ADR | Kiến trúc sư (+ Security nếu có tiền, phân quyền, dữ liệu cá nhân, migration) | cổng Thiết kế |
| 4 | Chuẩn của công ty; công cụ AI được phép | chỉ sửa tài liệu | [03-engineering](../../docs/03-engineering/README.md): chuẩn code, bảo mật, lỗi, test, [ai-tools](ai-tools.md) | Tech Lead | cổng Sẵn sàng giao việc |
| 5 | Bước 2–3 `Approved`; ưu tiên của PO | tính năng mới (Skill `task-planning`) | [04-project-management](../../docs/04-project-management/README.md): roadmap, goals, product-backlog, task-backlog, Task (mẫu [task-breakdown](task-breakdown.md) §4) | Tech Lead; PO quyết ưu tiên | cổng Sẵn sàng giao việc |
| 6 | Hạ tầng, quy định vận hành (DevOps) | chỉ sửa tài liệu, có thể làm song song từ bước 3 | [05-operations](../../docs/05-operations/README.md): deployment, monitoring, backup | Owner, tham khảo Tech Lead | trước cổng Vận hành |

Từ bước 5 trở đi, công việc đi qua [task-execution](../workflows/task-execution.md) theo mô hình **Plan → Task → Run** ([work-model](work-model.md)): Plan là kế hoạch thực hiện, tạo từ một Nguồn (Goal, Epic, User Story hoặc yêu cầu độc lập), có thể phục vụ nhiều Goal, gồm nhiều Task; mỗi Task chạy trong một phiên hoặc subagent riêng với model·effort riêng; mỗi lần chạy là một Run. Đầu vào và đầu ra:

| Bước | Đầu vào | Đầu ra | Người kiểm soát |
| --- | --- | --- | --- |
| Lập Plan | Nguồn (Goal, Epic, User Story hoặc yêu cầu độc lập); User Story, FR/BR/AC, thiết kế `Approved` | Plan theo [PLAN-TEMPLATE](../templates/PLAN-TEMPLATE.md) và một Task Manifest cho mỗi Task ([mẫu](../templates/TASK-MANIFEST-TEMPLATE.yaml)) ở `.ai/plans/<plan>/` | Tech Lead duyệt Plan: rủi ro, mức tự chủ, các mức model/effort thử, ngân sách, phạm vi của từng Task |
| Chạy Task | Plan đã duyệt | Diff hoặc tài liệu; `runs.md` ghi từng lần chạy, nâng mức, chi phí; kết quả test thật ([TEST-REPORT](../templates/TEST-REPORT-TEMPLATE.md)) | Orchestrator đánh giá bằng lệnh kiểm; cổng tự động (lint, test, build) |
| Bàn giao | Diff, kết quả test | [DELIVERY-REPORT](../templates/DELIVERY-REPORT-TEMPLATE.md); PR theo [PR-TEMPLATE](../templates/PR-TEMPLATE.md) | Reviewer (phiên AI khác hoặc người); rủi ro cao thêm reviewer độc lập |
| Phát hành | PR đã merge | [RELEASE-REPORT](../templates/RELEASE-REPORT-TEMPLATE.md) nháp | Owner quyết; DevOps thực hiện; AI không deploy |

Bạn không cần viết kín mọi tài liệu cho cả dự án trước khi code. Cổng Yêu cầu và cổng Thiết kế chỉ xét **phạm vi đang làm**: viết đủ cho mốc đầu tiên của roadmap, làm xong mốc đó rồi mở rộng.

### 3.5 Task đầu tiên
Khi qua cổng Sẵn sàng giao việc, giao Task theo §5. Thường bắt đầu bằng một Task làm tính năng nhỏ, rủi ro thấp hoặc vừa, để cả nhóm quen các điểm dừng.

## 4. Dự án cũ

### 4.1 Khác dự án mới ở đâu
- **Code đang chạy chưa phải là yêu cầu.** AI viết lại hồ sơ từ code (hiện trạng, *as-is*), nhưng một hành vi chỉ thành FR, BR khi PO/BA xác nhận đó là hành vi mong muốn ([documentation](../skills/documentation/SKILL.md), bước 2). Hành vi đáng ngờ được ghi thành câu hỏi mở hoặc bug, không tự sửa.
- **Lập hồ sơ theo phần cần, không lập hết một lần.** Trước khi giao Task vào một module, hồ sơ của module đó phải có và đã `Approved`; các module chưa đụng tới thì chưa cần.
- **An toàn trước tốc độ.** Hệ thống có người dùng thật, dữ liệu thật: lập lưới test trước khi sửa, khoanh vùng code nhạy cảm, không cho AI chạm production ([project-rules](../rules/project-rules.md) 13).

### 4.2 Đưa mã vào repo cha
1. Tạo repo cha như §3.1.
2. Clone các repo đang có vào `project/<repo>/`, giữ nguyên lịch sử Git và remote của chúng. Repo cha không theo dõi `project/` ([.gitignore](../../.gitignore)).
3. Ghi đường dẫn repo vào [PROJECT.md](../../PROJECT.md) §1, dòng Repository.

### 4.3 Rà chỉ dẫn AI có sẵn trong repo cũ
Repo cũ có thể đã có `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.cursor/rules/`, `.github/copilot-instructions.md`. Công cụ AI có thể tự nạp các file này khi làm việc trong thư mục con, và chúng có thể trái với `.ai/`.

| Nội dung trong file cũ | Xử lý |
| --- | --- |
| Lệnh build, test, chạy app; cấu trúc thư mục | Chuyển vào chuẩn ở [03-engineering](../../docs/03-engineering/README.md) (ví dụ [coding-standards](../../docs/03-engineering/coding-standards.md), [testing-strategy](../../docs/03-engineering/testing-strategy.md) §8–§9) |
| Quy tắc nghiệp vụ | Chuyển vào [business-rules](../../docs/01-requirements/business-rules.md) dạng `Draft` cho PO/BA xác nhận |
| Quy tắc trùng hoặc trái `.ai/` | Bỏ; nếu dự án thật sự cần giữ khác đi, ghi ở [PROJECT.md](../../PROJECT.md) §6 kèm lý do |

Sau khi chuyển xong, xoá file cũ hoặc thu lại thành một dòng trỏ về repo cha. Đây là thay đổi trong repo con, cần một Task chỉ sửa tài liệu riêng.

### 4.4 Khai báo PROJECT.md cho dự án cũ
Làm theo [CHECKLIST.md](../../CHECKLIST.md) như §3.2. Các điểm riêng của dự án cũ mà CHECKLIST.md không nêu:

| Mục PROJECT.md | Gợi ý cho dự án cũ |
| --- | --- |
| §1 Giai đoạn hiện tại | Ghi rõ: đang vận hành, bảo trì hay phát triển tiếp |
| §2.2 Vùng | 🔴 cho xác thực, phân quyền, thanh toán, migration, cấu hình CI/hạ tầng; 🟡 cho module chưa có test hoặc chưa có hồ sơ; 🟢 cho phần còn lại |
| §3 Dữ liệu | Liệt kê dữ liệu thật đang có. Dữ liệu bí mật không bao giờ đưa vào AI: không dán log production, dump DB, `.env` vào phiên AI |
| §4 Độ nghiêm ngặt | Dự án bảo trì gợi ý gọn hoặc chuẩn ([gates-and-rigor](gates-and-rigor.md) §2); có hợp đồng hoặc pháp lý thì theo yêu cầu đó |
| §6 Tailoring | Ghi cách lập hồ sơ theo phần (§4.1); ghi phiên bản thư viện thực tế nếu cũ hơn phiên bản mà reference của Skill nhắm tới (AI dùng theo phiên bản của codebase, [project-rules](../rules/project-rules.md) 16) |
| §7 Miễn trừ | Ghi những gì khung yêu cầu mà dự án chưa có, kèm hạn và kế hoạch khắc phục. Thường gặp: chưa có CI (chạy cổng tự động cục bộ), chưa có cơ chế chặn commit message sai chuẩn ([git-workflow-rules](../rules/git-workflow-rules.md) 3), nhánh chưa theo Gitflow (rule 2), độ phủ test dưới ngưỡng ([testing-strategy](../../docs/03-engineering/testing-strategy.md) §9) |

Không có miễn trừ thì AI sẽ dừng ở yêu cầu đó và xin miễn trừ ([project-rules](../rules/project-rules.md) 12). Khai báo trước giúp tránh việc này.

### 4.5 Lập hồ sơ hiện trạng
Mỗi dòng là một Task chỉ sửa tài liệu (rủi ro thấp, làm trọn Task là đủ vì chỉ viết tài liệu, không sửa code). Làm cho **module sắp có việc trước**, không cần theo thứ tự cả hệ thống.

| Thứ tự | Tài liệu | AI đọc gì | Ai xác nhận |
| --- | --- | --- | --- |
| 1 | [system-architecture](../../docs/02-architecture/system-architecture.md), [module-design](../../docs/02-architecture/module-design.md) | Cấu trúc thư mục, điểm vào, cấu hình, phụ thuộc giữa module | Kiến trúc sư |
| 2 | [database-design](../../docs/02-architecture/database-design.md) | Schema, migration hiện có (không đọc dữ liệu thật) | Kiến trúc sư (+ Security nếu có dữ liệu cá nhân) |
| 3 | [api-design](../../docs/02-architecture/api-design.md) | Route, controller, DTO, middleware phân quyền | Kiến trúc sư |
| 4 | [FR](../../docs/01-requirements/FR/README.md), [business-rules](../../docs/01-requirements/business-rules.md), [acceptance-criteria](../../docs/01-requirements/acceptance-criteria.md) của module | Hồ sơ 1–3 đã duyệt và code của module | PO/BA |
| 5 | [glossary](../../docs/00-project-overview/glossary.md), [scope](../../docs/00-project-overview/scope.md) | Hồ sơ đã có, tài liệu cũ (wiki, Confluence) bạn cung cấp | PO |
| 6 | [03-engineering](../../docs/03-engineering/README.md), [05-operations](../../docs/05-operations/README.md) | Lệnh build/test, CI, cách deploy hiện tại | Tech Lead; Owner cho phần vận hành |

Yêu cầu chung cho Task lập hồ sơ:
- Mỗi điều mô tả ghi nguồn `file:line` để người duyệt kiểm được.
- Chỗ code và tài liệu cũ mâu thuẫn, hành vi trông như lỗi, logic không rõ lý do: ghi `OQ-<NN>` vào sổ OQ đúng cấp ([open-questions](open-questions.md)), không đoán.
- Lỗi đã chắc chắn: lập bug theo [BUG-TEMPLATE](../templates/BUG-TEMPLATE.md) để sửa ở Task sửa lỗi riêng, không sửa trong Task tài liệu.

Mẫu Task (điền vào mẫu đầy đủ ở [task-breakdown](task-breakdown.md) §4):

```markdown
# TASK: PRJ-3 - Lập hồ sơ hiện trạng module Đơn hàng

## 1. Objective
Mô tả hiện trạng module Đơn hàng ở project/api vào module-design và api-design, trạng thái Draft.

## 2. Business Context
- Phân loại: chỉ sửa tài liệu · rủi ro thấp (chỉ viết tài liệu, dễ hoàn tác) · mức tự chủ làm trọn Task (người duyệt kết quả cuối)

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
Module chưa có test thì Task đầu tiên vào module đó nên là Task **chỉ viết test**: viết test ghi lại hành vi hiện tại, kể cả hành vi đang bị nghi là sai (ghi chú `OQ-<NN>` trong test). Task `refactor` bắt buộc có test nền trước ([task-types](../workflows/task-types.md), dòng `refactor`). Có lưới test rồi, Tech Lead có thể hạ module từ vùng vàng 🟡 xuống vùng xanh 🟢 trong [PROJECT.md](../../PROJECT.md) §2.2.

### 4.7 Chọn loại Task cho việc thường gặp

| Việc | Loại Task | Điều kiện trước |
| --- | --- | --- |
| Sửa lỗi | sửa lỗi | Có bug report; module có hồ sơ đủ để hiểu hành vi đúng |
| Thêm tính năng chưa có yêu cầu | tính năng mới, rồi làm tính năng | Hồ sơ hiện trạng của module liên quan đã `Approved` (§4.5) |
| Làm tính năng đã có FR, AC, thiết kế | làm tính năng | Như dự án mới |
| Dọn code, tách module | refactor | Có test nền (§4.6) |
| Đổi schema | đổi schema | database-design của phần liên quan đã `Approved` |
| Viết thêm test | chỉ viết test | — |
| Viết hoặc sửa tài liệu | chỉ sửa tài liệu | — |
| Sự cố production | sự cố production | — |

## 5. Giao việc hằng ngày (dùng chung)

### 5.1 Giao việc lớn hoặc Task
- **Việc lớn:** nêu Nguồn: Goal (kết quả muốn đạt, tiêu chí hoàn thành), Epic, User Story hoặc yêu cầu độc lập, kèm căn cứ FR/thiết kế. AI chia thành Plan và Task, đề xuất rủi ro, mức tự chủ, mức model·effort cho từng Task; bạn duyệt Plan là cấp các giá trị đó.
- **Việc nhỏ:** viết một Task theo mẫu ở [task-breakdown](task-breakdown.md) §4; Task chỉ giao AI khi đạt điều kiện sẵn sàng ở §7 của file đó. Ghi đủ: loại Task (danh sách ở [task-types](../workflows/task-types.md) §1), rủi ro, mức tự chủ. Task rủi ro thấp đủ điều kiện fast lane thì chạy ngay, không cần Plan.
- Một Task một việc: không gộp sửa lỗi với refactor lớn.

### 5.2 Mở phiên AI
Mở phiên ở thư mục gốc repo cha. Chọn model, effort **trước khi gõ câu mở đầu**:

| Phiên | Mức | Nghĩa |
| --- | --- | --- |
| Orchestrator lập Plan (bước 1–4) | theo `sessions.orchestrator`: opus/high; opus/xhigh nếu Plan có đổi kiến trúc hoặc API contract | Model mạnh · effort cao / rất cao |
| Orchestrator chạy Plan đã duyệt (bước 5–6: gửi Task, đánh giá, gộp, kiểm) | phiên **mới**, theo `sessions.dispatch`: sonnet/medium; dùng mức lập Plan nếu Plan có Task rủi ro cao, Skill `security-review` hoặc `authentication-rbac`, hoặc đổi kiến trúc | Model chuẩn · effort vừa |
| Orchestrator soạn báo cáo bàn giao (bước 7) | phiên **mới** sau bước 6, theo `sessions.report`: sonnet/high; dùng mức lập Plan nếu Plan có Task rủi ro cao hoặc đổi kiến trúc | Model chuẩn · effort cao |
| Fast lane (một Task rủi ro thấp) | Mức từ ai-config.yaml `tasks` (phần tử đầu của hàng Skill chính), ví dụ sửa tài liệu sonnet/low | Model chuẩn · effort thấp |
| Từng Task (Run) | Orchestrator tự chọn theo manifest; Task duyệt từng bước trở xuống hoặc công cụ không có subagent thì bạn mở phiên mới theo mức Orchestrator báo | — |
| Review (bước 8) | theo `sessions.review`, phiên mới, không dùng lịch sử phiên viết code | Model mạnh · effort cao |

- **Mức theo Task, không theo cả phiên:** mỗi Task có thứ tự thử `try` trong manifest (phần tử đầu là mức bắt đầu, cuối là mức tối đa). Task chạy thấp trước; kết quả không đạt vì năng lực thì Orchestrator tự nâng một bậc, tối đa tới mức tối đa bạn đã duyệt; thiếu đầu vào, yêu cầu mâu thuẫn, bị từ chối quyền thì dừng hỏi bạn ([model-effort](../workflows/model-effort.md) §3).
- **Task mức tự chủ duyệt từng bước trở xuống** (gồm mọi Task code rủi ro cao) không gửi cho subagent: Orchestrator đưa bạn manifest, đường dẫn worktree của Task và câu mở phiên; bạn mở phiên tương tác **trong worktree đó**, ở mức ghi trong manifest, duyệt từng bước, khi trả báo cáo thì kèm chi phí nếu công cụ hiển thị.
- Task rủi ro cao (đụng phân quyền, tiền, dữ liệu cá nhân, migration, bảo mật): mức tối thiểu là `high_risk_min` trong ai-config.yaml.
- Tên model thật nằm ở [ai-config.yaml](../../ai-config.yaml) (`sessions`, `tasks`, `high_risk_min`); đổi công cụ thì sửa `tool`, `auto_runs` và tên model ở đó ([model-effort](../workflows/model-effort.md) §4). Cách chạy Task bằng Claude Code: [ai-tools.md](ai-tools.md) §3. Công cụ không có effort thì mỗi mức chỉ ghi tên model, mức kế là model mạnh hơn.

Câu mở đầu:

```text
Lập Plan từ <GOAL-03 | EPIC-02 | US-WS-01 | yêu cầu: …>. Căn cứ: <FR, thiết kế>. Làm theo AGENTS.md.
```

hoặc với một Task:

```text
Task PRJ-12 (sửa lỗi · rủi ro thấp · làm trọn Task). Làm theo AGENTS.md.
<dán Task Specification hoặc link tới Task>
```

**Nguyên tắc viết prompt.** Prompt chỉ mang **việc gì** (Task, đầu vào, điều kiện riêng của lần này). **Làm thế nào** đã nằm trong Rule, Skill, workflow; không chép lại vào prompt, không viết "hãy cẩn thận", "đừng bịa". Muốn AI làm khác đi thì sửa Rule hoặc Skill bằng Task riêng, không vá bằng prompt. Không dán dữ liệu bí mật (gồm, dữ liệu cá nhân) vào prompt.

### 5.3 Mẫu prompt theo tình huống

Thay phần `<...>`. Mã Task, loại, rủi ro, mức tự chủ lấy từ Task đã viết theo §5.1.

| Tình huống | Prompt |
| --- | --- |
| Khai báo dự án | `Tạo PROJECT.md cho dự án <tên>. Loại: <nội bộ / gia công / bảo trì>. Quy mô: <số người, thời gian>. Dữ liệu xử lý: <mô tả>. Khách hàng: <có / không; đại diện là ai, đầu mối là ai>. Mục nào bạn không biết thì để trống và hỏi.` |
| Nhận tài liệu từ khách hàng | `Task <KEY>-<N> (chỉ sửa tài liệu · rủi ro thấp · duyệt từng bước). Đăng ký tài liệu nguồn vào docs/00-project-overview/sources/: <đường dẫn các file đã ẩn danh>. Người cung cấp: <tên>, ngày nhận: <ngày>. Liệt kê tài liệu còn thiếu thành OQ loại Input.` |
| Khám phá sản phẩm từ tài liệu nguồn | `Task <KEY>-<N> (tính năng mới · rủi ro <thấp/vừa/cao> · duyệt từng bước). Soạn vision, scope, glossary cho module <tên> từ SRC-<NN>, SRC-<NN>. Soạn gói câu hỏi gửi khách hàng cho các điểm chưa rõ.` |
| Phân tích yêu cầu | `Task <KEY>-<N> (tính năng mới · rủi ro <thấp/vừa/cao> · duyệt từng bước). Viết BRD, FR, BR, AC cho module <tên>. Căn cứ: vision, scope đã Approved; SRC-<NN>; OQ đã Closed.` |
| Soạn gói xác nhận gửi khách hàng | `Task <KEY>-<N> (chỉ sửa tài liệu · rủi ro thấp · duyệt từng bước). Soạn gói xác nhận cho <quy trình> theo CONFIRMATION-PACK-TEMPLATE từ SRC-<NN>: phạm vi, quy trình, wireframe từng màn hình, quy tắc, câu hỏi. Điểm chưa rõ thành OQ, không đoán.` Sau đó BA chạy `python3 -I .ai/scripts/export-pack.py <gói>.md --pdf` để gửi |
| Khách hàng đã trả lời | `Khách hàng trả lời các câu hỏi OQ-<NN>, OQ-<NN> (đã lưu SRC-<NN>). Cập nhật sổ OQ và các tài liệu bị ảnh hưởng; câu trả lời sinh câu hỏi mới thì mở OQ mới.` |
| Rà soát yêu cầu | `Task <KEY>-<N> (rà soát yêu cầu · rủi ro thấp · chỉ đọc). Rà soát FR-<MODULE>-* và AC trước khi trình PO duyệt.` |
| Thiết kế | `Task <KEY>-<N> (tính năng mới · rủi ro <thấp/vừa/cao> · duyệt từng bước). Thiết kế module <tên> trên nền <hệ thống sẵn có, đường dẫn code>. Căn cứ: FR-<MODULE>-* đã Approved.` |
| Lập Plan | `Lập Plan từ <GOAL-<NN> | EPIC-<NN> | US-<MODULE>-<NN> | yêu cầu: …>; phục vụ Goal <GOAL-<NN> hoặc không>. Căn cứ FR-<MODULE>-*, thiết kế đã Approved. Chia thành Plan và Task kèm manifest; đề xuất rủi ro, mức tự chủ, mức model·effort cho từng Task.` |
| Chạy Plan đã duyệt | `Plan PLAN-<NNN> đã duyệt. Chạy các Task theo manifest, ghi runs.md.` |
| Soạn báo cáo bàn giao (phiên mới) | `Plan PLAN-<NNN> đã qua bước 6. Soạn báo cáo bàn giao theo DELIVERY-REPORT-TEMPLATE từ runs.md và git diff <base>..<head>.` |
| Làm tính năng | `Task <KEY>-<N> (làm tính năng · rủi ro <...> · mức tự chủ <...>). Làm theo AGENTS.md.` + dán Task |
| Sửa lỗi | `Task <KEY>-<N> (sửa lỗi · rủi ro <...> · mức tự chủ <...>). Làm theo AGENTS.md.` + dán bug report theo BUG-TEMPLATE |
| Review PR (phiên mới) | `Task <KEY>-<N> (review PR · rủi ro <...> · chỉ đọc). Review PR <link/số> của Task <KEY>-<M>. Không dùng lịch sử phiên viết code.` Khi chưa có PR (review trên máy): `Task <KEY>-<N> (review PR · rủi ro <...> · chỉ đọc). Review thay đổi git diff <base>..<head> theo báo cáo bàn giao <đường dẫn>. Không dùng lịch sử phiên viết code.` |
| Tiếp tục phiên bị ngắt | `Tiếp tục Plan PLAN-<NNN> từ .ai/plans/<thư mục>. Đọc bảng Task trong PLAN.md và runs.md để biết đã làm tới đâu.` |
| Duyệt tài liệu | `<Vai> <tên> duyệt, chuyển <file> sang Approved.` |
| Trả lời câu hỏi cần quyết | `OQ-<NN>: chọn phương án <A/B>, lý do <...>.` hoặc `Chưa quyết OQ-<NN>, làm tiếp phần không bị chặn.` |

### 5.4 Việc của bạn ở từng điểm dừng
Các bước AI thực hiện ở [task-execution](../workflows/task-execution.md).

| Khi AI… | Bạn làm |
| --- | --- |
| Hỏi rủi ro, mức tự chủ, độ nghiêm ngặt hoặc loại Task | Trả lời; AI không tự gán |
| Gửi câu hỏi cần quyết (có Vấn đề, Phương án, Đề xuất) | Chọn phương án; muốn quyết sau thì nói rõ phần nào được làm tiếp |
| Gửi Plan và các Task Manifest | Duyệt hoặc yêu cầu sửa: rủi ro, mức tự chủ, thứ tự thử `try`, ngân sách, phạm vi từng Task, quỹ dự phòng và ba giá trị ngân sách (cảnh báo, hạn mức cấp thêm, quỹ). AI chưa chạy Task nào trước khi bạn duyệt |
| Dừng vì vượt mức tối đa, hết lượt hoặc hết ngân sách | Dòng này nay còn gồm các trường hợp: hạn mức cấp thêm đã hết, quỹ dự phòng đã hết, hoặc Task rủi ro cao cần cấp thêm. Đọc các mức đã thử và lỗi; thêm mức vào `try`, sửa manifest, hoặc tự làm |
| Cảnh báo Task dùng đến ngưỡng ngân sách | Đọc đánh giá của Orchestrator: việc đã xong, việc còn lại, vì sao tốn, ước tính để xong. Nếu Task được cấp thêm trong hạn mức thì không cần làm gì, chỉ cần biết số đã cấp (Orchestrator đã giữ chỗ trong sổ và sửa ngân sách trong manifest trước khi chạy tiếp) |
| Hỏi cấp thêm ngân sách | Chọn cấp thêm, đổi hướng, hoặc tự làm |
| Xong một Task | Đưa cho Orchestrator đường dẫn file transcript của phiên điều phối (trong `~/.claude/projects/`); Orchestrator chỉ lấy số liệu (model, token, thời gian), không chép nội dung hội thoại. Transcript có token, không có USD: đưa kèm số USD đọc từ `/cost` (tổng chi phí phiên hiện tại) hoặc từ mục Account & Usage của extension Claude Code; không đọc được thì ghi "không đo USD" |
| Bàn giao (báo cáo bàn giao, kết quả test thật) | Đọc phần giả định, câu hỏi còn mở, phần chưa kiểm |
| Mở PR (hoặc trước khi mở PR) | Review có thể chạy trên máy trước khi có PR, dựa trên báo cáo bàn giao và dải commit. Review bằng **một phiên AI khác** (Task review PR) hoặc người khác; Task rủi ro cao cần thêm một reviewer độc lập |
| Chờ merge, phát hành | Người merge; AI không tự merge, tag hay deploy |

### 5.5 Duyệt tài liệu
Chỉ người có thẩm quyền (cột "Người duyệt" ở [README](../../README.md), mục Giai đoạn và người duyệt) đổi `Draft` sang `Approved`, ghi tên và ngày vào bảng thuộc tính của tài liệu. Có thể tự sửa tay hoặc bảo AI: *"Tech Lead duyệt, chuyển … sang Approved"*. AI không tự chuyển.

Tài liệu cần khách hàng duyệt: Đầu mối gửi khách hàng → khách hàng duyệt, báo Đầu mối → Đầu mối lưu kết quả thành `SRC-<NN>` ([sources](../../docs/00-project-overview/sources/README.md)) → mới chuyển `Approved`, ghi mã `SRC` cạnh tên người duyệt. Khách hàng yêu cầu sửa: ghi thành OQ, AI sửa bản `Draft`, gửi lại.

## 6. Tình huống thường gặp

| Tình huống | Nguyên nhân | Xử lý |
| --- | --- | --- |
| AI dừng, báo thiếu spec, AC hoặc thiết kế | Task không đạt điều kiện sẵn sàng ([project-rules](../rules/project-rules.md) 2) | Bổ sung tài liệu và duyệt, hoặc đổi Task sang tính năng mới hoặc chỉ sửa tài liệu để soạn chúng trước |
| AI dừng, xin miễn trừ | Một yêu cầu của khung chưa đáp ứng được | Duyệt miễn trừ ở [PROJECT.md](../../PROJECT.md) §7, hoặc bổ sung cái còn thiếu |
| AI nói hành vi cũ "có thể là lỗi" | Code và tài liệu, hoặc code và câu trả lời của PO, không khớp | PO/BA quyết: giữ (ghi BR) hay sửa (lập bug, Task sửa lỗi) |
| AI không theo `.ai/`, làm theo chỉ dẫn khác | Repo con còn file chỉ dẫn AI cũ, hoặc phiên mở sai thư mục | Rà theo §4.3; mở phiên ở gốc repo cha |
| AI dùng API không có ở phiên bản thư viện đang chạy | Reference của Skill viết cho bản mới hơn | Ghi phiên bản thực tế ở [PROJECT.md](../../PROJECT.md) §6; nhắc phiên bản trong Task |
| Muốn sửa Rule, Skill trong `.ai/` | `.ai/rules/`, `.ai/skills/`, `.ai/workflows/`, `.ai/templates/`, `.ai/agents/`, `.ai/guide/` là vùng 🔴 (`.ai/plans/` là vùng 🟢) | Mở Task riêng, Tech Lead duyệt ([.ai/README](../README.md)) |
