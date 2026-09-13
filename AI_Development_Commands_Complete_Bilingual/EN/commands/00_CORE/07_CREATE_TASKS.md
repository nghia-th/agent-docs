# CREATE TASKS — Break Approved Design into Tasks

Feature has được APPROVED.

Read:
- `AGENTS.md`
- feature documentation
- relevant `docs/`
- relevant decisions

Chia implementation thành các task nhỏ, độc lập tối đa and has thể verify.

Mỗi task must has:
- ID
- Goal
- Scope
- Layer
- Dependencies
- Business/API/Data rules
- Acceptance criteria
- Tests
- Verification

Ưu tiên dependency:
Database/domain → Backend API → Frontend → Integration → Verification.

Do not code.
Update `TASKS.md` and tạo task files in `dev/tasks/` nếu project workflow yêu cầu.
