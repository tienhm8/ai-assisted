# Database Design

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt (dự án) | Kiến trúc sư |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | system-architecture.md, module-design.md, api-design.md, ../01-requirements/business-rules.md, ../03-engineering/coding-standards.md, ../03-engineering/security-standards.md, ../05-operations/deployment.md, ../05-operations/backup-recovery.md, ../../.ai/rules/database-rules.md, ../../.ai/skills/database-design/SKILL.md |

> **Mục đích.** Database Schema: mô hình dữ liệu, ràng buộc, quy tắc migration, seed và dữ liệu test (dữ liệu test là dữ liệu giả/ẩn danh).

## 1. Tổng quan cơ sở dữ liệu
Công nghệ và phiên bản ghi ở [system-architecture](system-architecture.md) §4, không lặp lại ở đây.

| Hạng mục | Nội dung |
| --- | --- |
| Kiến trúc (một DB chung, DB riêng theo module, đọc/ghi tách…) |  |
| Hệ quản trị | Xem [system-architecture](system-architecture.md) §4 |
| Instance theo môi trường | Xem [deployment](../05-operations/deployment.md) §3 |
| Vai trò của database (nguồn dữ liệu chính, cache, báo cáo…) |  |

## 2. Quy ước thiết kế
Quy ước đặt tên chung cho mã nguồn ở [coding-standards](../03-engineering/coding-standards.md) §4. Quy ước đặt tên bảng, cột và các quy ước riêng cho database do mục này sở hữu.

| Hạng mục | Quy ước |
| --- | --- |
| Đặt tên (bảng, cột, index, constraint) |  |
| Kiểu dữ liệu chuẩn (tiền, ngày giờ, văn bản, enum) |  |
| Khoá chính (auto-increment, UUID…) |  |
| Khoá ngoại (hành vi khi xoá/cập nhật) |  |
| Cột audit (người/thời điểm tạo, sửa) |  |
| Xoá mềm (soft delete) |  |
| Timestamp và múi giờ |  |
| Bảng mã, collation |  |
| Công cụ migration, thư mục, cách đặt tên file |  |
| Tài khoản CSDL (owner, migrator, app, read-only) |  |
| Quy ước riêng của hệ quản trị đã chốt (nếu có) |  |

## 3. Mô hình dữ liệu
Hệ quản trị đã chốt ở [system-architecture](system-architecture.md) §4; chọn hoặc đổi hệ quản trị cần ADR. Thuật ngữ trong file này theo CSDL quan hệ (bảng, cột, FK); CSDL tài liệu ánh xạ bảng → collection, cột → field, và ghi ở §3.3 cấu trúc document, §3.5 cách nhúng hay tham chiếu kèm lý do.

### 3.1 ERD / mô hình dữ liệu
Mô hình khái niệm và logic: thực thể chính và quan hệ. Mỗi thực thể thuộc một module sở hữu ([module-design](module-design.md)).
<!-- Điền theo từng dự án: sơ đồ (Mermaid hoặc ảnh trong repo) -->

### 3.2 Danh sách bảng
| Bảng | Module sở hữu | Mục đích | Khoá / ràng buộc | Dữ liệu nhạy cảm (D2/D3) |
| --- | --- | --- | --- | --- |
|  | | | | |

### 3.3 Chi tiết bảng
Chỉ mô tả bảng quan trọng hoặc có logic đặc biệt; bảng đơn giản để schema/migration trong mã nguồn làm nguồn chuẩn.

#### [Tên bảng]
| Cột | Kiểu | PK | FK | Null | Mặc định | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |

### 3.4 Mẫu truy cập và khối lượng
Mỗi index, partition hay phi chuẩn hoá phải truy ra một mẫu truy cập `AP-NN` ở đây.

| AP | Mô tả | Đọc/Ghi | Điều kiện lọc | Sắp xếp / phân trang | Tần suất | Độ trễ mục tiêu (NFR) |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |

| Bảng | Số dòng hiện tại | Tăng trưởng / tháng | Ước tính sau 3 năm | Ghi chú (điểm nóng ghi, tỉ lệ đọc/ghi) |
| --- | --- | --- | --- | --- |
|  | | | | |

### 3.5 Quan hệ, ràng buộc, index
| Loại | Bảng · Cột | Mục đích / BR / AP phục vụ |
| --- | --- | --- |
| Quan hệ (FK, hành vi xoá/cập nhật) |  | |
| Ràng buộc (check, unique) |  | |
| Index |  | |

Ràng buộc phản ánh business rule thì ghi mã `BR-<MODULE>-<NN>`, nội dung ở [business-rules](../01-requirements/business-rules.md).

### 3.6 Mở rộng (partition, lưu trữ, bản sao đọc, tách CSDL, sharding)
Chỉ ghi khi đã áp dụng; mỗi quyết định có ADR.

| Biện pháp | Bảng | Khoá (phân vùng / shard) | Lý do (AP, số liệu) | Hệ quả (ràng buộc, vận hành) | ADR |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |

### 3.7 Cache
Ngưỡng của dự án để xét điều kiện "thay đổi liên tục" và "ít được đọc" của Rule `cache`:

| Ngưỡng | Giá trị |
| --- | --- |
| Tỉ lệ đọc/ghi tối thiểu để được cache |  |
| Số lượt đọc tối thiểu trong một khoảng TTL |  |

<!-- Điền theo từng dự án -->

Chỉ ghi khi đã áp dụng; mỗi cache truy ra một AP ở §3.4 đã qua tối ưu truy vấn/index (§3.5) và ghi điều kiện được cache đã thoả thế nào. Quyết định kiến trúc (công nghệ cache, HA) ở [system-architecture](system-architecture.md) §7.

| Key mẫu | Module sở hữu | AP | Khoảng trễ chấp nhận | Mức dữ liệu | L1/L2 | Mô hình đọc/ghi | TTL từng tầng (jitter) | Sự kiện xoá key (mọi đường ghi) | Chống dồn tải (ghi "hot" nếu lock giữa instance) | Warm-up (W1/W2/không) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | | | | | |

Value chứa D3: ghi cách bảo vệ ở tầng cache và người duyệt Security. Công nghệ cache, quy ước key, trần kích thước value ghi ở đây nếu chưa có ở system-architecture §7.

Warm-up: trigger, timeout của W1, giới hạn N của W2, ngân sách tải CSDL (lô, đồng thời) và nơi snapshot hot list. Thứ tự chạy khi phát hành ghi ở [deployment](../05-operations/deployment.md) §9.

## 4. Vòng đời dữ liệu
| Giai đoạn | Quy tắc |
| --- | --- |
| Tạo |  |
| Cập nhật (lịch sử thay đổi) |  |
| Xoá (xoá mềm/cứng, xoá theo yêu cầu) |  |
| Lưu giữ (thời hạn, lưu trữ, huỷ) |  |

## 5. Bảo mật dữ liệu
Quy tắc bắt buộc về mức dữ liệu D0–D3, secret ở [security-standards](../03-engineering/security-standards.md); mục này chỉ áp dụng cho từng bảng/cột.

| Hạng mục | Quyết định |
| --- | --- |
| Cột nhạy cảm (liệt kê ở §3.2) |  |
| Mã hoá (lưu trữ, đường truyền) |  |
| Kiểm soát truy cập (tài khoản DB, quyền tối thiểu) |  |
| Che dữ liệu (masking) ở log, môi trường không phải production |  |

## 6. Transaction và đồng thời
Ranh giới transaction, mức cô lập, cách xử lý xung đột (khoá lạc quan/bi quan), idempotency cho thao tác có thể lặp.
<!-- Điền theo từng dự án -->

## 7. Migration và seed
Quy tắc viết migration (có thể quay lui, tương thích ngược khi deploy), thứ tự chạy, seed dữ liệu, dữ liệu test (giả/ẩn danh). Mức kiểm soát khi chạy migration production: xem [ai-governance](../03-engineering/ai-governance.md) §2. Quy trình triển khai migration xem [deployment](../05-operations/deployment.md) §9.
<!-- Điền theo từng dự án -->

## 8. Sao lưu và khôi phục
Xem [backup-recovery](../05-operations/backup-recovery.md). Thời hạn lưu giữ dữ liệu nghiệp vụ ở §4.
