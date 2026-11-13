# System Architecture

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt (dự án) | Kiến trúc sư |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | module-design.md, database-design.md, api-design.md, ADR/, ../00-project-overview/vision.md, ../00-project-overview/scope.md, ../00-project-overview/open-questions.md, ../01-requirements/NFR.md, ../03-engineering/security-standards.md, ../03-engineering/error-handling.md, ../05-operations/monitoring.md, ../05-operations/deployment.md, ../../.ai/rules/architecture-rules.md, ../../.ai/skills/architecture-design/SKILL.md |

> **Mục đích.** Kiến trúc tổng thể, ranh giới, chiều phụ thuộc, tích hợp ngoài, thiết kế Authentication & Authorization. Người quyết và điều kiện sẵn sàng build: xem [README](README.md).

## 1. Tổng quan hệ thống

### 1.1 Mô tả và bối cảnh
Tóm tắt 3–5 dòng hệ thống làm gì về mặt kỹ thuật. Bối cảnh nghiệp vụ và mục tiêu xem [vision](../00-project-overview/vision.md), không chép lại.
<!-- Điền theo từng dự án -->

### 1.2 Ranh giới hệ thống
Actor, hệ thống ngoài, và thành phần nằm ngoài hệ thống. Phạm vi nghiệp vụ trong/ngoài xem [scope](../00-project-overview/scope.md); mục này chỉ vẽ ranh giới kỹ thuật.
<!-- Điền theo từng dự án -->

## 2. Architecture Drivers

### 2.1 Yêu cầu chức năng quan trọng
FR có ảnh hưởng lớn tới kiến trúc (không liệt kê toàn bộ FR).
| FR | Ảnh hưởng tới kiến trúc |
| --- | --- |
|  | |

### 2.2 Yêu cầu phi chức năng quan trọng
NFR quyết định lựa chọn kiến trúc (hiệu năng, mở rộng, sẵn sàng, bảo mật, bảo trì). Nội dung và chỉ tiêu ở [NFR](../01-requirements/NFR.md), chỉ nêu mã `NFR-<NN>` và cách kiến trúc đáp ứng.
| NFR | Cách kiến trúc đáp ứng |
| --- | --- |
|  | |

### 2.3 Ràng buộc kỹ thuật
Ràng buộc công nghệ, hạ tầng ảnh hưởng thiết kế. Ràng buộc pháp lý, hợp đồng, ngân sách xem [scope](../00-project-overview/scope.md) §3.
<!-- Điền theo từng dự án -->

## 3. Kiến trúc tổng thể

### 3.1 Phong cách kiến trúc
Ví dụ: Monolith, Modular Monolith, Microservices, Event-driven. Lý do chọn ghi thành ADR.
<!-- Điền theo từng dự án -->

### 3.2 Sơ đồ kiến trúc
<!-- Điền theo từng dự án: sơ đồ tổng thể (Mermaid hoặc ảnh trong repo) -->

### 3.3 Các tầng và trách nhiệm
| Tầng | Trách nhiệm | Được phụ thuộc vào |
| --- | --- | --- |
|  | | |

### 3.4 Thành phần chính
Thành phần và ranh giới ở mức hệ thống. Chia module chi tiết ở [module-design](module-design.md).
| Thành phần | Trách nhiệm | Phụ thuộc |
| --- | --- | --- |
|  | | |

## 4. Stack và phiên bản
| Lớp | Công nghệ | Phiên bản | Mục đích |
| --- | --- | --- | --- |
|  | | | |

## 5. Tương tác hệ thống

### 5.1 Hệ thống ngoài
Danh sách hệ thống ngoài và hướng tích hợp. Đặc tả chi tiết (giao thức, xác thực, retry) ở [api-design](api-design.md) §2.
| Hệ thống | Hướng | Mục đích |
| --- | --- | --- |
|  | | |

### 5.2 Mẫu giao tiếp
Đồng bộ (REST/RPC), bất đồng bộ (queue, event), batch.
<!-- Điền theo từng dự án -->

### 5.3 Luồng dữ liệu chính
<!-- Điền theo từng dự án -->

## 6. Authentication & Authorization (thiết kế)
Cơ chế xác thực, mô hình phân quyền (vai trò, quyền, phạm vi dữ liệu), vòng đời phiên/token. Quy tắc bắt buộc ở [security-standards](../03-engineering/security-standards.md) §3–§4. Giá trị cụ thể (thời hạn phiên/token, ngưỡng khoá tài khoản, cookie flag) ghi tại security-standards §3, không lặp lại ở đây; chọn cơ chế khác mặc định thì có ADR.
<!-- Điền theo từng dự án -->

## 7. Cross-cutting Concerns
Chỉ ghi quyết định kiến trúc áp dụng toàn hệ thống; quy tắc chi tiết nằm ở tài liệu chuẩn.
| Mối quan tâm | Quyết định kiến trúc | Quy tắc chi tiết |
| --- | --- | --- |
| Logging |  | [error-handling](../03-engineering/error-handling.md) §7 |
| Monitoring |  | [monitoring](../05-operations/monitoring.md) |
| Triển khai |  | [deployment](../05-operations/deployment.md) |
| Xử lý lỗi |  | [error-handling](../03-engineering/error-handling.md) |
| Caching |  | [database-design](database-design.md) §3.7 |
| Quản lý transaction |  | [database-design](database-design.md) §6 |

## 8. Threat model (bắt buộc khi thiết kế đụng tới tiền, phân quyền, dữ liệu cá nhân, migration)
Ai làm được gì, lạm dụng thế nào, chặn bằng gì.
<!-- Điền theo từng dự án -->

## 9. Giả định và ràng buộc kiến trúc
Giả định chưa kiểm chứng đặt kèm cách xác nhận; giả định chưa rõ ghi vào [open-questions](../00-project-overview/open-questions.md).
<!-- Điền theo từng dự án -->

## 10. Quyết định liên quan
Danh mục ADR chỉ duy trì tại [ADR/README.md](ADR/README.md#danh-mục-adr), không liệt kê lại ở đây. Ở các mục trên, chỗ nào có quyết định lớn thì ghi kết quả và trỏ về `ADR-<NNNN>`.
