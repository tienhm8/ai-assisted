---
name: task-planning
description: Từ FR có AC và thiết kế Approved, soạn plan Draft trong .ai/plans và đề xuất các Task nhỏ cho task-breakdown và backlog để Tech Lead duyệt trước khi giao việc.
---

# Task Planning Skill

## 1. Mục tiêu

Chia yêu cầu đã duyệt thành plan và các Task nhỏ, kiểm chứng được, đủ rõ để giao cho AI mà không phải đoán. AI chỉ đề xuất; Tech Lead duyệt plan và gán chính thức rủi ro, mức tự chủ.

## 2. Cổng vào

Dừng và ghi `open-questions.md` (OQ-<NN>) nếu thiếu:
- FR có AC (acceptance-criteria.md) đã duyệt.
- Thiết kế liên quan (kiến trúc, API, CSDL) ở trạng thái Approved.
Chưa đủ thì không lập plan code.

## 3. Đầu vào

- FR, business-rules.md, acceptance-criteria.md, NFR
- Tài liệu thiết kế trong docs/02-architecture, ADR liên quan
- task-breakdown.md, backlog.md, roadmap.md
- PLAN-TEMPLATE; PROJECT.md (trần mức tự chủ của dự án)

## 4. Quy trình

1. **Đọc**: FR, AC, BR, thiết kế; xác định phụ thuộc và vùng nhạy cảm.
2. **Chia Task** theo nguyên tắc trong task-breakdown.md: nhỏ nguyên tử, một trách nhiệm; Task lớn thì chia nhỏ; Task lai (nhiều loại) thì tách.
3. **Điền từng Task**: objective, scope in/out, AC (`<FR>-AC<N>`), phụ thuộc, estimate, rủi ro R1–R3 và mức tự chủ A0–A4 ở dạng ĐỀ XUẤT kèm lý do, không vượt trần của dự án.
4. **Song song**: chỉ khi các Task không chung file, schema hay contract; còn lại xếp tuần tự.
5. **Soạn plan** trong .ai/plans/ theo PLAN-TEMPLATE, trạng thái Draft: file dự kiến đổi, chuỗi skill dự kiến và lý do, kế hoạch kiểm chứng (mỗi AC ứng với test nào).
6. **Kiểm Definition of Ready** (theo task-breakdown.md) cho từng Task; Task thiếu điều kiện thì không giao, ghi OQ.
7. **Đề xuất** Task vào task-breakdown.md và backlog.md ở dạng Proposed.
8. **Trình Tech Lead** duyệt plan. Chưa duyệt thì không giao việc cho AI.
9. **Sau khi Task xong**: điền mục Kết quả của plan (đã làm gì, lệch kế hoạch, bằng chứng test).

## 5. Checklist

- [ ] Mỗi Task nhỏ, một trách nhiệm, có scope in/out.
- [ ] Mỗi Task có AC truy vết được về FR.
- [ ] Phụ thuộc và thứ tự rõ; song song có lý do.
- [ ] Rủi ro và mức tự chủ ghi là đề xuất, không vượt trần.
- [ ] Plan có kế hoạch kiểm chứng cho mọi AC.
- [ ] Definition of Ready đã kiểm.

## 6. Việc không được làm

- Không lập plan code khi FR chưa có AC hoặc thiết kế chưa Approved.
- Không tự gán chính thức rủi ro hay mức tự chủ; không nâng mức tự chủ.
- Không tự giao việc cho AI khi Tech Lead chưa duyệt plan.
- Không bịa yêu cầu để lấp chỗ trống; không mở rộng phạm vi ngoài FR.
- Không đánh dấu plan Approved.

## 7. Tiêu chí hoàn thành (DoD)

- Plan Draft đủ mục theo template; Task đề xuất đạt Definition of Ready hoặc nêu rõ thiếu gì.
- OQ mới đã ghi; Tech Lead nhận plan để duyệt.
- Sau thực thi: mục Kết quả đã điền.

## 8. Báo cáo bàn giao

- Plan và Task đã đề xuất (theo ID, file)
- Rủi ro, mức tự chủ đề xuất cần Tech Lead gán
- OQ và Task chưa sẵn sàng
- Điểm cần người quyết
