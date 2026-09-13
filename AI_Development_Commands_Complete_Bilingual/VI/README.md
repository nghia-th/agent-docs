# AI Development Commands — Hướng dẫn sử dụng

## Mục tiêu
Bộ lệnh này biến một ý tưởng thô thành design được duyệt, sau đó thành task, code, test và verification.

## Workflow chuẩn

```text
IDEA
  ↓
ANALYZE IDEA
  ↓
DESIGN
  ↓
REVIEW DESIGN
  ↓
CHANGE REQUEST (nếu có)
  ↓
APPROVE DESIGN
  ↓
CREATE TASKS
  ↓
IMPLEMENT TASK
  ↓
TEST
  ↓
CODE REVIEW
  ↓
FINAL VERIFICATION
```

## Quy tắc vàng
**Không cho AI nhảy thẳng từ IDEA → CODE.**

### 1. Có ý tưởng
Dùng `00_CORE/01_IDEA.md`.

### 2. Thiết kế
Dùng `00_CORE/02_ANALYZE_IDEA.md` rồi `00_CORE/03_DESIGN.md`.

### 3. Anh review
Dùng `00_CORE/04_REVIEW_DESIGN.md`.

### 4. Anh thay đổi ý tưởng
Dùng `00_CORE/06_CHANGE_REQUEST.md`.

### 5. Anh duyệt
Dùng `00_CORE/05_APPROVE_DESIGN.md`.

### 6. Chia việc
Dùng `00_CORE/07_CREATE_TASKS.md`.

### 7. Code
Dùng `02_TASK/01_IMPLEMENT_TASK.md` cho từng task.

### 8. Bug
Dùng nhóm `03_BUG/`.

### 9. Database/API/Security
Dùng nhóm tương ứng trong `04_DATABASE/`, `04_API/`, `05_SECURITY/`.

### 10. Kết thúc
Dùng `08_RELEASE/01_FINAL_VERIFICATION.md`.

## Cách dùng với OpenCode
Anh có thể copy nguyên nội dung một file command và paste vào chat. Chỉ thay phần `[PLACEHOLDER]`.

Nếu project đã có `dev/features/<feature>` hoặc `dev/tasks/<task>`, luôn chỉ rõ đường dẫn cho AI.

## Command nhanh

| Mục đích | Command |
|---|---|
| Ý tưởng | `00_CORE/01_IDEA.md` |
| Phân tích sâu | `00_CORE/02_ANALYZE_IDEA.md` |
| Thiết kế | `00_CORE/03_DESIGN.md` |
| Review design | `00_CORE/04_REVIEW_DESIGN.md` |
| Duyệt | `00_CORE/05_APPROVE_DESIGN.md` |
| Đổi design | `00_CORE/06_CHANGE_REQUEST.md` |
| Chia task | `00_CORE/07_CREATE_TASKS.md` |
| Làm task | `02_TASK/01_IMPLEMENT_TASK.md` |
| Bug | `03_BUG/02_INVESTIGATE_BUG.md` |
| Database | `04_DATABASE/01_DESIGN_DATABASE_CHANGE.md` |
| API | `04_API/01_DESIGN_API.md` |
| Security | `05_SECURITY/01_SECURITY_REVIEW.md` |
| Code review | `06_CODE/01_CODE_REVIEW.md` |
| Test plan | `07_TESTING/01_TEST_PLAN.md` |
| Verify | `08_RELEASE/01_FINAL_VERIFICATION.md` |
