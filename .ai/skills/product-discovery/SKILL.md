---
name: product-discovery
description: Biến ý tưởng hoặc brief của PO và tài liệu stakeholder thành bản nháp vision, scope, glossary và open-questions trong docs/00-project-overview; không viết BRD hay FR.
---

# Product Discovery Skill

Làm rõ vấn đề, đối tượng và phạm vi từ nguồn có thật của PO và stakeholder, ghi thành bản nháp đủ để PO duyệt.

## Cổng vào

- Có brief hoặc tài liệu nguồn từ PO hoặc stakeholder. Thiếu thì dừng và hỏi, không tự dựng ý tưởng.
- Biết ai là PO (người duyệt vision và scope).

Đọc: brief và quyết định đã có; vision, scope, glossary, open-questions hiện có; PROJECT.md.

## Quy trình

1. **Đọc nguồn:** đánh dấu từng ý theo nguồn (ai nói, tài liệu nào). Ý không có nguồn không được ghi như sự thật.
2. **vision:** vấn đề, đối tượng sử dụng, kết quả đo được dạng `OUT-<NN>` (chỉ số và cách đo). Chưa đo được thì ghi câu hỏi mở, không bịa số.
3. **scope:** trong phạm vi, ngoài phạm vi, ràng buộc. Ràng buộc, kể cả pháp lý, chỉ ghi khi có nguồn.
4. **glossary:** thuật ngữ lấy từ nguồn. Thuật ngữ mơ hồ hoặc trùng nghĩa thì ghi câu hỏi mở.
5. **open-questions:** mọi điểm thiếu, mâu thuẫn, giả định ghi thành `OQ-<NN>` kèm người quyết và hạn; giả định có hạn rà soát.
6. **Rà chéo:** vision, scope, glossary dùng cùng thuật ngữ và không mâu thuẫn nhau.
7. **Trình PO.** PO duyệt vision, scope và xử lý câu hỏi mở chặn phạm vi rồi mới chuyển `requirement-analysis`.

## Giới hạn

- Không viết BRD, FR, business rule hay thiết kế kỹ thuật.

## Hoàn thành khi

- Bốn tài liệu ở Draft, đủ mục theo mẫu; mỗi nội dung có nguồn hoặc được đánh dấu là giả định.
- Mỗi `OUT-<NN>` đo được hoặc đã có câu hỏi mở.
- Câu hỏi mở chặn phạm vi đã nêu người quyết.

## Báo cáo

File đã tạo hoặc sửa, `OUT-<NN>` và `OQ-<NN>` mới, nguồn đã dùng, giả định và hạn rà soát, mục cần PO duyệt.
