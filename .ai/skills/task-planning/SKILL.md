---
name: task-planning
description: Từ FR có AC và thiết kế Approved, soạn plan Draft trong .ai/plans và đề xuất các Task nhỏ cho task-breakdown và backlog để Tech Lead duyệt trước khi giao việc.
---

# Task Planning Skill

Chia yêu cầu đã duyệt thành plan và các Task nhỏ, kiểm chứng được, đủ rõ để giao mà không phải đoán. AI đề xuất; Tech Lead duyệt plan và gán mức rủi ro, mức tự chủ.

## Cổng vào

Thiếu thì dừng và ghi câu hỏi mở:
- FR có AC đã duyệt.
- Thiết kế liên quan (kiến trúc, API, CSDL) đã Approved.

Đọc: FR, business-rules, AC, NFR; tài liệu thiết kế và ADR liên quan; task-breakdown, backlog, roadmap; PLAN-TEMPLATE; PROJECT.md §2.

## Quy trình

1. **Đọc** FR, AC, BR, thiết kế; xác định phụ thuộc và vùng nhạy cảm.
2. **Chia Task** theo nguyên tắc trong task-breakdown: nhỏ, một trách nhiệm; Task nhiều loại việc thì tách.
3. **Điền từng Task:** mục tiêu, phạm vi làm và không làm, AC, phụ thuộc, ước lượng, mức rủi ro và mức tự chủ ở dạng đề xuất kèm lý do.
4. **Song song** chỉ khi các Task không chung file, schema hay contract.
5. **Soạn plan** trong `.ai/plans/` theo PLAN-TEMPLATE, trạng thái Draft.
6. **Kiểm Definition of Ready** theo task-breakdown cho từng Task; Task thiếu điều kiện thì không giao, ghi câu hỏi mở.
7. **Đề xuất Task** vào task-breakdown và backlog ở dạng Proposed.
8. **Trình Tech Lead** khi mọi điểm cần người quyết đã là câu hỏi mở đủ phần. Chưa duyệt thì chưa giao việc.
9. **Sau khi Task xong:** điền mục Kết quả của plan.

## Hoàn thành khi

- Mỗi Task có phạm vi làm và không làm, AC truy vết về FR, thứ tự và phụ thuộc rõ.
- Plan có test cho mọi AC.
- Task đạt Definition of Ready hoặc nêu rõ thiếu gì.

## Báo cáo

Plan và Task đã đề xuất (mã, file), mức rủi ro và mức tự chủ đề xuất, Task chưa sẵn sàng, mã `OQ-<NN>` cần người quyết.
