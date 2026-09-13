# Backend Architecture

Document actual backend technology and boundaries.

## Responsibilities
- API/controller: transport and contract
- Service/domain: business rules and transaction orchestration
- Repository: persistence
- Security: authentication/authorization
- DTO/mapper: external contract
- Exception/error handler: consistent API errors

## Transaction rule
Place transaction boundaries where business operations require atomicity. Document operations that must succeed or fail as one unit.

## Do not
- Put business rules only in controllers.
- Bypass authorization in service/repository paths.
- Return persistence entities blindly when DTOs are required.
