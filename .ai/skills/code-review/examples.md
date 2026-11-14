# Code Review – Examples

> Illustration. These are **illustrative examples**, not official project rules. The main procedure is in `SKILL.md`; thresholds and layer model come from project docs. Each bug pattern is described neutrally, then illustrated in several languages so the AI recognizes the same bug in other stacks.

## 1. Read the PR description (Step 1)

PR missing items:

```text
Title: fix order
Body: fix order creation bug
```

Reviewer does not read the code and returns:

```text
Not enough information to review. Fill in per the PR template:
- Which Task/AC? How is the bug reproduced?
- Behavior change or refactor only?
- Does it touch schema, API, job, cache?
- How was it tested (command + result)?
```

## 2. Wrong placement (priority 3)

Bug pattern: business rule at the request boundary.

```php
// Laravel – controller computes the discount itself
public function store(Request $request) {
    $total = $request->subtotal;
    if ($request->user()->is_vip && $total > 1_000_000) { $total *= 0.9; }
    Order::create([...$request->all(), 'total' => $total]);
}
```

```ts
// Express – handler computes the discount itself
router.post('/orders', async (req, res) => {
  let total = req.body.subtotal;
  if (req.user.isVip && total > 1_000_000) total *= 0.9;
  await db.order.create({ data: { ...req.body, total } });
});
```

Finding:

```text
[Medium] app/Http/Controllers/OrderController.php:24
VIP discount rule (BR-ORD-07) lives in the controller → other order-creation flows (mobile API, import)
will not apply it or must copy it. Move it to the business layer (OrderService/use case).
```

The `$request->all()` / `...req.body` bug in the same snippet is a separate security finding (section 5).

## 3. Concurrency (priority 4)

Bug pattern: read then write without a lock.

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
Scenario: stock = 1, two requests buy 1 at the same time → both read stock = 1, both pass the check,
stock becomes 0 but 2 are sold → negative stock.
Fix direction: conditional update (UPDATE ... SET stock = stock - :qty WHERE id = :id AND stock >= :qty,
check affected row count) or row lock / optimistic locking per the project's chosen mechanism.
```

Bug pattern: emitting an event before commit.

```text
[High] OrderService:88
The confirmation email job is queued inside the transaction. The worker may run before
commit → order not found; transaction rolls back → customer still gets the email.
Fix direction: emit after commit (after-commit hook / outbox) per the project's mechanism.
```

## 4. Performance (priority 5)

Bug pattern: N+1.

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
1 order query + N customer queries; with 10 thousand orders that is 10,001 queries. It also loads the whole
table into memory. Fix direction: eager load the relation and process in batches/pages.
(Raise to High if this is a hot path with a performance NFR.)
```

## 5. Security (priority 6)

| Bug pattern | Common example | Fix direction |
| --- | --- | --- |
| Mass assignment | Laravel `Model::create($request->all())`; Rails `params.permit!`; Node `create({ ...req.body })`; Spring binding request directly to entity | Accept only validated fields: Laravel `$request->validated()`, Rails strong params, DTO with whitelist |
| IDOR | `Order::find($id)`, `repo.findById(id)` by ID from URL, no ownership check | Query scoped to the user or check per-record authorization (policy/guard) |
| SQL injection | `whereRaw("name = '$name'")`, `` `SELECT ... ${id}` ``, `cursor.execute(f"... {id}")` | Parameterized queries |
| XSS | Blade `{!! $x !!}`, React `dangerouslySetInnerHTML`, Jinja `|safe` with user data | Let the engine escape by default; if HTML is needed, sanitize |
| Sensitive field exposure | Returning the raw entity/model as JSON | Output formatting layer (resource/serializer/DTO) |

Finding:

```text
[Critical] app/Http/Controllers/OrderController.php:27
Order::create($request->all()) lets the client send "status":"paid", "total":0 → creates a paid
order priced 0. Use $request->validated() with a FormRequest declaring only allowed fields.
Trigger security-review (touches money).
```

## 6. Clean code (priority 8)

```text
[Low] OrderService:120
Function placeOrder ~90 lines does 4 things (check stock, price, save, notify). Does not block the PR;
suggest splitting on the next change to this function.
```

## 7. Sample review report

```text
PR #142 · Task SHOP-31 · R3 (touches money)
Understanding: adds VIP discount on order creation; behavior change; touches orders table, no API change.
PR description: missing rollback item.

Critical
1. OrderController.php:27 – mass assignment (section 5)
High
2. InventoryService.php:41 – negative stock on concurrent purchase (section 3)
3. Missing test for AC-SHOP-31-02 (does an order of exactly 1,000,000 get the discount?)
Medium
4. OrderController.php:24 – discount rule lives in the controller (section 2)
Questions
- BR-ORD-07: is the 1,000,000 threshold before or after tax?
Good points
- Migration has a down step, regression test for the old rounding bug.
Not applicable: priority 7 (no new job/config).
security-review triggered.

Recommendation: Do not approve (1 Critical, 2 High remain).
```
