# AGENTS.md — Full-Stack AI Coding Rules

## 1. Role
You are an AI coding agent working in a full-stack application. Before changing code, inspect the existing implementation, architecture, business rules, API contracts, database model, tests, and i18n conventions.

## 2. Source of truth
Priority:
1. Explicit user request
2. Existing project behavior and tests
3. Business rules
4. API contracts
5. Architecture/data model
6. Coding conventions
7. General assumptions

Do not silently invent business behavior. If the available documents do not define something important, state the gap.

## 3. Language
- User-facing explanations: Vietnamese with full diacritics unless English is explicitly requested.
- Technical identifiers, class names, function names, API paths, enum values, file names: preserve exactly.
- Source-code comments/JSDoc: English unless the project explicitly requires another language.
- UI text must use the project's i18n mechanism when one exists.

## 4. Scope
- Inspect before editing.
- Reuse existing abstractions.
- Do not create duplicate components/services/helpers.
- Do not change project configuration unless required by the task.
- Do not change database schema directly without a migration/schema plan.
- Do not weaken authentication, authorization, ownership checks, validation, or transaction boundaries.
- Do not commit, push, or create a PR unless explicitly requested.

## 5. Full-stack boundary
Frontend:
- Consumes documented APIs.
- Handles loading, empty, success and error states.
- Never treats client-side checks as the final security boundary.
- Must not call backend internals directly.

Backend:
- Owns authorization, validation, ownership, lifecycle, data integrity and transaction rules.
- Must enforce rules server-side even when the UI already checks them.
- API response/error contracts must remain consistent.
- Repository/database access belongs behind the project's established service/domain boundary.

## 6. Database
For a database-affecting change:
1. Identify affected tables/entities.
2. Identify columns, types, nullability, defaults and constraints.
3. Identify indexes and foreign keys.
4. Check existing data compatibility.
5. Define migration/rollback strategy where the project supports it.
6. Update backend model/repository/service as needed.
7. Update API contracts and frontend models if affected.
8. Add/update tests.

Never drop or rename production data structures casually.

## 7. API
For an API change:
- Document request, response, status codes and error behavior.
- Check authentication and authorization.
- Check ownership.
- Check validation and edge cases.
- Check backward compatibility.
- Update both backend tests and frontend integration expectations where applicable.

## 8. Security
Always consider:
- authentication
- role/permission checks
- resource ownership
- input validation
- sensitive data exposure
- correct HTTP status/error behavior
- ID enumeration/resource access
- transaction consistency

Do not expose fields that the caller is not authorized to see.

## 9. Testing
Use the project's existing test stack.
At minimum, choose the appropriate levels:
- Backend unit/service tests
- Controller/API tests
- Repository/integration tests when data behavior matters
- Security/authorization tests when access rules matter
- Frontend component/BLoC tests when UI behavior changes

Prefer non-interactive test commands in agent workflows.

## 10. Verification
Before finishing:
- inspect changed files
- run relevant tests
- run build/typecheck/lint when available
- verify API/database impact
- verify no unrelated files changed
- summarize remaining risks

Never claim a test passed unless it actually ran and passed.
