# Prompt — Thay Đổi Database

Phân tích schema/data change trước khi edit.

Trả về:
- entity/table bị ảnh hưởng
- column/type/constraint
- index/foreign key
- risk với data hiện có
- migration steps
- rollback
- backend impact
- API impact
- frontend impact
- tests

Không tự ý sửa schema production nếu project có migration mechanism mà chưa dùng nó.
