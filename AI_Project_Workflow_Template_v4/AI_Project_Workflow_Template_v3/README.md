# AI Project Workflow Template v3 — Full-Stack / Song ngữ

Bộ template dùng để làm việc với AI coding agent cho cả Frontend và Backend.

## Reading order / Thứ tự đọc
1. `AGENTS.md`
2. `docs/PROJECT.md`
3. `docs/ARCHITECTURE.md`
4. `docs/BUSINESS_RULES.md`
5. `docs/DATA_MODEL.md`
6. `docs/API.md`
7. Frontend docs / Backend docs
8. Chọn prompt phù hợp trong `prompts/`

## Principle / Nguyên tắc
- Business rules are defined before implementation.
- Backend is the final authority for authorization, validation, lifecycle and data integrity.
- Frontend must follow API contracts and must not reproduce security rules as the final authority.
- Database changes require an explicit migration/schema plan.
- API changes require compatibility analysis.
- Every feature must include verification and appropriate tests.

## Language
The EN and VI folders contain equivalent English/Vietnamese templates.
