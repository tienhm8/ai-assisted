# RUNS: PLAN-<NNN>

> Orchestrator ghi sau mỗi lần chạy Task, không sửa dòng cũ. Lưu ở `.ai/plans/PLAN-<NNN>-<slug>/runs.md`. Là nguồn số đo cho báo cáo bàn giao §8 và cho rà soát định kỳ mức mặc định ([model-effort](../workflows/model-effort.md) §2).

| Run | Agent | Cách chạy | Commit gốc (`base`) | Mức (model/effort) | Lý do chạy | Bắt đầu – kết thúc | Kết quả | Tiêu chí không đạt / lý do dừng | Bằng chứng | Chi phí lần này (token, USD) | Chi phí cộng dồn của Task (USD) | Trường không áp dụng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <KEY>-<N>#1 | executor | Gửi đi / Có người | `a1b2c3d` | `sonnet/low` | Lần đầu (lỗi 1) | | Đạt / Không đạt / Dừng | | lệnh + kết quả, commit | | | `max_output_tokens` |

- **Lý do chạy:** Lần đầu · Nâng cấp (từ mức nào trong thứ tự thử) · Chạy lại sau khi sửa môi trường hoặc quyền · Lỗi mới sau test bước 6 · Lỗi mới sau review bước 8. Ghi số thứ tự lỗi (lỗi 1, lỗi 2…): mỗi lỗi có tối đa 3 lần chạy (`project-rules` 18).
- **Commit gốc:** mỗi lỗi một commit gốc: commit ngay trước lần chạy đầu của lỗi đó (lỗi 1: commit Task bắt đầu; lỗi sau: kết quả đã nhận mà lần sửa này sửa). Lần nâng cấp đưa worktree về commit gốc của lỗi đó, không về commit đầu của Task (model-effort §3 quy tắc 3). Lỗi mới chạy từ mức của lần chạy được nhận gần nhất.
- **Chạy "Có người":** người mở phiên ghi chi phí (nếu công cụ hiển thị) khi trả báo cáo; không có thì ghi "không đo" và lý do.
- **Dòng Phiên điều phối sau mỗi Task:** mỗi phiên (lập Plan, chạy, báo cáo) ghi dòng riêng kèm mức model·effort của phiên; file transcript, khoảng thời gian cắt theo Task, token theo model; số USD do người đưa (đọc từ `/cost` hoặc Account & Usage), không có thì ghi "không đo USD" và lý do; chỉ trích số liệu, không chép nội dung hội thoại. Cộng vào ngân sách của Plan.
- **Chi phí cộng dồn** được so với ngân sách hiện hành của Task (ban đầu cộng cấp thêm), không so với ngân sách ban đầu.
- **Kết quả:** `Đạt` khi mọi kiểm tra Đầy đủ, Đúng, Hợp lệ qua (đạt một phần AC là `Không đạt`); `Không đạt` khi trượt và còn lượt (chạy mức kế tiếp trong thứ tự thử, hoặc chạy lại cùng mức nếu đã ở mức cuối); `Dừng` khi gặp `stop_on`, hết lượt hoặc hết ngân sách (ghi đề xuất bước tiếp).
- **Độ tin cậy** do agent tự báo: không bao giờ là căn cứ `Đạt` hay lý do nâng cấp. Lần chạy đạt nhưng agent báo chưa chắc thì ghi "Đạt, chờ người xem" và nêu điểm chưa chắc.

## Điều chỉnh ngân sách

| Lần | Task | Loại (mở quỹ / giữ chỗ cấp thêm / trả lại giữ chỗ / thu hồi / dừng hỏi người) | Số tiền (USD) | Ngân sách Task trước → sau | Số dư quỹ trước → sau | Lý do (kèm kết quả đánh giá lại: việc đã xong, việc còn lại, dạng ước tính) | Ngày |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | (Plan) | mở quỹ | số quỹ đã duyệt | — | 0 → số quỹ đã duyệt | Quỹ duyệt cùng Plan | (ngày) |
| 1 | <KEY>-<N> | giữ chỗ cấp thêm | 0,6 | 2 → 2,6 | 0,8 → 0,2 | Đã xong: …; còn lại: …; ước tính `DuKienThem` 0,9 | |

- **Mỗi điều chỉnh là một dòng mới**, không sửa dòng cũ. Số dư quỹ chỉ đọc từ bảng này.
- **Dòng mở quỹ** được ghi một lần, bởi Orchestrator, khi Plan được duyệt; đây là dòng đầu tiên, không có dòng nào đứng trước nó.
