---
name: architecture-design
description: Thiết kế và đánh giá kiến trúc phần mềm (ranh giới hệ thống, module, luồng dữ liệu, bảo mật, quyết định công nghệ) dựa trên yêu cầu đã duyệt; ghi vào tài liệu kiến trúc và ADR.
---

# Architecture Design Skill

Đề xuất kiến trúc đơn giản nhất đáp ứng yêu cầu đã duyệt: dễ bảo trì, an toàn, kiểm thử được.

## Cổng vào

FR đã có AC, kèm BR và NFR liên quan. Chưa đạt thì dừng và ghi câu hỏi mở.

Đọc: vision, scope, FR/BR/NFR; kiến trúc hiện có, công nghệ đã chốt, yêu cầu bảo mật. database-design và api-design chỉ đọc nếu đã có.

## Quy trình

1. **Phân tích yêu cầu:** năng lực nghiệp vụ, actor, thuộc tính chất lượng, tích hợp, ràng buộc kỹ thuật.
2. **Ranh giới hệ thống:** ứng dụng, module, dịch vụ ngoài, trust boundary, chủ sở hữu dữ liệu.
3. **Phong cách kiến trúc:** chọn phương án đơn giản nhất đáp ứng yêu cầu; phương án phân tán phải có lý do từ NFR.
4. **Module:** trách nhiệm, đầu vào/ra, phụ thuộc, dữ liệu sở hữu, giao diện, ranh giới lỗi, FR phục vụ. Ghi thành bảng ở module-design.
5. **Luồng dữ liệu:** request, xác thực, phân quyền, xử lý nghiệp vụ, truy cập dữ liệu, tích hợp ngoài, xử lý lỗi.
6. **Ranh giới bảo mật:** xác thực, nơi thực thi phân quyền, quyền của dịch vụ, dữ liệu nhạy cảm.
7. **Đánh giá chất lượng:** bảo trì, tin cậy, hiệu năng, mở rộng, bảo mật, quan sát, kiểm thử.
8. **ADR:** mỗi quyết định lớn tạo `ADR-<NNNN>-<slug>.md` từ `_template.md`, trạng thái Proposed, thêm vào danh mục ADR. Tài liệu thiết kế chỉ ghi kết quả và nêu mã ADR.
9. **Rà kiến trúc hiện có** (dự án đã có code): vi phạm ranh giới, phụ thuộc vòng, trách nhiệm trùng, coupling thừa.

## Giới hạn

- Không đổi công nghệ đã chốt.
- Ghi thẳng vào system-architecture, module-design, api-design; không tạo báo cáo kiến trúc song song.

## Hoàn thành khi

- Mỗi module truy ra được FR; ranh giới, sở hữu dữ liệu và ranh giới bảo mật rõ.
- Quyết định lớn có ADR Proposed trong danh mục.
- Người duyệt: Kiến trúc sư; thêm Security nếu đụng tiền, phân quyền, dữ liệu cá nhân hoặc migration.

## Báo cáo

File đã sửa, module ảnh hưởng, ADR đã tạo, đánh đổi và rủi ro, người cần duyệt. Không lặp nội dung tài liệu.
