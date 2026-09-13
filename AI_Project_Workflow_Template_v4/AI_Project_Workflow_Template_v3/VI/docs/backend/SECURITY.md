# Backend Security

## Authentication
Mô tả:
- cơ chế login
- token/session
- token claims
- expiry/refresh
- protected route

## Authorization
Với mỗi operation:
- role/permission
- ownership
- object-level access
- status/error khi từ chối

## Dữ liệu nhạy cảm
Ghi rõ field nào không được trả cho actor nào.

## Security tests
Có cả case đúng và case sai:
- chưa đăng nhập
- sai role
- không phải owner
- owner hợp lệ
- credential sai/hết hạn
