---
name: architecture-design
description: Thiết kế và đánh giá kiến trúc phần mềm (ranh giới hệ thống, module, luồng dữ liệu, bảo mật, quyết định công nghệ) dựa trên yêu cầu đã duyệt; ghi vào tài liệu kiến trúc và ADR.
---

# Architecture Design Skill

## 1. Mục tiêu

Đề xuất kiến trúc dễ bảo trì, an toàn, kiểm thử được, đáp ứng yêu cầu đã duyệt. AI chỉ soạn ở trạng thái Draft.

## 2. Cổng vào

Cần FR đã qua cổng (mỗi FR có AC) và BR, NFR liên quan. Chưa đạt thì dừng, ghi open-questions.md (`OQ-NN`) và báo lại.

## 3. Đầu vào

Vision, phạm vi, FR/BR/NFR đã duyệt, kiến trúc hiện có, ngăn xếp công nghệ đã chốt, yêu cầu bảo mật. Database design và API spec chỉ đọc "nếu đã có" (chúng là đầu ra ở bước sau).

## 4. Quy trình

1. **Phân tích yêu cầu:** năng lực nghiệp vụ, actor, thuộc tính chất lượng, tích hợp, ràng buộc kỹ thuật.
2. **Ranh giới hệ thống:** ứng dụng, module, dịch vụ ngoài, trust boundary, chủ sở hữu dữ liệu.
3. **Phong cách kiến trúc:** chọn phương án đơn giản nhất đáp ứng yêu cầu; không thêm độ phức tạp thừa; microservices phải có lý do.
4. **Module:** với mỗi module nêu trách nhiệm, đầu vào/ra, phụ thuộc, dữ liệu sở hữu, giao diện, ranh giới lỗi, và các FR phục vụ. Ghi thành bảng ở module-design.md.
5. **Luồng dữ liệu:** request, xác thực, phân quyền, xử lý nghiệp vụ, truy cập dữ liệu, tích hợp ngoài, xử lý lỗi.
6. **Ranh giới bảo mật:** xác thực, thực thi phân quyền, quyền dịch vụ, truy cập dữ liệu, dữ liệu nhạy cảm.
7. **Đánh giá chất lượng:** bảo trì, module hoá, tin cậy, hiệu năng, mở rộng, bảo mật, quan sát, kiểm thử.
8. **ADR:** quyết định lớn tạo ADR từ `_template.md` thành `ADR-<NNNN>-<slug>.md`, trạng thái Proposed, thêm vào danh mục ADR. Tài liệu thiết kế khác chỉ ghi kết quả và trỏ `ADR-<NNNN>`.
9. **Rà soát kiến trúc hiện có** (chỉ dự án đã có code): vi phạm ranh giới, phụ thuộc vòng, trách nhiệm trùng, coupling thừa, rủi ro mở rộng và bảo mật.

## 5. Checklist

- [ ] Đầu ra ghi trực tiếp vào system-architecture.md (bối cảnh, thành phần, luồng, bảo mật), module-design.md (module và FR phục vụ), api-design.md (nếu thuộc phạm vi) và ADR; không tạo báo cáo kiến trúc song song.
- [ ] Mỗi module truy ra được FR; ranh giới, sở hữu dữ liệu và ranh giới bảo mật rõ.
- [ ] Quyết định lớn đã có ADR (Proposed) trong danh mục.

## 6. Việc không được làm

- Kiến trúc đã Approved không tự đổi; chỉ đề xuất thay đổi qua ADR mới.
- Đổi kiến trúc hoặc RBAC phải được duyệt trước khi triển khai.
- Không đổi công nghệ đã chốt, không vượt ranh giới module, không tự quyết vấn đề nghiệp vụ chưa rõ.

## 7. Tiêu chí hoàn thành (DoD)

- Checklist ở mục 5 đạt; đầu ra ở trạng thái Draft.
- Người duyệt: Kiến trúc sư; thêm Security nếu đụng tiền, phân quyền, dữ liệu cá nhân hoặc migration. Chỉ họ chuyển sang Approved.

## 8. Báo cáo bàn giao

Nêu: file đã sửa, module ảnh hưởng, ADR đã tạo, đánh đổi và rủi ro, người cần duyệt. Không lặp lại nội dung tài liệu.
