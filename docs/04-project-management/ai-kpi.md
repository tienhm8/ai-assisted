# KPI đánh giá hiệu quả AI Development

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | roadmap.md, task-backlog.md, task-breakdown.md, ../03-engineering/testing-strategy.md, ../05-operations/monitoring.md |

> **Mục đích.** Chọn chỉ số, ghi baseline và kết quả đo để đánh giá AI có thực sự cải thiện việc phát triển hay không. Mục 2 định nghĩa KPI dự án chọn đo; KPI lấy thêm từ mục 1 phải điền đủ mục 2 trước khi đo. File này chỉ ghi chỉ số dự án chọn đo và số liệu thực tế. Không chỉ đo số dòng code AI tạo ra hoặc số Task hoàn thành.

## 1. Nhóm KPI

| Nhóm | KPI | Nguồn dữ liệu | Ghi chú |
| --- | --- | --- | --- |
| Productivity | Lead time; thời gian hoàn thành Task (cycle time); giờ người theo giai đoạn; thời gian review; thời gian tiết kiệm được | Công cụ quản lý việc, Git/PR, CD | Thời gian review tách theo R1/R2/R3 |
| Quality | Defect rate; escaped defects (lỗi phát hiện sau release); test pass rate; tỷ lệ PR bị từ chối khi review; bug mở lại | Issue tracker, CI hoặc kết quả test chạy local | Escaped defects tính trên số FR phát hành |
| Security | Critical vulnerabilities; authorization defects (lỗi phân quyền) | Công cụ quét, review, sự cố | Tách theo nguồn phát hiện: cổng, review, sau release |
| AI Efficiency | Tỷ lệ code AI được chấp nhận; số vòng sửa; chi phí AI / Task; chi phí người / Task | PR, Delivery Report §8, hoá đơn nhà cung cấp | "Chấp nhận" là dùng mà không phải viết lại lớn |
| Reliability | Tỷ lệ Task AI hoàn thành đúng AC; tỷ lệ làm lại (rework); số lần AI bịa thông tin (hallucination); Task bỏ dở; độ nhất quán khi chạy lại cùng đầu vào | Delivery Report, PR, nhật ký AI | Dựa trên Delivery Report của [task-breakdown](task-breakdown.md) |
| Governance | Tuân thủ quy chuẩn kỹ thuật; tuân thủ review của người; thay đổi ngoài phạm vi chưa khai; tuân thủ phê duyệt | PR, review, Delivery Report | Đối chiếu [.ai/rules](../../.ai/rules/README.md) |

## 2. Định nghĩa KPI

Mỗi KPI được chọn đo phải điền đủ bảng này trước khi ghi kết quả.

| KPI | Công thức | Nguồn | Tần suất | Mục tiêu | Người phụ trách |
| --- | --- | --- | --- | --- | --- |
| Lead time | Ngày hoàn thành − ngày Task vào task backlog | Công cụ quản lý việc | Mỗi mốc |  |  |
| Cycle time | Ngày Done − ngày bắt đầu Task | Công cụ quản lý việc | Mỗi mốc |  |  |
| Tỷ lệ code AI được chấp nhận | Số PR dùng không phải viết lại lớn / tổng PR có AI | PR | Mỗi mốc |  |  |
| Tỷ lệ rework | Số Task phải làm lại / tổng Task AI | Delivery Report, PR | Mỗi mốc |  |  |
| Escaped defects | Số lỗi sau release / số FR phát hành | Issue tracker | Mỗi release |  |  |

## 3. Nguyên tắc

- So sánh với baseline đo **trước** khi áp dụng AI.
- Theo dõi chất lượng sau release, không chỉ chất lượng lúc build.
- Không đặt KPI khiến Developer phải chấp nhận code AI kém chất lượng để chạy theo tốc độ: năng suất chỉ tính là cải thiện khi chỉ số Quality và Security không xấu đi.
- Đánh giá theo module và mức độ phức tạp của Task, không gộp chung toàn dự án.
- Chỉ số dùng để cải tiến hệ thống, không dùng để xếp hạng cá nhân.

## 4. Phạm vi và baseline

| Mục | Nội dung |
| --- | --- |
| Công cụ AI được đo |  |
| Hoạt động được đo |  |
| Kỳ đo |  |

| KPI | Giá trị baseline | Khoảng đo | Nguồn |
| --- | --- | --- | --- |
|  | | | |

## 5. Kết quả theo kỳ

| Kỳ | Module | Mức phức tạp | KPI | Giá trị | So với baseline | Nhận xét |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |

## 6. Rà soát và cải tiến

- **Tần suất rà soát:** mỗi mốc ở [roadmap](roadmap.md).
- **Phân tích:** xem xu hướng; với KPI xấu đi, tìm nguyên nhân gốc trước khi đề xuất thay đổi.
- **Hành động cải tiến:** ghi vào bảng dưới, phân loại theo đối tượng cải tiến (rule, skill, workflow, agent).

| Kỳ | Vấn đề phát hiện | Đối tượng cải tiến | Hành động | Người phụ trách | Kết quả |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |

## 7. Tham chiếu

- [roadmap](roadmap.md), [task-backlog](task-backlog.md), [task-breakdown](task-breakdown.md)
- [testing-strategy](../03-engineering/testing-strategy.md), [monitoring](../05-operations/monitoring.md)
