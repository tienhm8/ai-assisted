---
name: code-review
description: Review một thay đổi code (PR) không phụ thuộc ngôn ngữ, theo thứ tự ưu tiên đúng việc → test → đúng chỗ → đồng thời → hiệu năng → bảo mật → vận hành → clean code; đọc PR description trước khi đọc code, mỗi finding có vị trí, kịch bản lỗi và severity.
---

# Code Review Skill

## 1. Mục tiêu

Xác nhận thay đổi làm đúng việc, đúng phạm vi Task, đặt đúng chỗ trong kiến trúc, chịu được tải và đồng thời, an toàn, vận hành được và có bằng chứng kiểm thử thật trước khi merge.

Thứ tự ưu tiên quyết định cách xử lý finding: **logic sai thì không duyệt; code xấu thì comment, không chặn PR**.

## 2. Cổng vào

Thiếu một mục thì dừng, ghi rõ mục thiếu và trả PR về người viết, không review code:

- PR description đủ các mục ở Bước 1 (theo mẫu PR của dự án).
- Có phiếu Task với phạm vi, AC, mức rủi ro R và Definition of Done.
- Kết quả cổng tự động (build, lint, kiểm tra kiểu, test, quét secret) đã xanh: lấy từ CI; chưa có CI thì từ lần chạy cục bộ ghi trong PR, kèm lệnh và output.
- Kích thước PR nằm trong ngưỡng của dự án; vượt ngưỡng thì đề nghị tách, trừ khi PR ghi lý do (code sinh tự động, đổi tên hàng loạt…).
- Thay đổi không do chính phiên AI này viết.

## 3. Đầu vào

- PR description, phiếu Task, AC, FR/BR liên quan
- Tài liệu kiến trúc (tầng, ranh giới module, hướng phụ thuộc), coding-standards, error-handling, testing-strategy, NFR
- Rules: project-rules, coding-rules, architecture-rules, database-rules, security-rules, testing-rules
- Git diff **và ngữ cảnh ngoài diff**: nơi gọi tới đoạn code đổi, schema/migration, cấu hình, test hiện có
- Báo cáo test và báo cáo bàn giao (nếu Task do AI làm)

## 4. Quy trình

### Bước 0: Xác định mức review (R1–R3)

Task phải mang mức rủi ro; thiếu thì dừng và hỏi, không tự gán. AI không tự hạ mức.

| Mức | Khi nào | Cách review |
| --- | --- | --- |
| R1 (thấp) | Thay đổi nhỏ, không chạm vùng 🟡/🔴, không chạm xác thực, phân quyền, tiền, dữ liệu cá nhân hay migration | Một reviewer |
| R2 (vừa) | Logic nghiệp vụ, API, schema trong phạm vi Task, hoặc có file vùng 🟡 | Một reviewer; kích hoạt `security-review` nếu chạm điều kiện bảo mật |
| R3 (cao) | Chạm tiền, phân quyền, dữ liệu cá nhân, secret, migration production, hoặc file vùng 🔴 | Hai reviewer, trong đó một người độc lập với người/AI viết code; thiếu người thì ghi miễn trừ có thời hạn |

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

Đi lần lượt từ ưu tiên 1 đến 8. Với mỗi câu hỏi, đọc ngữ cảnh ngoài diff khi cần; không kết luận từ diff đơn lẻ.

**Ưu tiên 1: Code có làm đúng việc không?**

- Từng AC được đáp ứng ở đâu trong code; AC nào không thấy chỗ đáp ứng.
- Ca biên: rỗng, null/không có giá trị, giá trị biên, dữ liệu trùng, danh sách một phần tử, chuỗi rất dài, ký tự đặc biệt.
- Chuyển trạng thái: có chặn chuyển trạng thái không hợp lệ không.
- Xử lý lỗi: không nuốt lỗi; lỗi được phân loại theo error-handling; thông báo lỗi không lộ chi tiết nội bộ.
- Kiểu dữ liệu: tiền và số cần chính xác không dùng số dấu phẩy động; múi giờ và định dạng thời gian nhất quán; làm tròn đúng quy tắc nghiệp vụ.
- Ranh giới transaction: các ghi phải cùng thành công hoặc cùng thất bại có nằm chung một đơn vị nguyên tử không.
- Quy tắc nghiệp vụ lấy từ FR/BR, không phải do code tự đặt ra; chưa rõ thì ghi câu hỏi mở.

**Ưu tiên 2: Có test chứng minh không?**

- Mỗi AC có test truy vết (tên/chú thích mang ID AC) và output test thật. AC không có bằng chứng là finding High.
- Sửa lỗi có regression test đỏ trước, xanh sau.
- Có test cho ca lỗi, ca biên và ca bị từ chối quyền, không chỉ đường đi thành công.
- Test kiểm hành vi, không kiểm chi tiết cài đặt; không có assertion rỗng hoặc chỉ kiểm "không ném lỗi".
- Không test bị xoá, bỏ qua hoặc làm yếu để qua cổng.

**Ưu tiên 3: Code có đặt đúng chỗ không?**

Lấy bản đồ tầng và trách nhiệm từ tài liệu kiến trúc của dự án; không tự áp một mô hình tầng. Kiểm theo các trách nhiệm chung:

| Trách nhiệm | Câu hỏi |
| --- | --- |
| Biên nhận yêu cầu (handler, controller, resolver, CLI, UI component) | Chỉ điều phối (nhận yêu cầu → gọi nghiệp vụ → trả kết quả) hay đang chứa quy tắc nghiệp vụ, truy cập dữ liệu trực tiếp? |
| Kiểm tra đầu vào và phân quyền | Làm tại biên hệ thống, theo cơ chế chung của dự án, không rải rác trong nghiệp vụ? Chỉ nhận các trường được phép (whitelist), không gán toàn bộ input vào đối tượng? |
| Nghiệp vụ (service, use case) | Quy tắc nghiệp vụ nằm ở đây và chỉ ở một nơi? |
| Domain (entity, model, value object) | Hành vi gắn chặt với dữ liệu (kiểm bất biến, chuyển trạng thái) nằm cùng đối tượng của nó? |
| Truy cập dữ liệu (repository, DAO, query) | Tầng trên không tự dựng truy vấn vượt tầng; không truy cập dữ liệu của module khác ngoài interface công khai? |
| Bất đồng bộ và side effect (job, event, consumer, gửi thông báo, gọi hệ thống ngoài) | Side effect chậm hoặc không hoàn tác được có được tách khỏi luồng chính và khỏi transaction không? |
| Định dạng đầu ra | Trả về dạng dữ liệu đã định nghĩa cho bên ngoài, không trả nguyên đối tượng nội bộ? |

Dấu hiệu cần xem xét (không phải luật; ngưỡng cụ thể theo coding-standards của dự án): hàm hoặc class vượt ngưỡng kích thước; một hàm làm nhiều việc; lồng điều kiện sâu; quá nhiều dependency; một đơn vị bị sửa vì nhiều lý do khác nhau; phụ thuộc vòng; logic trùng lặp.

**Ưu tiên 4: Khi hệ thống chịu tải và chạy đồng thời thì sao?**

- Hai yêu cầu cùng lúc trên cùng dữ liệu: có mẫu "đọc rồi ghi" (đọc giá trị, quyết định, ghi lại) mà không có khoá, optimistic locking hoặc cập nhật có điều kiện không?
- Ràng buộc duy nhất có được bảo đảm ở tầng lưu trữ không, hay chỉ kiểm "đã tồn tại chưa" bằng code (dễ trùng khi đồng thời)?
- Tác vụ chạy lại (retry, message giao hai lần, người dùng bấm hai lần): có idempotent không, có khoá idempotency cho thao tác tạo/thanh toán không?
- Tác vụ nền: có timeout, giới hạn số lần retry, backoff, nơi xử lý khi thất bại cuối cùng; có chặn chạy chồng khi cần không?
- Event/tác vụ nền được phát **sau khi** transaction commit, không phát trước (tránh xử lý dữ liệu chưa tồn tại hoặc đã rollback).
- Trạng thái dùng chung trong bộ nhớ tiến trình (biến toàn cục, singleton có trạng thái) có an toàn khi nhiều request hoặc nhiều instance không?
- Lời gọi ra ngoài có timeout; lỗi của hệ thống ngoài không kéo đổ luồng chính.

**Ưu tiên 5: Hiệu năng, dữ liệu, cache**

- Truy vấn hoặc lời gọi mạng nằm trong vòng lặp (N+1), kể cả gọi gián tiếp qua thuộc tính lazy-load.
- Truy vấn chạy trên bao nhiêu bản ghi, hôm nay và khi dữ liệu tăng; có giới hạn, phân trang, xử lý theo lô hoặc stream không, hay nạp toàn bộ vào bộ nhớ?
- Chỉ lấy cột và dữ liệu cần dùng.
- Điều kiện lọc, join và sắp xếp có index phù hợp không (kể cả thứ tự cột trong index ghép); điều kiện có làm index không dùng được không.
- Migration trên bảng lớn có khoá bảng lâu, có cần chạy theo lô hoặc tách bước không.
- Có nên cache không; nếu cache: khi nào làm mất hiệu lực, thời gian sống, khoá cache có tách theo người dùng/tenant/quyền không (thiếu là lộ dữ liệu chéo), nhiều request cùng miss cache thì sao.
- Đối chiếu NFR hiệu năng khi thay đổi nằm trên luồng nóng.

**Ưu tiên 6: Bảo mật (theo OWASP Top 10)**

Kiểm nhanh các lỗi hay gặp nhìn thấy được trong diff:

- Thiếu kiểm quyền ở backend, đặc biệt quyền trên từng bản ghi (lấy theo ID mà không kiểm quyền sở hữu: IDOR/BOLA).
- Gán toàn bộ input vào đối tượng (mass assignment/over-posting) thay vì chỉ nhận trường đã kiểm.
- Injection: nối chuỗi vào truy vấn, lệnh hệ thống, template, biểu thức đường dẫn.
- Đầu ra không được mã hoá/escape theo ngữ cảnh (XSS).
- Trả về hoặc ghi log trường nhạy cảm, secret, token, dữ liệu D3.
- Upload: không kiểm loại, kích thước, nội dung, nơi lưu.
- Gọi URL do người dùng cung cấp (SSRF); đường dẫn file từ input (path traversal).
- Thiếu giới hạn tần suất ở điểm nhạy cảm (đăng nhập, OTP, đặt lại mật khẩu).
- Dependency mới có lỗ hổng đã biết hoặc chưa ghi lý do.

Diff chạm xác thực, phân quyền, dữ liệu nhạy cảm hoặc input từ bên ngoài thì kích hoạt `security-review`; không tự làm thay trong skill này.

**Ưu tiên 7: Vận hành được không?**

- Lỗi quan trọng được ghi log kèm ngữ cảnh và correlation ID, không ghi dữ liệu nhạy cảm.
- Tác vụ nền thất bại thì có người biết (log, alert, hàng đợi lỗi).
- Cần metric hoặc alert mới không; cấu hình mới đã có giá trị cho mọi môi trường chưa.
- Có rollback được không; feature flag có kế hoạch gỡ không.

**Ưu tiên 8: Clean code và style**

Ưu tiên thấp nhất, không bỏ qua nhưng không chặn PR: đặt tên, độ dài, comment, code chết, import thừa, độ đọc hiểu. Những gì formatter/linter đã bắt được thì không comment.

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

AI chỉ khuyến nghị kết luận; người có thẩm quyền theo mức R quyết định merge.

## 5. Checklist

- [ ] Cổng vào đạt: PR description đủ mục, cổng tự động xanh, PR trong ngưỡng kích thước.
- [ ] Đã đọc PR description và lập giả thuyết trước khi đọc code.
- [ ] Diff khớp phạm vi Task; file vùng 🟡/🔴, file ngoài phạm vi, test bị làm yếu đã được báo.
- [ ] Đã đi đủ 8 ưu tiên theo thứ tự; ưu tiên nào không áp dụng ghi lý do.
- [ ] Đã đọc ngữ cảnh ngoài diff cho các finding về đồng thời, hiệu năng, kiến trúc.
- [ ] Mỗi AC có test truy vết và output thật.
- [ ] Đã kích hoạt `security-review` khi chạm điều kiện bảo mật.
- [ ] Mỗi finding có `file:dòng`, kịch bản lỗi, severity, yêu cầu sửa; điều chưa chứng minh được ghi là câu hỏi.
- [ ] Có kết luận khuyến nghị và lý do.

## 6. Việc không được làm

- Đọc code trước khi hiểu PR muốn làm gì; review PR thiếu mô tả bằng cách tự đoán mục đích.
- Duyệt khi còn finding Critical/High chưa xử lý.
- Chặn PR chỉ vì style hay sở thích cá nhân.
- Cho rằng code đúng chỉ vì test pass.
- Kết luận về đồng thời, hiệu năng hay kiến trúc chỉ từ diff mà không đọc ngữ cảnh.
- Bịa lỗi không có kịch bản hoặc bằng chứng kỹ thuật.
- Tự đặt quy tắc nghiệp vụ hay mô hình tầng không có trong tài liệu dự án.
- Viết lại code ngoài phạm vi trong lúc review.
- Tự duyệt thay đổi do chính mình viết, hoặc coi đó là review độc lập.

## 7. Tiêu chí hoàn thành (DoD)

- Cổng vào và 8 ưu tiên đã được đi qua, mục không áp dụng có lý do.
- Mọi finding có severity, vị trí, kịch bản lỗi và yêu cầu sửa.
- Bằng chứng test đã được đánh giá.
- Có kết luận khuyến nghị: duyệt / duyệt có điều kiện / không duyệt.

## 8. Báo cáo bàn giao

- Tóm tắt PR theo hiểu biết của reviewer (vấn đề, thay đổi hành vi hay refactor, phạm vi ảnh hưởng), mức R, file đã review (kể cả file vùng 🟡/🔴 và ngoài phạm vi)
- Mục còn thiếu trong PR description (nếu có)
- Finding theo severity, mỗi cái có `file:dòng`, kịch bản lỗi, yêu cầu sửa
- Câu hỏi cho người viết
- Đánh giá test: AC có/thiếu bằng chứng, nguồn kết quả cổng (CI hoặc cục bộ)
- Ưu tiên không áp dụng và lý do; `security-review` có được kích hoạt không
- Điểm tốt đáng ghi nhận
- Kết luận khuyến nghị và điều kiện (nếu có)
