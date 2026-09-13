# API Contract

For every endpoint document:
- Method/path
- Authentication requirement
- Role/permission
- Ownership rule
- Request params/body
- Response body
- Status codes
- Error codes/messages
- Validation
- Pagination/filter/sort
- Idempotency where relevant

## Compatibility
For a breaking change:
1. Identify consumers.
2. Define migration path.
3. Update documentation.
4. Update tests.
5. Only remove old behavior when explicitly approved.

## Security
Never expose protected fields merely because they exist in the entity/database.
