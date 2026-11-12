# Testing Rules

> Trạng thái: **Approved**. Rule bắt buộc.

1. Mỗi AC của Task có ít nhất một test; tên hoặc chú thích test ghi ID AC để truy vết.
2. Sửa lỗi phải kèm test hồi quy: chạy thấy đỏ trước khi sửa, xanh sau khi sửa.
3. Test cả nhánh thành công và nhánh lỗi, gồm giá trị biên và ca bị từ chối quyền.
4. Không mock chính hành vi đang được kiểm thử.
5. Không xoá, tắt hay làm yếu test; không hạ ngưỡng coverage.
6. Trước khi báo hoàn thành, chạy đủ các cổng kiểm tra của dự án (build, lint, kiểm tra kiểu, test, quét secret). Chưa có CI thì chạy cục bộ và ghi miễn trừ có thời hạn, không bỏ qua âm thầm.
7. Không khẳng định test đạt khi chưa chạy. Báo cáo kèm lệnh đã chạy và kết quả thật; phân biệt rõ pass, fail, skipped, not-run.
8. Dữ liệu test là dữ liệu giả hoặc đã ẩn danh; không chạm production.
