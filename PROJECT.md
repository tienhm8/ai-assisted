# PROJECT

> Khi có yêu cầu "tạo/cập nhật PROJECT.md cho dự án …" thì mới cập nhật.

Người quyết: Tech Lead.
Điều kiện duyệt: Thông tin dự án, Công cụ AI đã điền.

> **Mục đích.** Bản khai báo giá trị riêng của dự án: công cụ AI, trần mức tự chủ, bản đồ vùng, dữ liệu theo mức, độ nghiêm ngặt, vai trò, tailoring và miễn trừ. Không định nghĩa thang, không chứa quy tắc: định nghĩa và điều bắt buộc ở `.ai/rules/`, chuẩn kỹ thuật ở `docs/`.

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

## 2. Công cụ AI
Công cụ chính chỉ chọn một; công cụ khác dùng cho việc chuyên biệt. Rule và Skill ở `.ai/`, mỗi công cụ chỉ có file tích hợp mỏng trỏ về đó.

| Công cụ | Vai trò (chính / phụ) | Phiên bản | Dùng cho việc | Quyền được cấp (terminal, Git, browser, ...) |
| --- | --- | --- | --- | --- |
|  | | | | |

### 2.1 Công cụ cấp cho AI (MCP server, plugin)
Công cụ mà AI gọi được, ví dụ MCP server của Laravel Boost. Guideline đi kèm công cụ không cài thẳng mà tiếp nhận theo [skills/README](.ai/skills/README.md) mục "Tiếp nhận Skill bên ngoài". Mỗi công cụ ghi rõ môi trường được kết nối và tính năng bị tắt. Tính năng ghi dữ liệu hoặc chạy code tuỳ ý (ví dụ tinker, câu query ghi) xếp vào vùng 🟡/🔴 ở §3.2.

| Công cụ · phiên bản | Tính năng được dùng | Môi trường kết nối | Tính năng bị tắt / giới hạn | Người duyệt |
| --- | --- | --- | --- | --- |
|  | | | | |

## 3. Mức tự chủ và bản đồ vùng
Định nghĩa A0–A4, trần mặc định và nghĩa của ba vùng ở [project-rules](.ai/rules/project-rules.md).

### 3.1 Trần mức tự chủ của dự án
Chỉ ghi dòng dự án siết thấp hơn trần mặc định, hoặc danh mục việc hẹp được bật A4. Để trống là dùng trần mặc định.
| Loại việc | Mức rủi ro | Mức tối đa | Lý do |
| --- | --- | --- | --- |
|  | | | |

### 3.2 Bản đồ vùng 🟢🟡🔴
Phân vùng file/thư mục theo mức kiểm soát. Ví dụ vùng 🔴: `.ai/`, cổng CI, cấu hình bảo mật.
| Vùng | Đường dẫn / loại file | Ghi chú |
| --- | --- | --- |
| 🟢 | | |
| 🟡 | | |
| 🔴 | | |

## 4. Dữ liệu của dự án theo mức (D0–D3)
Định nghĩa D0–D3 ở [project-rules](.ai/rules/project-rules.md); cách xử lý theo mức (log, môi trường không phải production) ở [security-standards](docs/03-engineering/security-standards.md) §1.
| Mức | Dữ liệu của dự án | Được đưa vào AI |
| --- | --- | --- |
| D0 | | |
| D1 | | |
| D2 | | |
| D3 | | Không |

## 5. Độ nghiêm ngặt và mức ASVS
Định nghĩa S1–S3 và cách chọn ở [gates-and-rigor](docs/04-project-management/gates-and-rigor.md).
| Hạng mục | Giá trị |
| --- | --- |
| Độ nghiêm ngặt quy trình (S1–S3) | |
| Lý do chọn S | Theo loại dự án (§1), quy mô, yêu cầu pháp lý hoặc hợp đồng |
| Mức ASVS mục tiêu (L1–L3) | Không thấp hơn mức tối thiểu ở [security-standards](docs/03-engineering/security-standards.md) §13.1 |
| Lý do chọn mức ASVS | Theo mức dữ liệu (§4), có tài khoản/phân quyền, tiền, ràng buộc pháp lý |

## 6. Vai trò
| Vai trò | Người đảm nhiệm |
| --- | --- |
| Tech Lead | |
| Product Owner (PO) | |
| Business Analyst (BA) | |
| Kiến trúc sư | |
| Security | |
| QA | |
| DevOps | |
| Owner (người quyết phát hành) | |

## 7. Lựa chọn áp dụng khung (Tailoring)
Ghi lý do khi gộp, bỏ hoặc đổi cách dùng tài liệu cho phù hợp quy mô dự án.
| Hạng mục | Lựa chọn | Lý do |
| --- | --- | --- |
| Phạm vi file AC | Một file hoặc đặt trong `FR/FR-<MODULE>.md` ([acceptance-criteria](docs/01-requirements/acceptance-criteria.md)) | |
| Tài liệu gộp / bỏ | | |

## 8. Miễn trừ (Waiver)
Miễn trừ có thời hạn một yêu cầu của khung. Ví dụ: chưa có CI/CD thì chạy cổng tự động cục bộ.
| Yêu cầu được miễn | Lý do | Người duyệt | Hết hạn | Kế hoạch khắc phục |
| --- | --- | --- | --- | --- |
|  | | | | |
