# Data Model

Mô tả entity/table và quan hệ.

Mỗi entity:
- Mục đích
- Primary key
- Field và type
- Nullability/default
- Unique constraint
- Foreign key
- Index
- Lifecycle/status
- Ownership
- Field nhạy cảm

Khi thay đổi phải ghi rõ migration impact và compatibility.

Không suy ra quyền hiển thị chỉ từ database model; phải định nghĩa ở API boundary.
