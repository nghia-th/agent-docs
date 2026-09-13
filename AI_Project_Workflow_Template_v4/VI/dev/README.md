# dev/ — Development Workspace

`dev/` là khu vực phục vụ công việc phát triển cụ thể. Không chứa source code production và không thay thế tài liệu ổn định trong `docs/`.

## Các cấp độ
1. `dev/features/` — workspace của feature hoàn chỉnh.
2. `dev/tasks/` — các công việc nhỏ, cụ thể và có thể thực thi.
3. `dev/bugs/` — điều tra và xử lý bug.

## Tài liệu hỗ trợ
- `dev/decisions/` — các quyết định đã được chốt.
- `dev/prompts/` — prompt phục vụ workflow phát triển.

## Relationship
`docs/` = kiến thức ổn định của hệ thống.
`dev/features/` = workspace feature đang phát triển.
`dev/tasks/` = công việc có thể thực thi.
`dev/bugs/` = defect investigation.
`dev/decisions/` = các quyết định đã ghi nhận.

Không đưa ghi chú tạm thời và scratch material vào `docs/` trừ khi chúng trở thành tài liệu chính thức.
