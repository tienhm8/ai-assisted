---
name: requirement-analysis
description: Phân tích nhu cầu nghiệp vụ thành yêu cầu phần mềm có thể truy vết (BRQ, FR, business rules, NFR, acceptance criteria) và ghi vào đúng tài liệu yêu cầu; điểm chưa rõ ghi vào open-questions.
---

# Requirement Analysis Skill

## 1. Mục tiêu

Biến nhu cầu nghiệp vụ thành yêu cầu rõ ràng, kiểm thử được, truy vết được, đủ cho kiến trúc sư, developer và QA dùng. AI chỉ soạn ở trạng thái Draft; không tự chuyển Approved.

## 2. Cổng vào

- Có mục tiêu nghiệp vụ và phạm vi (vision, scope) ở trạng thái Approved, hoặc nguồn từ stakeholder đã duyệt. Thiếu thì dừng và hỏi; nếu chưa có vision/scope thì chuyển product-discovery.
- Điểm chưa rõ chặn phạm vi: ghi `OQ-NN`, không tự trả lời.

## 3. Đầu vào

Đọc trước: mục tiêu nghiệp vụ, phạm vi, BRD, FR/business-rules/NFR/acceptance-criteria hiện có, glossary, open-questions.md, và nguồn từ stakeholder (tài liệu, quyết định đã duyệt).

## 4. Quy trình

**Quy ước ID và truy vết**

- ID: `BRQ-NN`, `FR-<MODULE>-NN`, `BR-<MODULE>-NN`, `NFR-NN`, `<FR>-AC<N>`, `OQ-NN`.
- Truy vết một chiều: FR giữ liên kết tới BRQ và BR; AC trỏ tới FR (và BR nó kiểm chứng). Không khai báo chiều ngược lại ở BRD hay business-rules.md. Không lập Traceability Matrix riêng.

**Các bước**

1. **Bối cảnh:** vấn đề, mục tiêu, người dùng, stakeholder, phạm vi và ngoài phạm vi, ràng buộc. Ghi mục tiêu vào BRD (BRQ).
2. **Actor:** vai trò, trách nhiệm, quyền; không giả định mọi actor có quyền như nhau.
3. **FR:** tách nhu cầu thành FR, ghi vào bảng FR của `FR/FR-<MODULE>.md`. Mô tả một câu. Chỉ FR rủi ro cao hoặc mơ hồ mới thêm chi tiết (điều kiện tiên quyết, luồng chính, luồng lỗi) dưới bảng.
4. **Business rule:** chỉ ghi vào business-rules.md khi có nguồn đã duyệt (ghi rõ nguồn). Chưa có nguồn thì ghi thành OQ, không tự đặt.
5. **NFR:** ghi vào NFR.md, mỗi NFR đo được (chỉ số + cách đo); không đo được thì ghi OQ.
6. **Acceptance criteria:** ghi vào acceptance-criteria.md, dạng Given / When / Then, kết quả quan sát được; gồm luồng lỗi và giá trị biên.
7. **Phụ thuộc:** giữa FR, module, API, thực thể dữ liệu, dịch vụ ngoài, vai trò; ghi tại FR liên quan.
8. **Điểm chưa rõ:** mơ hồ, thiếu quyết định, mâu thuẫn, giả định, mục ngoài phạm vi đều ghi vào open-questions.md (`OQ-NN`). Giả định phải có hạn rà soát. Không tự giải quyết ngầm.

## 5. Checklist

- [ ] Mỗi FR có nguồn BRQ; mỗi BR có nguồn đã duyệt.
- [ ] Mỗi FR có AC dạng Given / When / Then, gồm luồng lỗi và giá trị biên.
- [ ] NFR có chỉ số và cách đo.
- [ ] Mọi điểm chưa rõ đã thành `OQ-NN`; giả định có hạn rà soát.
- [ ] Thuật ngữ khớp glossary.

## 6. Việc không được làm

- Không bịa yêu cầu hay quy tắc nghiệp vụ; không tự quyết thay stakeholder.
- Không trộn FR với chi tiết triển khai kỹ thuật.
- Không đánh dấu Approved. Sửa FR đã Approved phải ghi lịch sử thay đổi (ngày, FR, thay đổi, lý do, người duyệt), không sửa lặng lẽ.
- Quyết định ảnh hưởng lớn đến triển khai mà chưa rõ thì dừng và hỏi.

## 7. Tiêu chí hoàn thành (DoD)

- Mọi FR trong phạm vi có AC kiểm thử được (gồm luồng lỗi, biên); mọi BR có AC.
- NFR đo được.
- Mọi ID duy nhất, liên kết FR→BRQ/BR đầy đủ.
- Điểm chưa rõ và giả định đã ghi vào open-questions.md.
- Sẵn sàng chuyển requirement-review.

## 8. Báo cáo bàn giao

Nêu: yêu cầu đã tạo/sửa (theo ID và file), BR ghi và nguồn, OQ mới, giả định và hạn rà soát, mục cần người duyệt. Không lặp lại nội dung đã nằm trong tài liệu.
