# Gates and Rigor

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người duyệt (dự án) | Tech Lead |
| Tài liệu liên quan | ../../README.md, ../../PROJECT.md §4, task-breakdown.md |

> **Mục đích.** Tám cổng duyệt (điều kiện qua, người duyệt), độ nghiêm ngặt quy trình (gọn, chuẩn, nghiêm ngặt) và quy ước áp dụng khung vào dự án.

## 1. Tám cổng duyệt
- **Khái niệm:** Cổng duyệt là chốt kiểm tra bắt buộc để kết thúc một giai đoạn (riêng cổng **Khai báo dự án** nằm ngay trước giai đoạn đầu tiên).
- **Nguyên tắc qua cổng:** Chỉ công nhận bằng chứng cụ thể (tài liệu `Approved`, kết quả test, biên bản review), không chấp nhận xác nhận bằng lời nói.
- **Quy trình lưu vết:** Kết quả duyệt phải được lưu thành mã `SRC-<NN>` trước khi chuyển trạng thái sang `Approved`. Nếu thiếu mã `SRC` này, hệ thống coi như chưa qua cổng.
- **Quy trình với khách hàng:** Nếu dự án có Đại diện khách hàng (theo `PROJECT.md §5`), Đầu mối dự án sẽ gửi tài liệu, nhận phản hồi, lưu mã `SRC-<NN>` rồi mới chuyển `Approved` (hoặc người ở cột **Người duyệt** tự cập nhật dựa trên mã `SRC` đó).
- **Giới hạn của AI:** AI chỉ hỗ trợ chuẩn bị và đề xuất, tuyệt đối không tự ý phê duyệt.

| Cổng | Cuối giai đoạn | Điều kiện qua | Người duyệt | Phối hợp |
| --- | --- | --- | --- | --- |
| Khai báo dự án | trước Khám phá sản phẩm | `PROJECT.md` đã duyệt: độ nghiêm ngặt, mức dữ liệu, công cụ AI được phép | Tech Lead | PO xác nhận phạm vi; DevOps phối hợp cấu hình |
| Phạm vi | Khám phá sản phẩm | Vision và phạm vi được duyệt; tài liệu nguồn có mã `SRC`; điểm chưa rõ đã ghi nhận | PO | BA, Tech Lead tư vấn; Đại diện khách hàng duyệt phạm vi qua Đầu mối |
| Yêu cầu | Yêu cầu | Mọi FR trong phạm vi có AC kiểm thử được và truy được về `SRC`/BRQ; điểm chưa chốt ghi `Open`/`Asked` | PO/BA | QA rà khả năng kiểm thử; Tech Lead tư vấn; Đại diện khách hàng duyệt yêu cầu qua Đầu mối |
| Thiết kế | Thiết kế | Thiết kế của phạm vi đã duyệt; có ADR cho quyết định kiến trúc quan trọng; có threat model khi cần, nhất là Task rủi ro cao. Chưa đạt thì không code tính năng | Kiến trúc sư | Security duyệt phần liên quan bảo mật (tiền, phân quyền, dữ liệu cá nhân, migration); PO/BA xác nhận yêu cầu |
| Sẵn sàng giao việc | Chuẩn bị ngữ cảnh AI | Chuẩn ở 03-engineering và `PROJECT.md` đã Approved; mỗi Task có objective, phạm vi in/out, AC, rủi ro và mức tự chủ | Tech Lead | Dev, QA phối hợp; Security khi cần |
| Code xong | Lập trình | Cổng tự động cục bộ đạt; báo cáo bàn giao đủ; không có thay đổi ngoài phạm vi chưa khai | Tech Lead | Tác giả chịu trách nhiệm bàn giao; AI không phê duyệt |
| Sẵn sàng phát hành | Kiểm thử | CI đạt; review đủ theo rủi ro; AC được xác nhận; lỗi nghiêm trọng đã xử lý hoặc được chấp nhận chính thức | Tech Lead | Reviewer theo rủi ro; QA nghiệm thu |
| Vận hành | Phát hành và vận hành | Smoke test đạt; không có sự cố nghiêm trọng trong thời gian giám sát; có thể rollback | Owner | Tech Lead tham khảo; DevOps thực hiện; AI không tự deploy |

## 2. Độ nghiêm ngặt quy trình
Chọn một mức cho cả dự án. Độ nghiêm ngặt độc lập với rủi ro của từng Task.
| Mức | Cổng duyệt | Tài liệu | Review | Truy vết | Nhật ký AI |
| --- | --- | --- | --- | --- | --- |
| Gọn | Ba cổng Phạm vi, Yêu cầu, Thiết kế gộp thành một cổng | Tối thiểu | 1 người cho Task rủi ro thấp hoặc vừa | PR có ID Task/FR | Mức PR |
| Chuẩn | Tám cổng tách riêng | Theo phạm vi dự án | Theo rủi ro | FR ↔ PR ↔ test | Theo từng Task, ghi trong báo cáo bàn giao |
| Nghiêm ngặt | Tách riêng, có biên bản | Hồ sơ sẵn sàng cho kiểm toán | Độc lập | Hai chiều đầy đủ | Chi tiết, lưu dài hạn |

### Chọn mức nào?
Chưa chắc thì bắt đầu từ mức chuẩn; chọn nghiêm ngặt khi có yêu cầu pháp lý, hợp đồng hoặc kiểm soát đặc biệt. Bảng dưới mang tính định hướng

| Loại dự án | Mức khuyến nghị | Ghi chú |
| --- | --- | --- |
| Dự án nội bộ | chuẩn | Quy trình chuẩn |
| Dự án thuê ngoài / gia công | chuẩn | Dùng nghiêm ngặt nếu hợp đồng yêu cầu |
| Dự án thuộc lĩnh vực có quy định pháp lý | nghiêm ngặt | Cần hồ sơ và khả năng kiểm toán |
| Dự án dữ liệu / AI / ML | chuẩn hoặc nghiêm ngặt | Chọn theo mức độ rủi ro và yêu cầu quản trị |
| Dự án bảo trì | gọn hoặc chuẩn | Tùy phạm vi thay đổi |
| Dự án nhỏ, ít rủi ro | gọn | Tối đa 3 người, tối đa 3 tháng |

## 3. Áp dụng khung vào dự án
Tài liệu trong `docs/` là mẫu dùng chung và luôn ở trạng thái `Draft`, không ghi phiên bản, ngày. Việc Tech Lead duyệt mẫu ghi bằng PR có người duyệt trong repo khung, không ghi vào dòng Trạng thái. Dòng "Người duyệt (dự án)" là người duyệt nội dung khi áp vào dự án.

- Chỉ người duyệt của dự án chuyển một tài liệu sang `Approved`, sau khi nội dung dự án đã điền. Repo khung không chứa tài liệu `Approved` nào trong `docs/`.
- Lịch sử thay đổi là lịch sử git và PR có người duyệt. Bảng "Lịch sử thay đổi" trong file chỉ bắt buộc ở `00-project-overview` và `01-requirements` (nội dung nghiệp vụ, người duyệt không dùng git).
- Dòng mẫu trong bảng dùng mã dạng `<...>` (ví dụ `FR-<MODULE>-<NN>`); thay bằng mã thật hoặc xoá, không giữ làm dữ liệu.
- Nội dung trong `docs/` thuộc một trong hai loại:

| Loại | Đánh dấu | Dự án được |
| --- | --- | --- |
| Mặc định khung | ghi "Mặc định khung" tại chỗ | Chỉnh, ghi lý do ở `PROJECT.md` §6 |
| Chỗ dự án điền | `<!-- Điền theo từng dự án: … -->` | Điền; mục không áp dụng ghi "Không áp dụng" kèm lý do |

Sàn (điều dự án chỉ được siết, không được nới) nằm ở `.ai/rules/`; `docs/` chỉ ghi giá trị dự án siết thêm.
