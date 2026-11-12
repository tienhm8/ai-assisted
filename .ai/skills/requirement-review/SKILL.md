---
name: requirement-review
description: Rà soát yêu cầu về tính đầy đủ, rõ ràng, nhất quán, kiểm thử được và truy vết được trước khi thiết kế/triển khai; chỉ khuyến nghị, không đổi trạng thái hay sửa tài liệu.
---

# Requirement Review Skill

Tìm lỗ hổng, mâu thuẫn, điểm mơ hồ và rủi ro trong yêu cầu. Chỉ đề xuất trong báo cáo: không sửa file yêu cầu.

## Cổng vào

Có tài liệu yêu cầu cần rà (BRD, bảng FR, AC) ở Draft hoặc In Review. Thiếu thì dừng và hỏi.

Đọc: BRD, bảng FR, business-rules, NFR, acceptance-criteria, scope, glossary, open-questions, tài liệu kiến trúc liên quan nếu có.

## Quy trình

1. **Đầy đủ:** luồng chính, thay thế, lỗi; validate đầu vào; kết quả đầu ra; quyền; sở hữu dữ liệu; chuyển trạng thái.
2. **Rõ ràng:** câu không mơ hồ, thuật ngữ khớp glossary, actor rõ, ràng buộc đo được.
3. **Nhất quán:** FR với BR, với NFR, với phạm vi, với phân quyền, với quyết định đã có, giữa các FR.
4. **Kiểm thử được:** AC quan sát được, có điều kiện đầu và kết quả, có biên và luồng lỗi.
5. **Truy vết một chiều:** mỗi FR có liên kết BRQ/BR; mỗi AC trỏ FR; mọi BR có AC. Tài liệu khai báo liên kết hai chiều là finding.
6. **Câu hỏi mở:** câu đang Open chặn phạm vi nào; giả định đã quá hạn rà soát; điểm mơ hồ chưa có câu hỏi mở.
7. **Khả thi:** chỉ đánh dấu rủi ro (kỹ thuật, tích hợp, dữ liệu, hiệu năng, bảo mật) để chuyển `architecture-design`; không quyết định kiến trúc.
8. **Phân loại finding:** Critical (chặn triển khai) · High (thiếu hoặc mâu thuẫn lớn) · Medium (chưa rõ) · Low (cải thiện tài liệu).

## Hoàn thành khi

Đã rà đủ bảy khía cạnh ở trên; mỗi finding đủ trường; báo cáo nêu khuyến nghị và điều kiện chưa đạt.

## Báo cáo

Một báo cáo: số yêu cầu đã rà, số finding theo mức, danh sách finding, vấn đề chặn, khuyến nghị duyệt.

- Mỗi finding: mã `FND-<NN>` (chỉ dùng trong báo cáo này), mức độ, mã yêu cầu liên quan, mô tả, tác động, đề xuất sửa.
- Khuyến nghị duyệt khi: mọi FR có AC, QA đã rà, không còn câu hỏi mở chặn phạm vi.
