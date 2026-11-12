# Architecture Rules

> Trạng thái: **Approved**. Rule bắt buộc, trung lập về kiến trúc.

1. Mục thiết kế liên quan còn Draft hoặc trống: dừng và hỏi, không tự giả định tầng, phong cách hay công nghệ.
2. Tôn trọng các tầng và ranh giới module đã khai báo: không bỏ qua tầng, không truy cập trực tiếp dữ liệu hay nội bộ của module khác, không tạo phụ thuộc vòng.
3. Ngoại lệ so với tầng hoặc ranh giới module cũng là đổi kiến trúc: AI chỉ soạn ADR nháp (trạng thái Proposed); Kiến trúc sư duyệt trước khi code.
4. Không để logic nghiệp vụ trong lớp trình bày, và lớp trình bày không truy cập dữ liệu trực tiếp (nếu dự án có lớp trình bày).
5. API khớp đặc tả đã duyệt; thay đổi phá vỡ tương thích cần ADR.
6. Thay đổi ảnh hưởng hiệu năng, sẵn sàng hoặc bảo mật phải đối chiếu yêu cầu phi chức năng (NFR).
