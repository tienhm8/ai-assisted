# Skill Orchestration Workflow

> Trạng thái: **Draft**. Làm rõ dần theo Task thật; người có thẩm quyền mới chuyển sang Approved.
> Sửa file này thuộc vùng 🔴 (luật chơi của AI): cần Task riêng và người duyệt.

Quy trình để AI **nhận diện loại Task → chọn Skill → phối hợp Skill theo thứ tự → kiểm tra điều kiện đầu ra → bàn giao**. Workflow này là lớp điều phối trên 17 Skill trong [../skills/](../skills/README.md); nó không lặp lại nội dung từng Skill.

Quan hệ với các thành phần khác:

| Thành phần | Vai trò | Nằm ở |
| --- | --- | --- |
| Rule | Điều bắt buộc, luôn áp dụng | [../rules/](../rules/README.md) |
| Skill | Cách làm một loại việc | [../skills/](../skills/README.md) |
| Workflow này | Chọn và xếp Skill cho một Task | file này + [skill-selection.md](skill-selection.md) |
| Tài liệu nghiệp vụ | Nguồn sự thật về nghiệp vụ | `docs/` |

Workflow cụ thể hoá bước 1–8 của "Quy trình thực hiện một Task" ([task-execution.md](task-execution.md)) cho việc dùng Skill. Khi hai bên khác nhau, task-execution.md và Rule thắng.

## Nguyên tắc

1. **Chỉ nạp Skill cần cho Task.** Không đọc cả 17 Skill mỗi lần; chọn theo loại Task ([skill-selection.md](skill-selection.md)).
2. **Skill không thay Rule, không thay tài liệu nghiệp vụ.** Đọc FR/BR trước; ví dụ trong Skill không phải nghiệp vụ chính thức.
3. **Mỗi Skill có cổng vào và cổng ra.** Chưa qua cổng ra thì không chuyển Skill tiếp theo.
4. **Có bằng chứng mới qua cổng** (P4): output test, diff, tài liệu Approved. Không báo pass khi chưa chạy.
5. **Không tự chốt quyết định.** Yêu cầu, kiến trúc, quyền, bảo mật chưa được duyệt thì ghi thành câu hỏi mở, không triển khai theo phỏng đoán.
6. **Skill không được nâng mức tự chủ.** Mức tự chủ do Task cấp (A0–A4); Skill chỉ hướng dẫn cách làm.

## Sáu giai đoạn điều phối

### 1. Intake và phân loại Task

AI đọc Task (mục tiêu, actor, phạm vi, AC, mức rủi ro, mức tự chủ) và xác định:

- **Loại Task** theo bảng ở [skill-selection.md](skill-selection.md). Task lai (ví dụ "sửa lỗi + thêm trường") thì tách thành các Task con, mỗi Task một loại.
- **Mức rủi ro (R1–R3)** và **mức tự chủ (A0–A4)** do Task cấp. Thiếu thì dừng và hỏi, không tự gán.
- **Điểm chưa rõ:** mâu thuẫn tài liệu, thiếu AC, thiếu quyết định nghiệp vụ.

Đầu ra: loại Task + danh sách câu hỏi (nếu có). Gặp điều kiện dừng ở mục "Dừng và hỏi" thì không đi tiếp phần bị ảnh hưởng.

### 2. Nạp ngữ cảnh

Thứ tự nạp: `PROJECT.md` (nếu có) → Task/Scope/AC → quyết định liên quan (ADR) → FR/BR/contract/kiến trúc trong `docs/` → Rules → Skill đã chọn → code, test, cấu hình → Git diff.

Đầu ra: context set ghi trong plan (tài liệu và file đã đọc).

### 3. Lập chuỗi Skill (plan)

AI lập plan gồm:

- Danh sách Skill sẽ dùng, theo thứ tự, và Skill nào chạy song song.
- Với mỗi Skill: đầu vào lấy từ đâu, đầu ra mong đợi.
- File dự kiến đổi, kế hoạch test, rủi ro.
- Skill nào **không** dùng và lý do (khi dễ gây thắc mắc, ví dụ bỏ `security-review` ở Task R1).

Quy tắc xếp thứ tự:

- Phân tích và thiết kế trước, code sau; test viết cùng hoặc ngay sau code.
- Skill review (`code-review`, `security-review`) chạy **sau** khi có diff và kết quả test.
- `documentation` chạy sau khi hành vi đã ổn định, trước bàn giao.
- `deployment` luôn là bước cuối và là Task riêng khi chạm production.
- Skill độc lập (không dùng đầu ra của nhau) được chạy song song, ví dụ `frontend-development` và `backend-development` khi API contract đã chốt.

### 4. Điểm chờ duyệt

AI dừng và xin duyệt plan khi:

- Vượt phạm vi Task, hoặc đổi kiến trúc, contract, quyền, schema, dữ liệu.
- Task R3, hoặc mức tự chủ chỉ cho phép A2 trở xuống (duyệt từng bước).
- Chuỗi có Skill thuộc nhóm **cần phê duyệt hành động** (xem bảng "Giới hạn hành động").

Đầu ra: plan được duyệt, hoặc câu hỏi còn mở.

### 5. Thực thi từng Skill

Với mỗi Skill trong chuỗi:

1. **Cổng vào:** đầu vào bắt buộc của Skill đã sẵn sàng (xem "Điều kiện đầu ra" của Skill trước). Thiếu thì quay về Skill trước hoặc hỏi.
2. **Thực hiện:** theo Workflow trong `SKILL.md` của Skill đó, trong phạm vi và mức tự chủ được cấp.
3. **Cổng ra:** kiểm tra mục "Definition of Done" của Skill và đối chiếu bảng "Điều kiện đầu ra" bên dưới. Lưu bằng chứng.
4. **Chuyển giao:** ghi đầu ra để Skill kế tiếp dùng (đường dẫn file, diff, kết quả test).

**Vòng lặp khi có lỗi:**

| Phát hiện | Quay lại |
| --- | --- |
| Test fail do lỗi code | `bug-fixing` hoặc Skill đang code, rồi chạy lại test |
| Review nêu lỗi đúng/logic | Skill code tương ứng, rồi chạy lại test và review |
| Review phát hiện thiếu/mâu thuẫn yêu cầu | **Dừng**; `requirement-review`, chờ người quyết định |
| Thiết kế không thực hiện được | `architecture-design` hoặc `database-design`; đổi kiến trúc cần duyệt |
| Security finding Critical/High | Skill code tương ứng; chạy lại `security-review` phần bị ảnh hưởng |
| Test fail do môi trường/dữ liệu test | Báo rõ, sửa môi trường; không nới assertion |

Giới hạn vòng lặp: tối đa **3 vòng** sửa–chạy cổng cho một lỗi (con số mặc định, điều chỉnh khi có số liệu). Quá giới hạn thì dừng, báo nguyên nhân đã thử và đề xuất hướng tiếp theo, không tiếp tục đoán mò.

### 6. Kiểm tra tổng và bàn giao

Trước khi bàn giao, AI tự rà toàn bộ diff và kiểm tra Definition of Done của Task:

- [ ] Đáp ứng từng AC, có bằng chứng cho từng AC.
- [ ] Không có thay đổi ngoài phạm vi chưa khai báo.
- [ ] Tuân thủ Rules; mọi Skill trong plan đã qua cổng ra (hoặc ghi rõ Skill bị bỏ và lý do).
- [ ] Test pass / fail / skipped / not-run được báo rõ.
- [ ] Bảo mật và quyền truy cập đã xem xét khi liên quan.
- [ ] Tài liệu, contract, schema đã cập nhật khi cần.
- [ ] Không còn blocker hoặc rủi ro nghiêm trọng chưa công bố.

Báo cáo bàn giao theo mẫu báo cáo bàn giao. Phần bổ sung do workflow này yêu cầu:

- Chuỗi Skill đã dùng, theo thứ tự thực tế (kể cả vòng lặp).
- Skill đã bỏ và lý do.
- Quyết định, giả định, câu hỏi còn mở cần người trả lời.
- Hành động cần người thực hiện hoặc phê duyệt (merge, migrate production, deploy).

AI **không** tự chuyển tài liệu sang Approved và **không** tự giữ vai chịu trách nhiệm cuối.

## Điều kiện đầu ra theo Skill (cổng ra)

Rút từ mục "Definition of Done" của từng `SKILL.md`; nếu khác, `SKILL.md` là nguồn chính.

| Skill | Cổng ra tối thiểu | Bằng chứng |
| --- | --- | --- |
| requirement-analysis | Yêu cầu có ID, AC kiểm thử được, câu hỏi mở được ghi | Tài liệu FR/BR/AC dạng Draft |
| requirement-review | Mỗi finding có ID, mức độ, tác động, đề xuất; có khuyến nghị duyệt | Báo cáo review |
| architecture-design | Thiết kế truy vết được tới yêu cầu; ADR cho quyết định lớn; **chờ duyệt** | Tài liệu + ADR (Proposed) |
| database-design | ERD, ràng buộc, index, migration đã soạn; **chờ duyệt** | Migration + tài liệu schema |
| api-development | API theo spec; validation, quyền, test đã có | Diff + kết quả test |
| backend-development | Logic đúng rule; lỗi, transaction được xử lý; test chạy | Diff + kết quả test |
| frontend-development | UI đúng yêu cầu; trạng thái loading/lỗi/quyền; test chạy | Diff + kết quả test |
| authentication-rbac | Quyền thực thi ở backend; test ranh giới quyền đạt | Kết quả test quyền |
| unit-testing | Ca test cần thiết đã viết và chạy; khoảng trống được ghi | Output test thật |
| integration-testing | Ranh giới quan trọng được test trong môi trường cô lập | Output test thật |
| e2e-testing | Hành trình quan trọng chạy được; có trace khi lỗi | Output test + trace |
| code-review | Finding có mức độ; có khuyến nghị merge | Báo cáo review |
| security-review | Phạm vi xong; finding có bằng chứng; Critical được báo | Báo cáo bảo mật |
| bug-fixing | Nguyên nhân gốc xác định; có regression test; test liên quan đạt | Diff + test trước/sau |
| refactoring | Hành vi giữ nguyên; test baseline và sau refactor đạt | Diff + test trước/sau |
| documentation | Tài liệu cập nhật; xung đột nguồn được báo; link hợp lệ | Diff tài liệu |
| deployment | Chỉ chuẩn bị/kiểm tra; deploy **cần phê duyệt**; verify sau deploy | Release report |

## Giới hạn hành động

Skill hướng dẫn cách làm, **không** cấp thêm quyền. Mức tự chủ tối đa theo loại việc lấy từ (profile chỉ được siết).

| Skill / hành động | AI được làm | AI không tự làm |
| --- | --- | --- |
| `deployment` | Chuẩn bị và kiểm tra release, soạn release note, runbook, kiểm tra readiness | Deploy production, đổi secret, đổi dữ liệu production khi chưa được phê duyệt (mức A0–A1) |
| `database-design` | Thiết kế, viết migration, chạy thử trên DB không phải production | Chạy migration production ngoài quy trình phê duyệt |
| `architecture-design`, `requirement-*` | Đề xuất; đầu ra luôn là Proposed/Draft | Chuyển sang Approved |
| `authentication-rbac`, `security-review` | Triển khai và rà soát theo policy đã duyệt | Đổi định nghĩa role/policy, nới kiểm tra để test qua |
| `code-review` | Rà và khuyến nghị | Tự duyệt thay đổi do chính mình viết; thay người duyệt |
| `bug-fixing`, `refactoring` | Sửa trong phạm vi Task | Đổi business rule; trộn refactor lớn với sửa lỗi |

## Dừng và hỏi

AI dừng phần bị ảnh hưởng (và vẫn làm tiếp phần độc lập, an toàn) khi:

- Yêu cầu hoặc tài liệu mâu thuẫn chưa giải quyết; thiếu quyết định nghiệp vụ hoặc kiến trúc.
- Cần đổi quyền, bảo mật, dữ liệu production, hoặc hành động vượt mức tự chủ được cấp.
- Phát hiện secret, dữ liệu nhạy cảm hoặc lỗ hổng có nguy cơ lộ.
- Không xác định được loại Task, môi trường hoặc lệnh chạy.
- Không thiết lập được nguyên nhân gốc của lỗi (`bug-fixing`).
- Vượt giới hạn vòng lặp.

Khi dừng, AI nêu rõ: phần đã làm, phần bị chặn, cần ai quyết định điều gì.

## Skill gọi Skill khác

Skill có thể yêu cầu Skill khác khi cần. Nhờ vậy `SKILL.md` giữ nguyên, quan hệ phụ thuộc được khai báo ở đây:

| Skill | Có thể kích hoạt thêm | Khi nào |
| --- | --- | --- |
| backend-development | unit-testing, integration-testing, security-review | Có logic mới; chạm DB/tích hợp; chạm quyền hoặc dữ liệu nhạy cảm |
| api-development | authentication-rbac, unit-testing, integration-testing | Endpoint cần phân quyền; có validation và logic cần test |
| frontend-development | unit-testing, e2e-testing | Có component, form, hành trình người dùng quan trọng |
| database-design | integration-testing, documentation | Đổi schema; cập nhật tài liệu schema |
| authentication-rbac | security-review, integration-testing | Luôn rà lại ranh giới quyền sau khi triển khai |
| bug-fixing | unit-testing hoặc integration-testing | Viết regression test |
| refactoring | unit-testing | Lập baseline trước và kiểm tra sau |
| code-review | security-review | Diff chạm xác thực, phân quyền, dữ liệu nhạy cảm, input ngoài |
| requirement-analysis | requirement-review | Sau khi soạn xong, trước khi thiết kế |
| architecture-design | documentation | Ghi ADR và cập nhật tài liệu kiến trúc |

Kích hoạt chéo phải ghi vào plan và báo cáo bàn giao, không âm thầm mở rộng phạm vi Task.

## Phiên bản và kiểm thử workflow

- Workflow này và từng Skill phải **được thử trên Task thật** trước khi chuyển Approved.
- Sau mỗi Task đầu tiên, ghi lại: AI có chọn đúng Skill không, có bỏ sót bước hay chạy thừa Skill không, vòng lặp có hợp lý không. Dùng kết quả để chỉnh [skill-selection.md](skill-selection.md).
- Bài học đưa vào bản ghi bài học và đề xuất sửa qua kênh

Ghi chú khi áp dụng cho dự án: bổ sung phiên bản, người phụ trách, và kết quả chạy thử Task đầu tiên.
