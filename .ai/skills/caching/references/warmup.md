# Warm-up cache

Mẫu chống dồn tải và hàm nạp dùng chung ở `patterns.md` §3, §6. Phạm vi job chọn lọc: chỉ nạp những key mà thiếu thì request đầu tiên chậm hoặc CSDL bị dội. Mọi key khác để luồng đọc tự nạp khi miss.

## 1. Khi nào chạy

L2 không mất dữ liệu khi deploy lại ứng dụng, nên deploy bình thường **không** cần warm-up lại. Job chạy theo dấu hiệu, không chạy mù mỗi lần deploy:

| Trigger | Cách nhận biết |
| --- | --- |
| Cache mất dữ liệu (restart, failover, flush) | Mất key mốc `<service>:cache:epoch`. Job ghi key này sau khi xong tầng 1 |
| Đổi format của key hoặc value | Tăng version prefix của nhóm, khiến nhóm mới rỗng. Warm-up nhóm mới **trước** khi bản code đọc version mới nhận traffic |
| Invalidate một nhóm lớn (đổi cấu hình, import hàng loạt) | Sự kiện do module sở hữu phát ra |
| Trước giờ cao điểm đã biết | Lịch |
| Refresh-ahead cho tầng 1 | Chạy định kỳ với chu kỳ nhỏ hơn TTL |

## 2. Phân tầng

| Tầng | Nội dung | Cách nạp | Chặn mở traffic |
| --- | --- | --- | --- |
| W1 · bắt buộc | Key mà hầu hết request đều cần: cấu hình, danh mục, quyền theo vai trò. Số lượng nhỏ, liệt kê được hết | Nạp toàn bộ; refresh-ahead định kỳ | Có, với timeout. Quá hạn thì vẫn mở traffic (fail-open) |
| W2 · hot | Chi tiết bản ghi, top N theo truy cập thực tế | Chạy nền sau khi mở traffic, có giới hạn tốc độ | Không |
| Còn lại | — | Luồng đọc tự nạp khi miss | — |

Không nạp cả CSDL: tốn bộ nhớ, đẩy key hot ra ngoài, và chính job trở thành nguồn dồn tải.

## 3. Quản lý tập key warm-up

Cần có cơ chế, nhưng là **registry của nhóm** chứ không phải danh sách key ghi cứng. Danh sách cứng sẽ lệch ngay khi dữ liệu thay đổi.

- **Registry trong code:** mỗi module khai báo nhóm warm-up của mình gồm tên nhóm, tầng, hàm liệt kê mã, hàm nạp, N tối đa, cỡ lô và mức đồng thời.
  - Hàm liệt kê mã: W1 truy vấn toàn bộ; W2 đọc hot list.
  - Hàm nạp **là chính hàm của luồng đọc**: cùng key, cùng serializer, cùng TTL.
  - Module sở hữu dữ liệu sở hữu nhóm warm-up của nó.
- **Hot list cho W2:**
  - Lấy mẫu truy cập (vài phần trăm request) và ghi vào sorted set `<service>:<module>:hot:<thực thể>` bằng `ZINCRBY`, chia theo cửa sổ ngày.
  - Định kỳ cắt còn khoảng 2N phần tử.
  - Định kỳ snapshot hot list ra nơi lưu bền (CSDL hoặc file). Lý do: cache mất thì hot list mất theo, đúng lúc cần nó nhất.
  - Chưa có snapshot thì lấy theo nguồn nghiệp vụ (bản ghi được cập nhật hoặc dùng gần đây), hoặc chỉ chạy W1.
- **Key mốc epoch:** không đặt TTL. Nếu eviction policy xoá mất key này thì job chạy thừa một lần. Việc đó vô hại vì job idempotent.

## 4. Luật chạy job

- **Chỉ một instance chạy:** lock phân tán có TTL và gia hạn định kỳ, hoặc scheduler có dedupe. N instance cùng warm-up là tự gây herd.
- **Có ngân sách tải CSDL:**
  - Nạp theo lô, giới hạn đồng thời và chỉ dùng một phần nhỏ connection pool.
  - Đọc từ bản sao chỉ đọc nếu có.
  - Khi độ trễ CSDL tăng thì tạm dừng.
- **Rải thời điểm hết hạn:** key nạp đồng loạt cần TTL rải rộng hơn jitter thường, ví dụ ngẫu nhiên trong khoảng TTL × [0,5; 1]. Nếu không, đúng một TTL sau chúng cùng hết hạn.
- **Không ghi đè dữ liệu mới hơn:**
  - W2 chỉ ghi khi key chưa tồn tại (`SET NX`).
  - Refresh-ahead của W1 ghi đè có so version hoặc timestamp.
- **Chạy lại được:** lưu checkpoint tiến độ; lỗi giữa chừng thì lần sau chạy tiếp.
- **Job lỗi:** ghi log và cảnh báo.
- **Đo:**
  - Hit ratio trong 5–15 phút đầu sau trigger.
  - Thời gian chạy W1.
  - Số key đã nạp và số key lỗi.
  - Tải CSDL trong lúc job chạy.

