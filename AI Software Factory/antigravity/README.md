# Antigravity — Custom Agents + Rule cho AI Software Factory

## Cách dùng
Copy thư mục `.agents/` này vào **gốc repo** của anh (hoặc gốc workspace Antigravity).
Cấu trúc:

```
.agents/
├── agents/                 # 8 Custom Agents (mỗi file = 1 vai)
│   ├── ba-agent.md
│   ├── architect-agent.md
│   ├── ui-ux-agent.md            # Bước 2.5 (chỉ khi dự án có giao diện)
│   ├── detail-designer-agent.md
│   ├── backend-coder-agent.md    # task [BE]
│   ├── frontend-coder-agent.md   # task [FE] (doc-04 + doc-09)
│   ├── tester-agent.md
│   └── reviewer-agent.md
└── rules/
    └── ai-software-factory-conventions.md   # quy ước chung (Always On)
```

## Việc cần làm sau khi copy
1. Mở từng file trong `agents/`, thay `model: <model>` bằng model anh muốn (mỗi vai có thể model khác nhau — đây là "swappable").
2. Với `backend-coder-agent`, `frontend-coder-agent`, `tester-agent`, `reviewer-agent`: mở dòng `# tools:` và cấp quyền đọc/ghi file + terminal (theo tên tool của Antigravity) để agent đụng được repo thật.
3. (Tuỳ chọn) Đặt rule ở chế độ Always On trong panel Rules, hoặc để global tại `~/.gemini/GEMINI.md`.
4. Gọi agent: chọn từ dropdown (main agent), hoặc CLI `agy --agent ba-agent`. Muốn tự bàn giao: tạo thêm 1 coordinator agent gọi các agent này làm subagent.

## Nguồn nội dung
- 8 file agent = nội dung doc-01 → doc-09 (thêm frontmatter); `frontend-coder-agent` = doc-04 + doc-09.
- File rule = bản rút gọn của doc-00 (quy ước chung) — **cập nhật tay** khi doc-00 Mục 9/10 đổi (pipeline, cổng QA, vòng đời trạng thái).

## Đồng bộ khi sửa doc-01 → doc-09
Không sửa trực tiếp file trong `.agents/agents/`. Sửa ở doc gốc rồi chạy (từ thư mục `AI Software Factory`):

```
python3 antigravity/sync_agents.py          # tạo lại 8 file agent (giữ nguyên frontmatter, kể cả dòng model/tools anh đã điền)
python3 antigravity/sync_agents.py --check  # chỉ kiểm tra lệch, không ghi (thoát mã 1 nếu có file lệch)
```
