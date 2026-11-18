# PROJECT

> Khi có yêu cầu "tạo/cập nhật PROJECT.md cho dự án …" thì mới cập nhật.

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
Định nghĩa A0–A4, trần mặc định và nghĩa của ba vùng ở [project-rules](.ai/rules/project-rules.md).

### 2.1 Trần mức tự chủ của dự án
Chỉ ghi dòng dự án siết thấp hơn trần mặc định, hoặc danh mục việc hẹp được bật A4. Để trống là dùng trần mặc định.
| Loại việc | Mức rủi ro | Mức tối đa | Lý do |
| --- | --- | --- | --- |
|  | | | |

### 2.2 Bản đồ vùng 🟢🟡🔴
| Vùng | Đường dẫn / loại file | Ghi chú |
| --- | --- | --- |
| 🟢 | | |
| 🟡 | | |
| 🔴 | `.ai/` | Rule, Skill, workflow của AI; sửa cần Task riêng và Tech Lead duyệt |

## 3. Dữ liệu của dự án theo mức (D0–D3)
Định nghĩa D0–D3 ở [project-rules](.ai/rules/project-rules.md); cách xử lý theo mức (log, môi trường không phải production) ở [security-standards](docs/03-engineering/security-standards.md) §1.
| Mức | Dữ liệu của dự án | Được đưa vào AI |
| --- | --- | --- |
| D0 | | |
| D1 | | |
| D2 | | |
| D3 | | Không |

## 4. Độ nghiêm ngặt và mức ASVS
Định nghĩa S1–S3 và cách chọn ở [gates-and-rigor](docs/04-project-management/gates-and-rigor.md).
| Hạng mục | Giá trị |
| --- | --- |
| Độ nghiêm ngặt quy trình (S1–S3) | Chọn theo [gates-and-rigor](docs/04-project-management/gates-and-rigor.md) §2 (bảng "Chọn mức nào?") |
| Lý do chọn S | Theo loại dự án (§1), quy mô, yêu cầu pháp lý hoặc hợp đồng |
| Mức ASVS mục tiêu (L1–L3) | Không thấp hơn mức tối thiểu ở [security-standards](docs/03-engineering/security-standards.md) §13.1 |
| Lý do chọn mức ASVS | Theo mức dữ liệu (§3), có tài khoản/phân quyền, tiền, ràng buộc pháp lý |

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
| Owner (người quyết phát hành) | |
| Đại diện khách hàng (cung cấp tài liệu nguồn, trả lời câu hỏi, duyệt tài liệu được gửi sang; không trực tiếp chuyển trạng thái tài liệu trong repo) | |
| Đầu mối với khách hàng (nhận gói câu hỏi từ AI, gửi tài liệu cho khách hàng duyệt, lưu câu trả lời và kết quả duyệt; chỉ chuyển `Approved` khi khách hàng đã duyệt; thường là BA) | |

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
