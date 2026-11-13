# Cache dữ liệu (L1/L2): mẫu thiết kế và cài đặt

Điều bắt buộc nằm ở Rule `cache`; file này chỉ ghi cách làm.

## 1. Mô hình

- **L1:** cache cục bộ, trong một request hoặc trong RAM của một process. Tuỳ chọn.
- **L2:** cache dùng chung giữa các instance. Công nghệ cụ thể theo kiến trúc của dự án.
- **CSDL:** nguồn sự thật duy nhất.
- Cache là lớp đặt trên truy vấn đã tối ưu, không phải cách né tối ưu. Truy vấn chậm vì thiếu index thì cache chỉ che lỗi: mỗi lần miss, warm-up hay cache sập, truy vấn chậm đó lại chạy.
- Dữ liệu có cache thì đọc tầng gần trước: L1 → L2 → CSDL. Dữ liệu không thoả điều kiện cache thì đọc thẳng CSDL.

## 2. Phân loại dữ liệu

Bảng dưới là gợi ý ban đầu. Mỗi cache vẫn phải đủ sáu điều kiện ở Rule `cache`.

| Loại dữ liệu | Cache? | Điều kiện kèm |
| --- | --- | --- |
| Master data, reference data, danh sách category | Có | |
| Cấu hình hệ thống | Có | |
| Product catalog | Có | |
| Kết quả truy vấn đọc nhiều | Có | Key xác định được từ tham số, xoá đúng được |
| Báo cáo tổng hợp | Có | |
| Dashboard statistics | Có | Nghiệp vụ chấp nhận trễ; ghi rõ khoảng trễ |
| User profile | Có | Invalidation đủ mọi đường ghi; theo §8 nếu chứa D3 |
| Permission / Role | Có điều kiện | Đổi quyền thì xoá ngay, kể cả L1 trên mọi instance; TTL ngắn |
| Search result | Có điều kiện | TTL ngắn; giới hạn số key (chỉ trang đầu, tham số phổ biến) |
| Danh sách lọc hoặc phân trang tự do | Không mặc định | Tổ hợp key vô hạn, không xoá đúng được. Cần thì xoá theo nhóm bằng version prefix, chỉ khi tần suất ghi thấp |

Câu hỏi quyết định khoảng trễ: *"Người dùng thấy dữ liệu cũ X phút thì có ai bị thiệt không?"* Có thì không cache, hoặc giảm X.

## 3. Luồng đọc

```
L1 hit           → trả
L1 miss, L2 hit  → nạp L1 → trả
L2 miss          → single-flight → đọc CSDL → ghi L2 rồi L1 → trả
L2 lỗi           → bỏ qua cache → đọc CSDL → trả; ghi log, đếm fail-open
```

- **Phân biệt miss với lỗi:** miss là key không có; lỗi là timeout, mất kết nối, deserialize hỏng. Miss thì nạp và ghi lại cache; lỗi thì không ghi lại, chỉ đọc nguồn. Đo riêng hai số này.
- **Single-flight là mặc định** và đặt trong một hàm đọc dùng chung (dạng `remember(key, ttl, loader)`), không viết lại ở từng luồng:
  - Trong một process: gộp các request cùng key vào một promise.
  - Giữa các instance: lock `SET NX` có TTL, chỉ cho key được đánh dấu hot. Key hot đánh dấu ở cột "Chống dồn tải" của bảng cache trong database-design, dựa trên tần suất ở bảng AP. Key thường chấp nhận tối đa một truy vấn mỗi instance.
  - Request chờ có giới hạn (vd 5 × 50 ms; ngưỡng thật tính theo độ trễ mục tiêu của AP). Hết hạn thì tự đọc CSDL, không trả lỗi; số truy vấn đồng thời xuống CSDL vẫn bị giới hạn bởi connection pool.
- Dự án đã có hàm đọc cache dùng chung thì dùng lại, không tạo hàm thứ hai.

## 4. Luồng ghi và invalidation

```
Transaction commit → xoá key L2 → phát sự kiện invalidation → mọi instance xoá L1
```

- **Sau commit:** gắn vào hook after-commit của transaction, hoặc outbox. Xoá trước commit thì một request đọc chen vào sẽ nạp lại bản cũ; transaction rollback thì đã xoá oan.
- **Xoá, không cập nhật.** Hai request ghi đồng thời mà cùng cập nhật cache thì thứ tự observer không theo thứ tự commit, cache có thể giữ giá trị cũ tới hết TTL. Xoá thì request đọc sau nạp lại giá trị đúng.
- **Cập nhật chỉ khi có version:** giá trị cache mang version (hoặc `updated_at` đủ chính xác); ghi bằng script so-rồi-ghi, chỉ ghi khi version mới hơn. Dùng cho key W1 (cấu hình, danh mục) khi không muốn cache trống sau ghi.
- **Đọc ngay sau ghi phải đúng:** thêm xoá kép trễ (xoá → ghi CSDL → đợi một nhịp → xoá lại) hoặc version. Không có thì TTL là lưới an toàn cuối.
- **Xoá thất bại không được bỏ qua** như đọc thất bại: key cũ sẽ sống tới hết TTL. Retry có giới hạn; hết lượt thì đẩy vào hàng đợi xử lý lại và ghi log cảnh báo.
- **Sự kiện invalidation L1** có retry hoặc cơ chế phục hồi. Instance mất kết nối tới kênh sự kiện thì xoá sạch L1 khi kết nối lại. TTL ngắn của L1 là lưới an toàn khi sự kiện vẫn lọt.
- **Mọi đường ghi phải đi qua tầng truy cập dữ liệu hoặc tự phát sự kiện:** update hàng loạt, SQL thô, migration, import, job, service khác ghi cùng CSDL. Observer của ORM không bắt được các đường này.
- **Gom việc xoá ở module sở hữu dữ liệu.** Cache tổng hợp ở module khác nghe sự kiện và tự xoá key của mình.
- Không dùng write-behind (ghi cache trước, đẩy xuống CSDL sau) cho dữ liệu nghiệp vụ.

## 5. Key và TTL

- **Định dạng key** theo quy ước của dự án; mặc định `<service>:<module>:<thực thể>:<mã>[:<biến thể>]`. Nhìn key là biết module sở hữu và xoá được theo nhóm.
- **Key không chứa dữ liệu nhạy cảm:** dùng mã nội bộ, không dùng email, số điện thoại, số giấy tờ. Key hiện ra trong log và công cụ giám sát.
- **Version trong key** (`v42:…`) khi đổi cấu trúc value hoặc cần xoá cả nhóm: tăng version là cả nhóm mất hiệu lực.
- **TTL theo loại dữ liệu**, không dùng một TTL chung. Danh mục, cấu hình: phút đến giờ. Dữ liệu hiển thị: ngắn. Quyền: ngắn.
- **TTL của L1 ≤ TTL của L2**; L1 sống lâu hơn một request thì giữ vài giây đến vài chục giây.
- **Jitter ±10–20%** để các key nạp cùng lúc không hết hạn cùng giây.
- **Negative caching:** kết quả rỗng hợp lệ (mã không tồn tại) được cache với TTL ngắn. Không cache lỗi hoặc ngoại lệ.
- **Xoá theo nhóm:** version prefix hoặc `SCAN` theo lô. Không dùng `KEYS`.

## 6. Chống dồn tải

| Hiện tượng | Biện pháp mặc định | Thêm khi cần |
| --- | --- | --- |
| Nhiều key hết hạn cùng lúc (sau deploy, warm-up, xoá nhóm) | Jitter TTL; xoá nhóm bằng version prefix | Warm-up giãn nhịp (`warmup.md`) |
| Một key bị miss, N request cùng đi CSDL | Single-flight (§3) | Key cực hot: **stale-while-revalidate**. Lưu soft TTL < hard TTL; quá soft TTL thì vẫn trả bản cũ và chỉ một request nạp lại nền. Key hot biết trước: đưa vào W1 của warm-up |
| Hỏi mã không tồn tại, luôn xuống CSDL | Validate input ở biên; negative caching | Bloom filter, chỉ khi có số liệu về lưu lượng mã rác lớn |
| Cả tầng cache sập | Fail-open (§7); giới hạn số truy vấn đồng thời xuống CSDL | HA cho cache, circuit breaker, rate limit ở biên, theo NFR sẵn sàng |

Lock chống dồn tải **không phải khoá nghiệp vụ**. Chống bán trùng, ghi trùng dùng transaction, khoá ở CSDL hoặc distributed lock riêng.

## 7. Lỗi và fail-open

- Cache lỗi thì bỏ qua cache, đọc nguồn, ghi log; không trả lỗi cho người dùng vì cache.
- Timeout gọi cache ngắn hơn hẳn truy vấn gốc; connection pool tới cache có giới hạn; retry có giới hạn, không retry vô hạn.
- Cache sập thì mọi request đổ xuống CSDL: giới hạn đồng thời (pool, bulkhead) để CSDL không sập theo. Circuit breaker giúp bỏ qua cache ngay thay vì chờ timeout ở từng request.
- Không phụ thuộc thứ tự xử lý request giữa các instance.

## 8. Dữ liệu cá nhân (D3)

Điều kiện bắt buộc ở Rule `cache`. Cách đáp ứng:

- **Chỉ cache trường cần dùng:** tạo kiểu dữ liệu riêng cho value cache theo màn hình hoặc API dùng nó, không serialize nguyên entity. Màn hình cần tên thì value chỉ có mã và tên.
- **Key:** `<service>:<module>:<thực thể>:<mã nội bộ>`, cộng mã tenant khi đa tenant. Tra theo email hay số điện thoại thì tra CSDL ra mã nội bộ trước, không tạo key theo email.
- **TLS và tài khoản:** mỗi service một tài khoản trên cache, chỉ có quyền trên tiền tố key của nó (ACL theo tiền tố nếu công nghệ hỗ trợ). Không dùng mật khẩu chung.
- **Lưu đĩa:** cache bật snapshot hoặc append log thì đĩa mã hoá, hoặc đặt nhóm key D3 ở instance cache tắt lưu đĩa. Bản sao replica và file sao lưu của cache cũng thuộc phạm vi này.
- **TTL ngắn:** theo khoảng trễ chấp nhận được, và không dài hơn thời hạn mà yêu cầu xoá phải có hiệu lực.
- **Xoá theo yêu cầu:** luồng xoá tài khoản gọi xoá mọi key D3 của người đó (liệt kê trong dòng cache ở database-design), kể cả L1 trên mọi instance; test chứng minh sau khi xoá không còn đọc được từ cache.

## 9. Bẫy

- **Serialize làm mất kiểu:** qua JSON, ngày giờ, số lớn, số thập phân thành chuỗi. Đọc ra phải chuyển lại kiểu, có test.
- **Value lớn:** giới hạn kích thước value theo trần của dự án; vượt thì chỉ cache phần cần dùng, hoặc nén.
- **Thiếu `maxmemory` và eviction policy:** cache đầy thì lỗi ghi. Policy chỉ evict key có TTL thì key thiếu TTL không bao giờ bị đẩy ra.

## 10. Đo lường

Tối thiểu:

- Hit rate và miss rate của L1, L2.
- Latency gọi L2 (p95, p99); số lần timeout, lỗi và fail-open.
- Bộ nhớ đã dùng; eviction rate.
- Tải CSDL khi miss.
- Số lần single-flight phải chờ; hot key.
- Số lần xoá key thất bại; số sự kiện invalidation lỗi và độ trễ.

Không có số đo thì không chứng minh được cache có ích, và không biết khi nào nó hỏng.

## 11. Ghi vào thiết kế

Mỗi cache là một dòng trong bảng cache của database-design. Mỗi dòng ghi:

- Key mẫu và module sở hữu.
- AP phục vụ và sáu điều kiện của Rule `cache` đã thoả thế nào (khoảng trễ chấp nhận được ghi bằng số).
- Mức dữ liệu cao nhất trong value; D3 thì ghi cách bảo vệ theo §8.
- L1, L2 hay cả hai; TTL từng tầng (đã có jitter).
- Mô hình đọc/ghi: xoá hay cập nhật có version.
- Sự kiện xoá key: mọi đường ghi chạm dữ liệu đó.
- Biện pháp chống dồn tải; key hot (lock giữa instance) hay không.
- Tầng warm-up (W1, W2 hoặc không), kèm trigger và ngân sách tải CSDL.
