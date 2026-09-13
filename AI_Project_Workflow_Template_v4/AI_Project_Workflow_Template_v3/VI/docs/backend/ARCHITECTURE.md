# Backend Architecture

Mô tả công nghệ và boundary thực tế của backend.

## Trách nhiệm
- API/controller: transport và contract
- Service/domain: business rules và transaction orchestration
- Repository: persistence
- Security: authentication/authorization
- DTO/mapper: external contract
- Exception/error handler: API error nhất quán

## Transaction
Đặt transaction boundary tại business operation cần tính atomicity. Ghi rõ operation nào phải thành công hoặc thất bại cùng nhau.

## Không được
- Chỉ đặt business rule ở controller.
- Bypass authorization.
- Trả persistence entity trực tiếp khi project yêu cầu DTO.
