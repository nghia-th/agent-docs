# Business Rules

Ghi business rule theo ngôn ngữ có thể kiểm thử.

Mỗi rule gồm:
- ID
- Mô tả
- Actor
- Điều kiện trước
- Operation được phép
- Điều kiện từ chối
- Error/status mong đợi
- Data bị ảnh hưởng
- API/UI liên quan

Backend phải enforce business rule ở server.
Frontend chỉ hỗ trợ UX và không phải authority cuối cùng.
