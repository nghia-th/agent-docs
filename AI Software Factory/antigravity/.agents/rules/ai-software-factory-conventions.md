---
name: ai-software-factory-conventions
description: Quy ước chung AI Software Factory — áp dụng cho MỌI agent (Always On).
trigger: always_on
---

# AI Software Factory — Quy ước chung (áp dụng cho mọi agent)

## Pipeline 7 bước (+ Bước 2.5 nếu có giao diện) & agent phụ trách
0. (Chỉ brownfield, một lần) Khảo sát codebase — `architect-agent` → `docs/codebase-overview.md`
1. Phân tích yêu cầu — `ba-agent` → PRD, User Stories, User Flow
2. Thiết kế hệ thống — `architect-agent` → kiến trúc, API contract, ERD, coding conventions
2.5. (Chỉ khi dự án có giao diện) Thiết kế UI/UX — `ui-ux-agent` → `docs/ux/design-system.md` + `docs/ux/ux-spec-<module>.md` (màn hình `SCR-xx`)
3. Thiết kế chi tiết + chia Task — `detail-designer-agent` → Detail Design + Task Tracker
4. Viết code — `backend-coder-agent` (task `[BE]`), `frontend-coder-agent` (task `[FE]`); mỗi agent chỉ nhận task đúng nhãn
5. Test — `tester-agent`
6. Review — `reviewer-agent`
7. Nghiệm thu — Product Owner (con người)

## Cổng duyệt của Product Owner (human)
- Sau Bước 0 (duyệt codebase-overview, brownfield), sau Bước 1 (duyệt yêu cầu), sau Bước 2 (duyệt System Design), sau Bước 2.5 (duyệt Design System & UX Spec, nếu có giao diện), sau Bước 3 (duyệt Detail Design & sơ đồ task), Bước 7 (nghiệm thu code).
- Không tự chuyển bước khi chưa có phê duyệt của PO ở các mốc này.

## Vòng lặp sửa lỗi
- Bước 4→5→6 lặp: Test-Fail/Review-Fail → về coder (backend/frontend đúng nhãn) sửa → test lại → review lại. Chỉ khi test PASS + review PASS mới trình PO nghiệm thu. Cùng một task Fail 2 lần liên tiếp → coder dừng (Halt & Query), PO can thiệp.

## Truy vết (Traceability)
- BA sinh ID: `US-xx`, `FR-xx`, `NFR-xx`.
- Task mang ID `T-xx` và tham chiếu ngược `US-xx`/`FR-xx`.
- Mọi API/bảng/module/màn hình/task đều map ngược về FR/US.

## Độ ưu tiên
- MoSCoW (`Must/Should/Could/Won't`) do BA gắn cho từng User Story; các bước sau dùng làm căn cứ Priority Mapping.

## Ngôn ngữ
- Tài liệu nghiệp vụ & thiết kế (PRD, System Design, Detail Design, Task map): tiếng Việt.
- Mã nguồn và comment trong code: tiếng Anh.

## Task Tracker (nguồn sự thật duy nhất về trạng thái task)
- File dùng chung: `task-tracker.md` (một file/module), do `detail-designer-agent` khởi tạo (mọi task = `Todo`).
- Vòng đời: `Todo` → `Planning` → `In-Progress` → `Coded` → `Test-Pass` → `Review-Pass` → `Accepted`. `Test-Fail`/`Review-Fail` → coder đúng nhãn chuyển task về `In-Progress` khi bắt đầu sửa (tester/reviewer chỉ đặt trạng thái Fail).
- Ai cập nhật: coder (`Planning`,`In-Progress`,`Coded`); tester (`Test-Pass`/`Test-Fail`); reviewer (`Review-Pass`/`Review-Fail`); PO (`Accepted`).
- Cột: `Task ID | Loại (BE/FE) | Mô tả | FR/US | Ưu tiên | Phụ thuộc | Trạng thái | Cập nhật bởi | Ghi chú`.

## Điểm vào & Thứ tự đọc (Entry note)
- Mỗi tài liệu bàn giao mở đầu bằng Entry note chỉ rõ agent nhận đọc từ đâu.
- architect đọc PRD: Tổng quan→User Stories→FR/NFR→Ràng buộc.
- ui-ux đọc PRD (User Stories→User Flow→Nền tảng) rồi System Design (tech stack frontend, UI library, API).
- detail-designer đọc System Design: Thành phần→API→ERD→Coding Conventions; đọc PRD lấy Acceptance Criteria; nếu có giao diện đọc UX Spec (`SCR-xx`).
- coder (task FE đọc thêm UX Spec + Design System) đọc Detail Design: Sơ đồ Task trước → đặc tả task tham chiếu → Coding Conventions → Acceptance Criteria.
- tester đọc Detail Design: Sơ đồ Task → DoD + Acceptance Criteria từng task.
- reviewer đọc: Coding Conventions + Detail Design + code, đối chiếu Acceptance Criteria/DoD.

## Nguyên tắc nền
- Agent định danh theo VAI TRÒ; model là cấu hình swappable (đổi model không đổi vai/prompt/pipeline).
- Chaining: output bước trước đã duyệt = input bước sau; không tự suy diễn từ ngữ cảnh rời rạc.
- Context Isolation: chỉ nạp tài liệu của đúng module đang làm.
- Brownfield: tôn trọng & tái sử dụng codebase/stack hiện có; không code thừa; không tự đổi thiết kế đã duyệt.
