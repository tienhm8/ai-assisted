---
name: requirement-review
description: Rà soát yêu cầu về tính đầy đủ, rõ ràng, nhất quán, kiểm thử được và truy vết được trước khi thiết kế/triển khai; chỉ khuyến nghị, không đổi trạng thái hay sửa tài liệu.
---

# Requirement Review Skill

## 1. Mục tiêu

Tìm lỗ hổng, mâu thuẫn, điểm mơ hồ và rủi ro trong yêu cầu. Skill chỉ **đề xuất trong báo cáo**: không sửa trực tiếp file yêu cầu, không đổi trạng thái, không duyệt thay stakeholder.

## 2. Cổng vào

- Có tài liệu yêu cầu cần rà (BRD, bảng FR, AC) ở trạng thái Draft hoặc In Review. Thiếu thì dừng và hỏi.

## 3. Đầu vào

BRD, bảng FR, business-rules.md, NFR.md, acceptance-criteria.md, phạm vi, glossary, open-questions.md, và tài liệu kiến trúc liên quan (nếu có).

## 4. Quy trình

1. **Đầy đủ:** luồng chính, thay thế, lỗi; validate đầu vào; kết quả đầu ra; quyền; sở hữu dữ liệu; chuyển trạng thái; xử lý lỗi.
2. **Rõ ràng:** câu không mơ hồ, thuật ngữ khớp glossary, actor rõ, ràng buộc đo được.
3. **Nhất quán:** FR với BR, FR với NFR, với phạm vi, với phân quyền, với quyết định đã có, giữa các FR.
4. **Kiểm thử được:** AC quan sát được, có điều kiện đầu và kết quả, có biên và luồng lỗi.
5. **Truy vết (một chiều):** mỗi FR có liên kết BRQ/BR; mỗi AC trỏ FR; mọi BR có AC. Báo lỗi nếu tài liệu khai báo liên kết hai chiều.
6. **Open-questions:** OQ trạng thái Open chặn phạm vi nào; giả định đã hết hạn rà soát; điểm mơ hồ phát hiện được mà chưa có OQ.
7. **Khả thi:** chỉ đánh dấu rủi ro (kỹ thuật, tích hợp, dữ liệu, hiệu năng, bảo mật) rồi chuyển architecture-design; không quyết định kiến trúc.
8. **Phân loại:** Critical (chặn triển khai) · High (thiếu/mâu thuẫn lớn) · Medium (chưa rõ) · Low (cải thiện tài liệu).

## 5. Checklist

- [ ] Đầy đủ, rõ ràng, nhất quán, kiểm thử được, truy vết một chiều (xem các bước ở mục 4).
- [ ] Mọi FR có AC; mọi BR có AC.
- [ ] Không còn OQ Open chặn phạm vi chưa được nêu trong báo cáo.

## 6. Việc không được làm

- Không viết lại yêu cầu đã Approved, không biến giả định thành yêu cầu, không bịa hành vi nghiệp vụ.
- Giữ nguyên ID yêu cầu.

## 7. Tiêu chí hoàn thành (DoD)

Mọi mục ở §3 đã được kiểm, mọi finding đủ trường ở §5, báo cáo nêu rõ khuyến nghị và điều kiện chưa đạt.

## 8. Báo cáo bàn giao (báo cáo rà soát)

Một báo cáo duy nhất gồm: tóm tắt (số yêu cầu đã rà, số finding theo mức), danh sách finding, vấn đề chặn, khuyến nghị duyệt.

Mỗi finding: mã finding `FND-NN` (chỉ dùng trong báo cáo này), mức độ, ID yêu cầu liên quan (FR/BR/AC/NFR/OQ), mô tả, tác động, đề xuất sửa.

**Khuyến nghị duyệt** dựa trên điều kiện: mọi FR có AC; QA đã rà; OQ đã ghi đầy đủ và không còn OQ Open chặn phạm vi. Đây chỉ là khuyến nghị; người có thẩm quyền mới duyệt.
