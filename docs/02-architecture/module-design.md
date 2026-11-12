# Module Design

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt | Kiến trúc sư |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | system-architecture.md, database-design.md, api-design.md, ../01-requirements/FR/, ../01-requirements/business-rules.md, ../03-engineering/error-handling.md, ADR/, ../../.ai/rules/architecture-rules.md, ../../.ai/skills/backend-development/SKILL.md |

> **Mục đích.** Module Architecture: chia module, trách nhiệm, API nội bộ và chiều phụ thuộc.

## 1. Tổng quan module

### 1.1 Cách phân loại
Chia theo domain hoặc năng lực nghiệp vụ. Mã `<MODULE>` dùng thống nhất với `FR-<MODULE>-<NN>` và `BR-<MODULE>-<NN>`.
<!-- Điền theo từng dự án -->

### 1.2 Danh sách module
| Mã module | Tên | Trách nhiệm | Phụ thuộc | FR phục vụ | Chủ module |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |

Ưu tiên không ghi ở đây: ưu tiên yêu cầu theo MoSCoW ở [FR](../01-requirements/FR/README.md), thứ tự làm ở [backlog](../04-project-management/backlog.md) và [roadmap](../04-project-management/roadmap.md).

## 2. Chi tiết module
Lặp lại mẫu dưới đây cho từng module. Module nhỏ chỉ cần điền các dòng có nội dung; không viết lại nội dung đã có ở tài liệu khác, chỉ dẫn mã và liên kết.

### 2.1 [Mã module] · [Tên module]

| Hạng mục | Nội dung |
| --- | --- |
| Mục đích và trách nhiệm chính |  |
| Phạm vi (làm / không làm) |  |
| Năng lực nghiệp vụ |  |
| FR liên quan | `FR-<MODULE>-<NN>`; yêu cầu ở [FR](../01-requirements/FR/README.md) |
| Business rule áp dụng | `BR-<MODULE>-<NN>`; nội dung ở [business-rules](../01-requirements/business-rules.md), không chép lại |
| Thành phần bên trong |  |
| Dữ liệu sở hữu | Chỉ ghi tại [database-design](database-design.md) §3.2 (cột "Module sở hữu"); mỗi bảng chỉ một module sở hữu |
| Interface cung cấp | API công khai ở [api-design](api-design.md) §1; interface liên module: tên và mục đích nêu tại đây, hợp đồng chi tiết ở [api-design](api-design.md) §2 |
| Phụ thuộc | Module hoặc hệ thống ngoài |
| Xử lý lỗi | Lỗi đặc thù của module; quy ước chung ở [error-handling](../03-engineering/error-handling.md) |
| Phân quyền và bảo mật | Quyền cần có, dữ liệu nhạy cảm; thiết kế chung ở [system-architecture](system-architecture.md) §6 |

## 3. Phụ thuộc giữa các module

### 3.1 Ma trận phụ thuộc
Hàng phụ thuộc cột. Đánh dấu `S` (gọi đồng bộ), `A` (bất đồng bộ/sự kiện), `D` (đọc chung dữ liệu, cần giải thích).
| Module | M1 | M2 | M3 |
| --- | --- | --- | --- |
| M1 | – | | |
| M2 | | – | |
| M3 | | | – |

### 3.2 Sơ đồ phụ thuộc
<!-- Sơ đồ (Mermaid hoặc ảnh trong repo) -->

### 3.3 Quy tắc phụ thuộc
Chiều phụ thuộc cho phép, cấm vòng phụ thuộc, cấm truy cập trực tiếp dữ liệu của module khác. Ngoại lệ phải có ADR.
<!-- Điền theo từng dự án -->

## 4. Giao tiếp giữa các module
| Kiểu | Khi dùng | Quy ước |
| --- | --- | --- |
| Đồng bộ (gọi interface nội bộ) |  | |
| Bất đồng bộ / sự kiện |  | |

Mẫu giao tiếp mức hệ thống ở [system-architecture](system-architecture.md) §5.2; đặc tả từng điểm tích hợp (hệ thống ngoài và liên module) ở [api-design](api-design.md) §2.

## 5. Ranh giới và quyền sở hữu
Quy tắc nghiệp vụ thuộc module nào (dữ liệu: xem [database-design](database-design.md) §3.2); ai quyết khi thay đổi vượt ranh giới. Thay đổi ranh giới giữa module phải có ADR tại [ADR/](ADR/).
<!-- Điền theo từng dự án -->
