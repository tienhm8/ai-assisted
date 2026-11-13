# Code Review – Checklist đúng việc, test, đúng chỗ (ưu tiên 1–3)

## Ưu tiên 1: Code có làm đúng việc không?

- Từng AC được đáp ứng ở đâu trong code; AC nào không thấy chỗ đáp ứng.
- Ca biên: rỗng, null/không có giá trị, giá trị biên, dữ liệu trùng, danh sách một phần tử, chuỗi rất dài, ký tự đặc biệt.
- Chuyển trạng thái: có chặn chuyển trạng thái không hợp lệ không.
- Xử lý lỗi: không nuốt lỗi; lỗi được phân loại theo error-handling; thông báo lỗi không lộ chi tiết nội bộ.
- Kiểu dữ liệu: tiền và số cần chính xác không dùng số dấu phẩy động; múi giờ và định dạng thời gian nhất quán; làm tròn đúng quy tắc nghiệp vụ.
- Ranh giới transaction: các ghi phải cùng thành công hoặc cùng thất bại có nằm chung một đơn vị nguyên tử không.
- Quy tắc nghiệp vụ lấy từ FR/BR, không phải do code tự đặt ra; chưa rõ thì ghi câu hỏi mở.

## Ưu tiên 2: Có test chứng minh không?

- Mỗi AC có test truy vết (tên/chú thích mang ID AC) và output test thật. AC không có bằng chứng là finding High.
- Sửa lỗi có regression test đỏ trước, xanh sau.
- Có test cho ca lỗi, ca biên và ca bị từ chối quyền, không chỉ đường đi thành công.
- Test kiểm hành vi, không kiểm chi tiết cài đặt; không có assertion rỗng hoặc chỉ kiểm "không ném lỗi".
- Không test bị xoá, bỏ qua hoặc làm yếu để qua cổng.

## Ưu tiên 3: Code có đặt đúng chỗ không?

Lấy bản đồ tầng và trách nhiệm từ tài liệu kiến trúc của dự án; không tự áp một mô hình tầng. Kiểm theo các trách nhiệm chung:

| Trách nhiệm | Câu hỏi |
| --- | --- |
| Biên nhận yêu cầu (handler, controller, resolver, CLI, UI component) | Chỉ điều phối (nhận yêu cầu → gọi nghiệp vụ → trả kết quả) hay đang chứa quy tắc nghiệp vụ, truy cập dữ liệu trực tiếp? |
| Kiểm tra đầu vào và phân quyền | Làm tại biên hệ thống, theo cơ chế chung của dự án, không rải rác trong nghiệp vụ? Chỉ nhận các trường được phép (whitelist), không gán toàn bộ input vào đối tượng? |
| Nghiệp vụ (service, use case) | Quy tắc nghiệp vụ nằm ở đây và chỉ ở một nơi? |
| Domain (entity, model, value object) | Hành vi gắn chặt với dữ liệu (kiểm bất biến, chuyển trạng thái) nằm cùng đối tượng của nó? |
| Truy cập dữ liệu (repository, DAO, query) | Tầng trên không tự dựng truy vấn vượt tầng; không truy cập dữ liệu của module khác ngoài interface công khai? |
| Bất đồng bộ và side effect (job, event, consumer, gửi thông báo, gọi hệ thống ngoài) | Side effect chậm hoặc không hoàn tác được có được tách khỏi luồng chính và khỏi transaction không? |
| Định dạng đầu ra | Trả về dạng dữ liệu đã định nghĩa cho bên ngoài, không trả nguyên đối tượng nội bộ? |

Dấu hiệu cần xem xét (không phải luật; ngưỡng cụ thể theo coding-standards của dự án): hàm hoặc class vượt ngưỡng kích thước; một hàm làm nhiều việc; lồng điều kiện sâu; quá nhiều dependency; một đơn vị bị sửa vì nhiều lý do khác nhau; phụ thuộc vòng; logic trùng lặp.
