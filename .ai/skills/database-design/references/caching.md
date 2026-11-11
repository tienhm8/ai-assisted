# Cache dữ liệu (L1/L2)

Nạp khi một mẫu truy cập `AP-NN` đã tối ưu truy vấn/index (bậc 1) mà vẫn không đạt NFR, hoặc khi review một cache sẵn có. Cache là bậc 2 của bậc mở rộng: chỉ thêm khi có số liệu đo.

## 1. Nguyên tắc nền

- **CSDL là nguồn sự thật, cache chỉ để tăng tốc.** Xoá sạch cache bất kỳ lúc nào thì hệ thống vẫn phải đúng, chỉ chậm hơn.
- **L2** là cache dùng chung giữa các instance (Redis, Memcached…). **L1** là cache cục bộ: trong một request, hoặc trong RAM của một process. Thứ tự đọc: L1 → L2 → CSDL.
- Chỉ đáng cache khi đủ cả ba điều kiện:
  1. Đọc nhiều hơn ghi rất nhiều.
  2. Đọc hoặc tính từ nguồn tốn kém.
  3. Nghiệp vụ chấp nhận dữ liệu trễ một khoảng.

  Thiếu một điều kiện thì không cache.

## 2. Nên và không nên cache

| Nên | Không |
| --- | --- |
| Chi tiết một bản ghi theo mã; danh mục; cấu hình; quyền đã tính sẵn; số tổng hợp tốn công tính | Số dư, giao dịch tiền; tồn kho hoặc trạng thái giữ chỗ đang tranh chấp; lock nghiệp vụ; secret, token, mật khẩu; danh sách lọc/phân trang tự do (tổ hợp vô hạn, không xoá đúng được) |

Câu hỏi quyết định: *"Người dùng thấy dữ liệu cũ X phút thì có ai bị thiệt không?"* Có thì không cache, hoặc giảm X.

## 3. Mô hình đọc/ghi

- **Mặc định: cache-aside.** Ứng dụng đọc cache; miss thì đọc CSDL rồi ghi cache.
- **Khi ghi: ghi CSDL xong thì xoá key, không cập nhật key.** Hai request ghi đồng thời mà cùng cập nhật cache dễ ghi đè nhau, khiến cache giữ giá trị sai.
- Chỉ khi nghiệp vụ đòi đọc ngay sau ghi phải đúng mới chọn thêm một trong hai cách, ghi lý do:
  - **Version trong key hoặc value:** ghi đè chỉ khi version mới hơn.
  - **Xoá kép trễ:** xoá → ghi CSDL → đợi một nhịp → xoá lại.
- Không dùng write-behind (ghi cache trước, đẩy xuống CSDL sau) cho dữ liệu nghiệp vụ: cache mất thì mất dữ liệu.
- **Gom việc xoá vào một chỗ:** tầng truy cập dữ liệu (repository/DAO) của module sở hữu dữ liệu. Thêm đường ghi mới mà quên xoá thì dữ liệu sai tới hết TTL. Module khác không xoá hộ: chúng phát sự kiện, module sở hữu tự xoá.

## 4. Key và TTL

- **Định dạng key:** `<module>:<thực thể>:<mã>[:<biến thể>]`. Nhìn key là biết module sở hữu và xoá được theo nhóm.
- **Yếu tố phân biệt phải nằm trong key:** dữ liệu phụ thuộc tenant, người xem, quyền hoặc ngôn ngữ thì key phải chứa yếu tố đó. Thiếu thì lộ dữ liệu chéo người dùng.
- **TTL là lưới an toàn, không phải cơ chế nhất quán chính.** Độ dài TTL theo mức chịu trễ của nghiệp vụ: danh mục, cấu hình để dài (phút đến giờ); dữ liệu hiển thị để ngắn.
- **Luôn cộng jitter ±10–20%.** Các key nạp cùng lúc với TTL cố định sẽ hết hạn cùng giây.
- **Xoá theo nhóm:** dùng version prefix (`v42:…`, tăng version là cả nhóm mất hiệu lực) hoặc quét dần (`SCAN`) theo lô. Không bao giờ dùng `KEYS`: lệnh này block cả server.
- **Không cache lỗi hoặc ngoại lệ.** Kết quả rỗng hợp lệ thì được cache, với TTL ngắn (xem §5).

## 5. Chống dồn tải

Gọi tên sự cố theo hiện tượng, không theo tên gọi, vì các tài liệu dùng tên lẫn lộn. Chỉ áp biện pháp cho sự cố mà mẫu truy cập thật sự có thể gặp.

| Hiện tượng | Biện pháp mặc định | Thêm khi cần |
| --- | --- | --- |
| Nhiều key hết hạn cùng lúc (sau deploy, warm-up, xoá nhóm) | Jitter TTL; xoá nhóm bằng version prefix | Warm-up giãn nhịp (§6) |
| Một key hot bị miss, N request cùng đi CSDL | **Single-flight**: trong một process, gộp các request chờ vào một promise dùng chung; giữa các instance, dùng lock `SET NX` **có TTL**. Request chờ có giới hạn (vd 5 × 50 ms); hết hạn thì tự đọc CSDL hoặc trả bản cũ | Key cực hot: **stale-while-revalidate**. Lưu soft TTL < hard TTL; quá soft TTL thì vẫn trả bản cũ và chỉ một request nạp lại nền. Key hot đã biết trước: đưa vào tầng T1 của warm-up (§6) |
| Hỏi mã không tồn tại, luôn xuống CSDL | Validate input ở biên; cache kết quả rỗng với TTL ngắn | Bloom filter, chỉ khi có số liệu về lưu lượng mã rác lớn |
| Cả tầng cache sập | Fail-open (§7); connection pool giới hạn số truy vấn đồng thời xuống CSDL | HA cho cache (replica/sentinel/cluster), circuit breaker, rate limit ở biên. Khi nào cần thì theo NFR sẵn sàng |

Lock chống herd **không phải khoá nghiệp vụ**. Chống bán trùng hoặc ghi trùng phải dùng transaction, khoá ở CSDL hoặc distributed lock riêng.

## 6. Warm-up

Production có cache thì phải có job warm-up. Phạm vi job chọn lọc: chỉ nạp những key mà thiếu thì request đầu tiên chậm hoặc CSDL bị dội. Mọi key khác để luồng đọc tự nạp khi miss.

### 6.1 Khi nào chạy

L2 không mất dữ liệu khi deploy lại ứng dụng, nên deploy bình thường **không** cần warm-up lại. Job chạy theo dấu hiệu, không chạy mù mỗi lần deploy:

| Trigger | Cách nhận biết |
| --- | --- |
| Cache mất dữ liệu (restart, failover, flush) | Mất key mốc `<app>:cache:epoch`. Job ghi key này sau khi xong tầng 1 |
| Đổi format của key hoặc value | Tăng version prefix của nhóm, khiến nhóm mới rỗng. Warm-up nhóm mới **trước** khi bản code đọc version mới nhận traffic |
| Invalidate một nhóm lớn (đổi cấu hình, import hàng loạt) | Sự kiện do module sở hữu phát ra |
| Trước giờ cao điểm đã biết | Lịch |
| Refresh-ahead cho tầng 1 | Chạy định kỳ với chu kỳ nhỏ hơn TTL |

### 6.2 Phân tầng

| Tầng | Nội dung | Cách nạp | Chặn mở traffic |
| --- | --- | --- | --- |
| T1 · bắt buộc | Key mà hầu hết request đều cần: cấu hình, danh mục, quyền theo vai trò. Số lượng nhỏ, liệt kê được hết | Nạp toàn bộ; refresh-ahead định kỳ | Có, với timeout. Quá hạn thì vẫn mở traffic (fail-open) |
| T2 · hot | Chi tiết bản ghi, top N theo truy cập thực tế | Chạy nền sau khi mở traffic, có giới hạn tốc độ | Không |
| Còn lại | — | Luồng đọc tự nạp khi miss | — |

Không nạp cả CSDL: tốn bộ nhớ, đẩy key hot ra ngoài, và chính job trở thành nguồn dồn tải.

### 6.3 Quản lý tập key warm-up

Cần có cơ chế, nhưng là **registry của nhóm** chứ không phải danh sách key ghi cứng. Danh sách cứng sẽ lệch ngay khi dữ liệu thay đổi.

- **Registry trong code:** mỗi module khai báo nhóm warm-up của mình gồm tên nhóm, tầng, hàm liệt kê mã, hàm nạp, N tối đa, cỡ lô và mức đồng thời.
  - Hàm liệt kê mã: T1 truy vấn toàn bộ; T2 đọc hot list.
  - Hàm nạp **là chính hàm của luồng đọc**: cùng key, cùng serializer, cùng TTL.
  - Module sở hữu dữ liệu sở hữu nhóm warm-up của nó.
- **Hot list cho T2:**
  - Lấy mẫu truy cập (vài phần trăm request) và ghi vào sorted set `<module>:hot:<thực thể>` bằng `ZINCRBY`, chia theo cửa sổ ngày.
  - Định kỳ cắt còn khoảng 2N phần tử.
  - Định kỳ snapshot hot list ra nơi lưu bền (CSDL hoặc file). Lý do: cache mất thì hot list mất theo, đúng lúc cần nó nhất.
  - Chưa có snapshot thì lấy theo nguồn nghiệp vụ (bản ghi được cập nhật hoặc dùng gần đây), hoặc chỉ chạy T1.
- **Key mốc epoch:** không đặt TTL. Nếu eviction policy xoá mất key này thì job chạy thừa một lần. Việc đó vô hại vì job idempotent.

### 6.4 Luật chạy job

- **Chỉ một instance chạy:** lock phân tán có TTL và gia hạn định kỳ, hoặc scheduler có dedupe. N instance cùng warm-up là tự gây herd.
- **Có ngân sách tải CSDL:**
  - Nạp theo lô, giới hạn đồng thời và chỉ dùng một phần nhỏ connection pool.
  - Đọc từ bản sao chỉ đọc nếu có.
  - Khi độ trễ CSDL tăng thì tạm dừng.
- **Rải thời điểm hết hạn:** key nạp đồng loạt cần TTL rải rộng hơn jitter thường, ví dụ ngẫu nhiên trong khoảng TTL × [0,5; 1]. Nếu không, đúng một TTL sau chúng cùng hết hạn.
- **Không ghi đè dữ liệu mới hơn:**
  - T2 chỉ ghi khi key chưa tồn tại (`SET NX`).
  - Refresh-ahead của T1 ghi đè có so version hoặc timestamp.
- **Chạy lại được:** lưu checkpoint tiến độ; lỗi giữa chừng thì lần sau chạy tiếp.
- **Fail-open:** job lỗi không chặn khởi động, chỉ ghi log và cảnh báo.
- **Đo:**
  - Hit ratio trong 5–15 phút đầu sau trigger.
  - Thời gian chạy T1.
  - Số key đã nạp và số key lỗi.
  - Tải CSDL trong lúc job chạy.

## 7. Fail-open và nhiều instance

- **Fail-open:** cache lỗi (down, timeout, deserialize hỏng) thì bỏ qua cache, đọc nguồn và ghi log. Không trả lỗi cho người dùng vì cache.
- **Timeout gọi cache ngắn hơn hẳn truy vấn gốc**, không retry vô hạn. Nếu không, cache chết sẽ kéo hệ thống treo theo.
- **L2** dùng chung nên tự nhất quán giữa các instance. **L1 sống lâu hơn một request thì không:** mỗi instance giữ một bản riêng. Khi đó phải broadcast lệnh xoá (pub/sub) tới mọi instance, hoặc giữ TTL của L1 rất ngắn (vài giây).

## 8. Bẫy và đo lường

- **Serialize làm mất kiểu:** qua JSON, ngày giờ, số lớn và số thập phân thành chuỗi. Đọc ra phải chuyển lại kiểu, và có test cho việc này.
- **Value lớn (vài MB) làm chậm mạng và cache:** chỉ cache phần cần dùng, hoặc nén.
- **Thiếu `maxmemory` và eviction policy:** cache đầy thì lỗi ghi.
- **Cần đo:** hit ratio, latency gọi cache, số lần fail-open, tải CSDL khi miss. Không có số đo thì không chứng minh được cache có ích, và cũng không biết khi nào nó hỏng.

## 9. Ghi vào thiết kế

Mỗi cache là một dòng trong bảng cache của database-design.md. Mỗi dòng ghi:
- Key mẫu và module sở hữu.
- AP phục vụ.
- Mô hình đọc/ghi.
- TTL (đã có jitter).
- Sự kiện xoá key: mọi đường ghi chạm dữ liệu đó.
- Biện pháp chống dồn tải.
- Tầng warm-up (T1, T2 hoặc không), kèm trigger và ngân sách tải CSDL.
- L1 hay L2.
