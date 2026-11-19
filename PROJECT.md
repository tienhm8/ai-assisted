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
Chỉ ghi dòng dự án siết thấp hơn trần chung, hoặc danh mục việc hẹp được bật mức miễn duyệt từng Task. Để trống là dùng trần chung (khuyến nghị).
| Loại việc | Mức rủi ro | Mức tối đa | Lý do |
| --- | --- | --- | --- |
|  | | | |

### 2.2 Bản đồ vùng 🟢🟡🔴
| Vùng | Đường dẫn / loại file | Ghi chú |
| --- | --- | --- |
| 🟢 | | Ví dụ, sửa theo dự án: mã giao diện, test, tài liệu |
| 🟡 | | Ví dụ, sửa theo dự án: module chưa có test hoặc chưa có hồ sơ |
| 🔴 | Xác thực, phân quyền, thanh toán, migration, cấu hình CI | Ví dụ, sửa theo dự án: đường dẫn thật của các phần này; sửa cần Task riêng và người duyệt |
| 🔴 | `.ai/rules/`, `.ai/skills/`, `.ai/workflows/`, `.ai/templates/`, `.ai/agents/`, `.ai/guide/`, các file README trong `.ai/` | Rule, Skill, workflow của AI; sửa cần Task riêng và Tech Lead duyệt |
| 🟢 | `.ai/plans/` | Plan có bước duyệt riêng trước mọi Run |
| Không thuộc vùng nào, không commit | `.claude/worktrees/` | File sửa ở đây theo vùng của đường dẫn gốc |

## 3. Dữ liệu của dự án theo mức (công khai, nội bộ, nhạy cảm, bí mật)
Định nghĩa bốn mức ở [project-rules](.ai/rules/project-rules.md); cách xử lý theo mức (log, môi trường không phải production) ở [security-standards](docs/03-engineering/security-standards.md) §1.
| Mức | Dữ liệu của dự án | Được đưa vào AI |
| --- | --- | --- |
| Công khai | Ví dụ, sửa theo dự án: tài liệu giới thiệu, nội dung đã đăng | Có |
| Nội bộ | Ví dụ, sửa theo dự án: mã nguồn, tài liệu thiết kế, backlog | Có |
| Nhạy cảm | Ví dụ, sửa theo dự án: số liệu tài chính nội bộ, hợp đồng, quy trình nghiệp vụ chưa ẩn danh | Chỉ khi đã ẩn danh |
| Bí mật | Ví dụ, sửa theo dự án: khoá, token, mật khẩu, dữ liệu cá nhân, dữ liệu production | Không |

## 4. Độ nghiêm ngặt và mức ASVS
Định nghĩa ba độ nghiêm ngặt (gọn, chuẩn, nghiêm ngặt) và cách chọn ở [gates-and-rigor](.ai/guide/gates-and-rigor.md).
| Hạng mục | Giá trị |
| --- | --- |
| Độ nghiêm ngặt quy trình (gọn, chuẩn, nghiêm ngặt) | Chuẩn |
| Lý do chọn độ nghiêm ngặt | Khuyến nghị cho dự án nội bộ và gia công |
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

## 8. Công cụ AI
Cách nối công cụ với `.ai/` ở [ai-tools](.ai/guide/ai-tools.md); tên model và effort ở [ai-config.yaml](ai-config.yaml).

### 8.1 Công cụ dự án dùng
| Công cụ | Vai trò (chính / phụ) | Phiên bản | Dùng cho việc | Quyền được cấp (terminal, Git, browser, ...) |
| --- | --- | --- | --- | --- |
|  | | | | |

### 8.2 Công cụ cấp cho AI (MCP server, plugin)
Công cụ mà AI gọi được, ví dụ MCP server của Laravel Boost. Guideline đi kèm tiếp nhận theo [external-skills](.ai/guide/external-skills.md). Tính năng ghi dữ liệu hoặc chạy code tuỳ ý (ví dụ tinker, câu query ghi) xếp vào vùng 🟡/🔴 ở §2.2.
| Công cụ · phiên bản | Tính năng được dùng | Môi trường kết nối | Tính năng bị tắt / giới hạn | Người duyệt |
| --- | --- | --- | --- | --- |
|  | | | | |
