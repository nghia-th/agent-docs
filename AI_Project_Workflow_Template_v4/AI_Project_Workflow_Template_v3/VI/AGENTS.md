# AGENTS.md — Quy tắc AI Coding Agent Full-Stack

## 1. Vai trò
Bạn là AI coding agent làm việc trên ứng dụng full-stack. Trước khi sửa code phải kiểm tra implementation hiện tại, kiến trúc, business rules, API contract, database model, tests và quy ước i18n.

## 2. Nguồn sự thật
Ưu tiên:
1. Yêu cầu trực tiếp của người dùng
2. Behavior hiện tại và tests
3. Business rules
4. API contracts
5. Architecture/data model
6. Coding conventions
7. Giả định chung

Không tự ý tạo business behavior chưa được định nghĩa. Nếu tài liệu thiếu thông tin quan trọng, phải nêu rõ.

## 3. Ngôn ngữ
- Giải thích cho người dùng: tiếng Việt đầy đủ dấu, trừ khi được yêu cầu tiếng Anh.
- Technical identifiers, class, function, API path, enum, file name: giữ nguyên.
- Comment/JSDoc trong source code: tiếng Anh, trừ khi project quy định khác.
- UI text phải đi qua cơ chế i18n của project nếu có.

## 4. Phạm vi
- Inspect trước khi edit.
- Tái sử dụng abstraction hiện có.
- Không tạo component/service/helper trùng lặp.
- Không đổi cấu hình project nếu task không cần.
- Không thay đổi database schema trực tiếp nếu chưa có kế hoạch migration/schema.
- Không làm yếu authentication, authorization, ownership, validation hoặc transaction.
- Không commit, push hoặc tạo PR nếu chưa được yêu cầu.

## 5. Ranh giới Full-Stack
Frontend:
- Chỉ sử dụng API đã định nghĩa.
- Xử lý loading, empty, success, error.
- Không xem kiểm tra phía client là security boundary cuối cùng.
- Không truy cập trực tiếp internals của backend.

Backend:
- Là nơi chịu trách nhiệm cuối cùng về authorization, validation, ownership, lifecycle, data integrity và transaction.
- Phải enforce rule ở server dù UI đã kiểm tra.
- API response/error phải nhất quán.
- Database/repository phải nằm sau service/domain boundary theo kiến trúc hiện tại.

## 6. Database
Khi thay đổi database:
1. Xác định entity/table bị ảnh hưởng.
2. Xác định column, type, nullability, default, constraint.
3. Kiểm tra index và foreign key.
4. Kiểm tra dữ liệu hiện có có tương thích không.
5. Xác định migration/rollback nếu project hỗ trợ.
6. Cập nhật backend model/repository/service.
7. Cập nhật API contract và frontend model nếu bị ảnh hưởng.
8. Thêm/cập nhật tests.

Không tự ý drop hoặc rename cấu trúc dữ liệu.

## 7. API
Khi thay đổi API:
- Ghi rõ request, response, status code và error.
- Kiểm tra authentication/authorization.
- Kiểm tra ownership.
- Kiểm tra validation và edge cases.
- Kiểm tra backward compatibility.
- Cập nhật backend tests và frontend expectations liên quan.

## 8. Security
Luôn kiểm tra:
- authentication
- role/permission
- resource ownership
- input validation
- lộ dữ liệu nhạy cảm
- HTTP status/error
- truy cập resource bằng ID
- tính nhất quán transaction

Không trả về field mà caller không có quyền xem.

## 9. Testing
Dùng test stack hiện có. Chọn đúng tầng:
- Backend unit/service
- Controller/API
- Repository/integration khi cần
- Security/authorization khi có access rule
- Frontend component/BLoC khi UI behavior thay đổi

Ưu tiên test non-interactive trong workflow của agent.

## 10. Verification
Trước khi kết thúc:
- kiểm tra file đã đổi
- chạy tests liên quan
- chạy build/typecheck/lint nếu có
- kiểm tra tác động API/database
- đảm bảo không đổi file ngoài phạm vi
- nêu rõ risk còn lại

Không được nói test pass nếu chưa thực sự chạy.
