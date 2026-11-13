# Code Review – Checklist đồng thời, hiệu năng, vận hành (ưu tiên 4, 5, 7)

## Ưu tiên 4: Khi hệ thống chịu tải và chạy đồng thời thì sao?

- Hai yêu cầu cùng lúc trên cùng dữ liệu: có mẫu "đọc rồi ghi" (đọc giá trị, quyết định, ghi lại) mà không có khoá, optimistic locking hoặc cập nhật có điều kiện không?
- Ràng buộc duy nhất có được bảo đảm ở tầng lưu trữ không, hay chỉ kiểm "đã tồn tại chưa" bằng code (dễ trùng khi đồng thời)?
- Tác vụ chạy lại (retry, message giao hai lần, người dùng bấm hai lần): có idempotent không, có khoá idempotency cho thao tác tạo/thanh toán không?
- Tác vụ nền: có timeout, giới hạn số lần retry, backoff, nơi xử lý khi thất bại cuối cùng; có chặn chạy chồng khi cần không?
- Event/tác vụ nền được phát **sau khi** transaction commit, không phát trước (tránh xử lý dữ liệu chưa tồn tại hoặc đã rollback).
- Trạng thái dùng chung trong bộ nhớ tiến trình (biến toàn cục, singleton có trạng thái) có an toàn khi nhiều request hoặc nhiều instance không?
- Lời gọi ra ngoài có timeout; lỗi của hệ thống ngoài không kéo đổ luồng chính.

## Ưu tiên 5: Hiệu năng, dữ liệu, cache

- Truy vấn hoặc lời gọi mạng nằm trong vòng lặp (N+1), kể cả gọi gián tiếp qua thuộc tính lazy-load.
- Truy vấn chạy trên bao nhiêu bản ghi, hôm nay và khi dữ liệu tăng; có giới hạn, phân trang, xử lý theo lô hoặc stream không, hay nạp toàn bộ vào bộ nhớ?
- Chỉ lấy cột và dữ liệu cần dùng.
- Index theo truy vấn mới hoặc đã đổi: điều kiện lọc, join và sắp xếp có index phù hợp không (kể cả thứ tự cột trong index ghép); điều kiện có làm index không dùng được không (`database-rules`).
- Index sau thay đổi còn hợp lý không: index cũ còn phục vụ mẫu truy cập nào không; index mới có trùng hoặc bị index sẵn có bao phủ (cùng tiền tố cột) không; cột đổi hoặc xoá kéo theo index nào. Thêm hoặc bỏ index phải có bằng chứng theo `database-rules` và bảng index ↔ mẫu truy cập trong tài liệu thiết kế CSDL được cập nhật cùng PR; thiếu thì yêu cầu người viết điều chỉnh, reviewer không tự sửa.
- Migration trên bảng lớn có khoá bảng lâu, có cần chạy theo lô hoặc tách bước không.
- Có nên cache không (điều kiện ở `cache-rules`); nếu cache: xoá key sau commit ở mọi đường ghi, L1 của instance khác có bị xoá không, thời gian sống, khoá cache có tách theo người dùng/tenant/quyền không (thiếu là lộ dữ liệu chéo), key có chứa dữ liệu nhạy cảm không, nhiều request cùng miss cache thì sao.
- Đối chiếu NFR hiệu năng khi thay đổi nằm trên luồng nóng.

## Ưu tiên 7: Vận hành được không?

- Lỗi quan trọng được ghi log kèm ngữ cảnh và correlation ID, không ghi dữ liệu nhạy cảm.
- Tác vụ nền thất bại thì có người biết (log, alert, hàng đợi lỗi).
- Cần metric hoặc alert mới không; cấu hình mới đã có giá trị cho mọi môi trường chưa.
- Có rollback được không; feature flag có kế hoạch gỡ không.
