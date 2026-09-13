# Error Handling

Định nghĩa error model ổn định.

Mỗi error:
- HTTP status
- application error code
- message an toàn cho user
- thông tin log nội bộ
- retryability
- frontend behavior

Không leak stack trace, SQL detail, token, secret hoặc thông tin nội bộ nhạy cảm.
