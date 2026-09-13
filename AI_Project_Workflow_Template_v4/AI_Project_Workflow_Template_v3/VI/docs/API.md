# API Contract

Mỗi endpoint cần mô tả:
- Method/path
- Yêu cầu authentication
- Role/permission
- Ownership
- Request params/body
- Response body
- Status code
- Error code/message
- Validation
- Pagination/filter/sort
- Idempotency nếu có

## Compatibility
Nếu là breaking change:
1. Xác định consumer.
2. Định nghĩa migration path.
3. Cập nhật tài liệu.
4. Cập nhật tests.
5. Chỉ xóa behavior cũ khi được duyệt.

## Security
Không trả về field được bảo vệ chỉ vì field đó tồn tại trong entity/database.
