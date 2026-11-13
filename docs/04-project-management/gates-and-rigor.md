# Gates and Rigor

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người duyệt | Tech Lead |
| Tài liệu liên quan | ../../README.md, ../../PROJECT.md §5, task-breakdown.md |

> **Mục đích.** Cổng duyệt G0–G7 (điều kiện qua, người duyệt) và độ nghiêm ngặt quy trình S1–S3. Dự án khai báo mức S ở [PROJECT.md](../../PROJECT.md) §5; không chép lại ở đây.

## 1. Cổng duyệt G0–G7
Cổng là điều kiện phải đạt để kết thúc một giai đoạn và sang giai đoạn kế. G0 đứng trước `[01]`; G1–G7 đứng cuối `[01]`–`[07]`. Qua cổng bằng bằng chứng (tài liệu Approved, output test, biên bản review), không bằng lời xác nhận. AI chuẩn bị và đề xuất, không tự phê duyệt.

| Cổng | Cuối giai đoạn | Điều kiện qua | Người duyệt | Phối hợp |
| --- | --- | --- | --- | --- |
| G0 Khởi tạo | trước `[01]` | `PROJECT.md` đã duyệt: độ nghiêm ngặt S, mức dữ liệu, công cụ AI được phép | Tech Lead | PO xác nhận phạm vi; DevOps phối hợp cấu hình |
| G1 Vision & Scope | `[01]` | Vision và phạm vi được duyệt; điểm chưa rõ đã ghi nhận | PO | BA, Tech Lead tư vấn |
| G2 Requirements | `[02]` | Mọi FR trong phạm vi có AC kiểm thử được; điểm chưa chốt ghi `Open` | PO/BA | QA rà khả năng kiểm thử; Tech Lead tư vấn |
| G3 Ready for Build | `[03]` | Thiết kế của phạm vi đã duyệt; có ADR cho quyết định kiến trúc quan trọng; có threat model khi cần, nhất là R3. Chưa đạt thì không code tính năng | Kiến trúc sư | Security duyệt phần liên quan bảo mật (tiền, phân quyền, dữ liệu cá nhân, migration); PO/BA xác nhận yêu cầu |
| G4 Task Ready | `[04]` | Mỗi Task có objective, phạm vi in/out, AC, mức R và mức A | Tech Lead | Dev, QA phối hợp; Security khi cần |
| G5 Implementation Complete | `[05]` | Cổng tự động cục bộ đạt; báo cáo bàn giao đủ; không có thay đổi ngoài phạm vi chưa khai | Tech Lead | Tác giả chịu trách nhiệm bàn giao; AI không phê duyệt |
| G6 Ready for Release | `[06]` | CI đạt; review đủ theo mức R; AC được xác nhận; lỗi nghiêm trọng đã xử lý hoặc được chấp nhận chính thức | Tech Lead | Reviewer theo R; QA nghiệm thu |
| G7 Delivery & Operations | `[07]` | Smoke test đạt; không có sự cố nghiêm trọng trong thời gian giám sát; có thể rollback | Owner | Tech Lead tham khảo; DevOps thực hiện; AI không tự deploy |

## 2. Độ nghiêm ngặt quy trình S1–S3
Dự án chọn một mức cho cả dự án, khai báo ở `PROJECT.md` §5. S độc lập với mức rủi ro R của từng Task. Ở mọi mức, cổng tự động và review theo R3 vẫn bắt buộc.

| Mức | Cổng duyệt | Tài liệu | Review | Truy vết | Nhật ký AI |
| --- | --- | --- | --- | --- | --- |
| S1 Gọn | G1–G3 gộp thành một cổng | Tối thiểu | 1 người cho Task R1–R2 | PR có ID Task/FR | Mức PR |
| S2 Chuẩn | G0–G7 tách riêng | Theo phạm vi dự án | Theo mức R | FR ↔ PR ↔ test | Theo từng Task, ghi trong báo cáo bàn giao |
| S3 Nghiêm ngặt | Tách riêng, có biên bản | Hồ sơ sẵn sàng cho kiểm toán | Độc lập | Hai chiều đầy đủ | Chi tiết, lưu dài hạn |

### Chọn mức nào?
S1–S3 áp dụng cho toàn dự án. Bảng dưới chỉ mang tính định hướng; mức cuối cùng cần xét thêm rủi ro và yêu cầu cụ thể của dự án. Chưa chắc thì bắt đầu từ S2; chọn S1 khi dự án nhỏ và ít rủi ro; chọn S3 khi có yêu cầu pháp lý, hợp đồng hoặc kiểm soát đặc biệt.

| Loại dự án | Mức S khuyến nghị | Ghi chú |
| --- | --- | --- |
| Dự án nội bộ | S2 | Quy trình chuẩn |
| Dự án thuê ngoài / gia công | S2 | Dùng S3 nếu hợp đồng yêu cầu |
| Dự án thuộc lĩnh vực có quy định pháp lý | S3 | Cần hồ sơ và khả năng kiểm toán |
| Dự án dữ liệu / AI / ML | S2–S3 | Chọn theo mức độ rủi ro và yêu cầu quản trị |
| Dự án bảo trì | S1–S2 | Tùy phạm vi thay đổi |
| Dự án nhỏ, ít rủi ro | S1 | Tối đa 3 người, tối đa 3 tháng |
