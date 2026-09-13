# Architecture

## Full-stack view
Document:
- Frontend application
- Backend application
- Database
- Authentication
- External services
- Deployment/runtime boundaries

## Backend layers
Adapt to the actual project. Typical responsibilities:
- Controller/API: HTTP contract only
- Service/domain: business behavior and transactions
- Repository/data access: persistence
- Entity/model: data representation
- Security: authentication and authorization
- Mapping/DTO: API boundary

Do not force this structure if the existing project uses a different architecture.

## Frontend layers
Document:
- routes/screens
- components
- state/BLoC/store
- API client
- i18n
- shared UI

## Cross-layer rule
A feature is complete only when affected layers and contracts are considered together.
