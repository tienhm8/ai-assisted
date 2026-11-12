# PROJECT

> Khi có yêu cầu "tạo/cập nhật PROJECT.md cho dự án …" thì mới cập nhật.

Người quyết: Tech Lead.
Điều kiện duyệt: Thông tin dự án, Công cụ AI đã điền.

> **Mục đích.** Hồ sơ riêng của dự án: công cụ AI, mức tự chủ, bản đồ vùng, mức dữ liệu, profile, vai trò, tailoring và miễn trừ. Chỉ khai báo lựa chọn của dự án, không chép lại quy tắc đã có ở `docs/` hoặc `.ai/`.

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
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
Công cụ mà AI gọi được, ví dụ MCP server của Laravel Boost. Guideline đi kèm công cụ không cài thẳng mà tiếp nhận theo [skills/README](.ai/skills/README.md) mục "Tiếp nhận Skill bên ngoài". Mỗi công cụ ghi rõ môi trường được kết nối; **không kết nối production hoặc dữ liệu D2/D3**. Tính năng ghi dữ liệu hoặc chạy code tuỳ ý (ví dụ tinker, câu query ghi) xếp vào vùng 🟡/🔴 ở §3.2.

| Công cụ · phiên bản | Tính năng được dùng | Môi trường kết nối | Tính năng bị tắt / giới hạn | Người duyệt |
| --- | --- | --- | --- | --- |
|  | | | | |

## 3. Mức tự chủ và bản đồ vùng

### 3.1 Mức tự chủ (A0–A4)
Nguồn chuẩn duy nhất của mức tự chủ. Mức tự chủ do từng Task cấp; mục này khai báo mức **tối đa** cho phép theo loại việc × rủi ro (R1–R3) của dự án. Vai ([.ai/agents/](.ai/agents/README.md)) không có mức riêng, chỉ lấy theo loại việc. Dự án chỉ được siết thêm so với mặc định bên dưới, không nới. Skill không tự nâng mức; thiếu thì dừng và hỏi.

**Định nghĩa (Draft, chờ Tech Lead duyệt):**
| Mức | AI được làm |
| --- | --- |
| A0 | Không thao tác; chỉ trả lời, giải thích |
| A1 | Chỉ đọc và báo cáo; không sửa file, không chạy lệnh có tác dụng phụ |
| A2 | Làm trong phạm vi Task, người duyệt từng bước trước khi sang bước sau |
| A3 | Làm hết Task trong phạm vi và worktree được cấp; người duyệt kết quả cuối (diff, bằng chứng test) |
| A4 | Như A3 nhưng không duyệt từng Task; chỉ cho danh mục việc hẹp đã được duyệt trước |

**Mặc định khung (trần; dự án chỉ siết thêm):**
| Loại việc | R1 | R2 | R3 |
| --- | --- | --- | --- |
| Phân tích, đề xuất, soạn tài liệu (gồm rà soát bảo mật và review code: chỉ khuyến nghị, không sửa code) | A3 | A3 | A3 (đầu ra luôn là Proposed/Draft) |
| Viết/sửa code tính năng, sửa lỗi, refactor | A3 | A3 | A2 |
| Viết test | A3 (A4*) | A3 | A3 |
| Deploy production, đổi secret, migration production, đổi RBAC | A0–A1, cần phê duyệt | A0–A1, cần phê duyệt | A0–A1, cần phê duyệt |

\* A4 mặc định tắt; chỉ bật cho danh mục việc hẹp do Tech Lead duyệt, ghi vào bảng dưới.

**Khai báo của dự án (siết thêm hoặc bật A4):**
| Loại việc | Mức tối đa |
| --- | --- |
|  | |

### 3.2 Bản đồ vùng 🟢🟡🔴
Phân vùng file/thư mục theo mức kiểm soát. Vùng 🔴 (ví dụ `.ai/`, cổng CI, cấu hình bảo mật) cần Task riêng và người duyệt.
| Vùng | Đường dẫn / loại file | Quy tắc |
| --- | --- | --- |
| 🟢 | | |
| 🟡 | | |
| 🔴 | | |

## 4. Mức dữ liệu (D0–D3)
Định nghĩa chung ở [glossary](docs/00-project-overview/glossary.md); quy tắc chi tiết ở [security-standards](docs/03-engineering/security-standards.md) §1. D3 gồm secret, token, dữ liệu cá nhân: không đưa vào AI, không ghi log.
| Mức | Dữ liệu của dự án | Được đưa vào AI |
| --- | --- | --- |
| D0 | | |
| D1 | | |
| D2 | | |
| D3 | | Không |

## 5. Profile và mức nghiêm ngặt
| Hạng mục | Giá trị |
| --- | --- |
| Profile áp dụng | |
| Mức nghiêm ngặt (S1–S3) | |
| Lý do chọn | |
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

## 7. Lựa chọn áp dụng khung
Ghi lý do khi gộp, bỏ hoặc đổi cách dùng tài liệu cho phù hợp quy mô dự án.
| Hạng mục | Lựa chọn | Lý do |
| --- | --- | --- |
| Phạm vi file AC | Một file hoặc đặt trong `FR/FR-<MODULE>.md` ([acceptance-criteria](docs/01-requirements/acceptance-criteria.md)) | |
| Tài liệu gộp / bỏ | | |

## 8. Miễn trừ (Waiver)
Miễn trừ có thời hạn một yêu cầu của khung; không bỏ qua âm thầm. Ví dụ: chưa có CI/CD thì chạy cổng tự động cục bộ.
| Yêu cầu được miễn | Lý do | Người duyệt | Hết hạn | Kế hoạch khắc phục |
| --- | --- | --- | --- | --- |
|  | | | | |

**Hotfix khẩn cấp** (áp dụng [release-workflow](.ai/workflows/release-workflow.md)):

| Hạng mục | Giá trị |
| --- | --- |
| Thời hạn bổ sung hồ sơ sau hotfix | |
| Người duyệt hotfix | |
