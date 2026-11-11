# Code Review – Examples

> Minh hoạ. Đây là **ví dụ minh hoạ**, không phải quy tắc chính thức của dự án. Quy trình chính ở `SKILL.md`; ngưỡng và mô hình tầng lấy từ tài liệu của dự án. Mỗi mẫu lỗi được viết trung lập rồi minh hoạ bằng vài ngôn ngữ để AI nhận ra cùng một lỗi ở stack khác.

## 1. Đọc PR description (Bước 1)

PR thiếu mục:

```text
Title: fix đơn hàng
Body: sửa lỗi tạo đơn
```

Reviewer không đọc code, trả về:

```text
Chưa đủ thông tin để review. Bổ sung theo mẫu PR:
- Task/AC nào? Lỗi tái hiện thế nào?
- Thay đổi hành vi hay chỉ refactor?
- Có chạm schema, API, job, cache không?
- Đã test thế nào (lệnh + kết quả)?
```

## 2. Đặt sai chỗ (ưu tiên 3)

Mẫu lỗi: quy tắc nghiệp vụ nằm ở biên nhận yêu cầu.

```php
// Laravel – controller tự tính giảm giá
public function store(Request $request) {
    $total = $request->subtotal;
    if ($request->user()->is_vip && $total > 1_000_000) { $total *= 0.9; }
    Order::create([...$request->all(), 'total' => $total]);
}
```

```ts
// Express – handler tự tính giảm giá
router.post('/orders', async (req, res) => {
  let total = req.body.subtotal;
  if (req.user.isVip && total > 1_000_000) total *= 0.9;
  await db.order.create({ data: { ...req.body, total } });
});
```

Finding:

```text
[Medium] app/Http/Controllers/OrderController.php:24
Quy tắc giảm giá VIP (BR-ORD-07) nằm trong controller → luồng tạo đơn khác (API mobile, import)
sẽ không áp dụng hoặc phải chép lại. Chuyển vào tầng nghiệp vụ (OrderService/use case).
```

Lỗi `$request->all()` / `...req.body` cùng đoạn này là finding bảo mật riêng (mục 5).

## 3. Đồng thời (ưu tiên 4)

Mẫu lỗi: đọc rồi ghi không có khoá.

```python
# Django
product = Product.objects.get(id=pid)
if product.stock >= qty:
    product.stock -= qty
    product.save()
```

```java
// Spring
Product p = repo.findById(id).orElseThrow();
if (p.getStock() >= qty) { p.setStock(p.getStock() - qty); repo.save(p); }
```

Finding:

```text
[High] inventory/services.py:41
Kịch bản: stock = 1, hai request mua 1 cùng lúc → cả hai đọc stock = 1, cả hai qua điều kiện,
stock thành 0 nhưng bán 2 → âm kho.
Hướng sửa: cập nhật có điều kiện (UPDATE ... SET stock = stock - :qty WHERE id = :id AND stock >= :qty,
kiểm số dòng bị ảnh hưởng) hoặc khoá dòng / optimistic locking theo cơ chế dự án đã chọn.
```

Mẫu lỗi: phát event trước khi commit.

```text
[High] OrderService:88
Job gửi email xác nhận được đẩy vào hàng đợi bên trong transaction. Worker có thể chạy trước khi
commit → không tìm thấy đơn; transaction rollback → khách vẫn nhận email.
Hướng sửa: phát sau khi commit (after-commit hook / outbox) theo cơ chế của dự án.
```

## 4. Hiệu năng (ưu tiên 5)

Mẫu lỗi: N+1.

```php
foreach (Order::all() as $order) { echo $order->customer->name; }   // Eloquent
```

```ruby
Order.all.each { |o| puts o.customer.name }                           # Rails
```

```ts
for (const o of await repo.find()) { console.log((await o.customer).name) } // TypeORM lazy
```

Finding:

```text
[Medium] reports/OrderReport:15
1 truy vấn đơn + N truy vấn khách; với 10 nghìn đơn là 10.001 truy vấn. Đồng thời nạp toàn bộ
bảng vào bộ nhớ. Hướng sửa: eager load quan hệ và xử lý theo lô/phân trang.
(Nâng lên High nếu đây là luồng nóng có NFR hiệu năng.)
```

## 5. Bảo mật (ưu tiên 6)

| Mẫu lỗi | Ví dụ dễ gặp | Hướng sửa |
| --- | --- | --- |
| Mass assignment | Laravel `Model::create($request->all())`; Rails `params.permit!`; Node `create({ ...req.body })`; Spring bind thẳng request vào entity | Chỉ nhận trường đã kiểm: Laravel `$request->validated()`, Rails strong params, DTO có whitelist |
| IDOR | `Order::find($id)`, `repo.findById(id)` theo ID từ URL, không kiểm chủ sở hữu | Truy vấn theo phạm vi người dùng hoặc kiểm quyền trên bản ghi (policy/guard) |
| SQL injection | `whereRaw("name = '$name'")`, `` `SELECT ... ${id}` ``, `cursor.execute(f"... {id}")` | Truy vấn tham số hoá |
| XSS | Blade `{!! $x !!}`, React `dangerouslySetInnerHTML`, Jinja `|safe` với dữ liệu người dùng | Để engine escape mặc định; nếu cần HTML thì sanitize |
| Lộ trường nhạy cảm | Trả nguyên entity/model ra JSON | Lớp định dạng đầu ra (resource/serializer/DTO) |

Finding:

```text
[Critical] app/Http/Controllers/OrderController.php:27
Order::create($request->all()) cho phép client gửi kèm "status":"paid", "total":0 → tạo đơn đã
thanh toán giá 0. Dùng $request->validated() với FormRequest chỉ khai báo các trường được phép.
Kích hoạt security-review (chạm tiền).
```

## 6. Clean code (ưu tiên 8)

```text
[Low] OrderService:120
Hàm placeOrder ~90 dòng làm 4 việc (kiểm tồn, tính giá, lưu, thông báo). Không chặn PR;
gợi ý tách khi có thay đổi tiếp theo trên hàm này.
```

## 7. Báo cáo review mẫu

```text
PR #142 · Task SHOP-31 · R3 (chạm tiền)
Hiểu biết: thêm giảm giá VIP khi tạo đơn; thay đổi hành vi; chạm bảng orders, không đổi API.
PR description: thiếu mục rollback.

Critical
1. OrderController.php:27 – mass assignment (mục 5)
High
2. InventoryService.php:41 – âm kho khi mua đồng thời (mục 3)
3. Thiếu test cho AC-SHOP-31-02 (đơn đúng 1.000.000 có được giảm không)
Medium
4. OrderController.php:24 – quy tắc giảm giá nằm ở controller (mục 2)
Câu hỏi
- BR-ORD-07: ngưỡng 1.000.000 là trước hay sau thuế?
Điểm tốt
- Migration có bước down, test regression cho lỗi làm tròn cũ.
Không áp dụng: ưu tiên 7 (không thêm job/cấu hình).
Đã kích hoạt security-review.

Kết luận khuyến nghị: Không duyệt (còn 1 Critical, 2 High).
```
