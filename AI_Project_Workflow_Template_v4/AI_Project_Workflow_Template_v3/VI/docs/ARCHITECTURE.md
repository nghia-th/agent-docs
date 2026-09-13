# Architecture

## Góc nhìn Full-Stack
Mô tả:
- Frontend
- Backend
- Database
- Authentication
- External services
- Runtime/deployment boundaries

## Các layer Backend
Điều chỉnh theo project thực tế. Thông thường:
- Controller/API: chỉ xử lý HTTP contract
- Service/domain: business behavior và transaction
- Repository/data access: persistence
- Entity/model: biểu diễn dữ liệu
- Security: authentication và authorization
- Mapping/DTO: ranh giới API

Không ép kiến trúc này nếu project hiện tại dùng cách khác.

## Các layer Frontend
Mô tả:
- routes/screens
- components
- state/BLoC/store
- API client
- i18n
- shared UI

## Quy tắc liên tầng
Một feature chỉ được coi là hoàn thành khi đã xem xét tất cả layer và contract bị ảnh hưởng.
