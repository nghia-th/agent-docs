# doc-07 — Hướng dẫn Vận hành Thủ công (Manual Runbook)

> Cách chạy pipeline **bằng tay** trên các app model (không cần CrewAI/Flowise/n8n). Product Owner (anh) tự duyệt trước khi sang bước kế. 6 file doc-01→06 đóng vai **system prompt** cho từng agent.

## 0. Nguyên tắc chung
* **b1→b3 chạy ở chat app** (thiết kế, sinh tài liệu). **b4→b6 chạy ở IDE agent** (Claude Code / Cursor) vì cần đụng file repo thật. **b7 = anh nghiệm thu**.
* **Nối tay (Chaining):** output bước trước = input bước sau. Chỉ dán tài liệu **đã duyệt**, đừng dựa trí nhớ chat cũ.
* **Task Tracker** (`task-tracker.md`) là nơi theo dõi trạng thái task (doc-00 Mục 10.6).

## 1. Chuẩn bị một lần (Setup)
1. Tạo 6 "hồ sơ agent", mỗi cái nạp doc tương ứng làm **custom instruction** (Claude Project / Custom GPT / Gemini Gem):
   * `ba_agent` → doc-01 | `architect_agent` → doc-02 | `detail_designer_agent` → doc-03
   * `coder_agent` → doc-04 | `tester_agent` → doc-05 | `reviewer_agent` → doc-06
2. Gán **model tùy vai** (ví dụ BA dùng model A, Architect/Coder dùng model B) — đây chính là "model swappable" khi chạy tay.
3. Tạo sẵn thư mục lưu output trong repo: `prd.md`, `system-design.md`, `detail-design.md`, `task-tracker.md`.

## 2. Quy trình từng bước

| Bước | App / Nơi chạy | Nạp instruction | Dán vào (Input) | Nhận ra (Output) | Cổng duyệt | Cập nhật Tracker |
|---|---|---|---|---|---|---|
| 1. Phân tích yêu cầu | Chat app | doc-01 | Ý tưởng của anh | `prd.md` | **PO duyệt** | — |
| 2. Thiết kế hệ thống | Chat app | doc-02 | `prd.md` | `system-design.md` | **PO duyệt** | — |
| 3. Thiết kế chi tiết + Task | Chat app | doc-03 | `system-design.md` + `prd.md` | `detail-design.md` + `task-tracker.md` (mọi task = `Todo`) | **PO duyệt** | Khởi tạo Tracker |
| 4. Code | IDE agent | doc-04 | mở repo + `detail-design.md` + `task-tracker.md` | code + Post-Coding Summary | — | `In-Progress` → `Coded` |
| 5. Test | IDE agent | doc-05 | code + task `Coded` | Test Report (+ Bug Report nếu fail) | — | `Test-Pass` / `Test-Fail` |
| 6. Review | IDE agent / Chat | doc-06 | code task `Test-Pass` | Review Report (verdict) | — | `Review-Pass` / `Review-Fail` |
| 7. Nghiệm thu | Anh (PO) | — | tất cả output | Chấp nhận & triển khai | **PO nghiệm thu** | `Accepted` |

> **Entry note khi dán:** mở mỗi tài liệu theo thứ tự đọc đã ghi (doc-00 Mục 10.5). VD Architect đọc PRD từ Mục 1→4; Coder mở `task-tracker.md`/Sơ đồ Task trước.

### 2.1. Chọn task kế tiếp khi chạy tay (thay cho orchestrator)
* Chạy tay tuần tự → **không cần agent điều phối**; anh chính là người phân task.
* Quy tắc chọn task kế: trong `task-tracker.md`, lấy task **`Todo` đã thỏa phụ thuộc** (task cha đã xong), rồi chọn **ưu tiên cao nhất** (Must → Should → Could) để làm.
* **Một lượt một task**: làm xong (tới `Coded`/`Test-Pass`/`Review-Pass`/`Accepted`) mới lấy task kế. LLM không có trạng thái 'rảnh/bận', nên chạy song song nhiều coder chỉ cần khi tự động hoá (script hàng đợi).

## 3. Vòng lặp sửa lỗi
* `Test-Fail` hoặc `Review-Fail` → đưa Bug Report/Review Feedback cho `coder_agent` → kéo task về `In-Progress` → sửa → `Coded` → test lại → review lại → khi `Review-Pass` mới trình PO.

## 4. Giữ chất lượng khi chạy tay
* **Context Isolation:** mỗi module một phiên chat riêng, chỉ nạp tài liệu của **đúng module đó** (tránh nhồi cả repo).
* **Truy vết:** giữ nguyên ID `US/FR/NFR/T-xx` xuyên suốt để soi ngược task ↔ yêu cầu.
* **Bám chuẩn:** Coding Conventions do `architect_agent` đặt (trong `system-design.md`) là chuẩn cho Coder và checklist cho Reviewer.

## 5. Mẹo thực dụng
* Lưu output mỗi bước thành **file trong repo** để bước sau và IDE agent đọc trực tiếp (thay vì copy tay dài dòng).
* Khi giao b4 cho IDE agent, chỉ cần trỏ nó đọc `detail-design.md` + `task-tracker.md` là đủ ngữ cảnh.
* Muốn nhẹ hơn nữa: gộp b5+b6 nếu dự án nhỏ; nhưng giữ nguyên nguyên tắc "người review khác người code".
