# KPI đánh giá hiệu quả AI Development

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | roadmap.md, backlog.md, ../03-engineering/testing-strategy.md, ../05-operations/monitoring.md |

> **Mục đích.** Chọn chỉ số, ghi baseline và kết quả đo để đánh giá AI có thực sự cải thiện việc phát triển hay không. Định nghĩa đầy đủ của từng chỉ số nằm ở; file này chỉ ghi chỉ số dự án chọn đo và số liệu thực tế. Không chỉ đo số dòng code AI tạo ra hoặc số Task hoàn thành.

## 1. Nhóm KPI

| Nhóm | KPI | Nguồn dữ liệu | Ghi chú |
| --- | --- | --- | --- |
| Productivity | Lead time; thời gian hoàn thành Task (cycle time); thời gian review | Công cụ quản lý việc, Git/PR, CD | Thời gian review tách theo R1/R2/R3 |
| Quality | Defect rate; escaped defects (lỗi phát hiện sau release); test pass rate | Issue tracker, CI hoặc kết quả test chạy local | Escaped defects tính trên số FR phát hành |
| Security | Critical vulnerabilities; authorization defects (lỗi phân quyền) | Công cụ quét, review, sự cố | Tách theo nguồn phát hiện: cổng, review, sau release |
| AI Efficiency | Tỷ lệ code AI được chấp nhận; số vòng sửa; chi phí AI / Task | PR, nhật ký AI, hoá đơn nhà cung cấp | "Chấp nhận" là dùng mà không phải viết lại lớn |

## 2. Nguyên tắc

- So sánh với baseline đo **trước** khi áp dụng AI.
- Theo dõi chất lượng sau release, không chỉ chất lượng lúc build.
- Không đặt KPI khiến Developer phải chấp nhận code AI kém chất lượng để chạy theo tốc độ: năng suất chỉ tính là cải thiện khi chỉ số Quality và Security không xấu đi.
- Đánh giá theo module và mức độ phức tạp của Task, không gộp chung toàn dự án.
- Chỉ số dùng để cải tiến hệ thống, không dùng để xếp hạng cá nhân.

## 3. Baseline

| KPI | Giá trị baseline | Khoảng đo | Nguồn |
| --- | --- | --- | --- |
|  | | | |

## 4. Kết quả theo kỳ

| Kỳ | Module | Mức phức tạp | KPI | Giá trị | So với baseline | Nhận xét |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |
