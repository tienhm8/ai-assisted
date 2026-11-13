---
name: code-review
description: Review một thay đổi code (PR) không phụ thuộc ngôn ngữ, theo thứ tự ưu tiên đúng việc → test → đúng chỗ → đồng thời → hiệu năng → bảo mật → vận hành → clean code; đọc PR description trước khi đọc code, mỗi finding có vị trí, kịch bản lỗi và severity.
---

# Code Review Skill

Xác nhận thay đổi làm đúng việc, đúng phạm vi Task, đặt đúng chỗ trong kiến trúc, chịu được tải và đồng thời, an toàn, vận hành được, và có bằng chứng kiểm thử thật trước khi merge.

**Logic sai thì không duyệt; code xấu thì comment, không chặn PR.**

## Cổng vào

Thiếu một mục thì dừng, nêu mục thiếu và trả PR về người viết; không review code:

- PR description đủ các mục ở Bước 1.
- Task có phạm vi, AC, mức rủi ro.
- Cổng tự động (build, lint, kiểm tra kiểu, test, quét secret) đã xanh: lấy từ CI; chưa có CI thì từ lần chạy cục bộ ghi trong PR, kèm lệnh và output.
- Kích thước PR trong ngưỡng của dự án; vượt ngưỡng thì đề nghị tách, trừ khi PR ghi lý do (code sinh tự động, đổi tên hàng loạt…).
- Thay đổi không do chính phiên này viết.

Đọc: PR description, Task, AC, FR/BR liên quan; tài liệu kiến trúc (tầng, ranh giới module, hướng phụ thuộc), coding-standards, error-handling, testing-strategy, NFR; git diff **và ngữ cảnh ngoài diff** (nơi gọi tới đoạn code đổi, schema, migration, cấu hình, test hiện có); báo cáo test và báo cáo bàn giao.

## Quy trình

### Bước 0: Số reviewer theo mức rủi ro

| Mức rủi ro của Task | Cách review |
| --- | --- |
| R1 | Một reviewer |
| R2 | Một reviewer; thêm `security-review` nếu chạm điều kiện bảo mật |
| R3 | Hai reviewer, một người độc lập với người hoặc AI viết code; thiếu người thì đề nghị miễn trừ có thời hạn |

### Bước 1: Đọc PR description trước, chưa đọc code

Từ PR description, trả lời được các câu sau; câu nào không trả lời được thì ghi finding hoặc câu hỏi, không tự suy ra từ code:

1. Vấn đề gì đang được giải quyết, liên kết Task và AC nào?
2. Thay đổi hành vi hay chỉ refactor? Refactor thì hành vi bên ngoài phải giữ nguyên.
3. Ảnh hưởng tới đâu: dữ liệu/schema, API/hợp đồng với bên gọi, job/tác vụ nền/message, cache, cấu hình/biến môi trường, quyền truy cập?
4. Ngoài phạm vi: những gì cố ý không làm?
5. Đã kiểm thử thế nào, bằng chứng ở đâu?
6. Thay đổi dữ liệu: khối lượng bị ảnh hưởng, có khoá bảng không, có tương thích ngược với code đang chạy không?
7. Breaking change, cần feature flag, thứ tự deploy (code trước hay migration trước), cách rollback?

Từ đó lập **giả thuyết về điều code phải làm**, rồi mới đọc diff để kiểm giả thuyết.

### Bước 2: Đối chiếu Task với diff

- Liệt kê file đổi, module bị ảnh hưởng; so với phạm vi trong phiếu Task và mục "ngoài phạm vi" của PR.
- Báo file thuộc vùng 🟡/🔴 và file ngoài phạm vi.
- Báo test bị xoá, tắt hoặc làm yếu; cột/bảng bị xoá ngoài phạm vi; dependency mới chưa ghi lý do.
- PR nói "chỉ refactor" mà diff đổi hành vi (đổi điều kiện, giá trị trả về, thứ tự side effect): finding.

### Bước 3: Review theo thứ tự ưu tiên

Đi lần lượt từ ưu tiên 1 đến 8. Đọc ngữ cảnh ngoài diff khi cần; không kết luận từ diff đơn lẻ. Nạp checklist chi tiết của nhóm đang làm, chưa làm tới thì chưa nạp:

| Ưu tiên | Câu hỏi chính | Checklist |
| --- | --- | --- |
| 1 | Code có làm đúng việc không? (AC, ca biên, trạng thái, lỗi, kiểu dữ liệu, transaction, BR từ FR/BR) | `references/correctness.md` |
| 2 | Có test chứng minh không? (mỗi AC có test và output thật; AC thiếu bằng chứng là High) | `references/correctness.md` |
| 3 | Code có đặt đúng chỗ không? (tầng và trách nhiệm theo tài liệu kiến trúc của dự án) | `references/correctness.md` |
| 4 | Chịu tải và đồng thời thì sao? (race, idempotency, retry, event sau commit) | `references/runtime.md` |
| 5 | Hiệu năng, dữ liệu, cache (N+1, khối lượng, index, migration bảng lớn) | `references/runtime.md` |
| 6 | Bảo mật theo OWASP Top 10 (quyền từng bản ghi, injection, XSS, lộ D3, upload, SSRF) | `references/security.md` |
| 7 | Vận hành được không? (log, alert, cấu hình, rollback) | `references/runtime.md` |
| 8 | Clean code và style: ưu tiên thấp nhất, không chặn PR; không comment điều formatter/linter đã bắt | — |

Diff chạm xác thực, phân quyền, dữ liệu nhạy cảm hoặc input từ bên ngoài thì kích hoạt `security-review`; không tự làm thay trong skill này.

### Bước 4: Viết finding

Mỗi finding phải có:

- Vị trí `file:dòng`.
- **Kịch bản lỗi cụ thể**: đầu vào hoặc trạng thái nào → kết quả sai gì. Không dựng được kịch bản thì ghi là **câu hỏi**, không ghi là lỗi.
- Severity theo thang chung, ánh xạ với ưu tiên:

| Severity | Thường gặp | Ảnh hưởng merge |
| --- | --- | --- |
| Critical | Mất/hỏng dữ liệu, lỗ hổng bảo mật khai thác được | Chặn |
| High | Logic sai so với AC/BR, race condition gây sai dữ liệu, AC không có test, migration không rollback được | Chặn |
| Medium | Đặt sai tầng, N+1 hoặc thiếu index trên dữ liệu còn nhỏ, thiếu xử lý lỗi ở nhánh phụ, thiếu log/alert | Không chặn; sửa trong PR hoặc tạo Task có hạn |
| Low | Clean code, đặt tên, cấu trúc nhỏ | Không chặn |
| Informational | Gợi ý, điểm cần theo dõi | Không chặn |

- Yêu cầu sửa hoặc hướng sửa; không viết lại code ngoài phạm vi.

Quy tắc trình bày:

- Gộp finding cùng nguyên nhân thành một; finding Low và Informational giới hạn số lượng, chỉ giữ những cái có giá trị nhất, để finding quan trọng không bị chìm.
- Ghi nhận điểm tốt cụ thể của thay đổi.
- Giọng góp ý hướng vào code, không hướng vào người viết.

### Bước 5: Kết luận

- **Không duyệt**: còn Critical/High, hoặc cổng vào không đạt.
- **Duyệt có điều kiện**: còn Medium; nêu rõ điều kiện (sửa trong PR hay tạo Task kèm hạn).
- **Duyệt**: chỉ còn Low/Informational hoặc không có finding.

AI chỉ khuyến nghị; người có thẩm quyền quyết định merge.

## Giới hạn

- Không chặn PR chỉ vì style hay sở thích cá nhân.
- Không cho rằng code đúng chỉ vì test pass.
- Không kết luận về đồng thời, hiệu năng hay kiến trúc chỉ từ diff.
- Không tự áp mô hình tầng không có trong tài liệu dự án.
- Không viết lại code trong lúc review.

## Hoàn thành khi

- Đã đi đủ 8 ưu tiên theo thứ tự; ưu tiên không áp dụng có ghi lý do.
- Mỗi finding có `file:dòng`, kịch bản lỗi, mức nghiêm trọng, yêu cầu sửa; điều chưa chứng minh được ghi là câu hỏi.
- Có kết luận khuyến nghị kèm lý do.

## Báo cáo

- Tóm tắt PR theo hiểu biết của reviewer: vấn đề, đổi hành vi hay refactor, phạm vi ảnh hưởng; mức rủi ro; file đã review, gồm file vùng 🟡/🔴 và file ngoài phạm vi.
- Mục còn thiếu trong PR description.
- Finding theo mức nghiêm trọng; câu hỏi cho người viết.
- Đánh giá test: AC có hoặc thiếu bằng chứng, nguồn kết quả cổng (CI hay cục bộ).
- Ưu tiên không áp dụng và lý do; có dùng `security-review` không.
- Điểm tốt đáng ghi nhận.
- Kết luận khuyến nghị và điều kiện.
