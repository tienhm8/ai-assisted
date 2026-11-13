---
name: caching
description: Thiết kế, cài đặt hoặc review cache dữ liệu L1/L2: xét điều kiện được cache, chọn key, TTL, luồng đọc có single-flight, xoá key sau commit kèm đồng bộ L1 giữa các instance, fail-open, warm-up và số đo; ghi vào bảng cache của database-design. Dùng khi thêm, sửa, đọc cache hoặc đổi dữ liệu đang được cache.
---

# Caching Skill

Đưa cache vào một luồng đọc sao cho nhanh hơn mà không sai: xoá sạch cache bất kỳ lúc nào thì kết quả nghiệp vụ vẫn y nguyên.

## Cổng vào

- Mẫu truy cập `AP-<NN>` đã qua tối ưu gốc (index, truy vấn, cấu trúc bảng) ở `database-design` bước 7. Nguồn là truy vấn CSDL thì có kế hoạch thực thi sau tối ưu; đang thiết kế, chưa có CSDL thì ghi giả định, kiểm chứng ở `database-design` bước 10 trước khi cài đặt cache. Nguồn là dịch vụ ngoài hoặc tính toán thì ghi độ trễ, chi phí đo được thay cho kế hoạch thực thi.
- Có tần suất, độ trễ mục tiêu của AP và khoảng trễ dữ liệu nghiệp vụ chấp nhận được. Thiếu khoảng trễ thì ghi câu hỏi mở cho PO/BA, không tự đặt.
- Đã biết module sở hữu dữ liệu và mọi đường ghi chạm dữ liệu đó.
- Cài đặt: dòng cache trong database-design §3.7 đã Approved. Chưa có thì làm bước 1–4 rồi dừng chờ duyệt.
- Value chứa D3: cần Security duyệt thiết kế trước khi cài đặt.

Nguồn chính: plan; mã cache hiện có (hàm đọc dùng chung, client, cấu hình).
Plan thiếu thì tra đúng mục: database-design §3.4 Mẫu truy cập và khối lượng, §3.7 Cache; module-design §5 Ranh giới và quyền sở hữu; system-architecture §7 Cross-cutting Concerns; error-handling §8 Retry, timeout, fallback, §9 Transaction và nhất quán dữ liệu; security-standards §1 Xử lý dữ liệu theo mức (D0–D3), §6 Bảo vệ dữ liệu; monitoring §4 Metrics; deployment §9 Database Deployment and Migration.

## Tài liệu tham khảo

| File trong `references/` | Nạp ở bước |
| --- | --- |
| `patterns.md` | Bước 1: §1, §2 · Bước 2: §5, §8 · Bước 3: §3, §4, §6, §7 · Bước 4: §11 · Bước 5: §9 · Bước 6: §10 |
| `warmup.md` | Bước 4, chỉ khi production có cache |

## Quy trình

1. **Xét có cache không.** Dùng chi phí truy vấn **sau** tối ưu, không dùng số trước tối ưu. Đối chiếu từng điều kiện của Rule `cache` với mẫu truy cập; ghi mỗi điều kiện thoả nhờ số liệu hay giả định. "Thay đổi liên tục", "ít được đọc" đối chiếu ngưỡng ở database-design §3.7; chưa có ngưỡng thì ghi giả định kèm số liệu từ bảng AP. Thuộc danh sách không cache, hoặc thiếu một điều kiện: dừng và báo, không cache.
2. **Key và TTL.** Định dạng key, yếu tố phân biệt (tenant, người xem, quyền, ngôn ngữ), version, TTL từng tầng theo khoảng trễ chấp nhận được, jitter. Gán mức dữ liệu cho value; D3 thì ghi đủ biện pháp bảo vệ.
3. **Luồng đọc và ghi.**
   - Đọc qua hàm đọc dùng chung có single-flight; chưa có thì cài trước và dùng cho mọi luồng.
   - Liệt kê **mọi** đường ghi chạm dữ liệu (repository, update hàng loạt, SQL thô, import, job, service khác) và nơi mỗi đường xoá key sau commit.
   - Có L1 sống lâu hơn một request: chọn kênh sự kiện xoá L1 và cách phục hồi khi sự kiện lỗi.
   - Ghi cách fail-open và giới hạn tải CSDL khi cache sập.
4. **Ghi thiết kế.** Thêm dòng vào bảng cache của database-design; production có cache thì khai báo nhóm warm-up. Đổi công nghệ cache hoặc HA là quyết định kiến trúc: soạn ADR nháp.
5. **Cài đặt** theo thiết kế đã duyệt: key, TTL, hàm nạp, xoá sau commit, sự kiện L1, nhóm warm-up, số đo.
6. **Kiểm chứng** bằng test chạy thật:
   - Xoá sạch cache rồi chạy lại các ca nghiệp vụ: kết quả không đổi.
   - Ghi xong đọc lại: không trả bản cũ, kể cả từ L1 của instance khác.
   - Cache down hoặc timeout: request vẫn thành công từ CSDL.
   - Nhiều request đồng thời cùng miss một key: số truy vấn xuống CSDL không tăng theo số request, tối đa một mỗi instance; key hot thì một.
   - Key khác người dùng, tenant không đọc chéo được.
   - Kiểu dữ liệu sau serialize và deserialize giữ nguyên.

## Giới hạn

- Không cache danh sách lọc hoặc phân trang tự do khi chưa chỉ ra cách xoá đúng mọi key liên quan.
- Không thêm đường ghi mới vào dữ liệu đang được cache mà thiếu bước xoá key.
- Không tạo hàm đọc cache thứ hai khi dự án đã có.

## Hoàn thành khi

- Mỗi cache có dòng trong database-design, truy ra AP, ghi đủ điều kiện được cache và mọi sự kiện xoá key.
- Các ca kiểm chứng ở bước 6 có output test thật.
- Số đo cache đã có trong monitoring hoặc ghi rõ phần còn thiếu.

## Báo cáo

Ghi vào báo cáo bàn giao: từng key mẫu kèm điều kiện được cache, TTL, mức dữ liệu; danh sách đường ghi và nơi xoá key; cách đồng bộ L1; biện pháp chống dồn tải; nhóm warm-up; số đo đã thêm.
