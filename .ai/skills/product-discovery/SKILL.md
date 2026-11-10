---
name: product-discovery
description: Biến ý tưởng hoặc brief của PO và tài liệu stakeholder thành bản nháp vision, scope, glossary và open-questions trong docs/00-project-overview; không viết BRD hay FR.
---

# Product Discovery Skill

## 1. Mục tiêu

Làm rõ vấn đề, đối tượng và phạm vi từ nguồn có thật của PO/stakeholder, ghi thành bản nháp đủ để PO duyệt và chuyển sang `requirement-analysis`. AI chỉ soạn Draft/Proposed; không tự chuyển Approved.

## 2. Cổng vào

- Có brief hoặc tài liệu nguồn từ PO hoặc stakeholder. Thiếu thì dừng và hỏi, không tự dựng ý tưởng.
- Biết ai là PO (người duyệt vision và scope).
- Mức tự chủ của Task cho phép soạn tài liệu; không tự nâng.

## 3. Đầu vào

- Brief của PO, tài liệu và quyết định đã có từ stakeholder
- vision.md, scope.md, glossary.md, open-questions.md hiện có trong docs/00-project-overview
- PROJECT.md (khai báo của dự án, mức tự chủ, mức dữ liệu)

## 4. Quy trình

1. **Đọc nguồn**: đánh dấu từng ý theo nguồn (ai nói, tài liệu nào). Ý không có nguồn không được ghi như sự thật.
2. **vision.md**: vấn đề, đối tượng sử dụng, mục tiêu thành kết quả đo được dạng `OUT-NN` (chỉ số + cách đo). Chưa đo được thì ghi OQ, không bịa số.
3. **scope.md**: trong phạm vi, ngoài phạm vi, ràng buộc. Ràng buộc (kể cả pháp lý) chỉ ghi khi có nguồn.
4. **glossary.md**: thuật ngữ lấy từ nguồn. Không tự đặt nghĩa mới; thuật ngữ mơ hồ hoặc trùng nghĩa thì ghi OQ.
5. **open-questions.md**: mọi điểm thiếu, mâu thuẫn, giả định ghi thành `OQ-<NN>` kèm người quyết và hạn; giả định phải có hạn rà soát.
6. **Rà soát chéo**: vision, scope, glossary dùng cùng thuật ngữ và không mâu thuẫn nhau.
7. **Trình PO**: PO duyệt Approved vision và scope, xử lý các OQ chặn phạm vi. Sau đó mới chuyển `requirement-analysis`.

## 5. Checklist

- [ ] Mỗi nội dung có nguồn hoặc được đánh dấu giả định.
- [ ] Mỗi OUT-NN đo được hoặc đã có OQ.
- [ ] Phạm vi có cả trong và ngoài.
- [ ] Thuật ngữ nhất quán giữa các file.
- [ ] Mọi điểm chưa rõ đã vào open-questions.md.

## 6. Việc không được làm

- Không bịa mục tiêu, số liệu thành công hay ràng buộc pháp lý.
- Không tự đặt nghĩa mới cho thuật ngữ.
- Không viết BRD, FR, business rule hay thiết kế kỹ thuật.
- Không chuyển trạng thái sang Approved.
- Không tự giải quyết OQ thay PO; thiếu thông tin thì dừng và hỏi.

## 7. Tiêu chí hoàn thành (DoD)

- Cổng vào thoả; bốn tài liệu ở trạng thái Draft/Proposed, đầy đủ mục theo mẫu.
- Không còn nội dung không nguồn mà không đánh dấu.
- OQ chặn phạm vi đã nêu rõ người quyết.
- PO đã nhận bản nháp để duyệt; chưa duyệt thì chưa chuyển `requirement-analysis`.

## 8. Báo cáo bàn giao

- File đã tạo/sửa, OUT-NN và OQ mới (theo ID)
- Nguồn đã dùng; giả định và hạn rà soát
- Mục cần PO duyệt hoặc quyết
- Rủi ro còn lại
