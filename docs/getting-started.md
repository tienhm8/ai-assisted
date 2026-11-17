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
| Chọn công cụ AI | [ai-tools](03-engineering/ai-tools.md) §1 |
| Tạo symlink cho công cụ AI | [ai-tools](03-engineering/ai-tools.md) §2 |
| Khai báo giá trị riêng của dự án | [PROJECT.md](../PROJECT.md) |
| Cần biết AI làm một Task qua những bước nào | [task-execution](../.ai/workflows/task-execution.md), [task-types](../.ai/workflows/task-types.md) |
| Cần hiểu vì sao AI bị kiểm soát | [ai-governance](03-engineering/ai-governance.md) |
| Cần điều kiện duyệt | [gates-and-rigor](04-project-management/gates-and-rigor.md) |

## 2. Năm khái niệm cần biết trước

| Khái niệm | Nói ngắn | Định nghĩa |
| --- | --- | --- |
| Draft / Approved | AI chỉ soạn `Draft`; chỉ người có thẩm quyền đổi sang `Approved`. AI chỉ dựa vào tài liệu `Approved` | [project-rules](../.ai/rules/project-rules.md) 4, 14 |
| Cổng G0–G7 | Điều kiện phải đạt để sang giai đoạn sau, qua bằng bằng chứng | [gates-and-rigor](04-project-management/gates-and-rigor.md) §1 |
| Độ nghiêm ngặt S1–S3 | Chọn một lần cho cả dự án | [gates-and-rigor](04-project-management/gates-and-rigor.md) §2 |
| Task với R và A | Mỗi Task có mức rủi ro R1–R3 và mức tự chủ A0–A4; thiếu thì AI dừng và hỏi | [project-rules](../.ai/rules/project-rules.md), mục "Thang dùng chung" |
| Vùng 🟢🟡🔴 | Đường dẫn AI được sửa tự do, sửa khi plan đã duyệt, hay cần Task riêng | [PROJECT.md](../PROJECT.md) §2.2 |

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

Mỗi dòng là một hoặc nhiều Task; AI soạn `Draft`, người ở cột "Duyệt" chuyển `Approved`.

| Bước | Tài liệu | Loại Task giao AI | Duyệt | Cổng |
| --- | --- | --- | --- | --- |
| 1 | [00-project-overview](00-project-overview/README.md): vision, scope, glossary | T1 (Skill `product-discovery`) hoặc T12 | PO | G1 |
| 2 | [01-requirements](01-requirements/README.md): BRD, FR, NFR, BR, AC | T1 (phần yêu cầu), rà bằng T8 | PO/BA, QA rà | G2 |
| 3 | [02-architecture](02-architecture/README.md): kiến trúc, module, DB, API, ADR | T1 (phần thiết kế) hoặc T7 | Kiến trúc sư (+ Security nếu có tiền, phân quyền, dữ liệu cá nhân, migration) | G3 |
| 4 | [03-engineering](03-engineering/README.md): chuẩn code, bảo mật, lỗi, test | T12 | Tech Lead | G4 |
| 5 | [04-project-management](04-project-management/README.md): roadmap, backlog, chia Task | T1 (Skill `task-planning`) | Tech Lead; PO quyết ưu tiên | G4 |
| 6 | [05-operations](05-operations/README.md): deployment, monitoring, backup | T12, có thể làm song song từ bước 3 | Owner, tham khảo Tech Lead | trước G7 |

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

### 5.1 Viết Task
- Dùng mẫu ở [task-breakdown](04-project-management/task-breakdown.md) §4; Task chỉ giao AI khi đạt điều kiện sẵn sàng ở §7 của file đó.
- Ghi đủ: loại Task (T1–T15, danh sách ở [task-types](../.ai/workflows/task-types.md) §1), rủi ro R, mức tự chủ A. Thiếu là AI dừng và hỏi.
- Một Task một việc: không gộp sửa lỗi với refactor lớn.

### 5.2 Mở phiên AI
Mở phiên ở thư mục gốc repo cha, chọn model và effort theo cột "Model · Effort" của loại Task ([task-types](../.ai/workflows/task-types.md) §1; ánh xạ sang model thật ở [references/](../.ai/agents/references/) theo công cụ đang dùng). Câu mở đầu:

```text
Task PRJ-12 (T3 · R1 · A3). Làm theo AGENTS.md.
<dán Task Specification hoặc link tới Task>
```

### 5.3 Việc của bạn ở từng điểm dừng
Các bước AI thực hiện ở [task-execution](../.ai/workflows/task-execution.md).

| Khi AI… | Bạn làm |
| --- | --- |
| Hỏi R, A, S hoặc loại Task | Trả lời; AI không tự gán |
| Gửi câu hỏi cần quyết (có Vấn đề, Phương án, Đề xuất) | Chọn phương án; muốn quyết sau thì nói rõ phần nào được làm tiếp |
| Gửi plan (Task R3, A2 trở xuống, đụng schema/API/phân quyền, vùng 🟡) | Duyệt hoặc yêu cầu sửa plan; AI chưa sửa code trước khi bạn duyệt |
| Bàn giao (báo cáo bàn giao, kết quả test thật) | Đọc phần giả định, câu hỏi còn mở, phần chưa kiểm |
| Mở PR | Review bằng **một phiên AI khác** (Task T9) hoặc người khác; Task R3 cần thêm một reviewer độc lập |
| Chờ merge, phát hành | Người merge; AI không tự merge, tag hay deploy |

### 5.4 Duyệt tài liệu
Chỉ người có thẩm quyền (cột "Người duyệt" ở [README](../README.md), mục Giai đoạn và người duyệt) đổi `Draft` sang `Approved`, ghi tên và ngày vào bảng thuộc tính của tài liệu. Có thể tự sửa tay hoặc bảo AI: *"Tech Lead duyệt, chuyển … sang Approved"*. AI không tự chuyển.

## 6. Tình huống thường gặp

| Tình huống | Nguyên nhân | Xử lý |
| --- | --- | --- |
| AI dừng, báo thiếu spec, AC hoặc thiết kế | Task không đạt điều kiện sẵn sàng ([project-rules](../.ai/rules/project-rules.md) 2) | Bổ sung tài liệu và duyệt, hoặc đổi Task sang T1/T12 để soạn chúng trước |
| AI dừng, xin miễn trừ | Một yêu cầu của khung chưa đáp ứng được | Duyệt miễn trừ ở [PROJECT.md](../PROJECT.md) §7, hoặc bổ sung cái còn thiếu |
| AI nói hành vi cũ "có thể là lỗi" | Code và tài liệu, hoặc code và câu trả lời của PO, không khớp | PO/BA quyết: giữ (ghi BR) hay sửa (lập bug, Task T3) |
| AI không theo `.ai/`, làm theo chỉ dẫn khác | Repo con còn file chỉ dẫn AI cũ, hoặc phiên mở sai thư mục | Rà theo §4.3; mở phiên ở gốc repo cha |
| AI dùng API không có ở phiên bản thư viện đang chạy | Reference của Skill viết cho bản mới hơn | Ghi phiên bản thực tế ở [PROJECT.md](../PROJECT.md) §6; nhắc phiên bản trong Task |
| Muốn sửa Rule, Skill trong `.ai/` | `.ai/` là vùng 🔴 | Mở Task riêng, Tech Lead duyệt ([.ai/README](../.ai/README.md)) |
