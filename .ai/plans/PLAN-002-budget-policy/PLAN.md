# PLAN: PLAN-002 — Quy tắc cảnh báo, cấp thêm và thu hồi ngân sách

> AI (Orchestrator) soạn; người phát triển khung (vai Tech Lead của khung) duyệt trước khi chạy Task. Duyệt Plan là duyệt mức rủi ro, mức tự chủ, thứ tự thử model/effort, ngân sách, phạm vi của mọi Task, **và các giá trị ở §6.2** (ngưỡng cảnh báo, hạn mức cấp thêm, quỹ dự phòng).
> Plan này viết lựa chọn bằng chữ (`project-rules` 23).

| Mục | Giá trị |
| --- | --- |
| ID | `PLAN-002` |
| Nguồn (Source) | Yêu cầu độc lập của người phát triển khung, 2026-11-19: khi Task thiếu ngân sách so với thực tế chạy thì khung phải có cách xử lý (cảnh báo sớm, đánh giá lại, cấp thêm, thu hồi). Hai quyết định đã chốt cùng ngày: "Ngân sách tối đa" là trần của cả Plan (phương án A); Orchestrator được tự cấp thêm trong hạn mức nhỏ, vượt thì hỏi người (phương án C) |
| Goals (tuỳ chọn) | Không có |
| Trạng thái | Done |
| Người duyệt · Ngày duyệt | Người phát triển khung (vai Tech Lead của khung) · 2026-11-19: duyệt từ vựng và công thức §6.1, ba giá trị §6.2, cách đo §6.5, mức rủi ro và mức tự chủ §5, ngân sách tối đa 7,5 USD. Chưa chạy Task nào; BG-1 chỉ chạy sau khi PLAN-001 xong (§1 "Phụ thuộc ngoài") |
| Ngày tạo | 2026-11-19 |
| Branch · commit gốc | `refactor/AI-framework-refactor` · `135fe14` (đã gồm PLAN-001 xong, FW-8 đã gộp) |
| Model/effort của Orchestrator | opus/high (theo `sessions.orchestrator`; Plan không có Task đổi kiến trúc hay API contract) |
| Ngân sách tối đa của Plan | 7,5 USD = 4 (Task: BG-1 3, BG-2 1) + 0 (quỹ dự phòng) + 2 (Review) + 1,5 (phiên điều phối), thoả `NganSachToiDa >= NganSachTask + QuyDuPhong + Review + PhienDieuPhoi`, ước tính theo số Claude Code tự báo, không phải tiền thực trả qua proxy. **Không có quỹ dự phòng**: quy tắc cấp thêm do chính Plan này tạo ra nên chưa có hiệu lực. Chạm trần thì dừng, hỏi người |

## 1. Mục tiêu và phạm vi

**Đầu ra:** quy tắc ngân sách trong khung, gồm:
- Cảnh báo khi một Task dùng đến ngưỡng ngân sách, kèm bước đánh giá lại.
- Cấp thêm ngân sách từ quỹ dự phòng của Plan, trong hạn mức đã duyệt.
- Thu hồi phần chưa dùng của Task đã xong về quỹ dự phòng.
- Sổ ghi mọi điều chỉnh ngân sách trong `runs.md`.

**Làm:**
- Ba giá trị mặc định ghi thẳng vào `ai-config.yaml`.
- Quy tắc ở `model-effort.md` (quy tắc 9 đến 13), `task-execution.md`.
- Chỗ khai báo quỹ dự phòng ở mẫu Plan; sổ điều chỉnh ở mẫu `runs.md`; Skill `task-planning` biết khai báo quỹ.
- Hướng dẫn cho người (`getting-started.md`, `glossary.md`, `ai-tools.md`).

**Không làm:**
- Không sửa `project-rules` (xem §6.3 vì sao không cần).
- Không đổi thứ tự thử model/effort, số lượt chạy lại tối đa, hay cách đánh giá Đạt/Không đạt.
- Không tự động hoá việc cộng chi phí (Orchestrator vẫn cộng từ `runs.md` như hiện nay).
- Không sửa PLAN-001 và `check.py` của nó.

**Vì sao là một Plan riêng:** mục tiêu đầu ra khác PLAN-001 (chính sách ngân sách, không phải tái cấu trúc); có thể duyệt và chạy độc lập sau khi PLAN-001 xong.

**Phụ thuộc ngoài:** PLAN-001 đã xong (người phát triển khung xác nhận 2026-11-19; commit `135fe14` là báo cáo bàn giao, có đủ Run của FW-8). BG-1 và BG-2 bắt đầu từ `135fe14` trên nhánh `refactor/AI-framework-refactor`. Nhánh này chưa gộp vào `master`; xem §9.

## 2. Tiêu chí hoàn thành

- Mọi AC của BG-1 và BG-2 đạt; lệnh kiểm hồi quy (`links`, `vocab`, `types`, `config`, `tree`, `codes`) đạt 0 lỗi.
- Review bước 8 không có phát hiện mức Critical hay High.
- Người phát triển khung đọc §6.1 và xác nhận quy tắc viết trong file khớp với bảng đó.

## 3. Yêu cầu và ngữ cảnh đã nạp

Không có FR (Plan kỹ thuật, sửa khung). Điểm áp dụng từ tài liệu hiện có:

| Tài liệu · mục | Điều áp dụng |
| --- | --- |
| `model-effort.md` §3 quy tắc 5, 6, 7 | Ngân sách cộng dồn theo Task; vượt thì dừng. Là chỗ cần mở rộng, không thay |
| `task-execution.md` "Plan approval" | Duyệt Plan là duyệt ngân sách từng Task. Cấp thêm trong quy tắc đã duyệt coi như nâng mức trong `try` đã duyệt: không phải thay đổi cần duyệt lại |
| `ai-tools.md` | `claude -p --max-budget-usd` tính theo từng lần gọi và cắt Run khi chạm trần: giữa Run không có chỗ cảnh báo |
| `project-rules` 8, 19, 20 | Mức tự chủ do người duyệt cấp; Task rủi ro cao giữ cổng và review; AI không tự coi cổng duyệt đã qua |
| `project-rules` 18 | Trần chi tiêu của Task là giới hạn cứng, không được lách bằng chạy lại |

## 4. Chiến lược

- **Hai Task nối tiếp.** BG-1 viết quy tắc và mẫu cho AI (nguồn gốc). BG-2 viết hướng dẫn cho người, đọc lại từ chữ của BG-1 nên phải chờ BG-1 xong.
- **Chuỗi Skill:** `documentation`. Bước thiết kế đã làm ở §6, nên không cần `architecture-design`.
- **BG-1 bắt đầu ở mức cao** (`sonnet/high`, lệch mặc định có lý do), giống cách PLAN-001 xử lý FW-3: BG-1 viết lại quy tắc nâng mức mà mọi Plan sau dựa vào, chạy mức thấp dễ trượt rồi tốn thêm một Run.
- **Cách chạy:** như PLAN-001 §4: worktree riêng ở `.claude/worktrees/<Task>`, `claude -p` với `--max-budget-usd` bằng ngân sách còn lại.
- **Điểm dừng ⏸:** người phát triển khung xem kết quả BG-1 trước khi chạy BG-2, vì BG-2 chép lại ngôn từ của BG-1.

## 5. Task

Mọi Task chạm file của khung ở vùng đỏ. Rủi ro: **vừa (`medium`)**, người phát triển khung xác nhận 2026-11-19 (xem §8). Mức tự chủ đề xuất: **làm trọn Task (`full-task`: người duyệt kết quả cuối)**.

| Task | Tên | Loại | Rủi ro · Tự chủ | Cách chạy | Agent | Skill | Thứ tự thử | Ngân sách (USD) | Lệch mặc định | Phụ thuộc | Cổng | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BG-1 | Quy tắc và mẫu cho AI: ngân sách (3 giá trị, quy tắc 9 đến 13 của `model-effort`, `task-execution`, mẫu Plan, mẫu `runs.md`, mẫu manifest, Skill `task-planning`) | `docs-only` (chỉ sửa tài liệu) | `medium` (ảnh hưởng nhiều file khung đã Approved) · `full-task` (làm trọn, người duyệt kết quả cuối) | Gửi đi | executor | documentation | sonnet/high → opus/high | 3 | **Có**: bắt đầu ở mức cao; mặc định của `documentation` là `sonnet/low` → `sonnet/high`, và ngân sách 3 cao hơn mặc định 2. Lý do: viết lại quy tắc ngân sách và nâng mức mà mọi Plan sau dựa vào; ước tính theo FW-3 (1,489 USD, 3 Run) | PLAN-001 xong | ⏸ Người phát triển khung xem kết quả | New |
| BG-2 | Hướng dẫn cho người: `getting-started`, `glossary`, `ai-tools` | `docs-only` | `medium` · `full-task` | Gửi đi | executor | documentation | sonnet/low → sonnet/high | 1 | Không (ước tính theo FW-7: 0,679 USD, 1 Run) | BG-1 | — | New |
| Review (bước 8) | Review độc lập toàn bộ diff | `pr-review` (review Pull Request; chạy trên máy từ báo cáo bàn giao và dải commit) | `medium` · `read-only` (chỉ đọc và báo cáo) | Gửi đi | reviewer | code-review | opus/high → opus/xhigh | 2 | Không | BG-1, BG-2 | — | New |

Tổng: 2 Task 4 USD, Review 2 USD, phiên điều phối 1,5 USD, cộng 7,5 USD. Mỗi Run đặt `--max-budget-usd` bằng ngân sách còn lại của Task.

## 6. Thiết kế

### 6.1 Quy tắc ngân sách (đây là phần người duyệt cần đọc kỹ)

Áp dụng cho Plan có quỹ dự phòng, từ Plan sau PLAN-002.

| Bước | Quy tắc | Nguồn |
| --- | --- | --- |
| 1. Khai báo | Plan chia ngân sách thành bốn phần và ghi cả công thức: `NganSachToiDa >= NganSachTask + QuyDuPhong + Review + PhienDieuPhoi`. `NganSachTask` là tổng ngân sách **ban đầu** của các Task; quỹ dự phòng mặc định `budget_pool_pct` % của số đó. Quỹ nằm **bên trong** ngân sách tối đa, không phải khoản cộng thêm; Review và phiên điều phối là hai khoản riêng, không lấy từ quỹ. Phần chưa phân bổ (vế trái lớn hơn vế phải) không dùng để cấp thêm. Ngân sách tối đa **không bao giờ tự tăng** | Phương án A; góp ý 2026-11-19 điểm 1 |
| 2. Cảnh báo | Sau mỗi Run, nếu chi phí cộng dồn của Task đạt `budget_warn_pct` % ngân sách hiện hành, hoặc Run bị công cụ cắt vì chạm trần: Orchestrator **không bắt đầu Run mới** và chuyển sang bước 3 | Yêu cầu của người phát triển khung |
| 3. Đánh giá lại | Orchestrator (không mở Run mới) đọc `runs.md` và ghi: việc đã xong (tiêu chí đã đạt), việc còn lại (tiêu chí chưa đạt), vì sao tốn nhiều (Run nào, lỗi nào), và **một** ước tính chi phí, ghi rõ tên: `DuKienTong` (tổng chi phí của Task tính từ đầu đến khi xong) hoặc `DuKienThem` (chi phí còn phải tiêu từ thời điểm hiện tại). Không ghi tên thì Orchestrator không được tính bước 4. Không nêu được việc còn lại cụ thể thì Task **dừng**, không cấp thêm | Yêu cầu; sửa "Agent đánh giá lại" thành Orchestrator (câu hỏi 2) |
| 4. Tính số thiếu | `NganSachHienHanh` = ngân sách ban đầu + đã cấp thêm. `DaDung` = chi phí cộng dồn trong `runs.md`. `ConLai = NganSachHienHanh − DaDung`. Nếu ước tính là `DuKienTong`: `Thieu = max(0, DuKienTong − NganSachHienHanh)`. Nếu là `DuKienThem`: `Thieu = max(0, DuKienThem − ConLai)`. Hai cách cho cùng kết quả khi số liệu nhất quán (`DuKienTong = DaDung + DuKienThem`). **Không nhầm tên**: không lấy `DuKienThem` trừ `NganSachHienHanh` (cấp thiếu), không lấy `DuKienTong` trừ `ConLai` (cấp thừa đúng bằng `DaDung`); cũng không trừ `ConLai` hai lần. Số cấp thêm = `Thieu` | Yêu cầu; góp ý điểm 2, người phát triển khung xác nhận công thức 2026-11-19 |
| 5. Điều kiện cấp thêm | Orchestrator tự cấp từ quỹ khi **đủ cả bốn**: (a) Task không phải rủi ro cao; (b) `Thieu` không vượt số dư quỹ trong sổ; (c) tổng đã cấp thêm cho Task cộng `Thieu` không vượt `budget_topup_max_pct` % ngân sách ban đầu; (d) dòng giữ chỗ ở bước 6 ghi được vào sổ. Thiếu một điều kiện thì dừng, hỏi người theo mẫu `project-rules` 21 | Phương án C |
| 6. Giữ chỗ và tuần tự | Số dư quỹ chỉ đọc từ sổ điều chỉnh trong `runs.md`, không từ trí nhớ. Orchestrator xử lý **từng** quyết định cấp thêm một, theo thứ tự Run kết thúc ghi trong `runs.md`: đọc số dư → kiểm điều kiện bước 5 → **ghi dòng giữ chỗ vào sổ (số dư giảm ngay)** → mới được sang bước 7. Quyết định sau đọc lại số dư đã giảm. Hai Task cùng đủ điều kiện mà quỹ chỉ đủ cho một thì Task sau không được cấp: dừng, hỏi người (không tự cấp một phần). Task chờ quyết định không bắt đầu Run mới | Góp ý điểm 4 |
| 7. Đồng bộ manifest | Sau khi giữ chỗ và trước Run kế tiếp, Orchestrator sửa trong manifest của Task **chỉ** `execution.budget.max_cost_usd` thành `NganSachHienHanh` mới. `initial_cost_usd` (ngân sách ban đầu lúc duyệt Plan) **không bao giờ sửa**; hạn mức cấp thêm tính trên số này. `--max-budget-usd` của Run kế tiếp = `max_cost_usd` mới trừ `DaDung`. Chi phí cộng dồn của Task vẫn bị chặn bởi `max_cost_usd`. Thứ tự bắt buộc: giữ chỗ → sửa manifest → Run; sửa manifest lỗi thì ghi dòng trả lại giữ chỗ vào sổ và không chạy. Sửa này không phải thay đổi cần duyệt lại | Góp ý điểm 3 |
| 8. Thu hồi | Task xong (kết quả được nhận) thì phần ngân sách hiện hành chưa dùng (`NganSachHienHanh − DaDung`) về quỹ, ghi vào sổ. Task bị huỷ hoặc dừng chờ người không trả về cho đến khi người quyết định | Yêu cầu |
| 9. Sổ điều chỉnh | Mọi lần giữ chỗ cấp thêm, trả lại giữ chỗ, thu hồi, dừng hỏi người ghi một dòng mới vào bảng "Điều chỉnh ngân sách" trong `runs.md`, không sửa dòng cũ: Task, loại, số tiền, ngân sách Task trước → sau, số dư quỹ trước → sau, lý do (kèm kết quả đánh giá lại), ngày | Yêu cầu: "mọi điều chỉnh phải được ghi nhận" |
| 10. Dừng | Task không thể xong thì dừng ngay, không tiêu thêm tiền (đã có ở `model-effort` quy tắc 7) | Yêu cầu |

### 6.2 Ba giá trị đặt thẳng vào `ai-config.yaml`

| Khoá | Giá trị | Ý nghĩa | Nguồn giá trị |
| --- | --- | --- | --- |
| `budget_warn_pct` | 80 | Ngưỡng cảnh báo, phần trăm ngân sách hiện hành của Task | Người phát triển khung nêu; xác nhận 2026-11-19 |
| `budget_topup_max_pct` | 50 | Tổng cấp thêm tối đa cho một Task, phần trăm ngân sách ban đầu | Người phát triển khung xác nhận 2026-11-19 (AI đề xuất ban đầu) |
| `budget_pool_pct` | 20 | Quỹ dự phòng mặc định của Plan, phần trăm tổng ngân sách các Task | Người phát triển khung xác nhận 2026-11-19 (AI đề xuất ban đầu) |

Giá trị đã đặt thẳng ở nơi dùng (không thêm tầng tra cứu). Plan được đặt khác mặc định nếu ghi lý do; khi đó Plan phải chờ duyệt như mọi lệch mặc định.

### 6.3 Vì sao không cần sửa `project-rules`

`project-rules` 8 nói mức tự chủ do người duyệt Plan cấp. Quy tắc ngân sách mới nằm trong Plan đã duyệt: duyệt Plan là duyệt số quỹ dự phòng, ba giá trị ở §6.2 và quy tắc ở §6.1. Orchestrator cấp thêm là làm theo thứ đã duyệt, giống nâng mức model trong `try` đã duyệt (`task-execution` "Re-approval": nâng mức trong `try` không phải thay đổi). Muốn tăng ngân sách tối đa, quỹ dự phòng, hoặc vượt hạn mức cấp thêm của một Task thì phải hỏi người như hiện nay.

Hệ quả cho ngoại lệ "không chờ duyệt Plan" ở `task-execution.md`: điều kiện "ngân sách nằm trong `budget_usd_per_task`" tính ở lúc lập Plan. Cấp thêm về sau không làm mất ngoại lệ, vì đã nằm trong quỹ dự phòng được duyệt.

### 6.4 Lựa chọn mặc định của AI (người duyệt có thể đổi)

- **Cảnh báo giữa các Run, không giữa một Run.** `claude -p` chỉ trả chi phí khi Run kết thúc và cắt Run ở trần, nên một Run có thể đi từ dưới 80% thẳng đến 100%. Run bị cắt coi như đã chạm ngưỡng. Cách khác (đặt trần mỗi Run thấp hơn ngân sách còn lại để luôn dừng ở 80%) tốn thêm Run nên không chọn.
- **Chỉ Task xong mới thu hồi.** Task bị huỷ hoặc dừng chờ người không trả tiền về quỹ cho đến khi người quyết định.
- **Đường nhanh cho Task rủi ro thấp (không có Orchestrator) không có quỹ dự phòng**: thiếu ngân sách thì dừng và hỏi người như hiện nay.
- **Phiên điều phối và Review có ngân sách riêng trong tổng Plan**, không lấy từ quỹ dự phòng.

### 6.5 Đo chi phí phiên điều phối: người cung cấp transcript sau mỗi Task

Người phát triển khung chọn phương án A (2026-11-19): chi phí phiên Orchestrator không nằm trong kết quả JSON của `claude -p`, nên **sau khi xong mỗi Task, người đưa cho Orchestrator file transcript** của phiên điều phối, ở `~/.claude/projects/-home-tienhm-projects-ai-assisted/<id>.jsonl`.

- **Orchestrator chỉ trích số liệu, không đọc nội dung hội thoại:** model, effort, token vào/ra/ghi cache/đọc cache theo từng model, thời gian bắt đầu và kết thúc. Transcript chứa toàn bộ trao đổi của người dùng nên không in nội dung ra báo cáo, `runs.md` hay commit.
- **Cắt theo khoảng thời gian của Task**, vì một file có thể chứa việc của Plan khác.
- **Ghi vào `runs.md` một dòng "Phiên điều phối" cho mỗi Task** (không sửa dòng cũ): tên file transcript, khoảng thời gian, token theo model. Số USD: transcript chỉ có token, không có USD, nên **người đọc USD của phiên và đưa cho Orchestrator cùng transcript**. Người phát triển khung nêu hai nơi đọc (2026-11-19): lệnh `/cost` (tổng chi phí phiên hiện tại bằng USD, kèm thời lượng và số token) và mục Account & Usage của extension Claude Code. AI chưa tự kiểm hai nơi này; lần đầu chạy, Orchestrator đối chiếu số USD người đưa với token trong transcript, lệch rõ thì hỏi lại. Không đọc được thì ghi "không đo USD" kèm lý do (đã có chỗ cho phép ở `RUNS-TEMPLATE`).
- **Áp dụng ngay từ PLAN-002**: đây là việc của người và Orchestrator, không cần chờ BG-1 viết xong. BG-1 chỉ ghi quy trình vào mẫu `runs.md` và `task-execution` để các Plan sau làm theo.

### 6.6 File dự kiến thay đổi

| Task | File |
| --- | --- |
| BG-1 | `ai-config.yaml`, `.ai/workflows/model-effort.md`, `.ai/workflows/task-execution.md`, `.ai/templates/PLAN-TEMPLATE.md`, `.ai/templates/RUNS-TEMPLATE.md`, `.ai/templates/TASK-MANIFEST-TEMPLATE.yaml`, `.ai/skills/task-planning/SKILL.md` |
| BG-2 | `.ai/guide/getting-started.md`, `.ai/guide/glossary.md`, `.ai/guide/ai-tools.md` |

Không thêm, đổi tên hay xoá file nào trong khung, nên cây "Cấu trúc" của `README.md` không đổi (`check.py tree` kiểm).

### 6.7 Góp ý của người phát triển khung ngày 2026-11-19 đã đưa vào §6.1

- **Điểm 1:** công thức bốn phần, quỹ nằm trong ngân sách tối đa (bước 1).
- **Điểm 2:** hai tên ước tính `DuKienTong`, `DuKienThem` và công thức `Thieu` (bước 3, 4). Người phát triển khung xác nhận ngày 2026-11-19: không bỏ qua `ConLai`; chỉ không được nhầm chi phí cần tiêu thêm với tổng chi phí dự kiến.
- **Điểm 3:** `max_cost_usd` = ngân sách hiện hành, thêm `initial_cost_usd` không bao giờ sửa, thứ tự giữ chỗ → sửa manifest → Run (bước 7).
- **Điểm 4:** giữ chỗ ghi sổ trước khi Task chạy tiếp, xử lý tuần tự (bước 6).
- **Cách đo (phương án A):** §6.5.

## 7. Kế hoạch kiểm thử

Chi tiết lệnh ở `acceptance_criteria` của từng manifest. Tóm tắt:
- Giá trị trong `ai-config.yaml` đọc được bằng YAML và đúng 80, 50, 20.
- Từ khoá bắt buộc có trong từng file (grep), gồm công thức bốn phần, `Thieu`, `DuKienTong`, `DuKienThem`, giữ chỗ, `initial_cost_usd`.
- Người kiểm đọc thử hai ví dụ số: một Task thiếu 0,3 USD khi quỹ còn 0,8; hai Task cùng thiếu 0,8 USD khi quỹ còn 0,8 (chỉ một Task được cấp).
- Hồi quy: `check.py links`, `vocab`, `types`, `config`, `tree`, `codes` trên các file đã sửa.
- Con người kiểm: quy tắc trong file khớp bảng §6.1; Task rủi ro cao luôn hỏi người; ngân sách tối đa không có chỗ nào tự tăng.

## 8. Rủi ro và điểm cần người quyết

Cả năm điểm trong bản nháp đã được người phát triển khung quyết ngày 2026-11-19. Không còn điểm mở nào chặn việc duyệt Plan.

| Điểm | Quyết định | Nơi áp dụng |
| --- | --- | --- |
| Ba giá trị | Cảnh báo ở 80% ngân sách Task; tổng cấp thêm tự động tối đa 50% ngân sách ban đầu của Task; quỹ dự phòng 20% tổng ngân sách các Task | §6.2 |
| Ai đánh giá lại | Orchestrator, từ `runs.md`, không mở Run chỉ để đánh giá | §6.1 bước 3 |
| Mức rủi ro | Vừa. Task rủi ro vừa được cấp thêm tự động trong hạn mức; Task rủi ro cao luôn hỏi người | §5, §6.1 bước 5 |
| Nhầm lẫn ước tính | Giữ `ConLai`; hai tên `DuKienTong`, `DuKienThem` với công thức `Thieu` | §6.1 bước 3, 4 |
| USD của phiên điều phối | Người đọc từ `/cost` hoặc Account & Usage, đưa cùng transcript | §6.5 |

**Việc còn lại sau khi duyệt:** đo 80/50/20 bằng số liệu thật ở Plan kế tiếp và chỉnh qua `periodic-review` nếu cần. Chưa có Plan nào chạy theo quy tắc mới.

## 9. Kết quả (điền sau khi xong)

Nguồn: [DELIVERY-REPORT](DELIVERY-REPORT.md) và [runs.md](runs.md). Cả hai Task đã được nhận; Plan và manifest chuyển `Done` theo `task-execution` bước 7.

**Người phát triển khung đã xác nhận BG-1-AC6 và BG-2-AC5** (quy tắc 9 đến 13 khớp PLAN §6.1; hướng dẫn khớp quy tắc 9 đến 13).

**Còn chờ (không chặn Done):** phiên điều phối: transcript và số USD từ `/cost` hoặc Account & Usage để ghi dòng PLAN-002-ĐIỀU-PHỐI#1.

**Kết quả:** BG-1 đạt, BG-2 đạt; review bước 8 (PLAN-002-REVIEW#1) duyệt có điều kiện, ba điều kiện Medium đã sửa ở BG-1#2. Chi phí các Run 0,701 + 0,114 USD; review 1,269 USD.

Đầu ra của từng Task, lệch kế hoạch ở đâu, Task nào phải nâng mức, bằng chứng test, trạng thái tiêu chí hoàn thành §2.
