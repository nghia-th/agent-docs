# Prompt mẫu cho từng Agent & Checklist khởi tạo Project

> **Cách dùng:** Mỗi khi bắt đầu một Project mới (hoặc một lượt chạy mới của một Agent), copy prompt tương ứng ở Phần 3, thay các chỗ `{{...}}` bằng nội dung của Project. Mỗi lượt chạy là **một phiên (session) mới** để không lẫn ngữ cảnh.
> Các file agent (`.agents/agents/*.md`) đã chứa quy trình chi tiết; prompt ở đây chỉ **giao việc** và trỏ đúng file cần đọc.

## Phần 1. Những chỗ phải thay khi đổi Project

| Ký hiệu | Ý nghĩa | Ví dụ |
| :--- | :--- | :--- |
| `{{PROJECT}}` | Tên Project (chỉ để ghi chú) | e-commerce, orchestration-agent |
| `{{N}}` | Số thứ tự nhóm/PRD | 1, 2, 3 |
| `{{TÊN_NHÓM}}` | Tên nhóm chức năng lấy từ BRD | Quản lý Project & AI Agent |
| `{{PHẦN_BRD}}` | Các Mục của BRD thuộc nhóm này (kèm phần vai trò/phi chức năng liên quan) | Mục 1 + phần Project Access ở Mục 10 |
| `{{FILE_PRD}}` | Tên file PRD | prd-01-project-agent-management.md |
| `{{XX}}` | Tiền tố ID của nhóm (2 chữ cái, không trùng nhóm khác) | PA, WF, CA, AR, AU |
| `{{PRD_ĐÃ_DUYỆT}}` | Danh sách PRD đã duyệt cần đọc thêm (lượt đầu: "không có") | prd-01…, prd-02… |
| `{{ĐIỂM_NỐI}}` | Các điểm nối/quan hệ với PRD khác cần chú ý (nếu có) | Trạng thái đơn hàng ở PRD-02 |
| `{{MODULE}}` | Tên module khi chạy UI/UX theo từng module | checkout, admin |
| `{{T-xx}}` | Mã task đang làm | T-05 |
| `{{TÊN_TASK}}` | Tên ngắn của task, dùng cho tên branch | dang-nhap |
| `{{DS_TASK}}` | Danh sách task cần tester/reviewer xử lý | T-05, T-06 |

Ngoài các ký hiệu trên, khi đổi Project còn phải đổi:
* **`docs/brd.md`**: viết mới hoàn toàn (nguồn yêu cầu gốc, người dùng cung cấp).
* **Cách chia nhóm PRD**: mỗi Project tự chia theo BRD (thường 3–6 PRD); mỗi PRD một tiền tố ID riêng.
* **Model của từng agent** (dòng `model:` trong frontmatter `.agents/agents/*.md`): chọn theo tài khoản/hạn mức của Project.
* **Tech stack, lệnh build/test/lint**: không ghi trong prompt; `architect_agent` ghi vào `system-design.md` và `codebase-overview.md`, các agent sau đọc từ đó.
* **Project không có giao diện**: bỏ Bước 2.5 (`ui_ux_agent`) và mọi task `[FE]`.
* **Project brownfield (đã có code)**: chạy thêm Bước 0 (mục 3.0 dưới đây); Project mới hoàn toàn thì bỏ qua.

**Những thứ KHÔNG đổi giữa các Project:** nội dung các file `.agents/agents/*.md` (sinh từ doc-01…doc-09 bằng `sync_agents.py`), file `.agents/rules/ai-software-factory-conventions.md`, quy tắc Approved, Task Tracker, quy ước branch/commit.

## Phần 2. Khởi tạo Project (làm một lần)

**Bước 1. Tạo thư mục Project và mở git (tùy chọn nhưng nên làm)**
```
mkdir {{PROJECT}} && cd {{PROJECT}}
git init
printf '.DS_Store\n' > .gitignore
```

**Bước 2. Tạo cấu trúc thư mục tài liệu**
```
mkdir -p docs/{prd,ux,plans,coding-summary,test-reports,bug-reports,review-reports}
touch docs/{prd,ux,plans,coding-summary,test-reports,bug-reports,review-reports}/.gitkeep
```

| Thư mục / file | Ai tạo nội dung | Bước |
| :--- | :--- | :--- |
| `docs/brd.md` | Người dùng (PO) đặt vào trước khi chạy BA | Đầu vào |
| `docs/codebase-overview.md` | `architect_agent` | 0 (chỉ brownfield) |
| `docs/prd/prd-0X-*.md` | `ba_agent` | 1 |
| `docs/system-design.md` | `architect_agent` | 2 |
| `docs/ux/design-system.md`, `docs/ux/ux-spec-<module>.md` | `ui_ux_agent` | 2.5 |
| `docs/detail-design.md`, `docs/task-tracker.md` | `detail_designer_agent` | 3 |
| `docs/plans/plan_T-xx.md`, `docs/coding-summary/T-xx.md` | coder | 4 |
| `docs/test-reports/T-xx.md`, `docs/bug-reports/T-xx.md` | `tester_agent` | 5 |
| `docs/review-reports/T-xx.md` | `reviewer_agent` | 6 |

**Bước 3. Cài bộ agent và quy tắc (copy từ repo template)**
```
cp -R "<đường dẫn template>/antigravity/.agents" ./.agents
```
Kiểm tra có đủ 8 file trong `.agents/agents/`: ba, architect, ui-ux, detail-designer, backend-coder, frontend-coder, tester, reviewer; và `.agents/rules/ai-software-factory-conventions.md`.

**Bước 4. Chỉnh model cho từng agent** (dòng `model:` trong frontmatter mỗi file agent) theo lựa chọn của Project.

**Bước 5. Đặt BRD vào `docs/brd.md`.** Nếu còn file yêu cầu cũ (SRS…), để riêng hoặc chuyển vào `docs/archive/`, và dặn BA không đọc.

**Bước 6. Kiểm tra trước khi chạy BA:** có `docs/brd.md`, đủ 8 agent, đủ thư mục, agent đọc được file rule.

## Phần 3. Prompt mẫu cho từng Agent

Quy tắc chung cho mọi lượt: mở **phiên mới**; agent hỏi **một câu mỗi lượt**; chỉ ghi file khi PO gõ đúng chữ **"Approved"**; agent không tự merge hay deploy.

### 3.0 Bước 0 — Khảo sát codebase (`architect_agent`, chỉ brownfield)
```
Bạn là architect_agent. Đọc .agents/agents/architect-agent.md và .agents/rules/ai-software-factory-conventions.md.
Nhiệm vụ: Bước 0 — khảo sát codebase hiện có của {{PROJECT}}.
- Lưu kết quả tại docs/codebase-overview.md (cấu trúc, tech stack, cách build/test/lint, quy ước code, điểm cần lưu ý).
- Chỉ đọc code, không sửa code.
Trình bày tóm tắt cho tôi duyệt. Chỉ ghi file khi tôi gõ đúng chữ "Approved".
```

### 3.1 Bước 1 — BA viết PRD (`ba_agent`)
```
Bạn là ba_agent. Đọc .agents/agents/ba-agent.md, .agents/rules/ai-software-factory-conventions.md và docs/brd.md.
Nhiệm vụ: viết PRD [Nhóm {{N}} — {{TÊN_NHÓM}}], lấy đúng {{PHẦN_BRD}} trong BRD.
- Lưu tại docs/prd/{{FILE_PRD}}
- Tiền tố ID: US-{{XX}}-xx, FR-{{XX}}-xx, NFR-{{XX}}-xx
- Đọc thêm các PRD đã duyệt trong docs/prd/: {{PRD_ĐÃ_DUYỆT}}. Tham chiếu ID của chúng, không định nghĩa lại. Chú ý các điểm nối: {{ĐIỂM_NỐI}}.
Việc đầu tiên: làm theo Mục 2.1 của ba-agent.md. Hỏi tôi MỘT câu mỗi lượt (kèm 2–3 phương án gợi ý; tôi có thể trả lời "tự quyết" để bạn ghi vào Giả định). Sau khi đủ thông tin, tóm tắt quyết định và giả định, rồi DỪNG. TUYỆT ĐỐI không tạo hay ghi file PRD cho đến khi tôi gõ đúng chữ "Approved".
Nếu thấy điểm nào ở các PRD đã duyệt cần sửa cho khớp nhóm này, chỉ ghi vào Mục 8 và báo PO; không tự sửa các PRD đó.
```
Ghi chú: lượt đầu tiên không có PRD trước → ghi "Chưa có PRD nào được duyệt, không cần tham chiếu". Nếu có file yêu cầu cũ không dùng nữa, thêm dòng "Không đọc file <tên file>".

### 3.2 Bước 2 — System Design (`architect_agent`)
```
Bạn là architect_agent. Đọc .agents/agents/architect-agent.md, .agents/rules/ai-software-factory-conventions.md, toàn bộ docs/prd/*.md đã duyệt{{, và docs/codebase-overview.md nếu là brownfield}}.
Nhiệm vụ: viết Tài liệu Thiết kế Hệ thống cho {{PROJECT}}, lưu tại docs/system-design.md.
Chọn tech stack (nêu rõ framework frontend và UI library nếu có giao diện), kiến trúc, dữ liệu, API tổng quan, quy ước code, cách build/test/lint. Đọc lại danh sách "điểm để lại cho Architect" trong Mục 8 của các PRD và xử lý từng điểm.
Hỏi tôi MỘT câu mỗi lượt cho các quyết định cần PO chọn. Tóm tắt rồi DỪNG; chỉ ghi file khi tôi gõ đúng chữ "Approved".
```

### 3.3 Bước 2.5 — UI/UX (`ui_ux_agent`, chỉ khi có giao diện; chạy từng module)
```
Bạn là ui_ux_agent. Đọc .agents/agents/ui-ux-agent.md, .agents/rules/ai-software-factory-conventions.md, docs/prd/*.md liên quan và docs/system-design.md.
Nhiệm vụ: thiết kế module {{MODULE}} của {{PROJECT}}.
- Nếu chưa có docs/ux/design-system.md thì tạo Design System trước; nếu đã có thì dùng lại, chỉ bổ sung khi cần.
- Lưu UX Spec tại docs/ux/ux-spec-{{MODULE}}.md (màn hình SCR-xx, luồng, trạng thái Loading/Empty/Error/Success, nội dung chữ, ánh xạ API).
Hỏi tôi MỘT câu mỗi lượt (kèm 2–3 phương án gợi ý). Tóm tắt rồi DỪNG; chỉ ghi file khi tôi gõ đúng chữ "Approved".
Điều cần Architect bổ sung ghi vào mục "Đề nghị bổ sung cho Architect", không tự sửa System Design.
```

### 3.4 Bước 3 — Detail Design & Task Tracker (`detail_designer_agent`)
```
Bạn là detail_designer_agent. Đọc .agents/agents/detail-designer-agent.md, .agents/rules/ai-software-factory-conventions.md, docs/prd/*.md, docs/system-design.md{{ và docs/ux/*}}.
Nhiệm vụ: viết Thiết kế Chi tiết cho {{PROJECT}}, lưu tại docs/detail-design.md, và khởi tạo docs/task-tracker.md (mọi task ở trạng thái Todo, có cột Loại BE/FE).
Mỗi task gắn nhãn [BE] hoặc [FE], tham chiếu FR-xx; giao diện chỉ liên kết SCR-xx, không thiết kế lại.
Hỏi tôi khi thiếu thông tin. Tóm tắt rồi DỪNG; chỉ ghi file khi tôi gõ đúng chữ "Approved".
```

### 3.5 Bước 4 — Code
Backend (`backend_coder_agent`, task `[BE]`):
```
Bạn là backend_coder_agent. Đọc .agents/agents/backend-coder-agent.md, .agents/rules/ai-software-factory-conventions.md, docs/detail-design.md, docs/task-tracker.md, docs/system-design.md.
Nhiệm vụ: làm task {{T-xx}} ({{TÊN_TASK}}) — chỉ task [BE].
Quy trình: viết docs/plans/plan_{{T-xx}}.md trước và chờ tôi gõ "Approved" rồi mới code trên branch task/{{T-xx}}-{{TÊN_TASK}}; commit "{{T-xx}}: [FR-xx] ..."; ghi docs/coding-summary/{{T-xx}}.md; cập nhật trạng thái trong task-tracker.md. Thiếu thông tin hoặc fail hai lần liên tiếp thì Halt & Query, không tự đoán. Không tự merge.
```
Frontend (`frontend_coder_agent`, task `[FE]`):
```
Bạn là frontend_coder_agent. Đọc .agents/agents/frontend-coder-agent.md, .agents/rules/ai-software-factory-conventions.md, docs/detail-design.md, docs/task-tracker.md, docs/system-design.md, docs/ux/design-system.md và UX Spec của màn hình liên quan.
Nhiệm vụ: làm task {{T-xx}} ({{TÊN_TASK}}) — chỉ task [FE].
Quy trình như backend, cộng thêm: bám UX Spec và Design System, không tự sáng tác giao diện; Plan có mục "Màn hình & Component"; Summary có mục "Đối chiếu UX Spec". Không tự merge.
```

### 3.6 Bước 5 — Kiểm thử (`tester_agent`)
```
Bạn là tester_agent. Đọc .agents/agents/tester-agent.md, .agents/rules/ai-software-factory-conventions.md, docs/prd/*.md, docs/detail-design.md, docs/task-tracker.md và docs/coding-summary/{{T-xx}}.md.
Nhiệm vụ: kiểm thử task {{DS_TASK}} (đang ở trạng thái Coded), trên branch của task.
Viết test theo tiêu chí nghiệm thu, chạy test, ghi docs/test-reports/T-xx.md. Nếu fail: ghi docs/bug-reports/T-xx.md và chỉ đặt trạng thái Fail; không sửa code nghiệp vụ. Commit test dạng "T-xx: test ...".
```

### 3.7 Bước 6 — Review (`reviewer_agent`)
```
Bạn là reviewer_agent. Đọc .agents/agents/reviewer-agent.md, .agents/rules/ai-software-factory-conventions.md, docs/detail-design.md, docs/task-tracker.md, docs/coding-summary/{{T-xx}}.md, docs/test-reports/{{T-xx}}.md.
Nhiệm vụ: review code của task {{DS_TASK}} (đã Test-Pass).
Ghi docs/review-reports/T-xx.md. Nếu không đạt: chỉ đặt trạng thái Fail và nêu lý do; không tự sửa code. Không tự merge.
```

### 3.8 Bước 7 — PO nghiệm thu
Không cần prompt. PO đọc báo cáo review, chạy thử, rồi tự merge branch `task/T-xx-...` và đặt task thành `Accepted` trong `docs/task-tracker.md`.

## Phần 4. Checklist nhanh mỗi lượt chạy
* [ ] Mở phiên mới; dán đúng prompt của bước hiện tại; đã thay hết `{{...}}`.
* [ ] Bước trước đã có "Approved" của PO (các cổng sau Bước 0, 1, 2, 2.5, 3, 7).
* [ ] Agent hỏi một câu mỗi lượt; không ghi file trước khi gõ "Approved".
* [ ] Sau khi ghi file: PO đọc lại hoặc nhờ kiểm tra trước khi sang bước tiếp.
* [ ] Đã commit tài liệu vừa sinh ra (nếu Project dùng git).
