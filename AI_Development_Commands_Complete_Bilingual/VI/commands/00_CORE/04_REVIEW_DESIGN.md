# REVIEW DESIGN — Review Before Approval

Chưa sửa source code.

Review design của feature:

[FEATURE]

Đọc toàn bộ tài liệu feature và tài liệu hệ thống liên quan.

Kiểm tra:
1. Có đáp ứng ý tưởng gốc không?
2. Business rules có đầy đủ và testable không?
3. Có assumption nào bị biến thành rule không?
4. Data model có đủ không?
5. API có rõ request/response/error/status không?
6. Security/authorization/ownership có đầy đủ không?
7. Database migration có an toàn không?
8. Frontend workflow có khớp API không?
9. Backend có enforce rule không?
10. Tests có bao phủ negative cases không?
11. Có breaking change không?
12. Có complexity không cần thiết không?

Phân loại:
- BLOCKER
- HIGH
- MEDIUM
- LOW
- PASS

Không sửa code.
Đưa ra danh sách cần chỉnh trước khi APPROVE.
