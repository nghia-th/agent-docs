# doc-07 — Hướng dẫn Vận hành Thủ công (Manual Runbook)

> Cách chạy pipeline **bằng tay** trên các app model (không cần CrewAI/Flowise/n8n). Product Owner (anh) tự duyệt trước khi sang bước kế. 6 file doc-01→06 đóng vai **system prompt** cho từng agent.

---

## 0. Nguyên tắc chung

* **b1→b3 chạy ở chat app** (thiết kế, sinh tài liệu). **b4→b6 chạy ở IDE agent** (Claude Code / Cursor) vì cần đụng file repo thật. **b7 = anh nghiệm thu**.
* **Nối tay (Chaining):** output bước trước = input bước sau. Chỉ dán tài liệu **đã duyệt**, đừng dựa trí nhớ chat cũ.
* **Task Tracker** (`task-tracker.md`) là nguồn sự thật duy nhất về tiến độ (doc-00 Mục 10.6).
* **Context Isolation:** mỗi module một phiên chat riêng, chỉ nạp tài liệu của đúng module đó.
* **Một lượt một task:** làm xong (tới `Planning`/`Coded`/`Test-Pass`/`Review-Pass`/`Accepted`) mới lấy task kế.

---

## 1. Chuẩn bị một lần (Setup)

### 1.1. Tạo hồ sơ agent

Tạo 8 "hồ sơ agent" (7 nếu dự án không có giao diện: bỏ `ui_ux_agent` và `frontend_coder_agent`), mỗi cái nạp doc tương ứng làm **custom instruction** (Claude Project / Custom GPT / Gemini Gem):

| Agent | Doc nạp | Môi trường chạy |
|---|---|---|
| `ba_agent` | doc-01 | Chat app |
| `architect_agent` | doc-02 | Chat app |
| `ui_ux_agent` | doc-08 | Chat app |
| `detail_designer_agent` | doc-03 | Chat app |
| `backend_coder_agent` | doc-04 | IDE agent |
| `frontend_coder_agent` | doc-04 + doc-09 (nạp nối tiếp, doc-09 sau doc-04) | IDE agent |
| `tester_agent` | doc-05 | IDE agent |
| `reviewer_agent` | doc-06 | IDE agent / Chat |

### 1.2. Gán model theo vai

Gán **model tùy vai** (đây chính là "model swappable" khi chạy tay):

| Vai | Khuyến nghị model | Lý do |
|---|---|---|
| BA, Architect | Model mạnh (GPT-4o+, Claude Opus) | Cần suy luận sâu, phân tích ngữ cảnh lớn |
| Detail Designer | Model mạnh (GPT-4o+, Claude Opus) | Cần độ chính xác cao khi phân rã task |
| UI/UX | Model mạnh, giỏi bố cục và ngôn ngữ giao diện | Thiết kế đặc tả giao diện nhất quán, đủ trạng thái |
| Coder (backend, frontend) | Model mạnh (GPT-4o+, Claude Sonnet+) | Code chính xác, bám sát convention; frontend_coder có thể dùng model khác backend_coder |
| Tester | Model trung bình (GPT-4o-mini, Claude Haiku) | Sinh test case/boilerplate, giảm chi phí |
| Reviewer | Model mạnh (khác model Coder) | Tránh thiên kiến, bắt lỗi khách quan |

### 1.3. Tạo cấu trúc thư mục output

Tạo sẵn thư mục trong repo:

```
project-root/
└── docs/
    ├── codebase-overview.md ← Output bước 0 (brownfield)
    ├── prd.md              ← Output bước 1
    ├── system-design.md    ← Output bước 2
    ├── ux/                 ← Output bước 2.5 (design-system.md, ux-spec-<module>.md)
    ├── detail-design.md    ← Output bước 3
    ├── task-tracker.md     ← Output bước 3 (khởi tạo)
    ├── plans/              ← Output bước 4 (plan_T-xx.md, mỗi task 1 file)
    ├── coding-summary/     ← Output bước 4 (T-xx.md, mỗi task 1 file)
    ├── test-reports/       ← Output bước 5
    ├── bug-reports/        ← Output bước 5 (khi fail)
    └── review-reports/     ← Output bước 6
```

---

## 2. Quy trình từng bước (chi tiết)

### Bảng tổng quan

| Bước | App | Instruction | Input | Output | Cổng duyệt | Cập nhật Tracker |
|---|---|---|---|---|---|---|
| 0. Khảo sát codebase *(brownfield, một lần)* | IDE agent | doc-02 (Mục 0) | Repo hiện có | `codebase-overview.md` | **PO duyệt** | — |
| 1. Phân tích yêu cầu | Chat | doc-01 | Ý tưởng của anh | `prd.md` | **PO duyệt** | — |
| 2. Thiết kế hệ thống | Chat | doc-02 | `prd.md` | `system-design.md` | **PO duyệt** | — |
| 2.5. Thiết kế UI/UX *(chỉ khi có giao diện)* | Chat | doc-08 | `prd.md` + `system-design.md` | `docs/ux/design-system.md` + `ux-spec-<module>.md` | **PO duyệt** | — |
| 3. Thiết kế chi tiết + Task | Chat | doc-03 | `system-design.md` + `prd.md` (+ `docs/ux/`) `detail-design.md` + `task-tracker.md` | **PO duyệt** | Khởi tạo |
| 4. Code | IDE | doc-04 (backend); doc-04 + doc-09 (frontend) | `detail-design.md` + `task-tracker.md` (+ `docs/ux/` cho task FE) | `plan_T-xx.md` → code + Post-Coding Summary | — | `Todo` → `Planning` → `In-Progress` → `Coded` |
| 5. Test | IDE | doc-05 | code task `Coded` | Test Report (+ Bug Report nếu fail) | — | `Test-Pass` / `Test-Fail` |
| 6. Review | IDE/Chat | doc-06 | code task `Test-Pass` | Review Report | — | `Review-Pass` / `Review-Fail` |
| 7. Nghiệm thu | Anh (PO) | — | tất cả output | Chấp nhận & triển khai | **PO nghiệm thu** | `Accepted` |

### 2.0. Bước 0 — Khảo sát codebase (Architect Agent, chỉ brownfield, một lần)

**Chuẩn bị:** mở IDE agent (cần đọc repo thật), chọn hồ sơ `architect_agent` (doc-02, Mục 0).

**Prompt mẫu:**
```
Thực hiện Bước 0 (Mục 0 trong doc-02) cho repo này. Chỉ đọc, KHÔNG sửa code.
Xuất docs/codebase-overview.md đúng template 9 mục. Lệnh build/lint/test phải là lệnh thật chạy được trong repo.
Chỗ nào không chắc, ghi vào Mục 9 "Cần PO xác nhận", đừng đoán.
```

**Kiểm tra đầu ra:**
- [ ] Đủ 9 mục; lệnh build/lint/test đối chiếu đúng với file cấu hình trong repo
- [ ] Coding Conventions rút ra từ code thực tế, không bịa

**PO duyệt** rồi mới sang bước 1/2.

### 2.1. Bước 1 — Phân tích yêu cầu (BA Agent)

**Chuẩn bị:**
- Mở chat app, chọn hồ sơ `ba_agent` (đã nạp doc-01).
- Có sẵn: ý tưởng dự án, yêu cầu kinh doanh từ PO.

**Prompt mẫu:**
```
Tôi cần bạn phân tích yêu cầu cho dự án sau:
[Tên dự án / Mô tả ngắn gọn]

Yêu cầu từ Product Owner:
- [Yêu cầu 1]
- [Yêu cầu 2]
- ...

Hãy xuất ra tài liệu PRD đầy đủ theo template, bao gồm:
- Tổng quan & Mục tiêu
- User Stories (có gán priority MoSCoW)
- Yêu cầu chức năng (FR-xx) và phi chức năng (NFR-xx)
- User Flow (mô tả hoặc Mermaid diagram)
- Ràng buộc & Giả định
- Acceptance Criteria cho từng US
```

**Kiểm tra đầu ra:**
- [ ] File `prd.md` có đầy đủ các mục theo template doc-01
- [ ] Mỗi yêu cầu có ID (`US-xx`, `FR-xx`, `NFR-xx`)
- [ ] Có gán priority MoSCoW cho từng US
- [ ] Không chứa nội dung thiết kế kỹ thuật
- [ ] Tài liệu tự chứa, không có `[TBD]`

**PO duyệt:** Đọc kỹ, chỉnh sửa nếu cần. Chỉ chuyển sang bước 2 khi PRD đã được duyệt.

### 2.2. Bước 2 — Thiết kế hệ thống (Architect Agent)

**Chuẩn bị:**
- Mở chat app, chọn hồ sơ `architect_agent` (đã nạp doc-02).
- Dán toàn bộ nội dung `prd.md` đã duyệt (và `codebase-overview.md` đã duyệt nếu là brownfield).

**Prompt mẫu:**
```
Dưới đây là PRD đã được PO duyệt. Hãy thiết kế kiến trúc hệ thống:

[PASTE toàn bộ prd.md]

Yêu cầu đầu ra:
- Kiến trúc tổng thể (Component Diagram)
- Tech Stack đề xuất (kèm lý do)
- API Contracts (REST/GraphQL endpoints)
- ERD / Data Model
- Coding Conventions (cho toàn dự án)
- Security & Performance considerations
```

**Kiểm tra đầu ra:**
- [ ] File `system-design.md` có đầy đủ các mục theo template doc-02
- [ ] Không thiết kế vượt ngoài phạm vi PRD
- [ ] Coding Conventions rõ ràng, đủ để Coder và Reviewer dùng
- [ ] Không có `[TBD]`

**PO duyệt:** Xác nhận tech stack, kiến trúc, và coding conventions trước khi sang bước 3.

### 2.2b. Bước 2.5 — Thiết kế UI/UX (UI/UX Agent, chỉ khi dự án có giao diện)

**Chuẩn bị:**
- Mở chat app, chọn hồ sơ `ui_ux_agent` (đã nạp doc-08).
- Dán (hoặc trỏ tới) PRD đã duyệt của module cần thiết kế và `system-design.md` (tech stack frontend, UI library, API contract). Nếu dự án chia nhiều PRD: chạy từng module một, dùng chung Design System.

**Prompt mẫu:**
```
Bạn là ui_ux_agent. Đọc doc-08 (đã nạp), PRD [file] và System Design [file].
Nhiệm vụ: thiết kế UI/UX cho module này. Lần đầu: tạo docs/ux/design-system.md; sau đó tạo docs/ux/ux-spec-<module>.md.
Việc đầu tiên: hỏi tôi TỪNG CÂU MỘT theo Mục 3.1 của doc-08 (kèm 2-3 phương án gợi ý, tôi có thể trả lời "tự quyết"). Khi hết câu hỏi, tóm tắt quyết định và giả định, rồi DỪNG. TUYỆT ĐỐI không ghi file cho đến khi tôi gõ "Approved".
```

**Kiểm tra đầu ra:**
- [ ] `design-system.md` có token đặt tên và danh mục component; `ux-spec-<module>.md` có danh sách màn hình `SCR-xx`
- [ ] Mọi `US`/`FR` có giao diện đều map tới màn hình; mọi màn hình map ngược `US`/`FR`
- [ ] Mỗi màn hình đủ trạng thái Loading/Empty/Error/Success, nội dung chữ, responsive, tiếp cận
- [ ] Mỗi vùng dữ liệu chỉ ra endpoint API; thiếu API được ghi ở mục "Đề nghị bổ sung cho Architect" (không tự thêm API)
- [ ] Chỉ thiết kế cho nền tảng PRD yêu cầu; không có code sản phẩm; không có `[TBD]`

**PO duyệt:** cổng QA sau Bước 2.5 — duyệt giao diện trước khi chia task. Mục "Đề nghị bổ sung cho Architect" nếu có thì PO chuyển cho `architect_agent` cập nhật System Design trước Bước 3.

### 2.3. Bước 3 — Thiết kế chi tiết & Lập Task (Detail Designer)

**Chuẩn bị:**
- Mở chat app, chọn hồ sơ `detail_designer_agent` (đã nạp doc-03).
- Dán `prd.md` + `system-design.md` đã duyệt (và `docs/ux/` nếu có giao diện).

**Prompt mẫu:**
```
Dưới đây là PRD và System Design đã duyệt. Hãy thiết kế chi tiết:

=== PRD ===
[PASTE prd.md]

=== System Design ===
[PASTE system-design.md]

Yêu cầu đầu ra:
1. Detail Design cho từng component/module (pseudocode, data flow, state management)
2. Sơ đồ Task (Task Map) — phân rã công việc thành các task T-xx
3. File task-tracker.md — tất cả task khởi tạo với status "Todo"
   - Cột: Task ID | Type (BE/FE) | Description | FR/US | Priority | Depends-on | Status | Updated-by | Notes
4. Gắn nhãn [BE]/[FE] cho từng task; ánh xạ màn hình SCR-xx → API → task (không thiết kế lại giao diện)
```

**Kiểm tra đầu ra:**
- [ ] File `detail-design.md` — mỗi component có đặc tả/pseudocode rõ ràng
- [ ] File `task-tracker.md` — mọi task = `Todo`, có dependency & priority, có nhãn loại BE/FE
- [ ] Mỗi `T-xx` tham chiếu ngược `US-xx`/`FR-xx`
- [ ] Task map tuân theo thứ tự ưu tiên MoSCoW
- [ ] Không có `[TBD]`

**PO duyệt:** Đây là cổng QA quan trọng — duyệt thứ tự thi công và phạm vi từng task.

### 2.4. Bước 4 — Viết code (Backend/Frontend Coder Agent)

**Chuẩn bị:**
- Mở IDE agent (Claude Code / Cursor), chọn hồ sơ theo nhãn task: task `[BE]` → `backend_coder_agent` (doc-04); task `[FE]` → `frontend_coder_agent` (doc-04 + doc-09). Mỗi agent chỉ làm task đúng nhãn.
- Mở repo project. Đảm bảo agent đọc được file trong repo.

**Prompt mẫu (giao 1 task):**
```
Đọc các file sau trong repo:
- docs/detail-design.md
- docs/task-tracker.md
- docs/system-design.md (phần Coding Conventions)
- docs/prd.md (phần Acceptance Criteria)

Chọn task đầu tiên thỏa: status = "Todo", đúng nhãn loại của agent này (BE hoặc FE), priority = Must, không phụ thuộc task chưa xong. Task FE đọc thêm docs/ux/ (màn hình SCR-xx liên quan + design-system.md).

Thực hiện task đó:
1. Đọc tracker + `docs/plans/` xem task nào đang dở (làm tiếp, không lập Plan lại); khảo sát code có sẵn để tái sử dụng
1b. **Lập Plan:** Tạo `docs/plans/plan_T-xx.md` (Files, Functions, APIs, Code tái sử dụng, Execution Order, Risks)
2. Cập nhật task-tracker: status → "Planning"
3. **PO có thể xem Plan** — nếu sai hướng sẽ yêu cầu sửa trước khi code
4. Cập nhật task-tracker: status → "In-Progress"
5. Tạo nhánh `task/T-xx-ten-task`, viết code theo đúng Plan đã lập (KHÔNG tự merge vào nhánh chính)
6. Tuân thủ Coding Conventions trong system-design.md
7. Chạy lint + build + test có sẵn liên quan (không phát sinh lỗi mới), rồi cập nhật task-tracker: status → "Coded"
8. Viết Post-Coding Summary vào docs/coding-summary/T-xx.md (có mục Plan vs Actual)
```

### 2.5. Bước 5 — Test (Tester Agent)
**Chuẩn bị:**
- Mở IDE agent (session riêng, khác Coder), chọn hồ sơ `tester_agent` (đã nạp doc-05).
- Chỉ test task đã `Coded`.
- Checkout nhánh `task/T-xx-...` của coder; commit test trên nhánh đó (`T-xx: test [FR-xx] ...`), chỉ sửa file test, không sửa code sản phẩm.

**Prompt mẫu:**
```
Đọc docs/detail-design.md (phần Sơ đồ Task) và docs/task-tracker.md.
Tìm task có status = "Coded".

Với mỗi task Coded:
1. Viết unit test / integration test
2. Chạy test
3. Nếu PASS: cập nhật task-tracker → "Test-Pass", viết Test Report
4. Nếu FAIL: cập nhật task-tracker → "Test-Fail", viết Bug Report (có: lỗi gì, file nào, dòng nào, cách tái hiện, gợi ý sửa)
```

**Kiểm tra đầu ra:**
- [ ] Task Tracker đã cập nhật (`Test-Pass` / `Test-Fail`)
- [ ] Test Report có: task ID, danh sách test case, kết quả
- [ ] Bug Report (nếu fail) đầy đủ: severity, vị trí, cách tái hiện, gợi ý sửa

### 2.6. Bước 6 — Review (Reviewer Agent)

**Chuẩn bị:**
- Mở IDE agent hoặc Chat, chọn hồ sơ `reviewer_agent` (đã nạp doc-06).
- Chỉ review task đã `Test-Pass`.
- **Quan trọng:** Reviewer là agent KHÁC với Coder.

**Prompt mẫu:**
```
Đọc các file:
- docs/task-tracker.md (tìm task "Test-Pass")
- docs/system-design.md (phần Coding Conventions)
- docs/detail-design.md (đặc tả task đó)
- Code của task

Review và kiểm tra:
1. Code có đúng Coding Conventions không?
2. Code có bám sát Detail Design không?
3. Có code thừa / logic sai không?
4. Test có cover đúng logic không?

Kết quả:
- PASS: cập nhật task-tracker → "Review-Pass", viết Review Report
- FAIL: cập nhật task-tracker → "Review-Fail", viết Review Report (mỗi finding có: severity + vị trí + lý do + gợi ý sửa)
```

**Kiểm tra đầu ra:**
- [ ] Task Tracker đã cập nhật (`Review-Pass` / `Review-Fail`)
- [ ] Review Report có: verdict, danh sách findings (nếu có)
- [ ] Mỗi finding có severity (Blocker/Major/Minor) + vị trí + gợi ý
- [ ] Ngôn ngữ tiếng Việt

### 2.7. Bước 7 — Nghiệm thu (Product Owner)

**PO thực hiện:**
1. Kiểm tra tất cả task `Review-Pass` trong Task Tracker
2. Đọc code, chạy thử nếu cần
3. Nếu OK → cập nhật task → `Accepted`
4. Nếu không OK → ghi lý do vào cột Notes của task và giao lại cho `coder_agent`; `coder_agent` sẽ chuyển task về `In-Progress` khi bắt đầu sửa

---

## 3. Cách chọn task khi chạy tay

* Chạy tay tuần tự → **không cần agent điều phối**; anh chính là người phân task.
* Quy tắc chọn task kế: trong `task-tracker.md`, lấy task **`Todo` đã thỏa phụ thuộc** (task cha đã xong), rồi chọn **ưu tiên cao nhất** (Must → Should → Could) để làm.
* **Một lượt một task**: làm xong (tới `Planning`/`Coded`/`Test-Pass`/`Review-Pass`/`Accepted`) mới lấy task kế.
* LLM không có trạng thái 'rảnh/bận', nên chạy song song nhiều coder chỉ cần khi tự động hoá (script hàng đợi).

---

## 4. Vòng lặp sửa lỗi

```
Task: Todo → Planning → In-Progress → Coded → Test → Test-Pass → Review → Review-Pass → PO → Accepted
                    ↘ Test-Fail                ↘ Review-Fail
                       ↓                          ↓
                    Bug Report                Review Report
                       ↓                          ↓
                    Coder sửa                 Coder sửa
                       ↓                          ↓
          coder chuyển → In-Progress   coder chuyển → In-Progress
                       ↓                          ↓
                    Code lại → Coded          Code lại → Coded
                       ↓                          ↓
                    Test lại...               Test lại → Review lại...
```

**Quy tắc:**
- `Test-Fail` hoặc `Review-Fail` → tester/reviewer chỉ đặt trạng thái Fail và đưa Bug Report/Review Feedback cho `coder_agent`
- `coder_agent` chuyển task về `In-Progress` khi bắt đầu sửa → `Coded` → test lại → review lại
- Chỉ khi `Review-Pass` mới trình PO nghiệm thu

---

## 5. Giữ chất lượng khi chạy tay

* **Context Isolation:** mỗi module một phiên chat riêng, chỉ nạp tài liệu của **đúng module đó** (tránh nhồi cả repo).
* **Truy vết:** giữ nguyên ID `US/FR/NFR/T-xx` xuyên suốt để soi ngược task ↔ yêu cầu.
* **Bám chuẩn:** Coding Conventions do `architect_agent` đặt (trong `system-design.md`) là chuẩn cho Coder và checklist cho Reviewer.
* **Tách biệt phiên:** mỗi agent dùng một phiên chat/project riêng. Không dùng chung phiên giữa Coder và Reviewer.

---

## 6. Xử lý sự cố thường gặp

### 6.1. Agent sinh output sai định dạng / thiếu mục

**Triệu chứng:** Output thiếu section, không theo template, hoặc sai định dạng Markdown.

**Cách xử lý:**
1. Dán lại toàn bộ doc hướng dẫn của agent đó (doc-0X) vào đầu prompt.
2. Nhấn mạnh: "Hãy xuất output theo ĐÚNG template ở Mục 4, không được bỏ sót mục nào."
3. Nếu vẫn sai → tách nhỏ prompt, yêu cầu agent sinh từng phần một.

### 6.2. Agent bịa ra yêu cầu / tính năng không có trong PRD

**Triệu chứng:** Architect hoặc Detail Designer thêm tính năng không có trong PRD.

**Cách xử lý:**
1. Prompt lại: "Chỉ thiết kế những gì có trong PRD. Nếu có ý tưởng thêm, ghi vào mục 'Gợi ý mở rộng' riêng, không đưa vào thiết kế chính."
2. Kiểm tra kỹ output trước khi duyệt.

### 6.3. Coder bỏ qua Coding Conventions

**Triệu chứng:** Code không theo style guide, đặt tên sai convention.

**Cách xử lý:**
1. Trong prompt giao task, luôn nhắc: "Đọc system-design.md → Coding Conventions trước khi code."
2. Nếu vẫn sai → thêm vào prompt: "Trước khi xuất code, tự kiểm tra lại Coding Conventions Mục X trong system-design.md."
3. Reviewer sẽ bắt lỗi này ở bước 6.

### 6.4. Task Tracker không được cập nhật

**Triệu chứng:** Agent code/test/review xong nhưng quên cập nhật `task-tracker.md`.

**Cách xử lý:**
1. Trong mỗi prompt giao việc, thêm dòng: "Việc đầu tiên: cập nhật task-tracker.md. Việc cuối cùng: cập nhật task-tracker.md."
2. Kiểm tra tracker sau mỗi bước. Nếu thiếu → yêu cầu agent cập nhật bổ sung.

### 6.5. Agent "ảo giác" — bịa file/thư mục không tồn tại

**Triệu chứng:** Agent tham chiếu file không có trong repo.

**Cách xử lý:**
1. Luôn bắt đầu prompt bằng: "Hãy liệt kê các file hiện có trong repo trước khi bắt đầu."
2. Yêu cầu agent dùng đường dẫn tuyệt đối hoặc tương đối chính xác từ gốc repo.

### 6.6. Context window quá tải

**Triệu chứng:** Agent bỏ sót thông tin, output thiếu hoặc sai ở phần sau.

**Cách xử lý:**
1. Chỉ nạp tài liệu liên quan đến task hiện tại (Context Isolation).
2. Với dự án lớn, chia nhỏ PRD/Design thành nhiều file theo module.
3. Nếu prompt quá dài → tóm tắt phần không liên quan, chỉ giữ nguyên phần task hiện tại.

### 6.7. Vòng lặp sửa lỗi không kết thúc

**Triệu chứng:** Task bị kẹt trong vòng Test-Fail → Sửa → Test-Fail → Sửa...

**Cách xử lý:**
1. Sau **2 lần fail liên tiếp** của cùng một task → `coder_agent` dừng (Halt & Query), PO can thiệp: đọc Bug Report/Review Report, xác định có phải lỗi thiết kế không.
2. Nếu lỗi thiết kế → quay lại Detail Designer sửa `detail-design.md`.
3. Nếu lỗi implementation → thử đổi model mạnh hơn cho Coder.
4. Không cho coder sửa lần thứ 3 khi chưa có chỉ đạo của PO.

---

## 7. Mẹo thực dụng

### 7.1. Tăng tốc pipeline

* **Gộp b5+b6 nếu dự án nhỏ:** nhưng giữ nguyên tắc "người review khác người code".
* **Song song hóa task độc lập:** nếu có 2 task `Todo` không phụ thuộc nhau → giao cho 2 IDE agent session riêng cùng lúc.
* **Dùng model nhẹ cho Tester:** GPT-4o-mini hoặc Claude Haiku đủ sức viết test case, tiết kiệm chi phí.
* **Template sẵn:** tạo file template cho Post-Coding Summary, Test Report, Review Report để agent chỉ cần điền vào.

### 7.2. Tránh lỗi phổ biến

* **Không dùng chung phiên chat:** mỗi agent một phiên riêng. KHÔNG chat tiếp trong phiên cũ.
* **Luôn dán lại toàn bộ tài liệu:** đừng dựa vào "chat history" — model có thể quên.
* **Lưu output thành file:** mỗi bước xong → lưu ngay vào `docs/`. Bước sau đọc file, không copy-paste thủ công.
* **Khi giao b4 cho IDE agent:** chỉ cần trỏ nó đọc `detail-design.md` + `task-tracker.md` là đủ ngữ cảnh.
* **Dùng Mermaid cho diagram:** PRD và System Design nên dùng Mermaid syntax để dễ render và dễ sửa.

### 7.3. Chuẩn bị cho tự động hóa sau này

Dù đang chạy tay, hãy giữ cấu trúc sao cho dễ chuyển sang CrewAI sau:
* File output đặt trong `docs/` với tên chuẩn (`prd.md`, `system-design.md`, ...)
* Task Tracker giữ đúng format bảng Markdown
* ID nhất quán (`US-xx`, `FR-xx`, `T-xx`) xuyên suốt
* Post-Coding Summary / Test Report / Review Report đặt trong thư mục con riêng

---

## 8. Checklist vận hành (Quick Reference)

### Trước mỗi dự án mới
- [ ] Đã tạo 8 hồ sơ agent (7 nếu không có giao diện) với doc-01→09 làm custom instruction (frontend_coder_agent = doc-04 + doc-09)
- [ ] Đã gán model phù hợp cho từng agent
- [ ] Đã tạo thư mục `docs/` với cấu trúc chuẩn
- [ ] Đã có ý tưởng/yêu cầu ban đầu từ PO

### Sau mỗi bước
- [ ] Output đã lưu thành file trong `docs/`
- [ ] PO đã duyệt (với bước 1, 2, 3)
- [ ] Task Tracker đã cập nhật (với bước 3, 4, 5, 6); bước 4 có trạng thái Planning
- [ ] File output đúng template, không có `[TBD]`

### Trước khi nghiệm thu (bước 7)
- [ ] Tất cả task trong tracker ở trạng thái `Review-Pass`
- [ ] Mỗi task có đủ: Post-Coding Summary + Test Report + Review Report
- [ ] Không còn Bug Report chưa resolved
- [ ] Code đã pass lint (nếu có cấu hình)

---

## 9. Biểu mẫu tham khảo nhanh

### 9.1. Prompt giao việc — Coder Agent (backend hoặc frontend)

```
Đọc các file trong repo:
- docs/detail-design.md
- docs/task-tracker.md

Chọn task "Todo" ưu tiên cao nhất, đúng nhãn loại của bạn (BE hoặc FE), đã thỏa phụ thuộc. Task FE: đọc thêm docs/ux/ (UX Spec + Design System).
1. Lập Plan → docs/plans/plan_T-xx.md (Files, Functions, APIs, Order, Risks)
2. Cập nhật tracker: status → "Planning"
3. (PO kiểm tra Plan nếu muốn)
4. Cập nhật tracker: status → "In-Progress"
5. Viết code theo Plan + Coding Conventions (system-design.md)
6. Chạy lint + build + test có sẵn liên quan; cập nhật tracker: status → "Coded"
7. Viết Post-Coding Summary (có Plan vs Actual) → docs/coding-summary/T-xx.md
```

### 9.2. Prompt giao việc — Tester Agent
```
Đọc docs/task-tracker.md, tìm task "Coded".
1. Viết và chạy test
2. PASS → tracker → "Test-Pass" + Test Report → docs/test-reports/T-xx.md
3. FAIL → tracker → "Test-Fail" + Bug Report → docs/bug-reports/T-xx.md
```

### 9.3. Prompt giao việc — Reviewer Agent

```
Đọc: task-tracker.md (task "Test-Pass") + system-design.md (Coding Conventions) + detail-design.md + code.
1. Review: convention, design compliance, code quality
2. PASS → tracker → "Review-Pass" + Review Report → docs/review-reports/T-xx.md
3. FAIL → tracker → "Review-Fail" + Review Report (có severity + vị trí + gợi ý)
```

---

## 10. Phụ lục: Mẫu Task Tracker

```markdown
# Task Tracker — [Tên dự án]

| Task ID | Type | Description | FR/US | Priority | Depends-on | Status | Updated-by | Notes |
|---|---|---|---|---|---|---|---|---|
| T-01 | BE | Khởi tạo project structure | FR-01 | Must | — | Accepted | PO | |
| T-02 | BE | Implement auth module | US-01 | Must | T-01 | Coded | backend_coder_agent | |
| T-03 | BE | Implement auth middleware | US-01 | Must | T-01 | Test-Pass | tester_agent | |
| T-04 | BE | Build dashboard API | US-02 | Should | T-01 | In-Progress | backend_coder_agent | |
| T-05 | FE | Build dashboard UI (SCR-01) | US-02 | Should | T-04 | Todo | — | Chờ API T-04 hoặc dùng mock theo OpenAPI |
```

---

*Cập nhật lần cuối: 2026-09-19 — Bổ sung xử lý sự cố, checklist, biểu mẫu prompt, mẫu Task Tracker, bước Planning cho Coder; đồng bộ với doc-04 (khảo sát code, build/test, nhánh task/, không tự merge) và quy tắc trạng thái khi lỗi.*
