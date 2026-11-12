---
name: requirement-analysis
description: Phân tích nhu cầu nghiệp vụ thành yêu cầu phần mềm có thể truy vết (BRQ, FR, business rules, NFR, acceptance criteria) và ghi vào đúng tài liệu yêu cầu; điểm chưa rõ ghi vào open-questions.
---

# Requirement Analysis Skill

Biến nhu cầu nghiệp vụ thành yêu cầu rõ ràng, kiểm thử được, truy vết được, đủ cho kiến trúc sư, developer và QA dùng.

## Cổng vào

- Vision và scope đã Approved, hoặc có nguồn từ stakeholder đã duyệt. Chưa có vision, scope thì chuyển `product-discovery`.

Đọc: vision, scope, BRD, FR, business-rules, NFR, acceptance-criteria hiện có; glossary; open-questions; nguồn từ stakeholder.

## Quy ước

- Mã: `BRQ-<NN>`, `FR-<MODULE>-<NN>`, `BR-<MODULE>-<NN>`, `NFR-<NN>`, `<FR>-AC<N>`, `OQ-<NN>`.
- Truy vết một chiều: FR giữ liên kết tới BRQ và BR; AC trỏ tới FR và BR nó kiểm chứng. Không khai báo chiều ngược lại, không lập ma trận truy vết riêng.

## Quy trình

1. **Bối cảnh:** vấn đề, mục tiêu, người dùng, phạm vi và ngoài phạm vi, ràng buộc. Ghi mục tiêu vào BRD.
2. **Actor:** vai trò, trách nhiệm, quyền; không giả định mọi actor có quyền như nhau.
3. **FR:** ghi vào bảng FR của `FR/FR-<MODULE>.md`, mỗi FR một câu. Chỉ FR rủi ro cao hoặc mơ hồ mới thêm chi tiết (điều kiện tiên quyết, luồng chính, luồng lỗi) dưới bảng.
4. **Business rule:** chỉ ghi vào business-rules khi có nguồn đã duyệt, ghi rõ nguồn. Chưa có nguồn thì ghi câu hỏi mở.
5. **NFR:** mỗi NFR có chỉ số và cách đo; không đo được thì ghi câu hỏi mở.
6. **AC:** dạng Given / When / Then, kết quả quan sát được; gồm luồng lỗi và giá trị biên.
7. **Phụ thuộc** giữa FR, module, API, thực thể dữ liệu, dịch vụ ngoài, vai trò: ghi tại FR liên quan.
8. **Điểm chưa rõ:** mơ hồ, thiếu quyết định, mâu thuẫn, giả định đều ghi vào open-questions; giả định có hạn rà soát.

## Giới hạn

- Không trộn FR với chi tiết triển khai kỹ thuật.
- Sửa FR đã Approved phải ghi lịch sử thay đổi (ngày, FR, thay đổi, lý do, người duyệt).

## Hoàn thành khi

- Mọi FR có nguồn BRQ và có AC; mọi BR có nguồn và có AC.
- Mọi NFR đo được; mã duy nhất; thuật ngữ khớp glossary.
- Sẵn sàng chuyển `requirement-review`.

## Báo cáo

Yêu cầu đã tạo hoặc sửa (theo mã và file), BR và nguồn, `OQ-<NN>` mới, giả định và hạn rà soát, mục cần người duyệt. Không lặp nội dung đã nằm trong tài liệu.
