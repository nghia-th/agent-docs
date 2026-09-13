# CREATE TASKS — Break Approved Design into Tasks

Feature đã được APPROVED.

Đọc:
- `AGENTS.md`
- feature documentation
- relevant `docs/`
- relevant decisions

Chia implementation thành các task nhỏ, độc lập tối đa và có thể verify.

Mỗi task phải có:
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

Không code.
Cập nhật `TASKS.md` và tạo task files trong `dev/tasks/` nếu project workflow yêu cầu.
