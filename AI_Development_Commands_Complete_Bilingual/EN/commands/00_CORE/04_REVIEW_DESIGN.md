# REVIEW DESIGN — Review Before Approval

Chưa sửa source code.

Review design of feature:

[FEATURE]

Read all tài liệu feature and tài liệu hệ thống relevant.

Check:
1. Có đáp ứng ý tưởng gốc not?
2. Business rules has complete and testable not?
3. Có assumption nào bị biến thành rule not?
4. Data model has đủ not?
5. API has clear request/response/error/status not?
6. Security/authorization/ownership has complete not?
7. Database migration has safe not?
8. Frontend workflow has khớp API not?
9. Backend has enforce rule not?
10. Tests has bao phủ negative cases not?
11. Có breaking change not?
12. Có complexity not need thiết not?

Classify:
- BLOCKER
- HIGH
- MEDIUM
- LOW
- PASS

Do not edit code.
Return danh sách need chỉnh trước khi APPROVE.
