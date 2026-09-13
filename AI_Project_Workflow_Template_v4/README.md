# AI Project Workflow Template v4 — Full-Stack / Song ngữ

Bộ template dành cho AI coding agent làm việc với Frontend, Backend, Database và workflow phát triển theo Feature/Task/Bug.

## Reading order / Thứ tự đọc
1. `AGENTS.md`
2. `docs/PROJECT.md`
3. `docs/ARCHITECTURE.md`
4. `docs/BUSINESS_RULES.md`
5. `docs/DATA_MODEL.md`
6. `docs/API.md`
7. Frontend / Backend docs
8. `dev/features/` cho feature đang làm
9. `dev/tasks/` hoặc `dev/bugs/` cho công việc cụ thể
10. Prompt tương ứng trong `dev/prompts/`

## Architecture of knowledge / Kiến trúc tài liệu

`docs/` = kiến thức ổn định của hệ thống.

`dev/features/` = workspace của feature hiện tại.

`dev/tasks/` = đơn vị công việc có thể giao cho AI.

`dev/bugs/` = hồ sơ điều tra bug.

`dev/decisions/` = quyết định đã chốt.

`src/` = source code thực tế.

## Recommended flow

`docs/` → `dev/features/` → `dev/tasks/` → code → tests → verification

EN và VI chứa hai phiên bản tương ứng.
