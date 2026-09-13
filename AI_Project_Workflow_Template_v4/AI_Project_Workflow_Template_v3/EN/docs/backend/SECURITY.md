# Backend Security

## Authentication
Document:
- login mechanism
- token/session
- token claims
- expiry/refresh
- protected routes

## Authorization
For every protected operation:
- required role/permission
- ownership rule
- object-level access
- rejection status/error

## Sensitive data
Document fields that must never be exposed to particular actors.

## Security tests
Include positive and negative cases:
- unauthenticated
- wrong role
- non-owner
- valid owner
- invalid/expired credentials
