# PROJECT

> Khi có yêu cầu "tạo/cập nhật PROJECT.md cho dự án …" thì mới cập nhật.
> Việc cần làm theo thứ tự: [CHECKLIST.md](CHECKLIST.md). Giá trị khuyến nghị đã điền sẵn; mục nào đúng thì giữ.

> **Người quyết:** Tech Lead.
> 
> **Điều kiện duyệt:** Thông tin dự án đã điền.
> 
> **Mục đích:** Bản khai báo giá trị riêng của dự án: trần mức tự chủ, bản đồ vùng, dữ liệu theo mức, độ nghiêm ngặt, vai trò, tailoring và miễn trừ.

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |

## 1. Thông tin dự án
| Hạng mục | Nội dung |
| --- | --- |
| Tên dự án |  |
| Mô tả ngắn | Bối cảnh và mục tiêu xem [vision](docs/00-project-overview/vision.md) |
| Loại dự án | |
| Giai đoạn hiện tại | |
| Repository | |

## 2. Mức tự chủ và bản đồ vùng
Định nghĩa năm mức tự chủ (chỉ trả lời, chỉ đọc, duyệt từng bước, làm trọn Task, miễn duyệt từng Task), trần chung và nghĩa của ba vùng ở [project-rules](.ai/rules/project-rules.md).

### 2.1 Trần mức tự chủ của dự án
Chỉ ghi dòng dự án siết thấp hơn trần chung, hoặc danh mục việc hẹp được bật mức miễn duyệt từng Task. Để trống là dùng trần chung (khuyến nghị). Xem Autonomy mục Shared scales (Thang dùng chung) ở [project-rules](.ai/rules/project-rules.md).
Mặc định: full-task (trần chung)

### 2.2 Bản đồ vùng 🟢🟡🔴
Xem rule 8 của [project-rules](.ai/rules/project-rules.md). Mặc định không dưới bảng là: 🟢
| Vùng | Đường dẫn / loại file | Ghi chú |
| --- | --- | --- |
| 🟡 | | Ví dụ, sửa theo dự án: module chưa có test hoặc chưa có hồ sơ |
| 🔴 | Xác thực, phân quyền, thanh toán, migration, cấu hình CI | Ví dụ, sửa theo dự án: đường dẫn thật của các phần này; sửa cần Task riêng và người duyệt |
| 🔴 | `.ai/rules/`, `.ai/skills/`, `.ai/workflows/`, `.ai/templates/`, `.ai/agents/`, `.ai/guide/`, các file README trong `.ai/` | Rule, Skill, workflow của AI; sửa cần Task riêng và Tech Lead duyệt |

## 3. Dữ liệu của dự án theo mức (công khai, nội bộ, nhạy cảm, bí mật)
Xử lý dữ liệu theo mức ở [security-standards](docs/03-engineering/security-standards.md) §1.

Mặc định: Nhạy cảm

## 4. Độ nghiêm ngặt và mức ASVS
Xem "Độ nghiêm ngặt quy trình" ở [gates-and-rigor](.ai/guide/gates-and-rigor.md).

Mặc định: Chuẩn

## 5. Vai trò
Một người có thể giữ nhiều vai. Dự án không có khách hàng bên ngoài thì ghi "Không áp dụng" ở hai dòng cuối.
| Vai trò | Người đảm nhiệm |
| --- | --- |
| Tech Lead | |
| Product Owner (PO) | |
| Business Analyst (BA) | |
| Kiến trúc sư | |
| Security | |
| QA | |
| DevOps | |
| Owner | |
| Đại diện khách hàng | |
| Đầu mối với khách hàng | |

## 6. Lựa chọn áp dụng khung (Tailoring)
Ghi lý do khi gộp, bỏ hoặc đổi cách dùng tài liệu cho phù hợp quy mô dự án.
| Hạng mục | Lựa chọn | Lý do |
| --- | --- | --- |
| Phạm vi file AC | Một file hoặc đặt trong `FR/FR-<MODULE>.md` ([acceptance-criteria](docs/01-requirements/acceptance-criteria.md)) | |
| Tài liệu gộp / bỏ | | |

## 7. Miễn trừ (Waiver)
Miễn trừ có thời hạn một yêu cầu của khung. Ví dụ: chưa có CI/CD thì chạy cổng tự động cục bộ.
| Yêu cầu được miễn | Lý do | Người duyệt | Hết hạn | Kế hoạch khắc phục |
| --- | --- | --- | --- | --- |
|  | | | | |

## 8. Công cụ AI
Cách nối công cụ với `.ai/` ở [ai-tools](.ai/guide/ai-tools.md); tên model và effort ở [ai-config.yaml](ai-config.yaml).
