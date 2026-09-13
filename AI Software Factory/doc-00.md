# TÀI LIỆU QUY TRÌNH PHÁT TRIỂN DỰ ÁN ĐA TÁC TỬ (MULTI-AGENT WORKFLOW)

## 1. Phân Công Vai Trò (Role Assignments)
*   **Product Owner (Anh):** Nắm quyền quyết định cao nhất. Đóng vai trò là chốt chặn kiểm duyệt (QA Approval Gate), trực tiếp phê duyệt toàn bộ yêu cầu nghiệp vụ, thiết kế tính năng, tài liệu kỹ thuật, sơ đồ task và mã nguồn trước khi triển khai.
*   **Nhóm Agent Kỹ thuật (`architect_agent` / `detail_designer_agent` / `coder_agent` / `reviewer_agent`):** Phụ trách tư duy logic, xây dựng kiến trúc hệ thống, thiết kế kỹ thuật chi tiết (Detail Design), lập sơ đồ thi công (Task Mapping) và sinh mã nguồn (UI/UX, logic code). Chịu trách nhiệm phân tích (reverse engineer) codebase có sẵn để tự động xuất ra tài liệu kỹ thuật chuẩn hóa định dạng Markdown.
*   **Agent Phân tích Nghiệp vụ (`ba_agent`):** Phụ trách phân tích yêu cầu nghiệp vụ, soạn thảo tài liệu đặc tả chức năng (PRD), định nghĩa User Stories và phân tích luồng trải nghiệm người dùng (User Flows).

## 2. Trạng Thái Hệ Thống & Môi Trường Điều Phối (Environment & Orchestration)
*   **Hệ thống điều phối đa tác tử (Multi-Agent Framework):** Sử dụng CrewAI làm bộ khung trung tâm để quản lý, phân chia tác vụ và duy trì luồng giao tiếp liên tục giữa các AI.
*   **Nền tảng Cloud (Core AI):** Sử dụng các model cloud mạnh (cấu hình hiện tại, có thể đổi) đóng vai trò là não bộ chính xử lý logic phức tạp, kiến trúc và phân tích ngữ cảnh sâu.
*   **Nền tảng Local (Phụ trợ):** Tích hợp môi trường LLM nội bộ (ví dụ: Ollama hoặc model local bất kỳ) để xử lý các tác vụ tạo khung code cơ bản (boilerplate), sinh test case hoặc các module nhỏ nhằm giảm tải và tối ưu chi phí.
*   **Nền móng mã nguồn (Codebase):** Khung dự án cơ bản (scaffold/boilerplate) đã được khởi tạo và cấu hình sẵn các thư mục, file thiết yếu trên môi trường cục bộ.

## 3. Chuẩn Hóa Tài Liệu Đầu Vào Cho Thiết Kế UI/UX & Code
Để các tác tử AI có thể tạo ra thiết kế chi tiết và mã nguồn chuẩn xác, hệ thống yêu cầu cung cấp bộ tài liệu đầu vào bao gồm:
*   Danh sách yêu cầu tính năng chi tiết (User Stories).
*   Hướng dẫn nhận diện thương hiệu (Brand Guidelines: màu sắc, font chữ).
*   Sơ đồ luồng đi của người dùng (User Flows).
*   Thông số kỹ thuật của thiết bị mục tiêu (Target Device Specs).

## 4. Sơ Đồ Luồng Thực Thi (Execution Flow)
Sơ đồ dưới đây thể hiện sự di chuyển của dữ liệu qua các Agent và các trạm kiểm duyệt của Product Owner:

    [ Ý Tưởng / Yêu Cầu Ban Đầu ]
               │
               ▼
    [ BA AGENT ] ───────────────> Phân tích nghiệp vụ (PRD, User Story, Flow)
               │
               ▼
    [ QA GATE - PO ] ───────────────> (Duyệt/Chỉnh sửa yêu cầu)
               │
               ▼
    [ DESIGN AGENT ] ───────────────> Thiết kế Detail Design (API, DB, Component) 
               │                      Phân rã & Lập sơ đồ Task (Priority Mapping)
               ▼
    [ QA GATE - PO ] ───────────────> (Duyệt kiến trúc và thứ tự thi công)
               │
               ▼
    [ CODER & TESTER ] ────────────> (Thực thi Code)
               │                      - coder_agent: Logic chính, UI/UX chuẩn hóa.
               │                      - tester_agent: Boilerplate, Test cases (chạy song song).
               ▼
    [ QA GATE - PO ] ───────────────> (Nghiệm thu mã nguồn & Triển khai)

## 5. Quy Trình Phối Hợp & Phê Duyệt (Workflow & QA Gate)

| Giai đoạn | Hành động cụ thể | Trách nhiệm |
| :--- | :--- | :--- |
| **1. Chuẩn hóa nền tảng** | Đọc toàn bộ cấu trúc thư mục, file cấu hình từ codebase hiện tại. Lập danh mục module, tạo sơ đồ kiến trúc và xuất ra tài liệu kỹ thuật Markdown. | architect_agent |
| **2. Phân tích nghiệp vụ** | Lên ý tưởng chức năng, viết đặc tả chi tiết, liệt kê User Stories và vẽ sơ đồ luồng người dùng (User Flow) để làm đầu vào cho khâu thiết kế. | ba_agent |
| **3. Thiết kế chi tiết (Detail Design)** | Nhận tài liệu nghiệp vụ từ ba_agent để tạo tài liệu thiết kế kỹ thuật: đặc tả API, cấu trúc cơ sở dữ liệu (schema), và sơ đồ luồng dữ liệu/component. | detail_designer_agent |
| **4. Phân rã & Lập sơ đồ tác vụ** | Phân rã Detail Design thành các đầu việc nhỏ. Lập sơ đồ biểu diễn tính phụ thuộc (task nào độc lập làm song song, task nào phải chờ), đánh giá độ ưu tiên và chốt thứ tự thi công. | detail_designer_agent |
| **5. Xây dựng mã nguồn** | Dựa trên bản Detail Design và Sơ đồ task đã duyệt, tuần tự viết code giao diện (HTML/React) và logic hệ thống đảm bảo tính sạch sẽ, không đụng độ (conflict). | coder_agent |
| **6. Hỗ trợ tự động hóa** | Chạy các tác vụ sinh khung code phụ, viết test case song song cho các task độc lập dựa trên mã nguồn đã có. | tester_agent |
| **7. QA Approval Gate** | Đánh giá, nghiệm thu các bản phác thảo tài liệu, sơ đồ task và mã nguồn ở từng bước. Chỉ khi được thông qua, hệ thống mới chuyển sang bước tiếp theo. | Product Owner (Anh) |

## 6. Hướng Dẫn Vận Hành Hệ Thống Bằng CrewAI
Để hiện thực hóa sơ đồ và quy trình trên, mã nguồn CrewAI của dự án sẽ được cấu trúc theo 3 thành phần chính:

*   **Định nghĩa Tác tử (Agents):** 
    Tạo các Agent với vai trò rõ ràng để không dẫm chân lên nhau.
    *   `ba_agent`: `role='Business Analyst'`, `goal='Phân tích và viết đặc tả PRD/User Stories'`.
    *   `architect_agent`: `role='System Architect'`, `goal='Thiết kế hệ thống, API contract, ERD, coding conventions'`.
    *   `detail_designer_agent`: `role='Detail Designer'`, `goal='Thiết kế chi tiết và chia sơ đồ Task'`.
    *   `coder_agent`: `role='Developer'`, `goal='Viết logic + UI bám Detail Design'`.
    *   `tester_agent`: `role='Junior Developer'`, `goal='Sinh test case và boilerplate, chạy song song'`.
    *   `reviewer_agent`: `role='Code Reviewer / QA'`, `goal='Review code đối chiếu Detail Design & coding convention'`.
    *   *(Mỗi agent định danh theo VAI TRÒ; model đứng sau là cấu hình `llm=<model>` có thể đổi — xem Mục 10.4.)*
*   **Định nghĩa Tác vụ (Tasks) & Thiết lập QA Gate:**
    Mỗi bước trong quy trình (Phân tích, Thiết kế, Chia Task, Code) tương ứng với một `Task` trong CrewAI.
    *   **Bắt buộc:** Kích hoạt tham số `human_input=True` (hoặc cấu hình Human-in-the-loop tùy chỉnh) tại các Task kết thúc một giai đoạn. Việc này buộc CrewAI phải tạm dừng, in kết quả ra màn hình (hoặc gửi qua UI) để Anh đọc, góp ý, hoặc gõ "Approved" trước khi nó chuyển tài liệu đó cho Agent tiếp theo.
*   **Khởi chạy Đội ngũ (Crew):**
    Gộp Agents và Tasks vào một `Crew`. Thiết lập tham số `process=Process.sequential` để đảm bảo luồng công việc chạy tuần tự đúng như sơ đồ. Khi các task độc lập được tạo ra (ở bước 4), có thể thiết lập `async_execution=True` cho các task của `tester_agent` để chạy song song.
## 7. Mẫu Prompt Chuẩn Cho Từng Tác Tử (Standardized Prompt Templates)

Để các Agent hiểu đúng vai trò và sinh ra kết quả chuẩn, các System Prompt (hoặc `backstory` trong CrewAI) cần được thiết lập chặt chẽ:

*   **`ba_agent` (Business Analyst):**
    > "Bạn là một Chuyên gia Phân tích Nghiệp vụ (Senior Business Analyst) dày dặn kinh nghiệm. Dựa trên yêu cầu ban đầu: [Mô tả ý tưởng], nhiệm vụ của bạn là phân tích và viết Đặc tả Yêu cầu (PRD) chi tiết. Hãy liệt kê danh sách các User Stories (theo chuẩn 'As a... I want to... So that...'), và vẽ sơ đồ luồng người dùng (User Flows). Kết quả phải được trình bày rõ ràng bằng định dạng Markdown."

*   **`architect_agent` / `coder_agent` (Architect & Developer):**
    > "Bạn là một Kiến trúc sư Hệ thống (Solution Architect) và Lập trình viên Trưởng (Lead Developer). Dựa trên [Tài liệu Nghiệp vụ / PRD] được cung cấp, hãy: 
    > 1. Xây dựng Thiết kế Chi tiết (Detail Design) bao gồm đặc tả API, Schema DB.
    > 2. Phân rã thiết kế thành sơ đồ các Task, chỉ rõ độ ưu tiên và tính phụ thuộc. 
    > 3. Tiến hành viết mã nguồn (UI/UX và Logic Code) tuân thủ nghiêm ngặt cấu trúc codebase hiện tại. 
    > Tuyệt đối không sinh code thừa, luôn bám sát tài liệu Detail Design."

*   **`tester_agent` (Junior Developer / Supporter):**
    > "Bạn là một Lập trình viên Phụ trợ (Junior Developer). Dựa trên [Detail Design] và [Mã nguồn Core] do Lead Developer vừa tạo ra, hãy sinh các đoạn mã boilerplate cần thiết và viết các Unit Test Cases bao phủ toàn bộ logic. Đảm bảo code của bạn chạy độc lập và không phá vỡ cấu trúc chính."

## 8. Kỹ Thuật Tối Ưu Hóa Ngữ Cảnh (Context Optimization Strategies)

Để các AI Agent (đặc biệt là các LLM có giới hạn Context Window) hiểu ngữ cảnh tốt nhất mà không bị "loãng" thông tin, dự án áp dụng các nguyên tắc sau:

1.  **Chaining (Tiếp nối dữ liệu khép kín):** Tuyệt đối không bắt AI tự suy luận lại từ đầu. Đầu ra (Output) của tác vụ trước phải là Đầu vào (Input) của tác vụ sau. Ví dụ: `coder_agent` sinh code *chỉ* dựa trên file PRD của `ba_agent` đã được Product Owner duyệt, không dựa trên các ý tưởng rời rạc.
2.  **Context Isolation (Cô lập ngữ cảnh):** Khi giao việc sinh code cho một module cụ thể (VD: Quản lý User), chỉ cung cấp cho AI cấu trúc thư mục và Detail Design của *riêng module đó*. Không nhồi nhét toàn bộ codebase khổng lồ vào Prompt để tránh làm AI bị "ảo giác" (hallucination) và quên mất trọng tâm.
3.  **Strict Formatting (Định dạng nghiêm ngặt):** Luôn yêu cầu AI trả về kết quả bằng định dạng chuẩn (Markdown đối với tài liệu, hoặc JSON đối với dữ liệu cấu trúc). Việc này giúp hệ thống CrewAI dễ dàng parse (trích xuất) dữ liệu để truyền đi tự động.
4.  **Reference Injecting (Tiêm tài liệu tham chiếu):** Nếu cần AI code UI, hãy "tiêm" thêm [Brand Guidelines] và [UI Components hiện có] vào Prompt để buộc AI sử dụng lại các component đã định nghĩa thay vì tự chế ra CSS mới.

---

# MULTI-AGENT PROJECT DEVELOPMENT WORKFLOW

## 1. Role Assignments
*   **Product Owner (User):** The final authority. Acts as the ultimate QA Approval Gate, responsible for reviewing and signing off on all business requirements, detailed technical designs, task maps, UI/UX designs, and code before deployment.
*   **Technical Agents (`architect_agent` / `detail_designer_agent` / `coder_agent` / `reviewer_agent`):** Handles system logic, architecture design, detailed technical design (Detail Design), task breakdown, and code generation (HTML, CSS, React, Logic). Tasked with reverse-engineering the existing initialized codebase into standardized technical documentation (Markdown).
*   **Business Analyst Agent (`ba_agent`):** Manages the gathering of business requirements, drafts functional documentation (PRDs, User Stories), and analyzes overarching user flows and UX layouts.

## 2. Environment & Orchestration
*   **Multi-Agent Framework (CrewAI):** Utilizing CrewAI as the central orchestration engine to manage task delegation and continuous communication pipelines between multiple AI agents.
*   **Cloud Models (Core):** Leveraging strong cloud models (current setup, swappable) for complex architectural reasoning, deep context analysis, and primary logic generation.
*   **Local Models (Auxiliary):** Integrating local LLM environments (e.g., Ollama or any local model) to offload repetitive tasks such as generating boilerplate code and writing test cases.
*   **Codebase Status:** The foundational project scaffolding and boilerplate code have already been initialized and structured locally.

## 3. Standardized Input Requirements for Design & Code
To ensure accurate design and code generation, the system requires the following documentation package:
*   Comprehensive Feature Lists and User Stories.
*   Brand Guidelines (color palettes, typography).
*   Detailed User Flow diagrams.
*   Target Device and Platform Specifications.

## 4. Execution & Data Flow
The diagram below illustrates the flow of data through the AI Agents and the Product Owner's checkpoints:

    [ Initial Idea / Request ]
               │
               ▼
    [ BA AGENT ] ───────────────> Business Analysis (PRD, User Story, Flow)
               │
               ▼
    [ QA GATE - PO ] ───────────────> (Review/Refine Requirements)
               │
               ▼
    [ DESIGN AGENT ] ───────────────> Detailed Design (API, DB, Component) 
               │                      Task Breakdown & Priority Mapping
               ▼
    [ QA GATE - PO ] ───────────────> (Review Architecture & Execution Order)
               │
               ▼
    [ CODER & TESTER ] ────────────> (Code Implementation)
               │                      - coder_agent: Core logic, standardized UI/UX.
               │                      - tester_agent: Boilerplate, Test cases (parallel).
               ▼
    [ QA GATE - PO ] ───────────────> (Final Code Review & Deployment)

## 5. Coordinated Execution & Approval Workflow

| Phase | Action Items | Assigned To |
| :--- | :--- | :--- |
| **1. Codebase Standardization** | Scan the existing directory structure and configuration files. Generate architectural diagrams, module specs, and output a standardized Markdown technical document. | architect_agent |
| **2. Business Analysis** | Outline functional requirements, create structured User Stories, and define the User Flow to serve as the blueprint for technical design. | ba_agent |
| **3. Detailed Technical Design** | Process the business requirements to generate comprehensive technical blueprints: API specifications, database schemas, and component/data flow diagrams. | detail_designer_agent |
| **4. Task Breakdown & Prioritization** | Deconstruct the Detailed Design into granular tasks. Map out task dependencies (identifying independent vs. sequential tasks) and assign priority levels to establish a conflict-free execution order. | detail_designer_agent |
| **5. Code Implementation** | Translate the tasks and Detailed Design into clean, standard-compliant UI/UX (HTML/React) and core logic code, following the strictly prioritized execution sequence. | coder_agent |
| **6. Automated Assistance** | Generate auxiliary boilerplate components and unit test cases in parallel for independent tasks based on the approved Detailed Design. | tester_agent |
| **7. QA Approval Gate** | Review and rigorously test all generated documentation, technical designs, task priorities, and code at each step. AI outputs must receive explicit sign-off before progressing. | Product Owner (User) |

## 6. CrewAI Implementation Guide
To operationalize the workflow above, the CrewAI configuration will be structured into three main components:

*   **Agent Configuration:** 
    *   `ba_agent`: `role='Business Analyst'`, `goal='Analyze and draft PRD/User Stories'`.
    *   `architect_agent`: `role='System Architect'`, `goal='Design architecture, API contracts, ERD, coding conventions'`.
    *   `detail_designer_agent`: `role='Detail Designer'`, `goal='Detailed design and task breakdown'`.
    *   `coder_agent`: `role='Developer'`, `goal='Implement logic + UI following Detail Design'`.
    *   `tester_agent`: `role='Junior Developer'`, `goal='Generate test cases and boilerplate, run in parallel'`.
    *   `reviewer_agent`: `role='Code Reviewer / QA'`, `goal='Review code against Detail Design & coding conventions'`.
    *   *(Each agent is identified by ROLE; the backing model is a swappable `llm=<model>` config — see Section 10.4.)*
*   **Task Definition & QA Gates:**
    Each phase maps to a specific `Task`.
    *   **Crucial Step:** Enable `human_input=True` on milestone tasks. This forces the framework to pause execution and prompt the Product Owner for feedback or approval before passing the output to the next agent in the pipeline.
*   **Crew Execution:**
    Combine the agents and tasks into a `Crew` instance. Set `process=Process.sequential` to enforce the strict chronological flow. For specific independent tasks assigned to `tester_agent`, enable `async_execution=True` to allow parallel processing.


## 7. Standardized Prompt Templates

To ensure agents perform their roles accurately, System Prompts (or `backstory` in CrewAI) must be strictly defined:

*   **`ba_agent` (Business Analyst):**
    > "You are a highly experienced Senior Business Analyst. Based on the initial request: [Idea Description], your task is to analyze and write a detailed Product Requirements Document (PRD). Outline comprehensive User Stories (using the 'As a... I want to... So that...' format) and map out the User Flows. The final output must be strictly formatted in Markdown."

*   **`architect_agent` / `coder_agent` (Architect & Developer):**
    > "You are a Solution Architect and Lead Developer. Based on the provided [PRD / Business Documentation], you must:
    > 1. Create a Detailed Technical Design including API specifications and Database Schemas.
    > 2. Break down this design into a prioritized Task Map, explicitly stating task dependencies.
    > 3. Implement the source code (UI/UX and Core Logic) in strict adherence to the existing codebase structure.
    > Do not generate redundant code. Strictly follow the Detailed Design."

*   **`tester_agent` (Junior Developer / Supporter):**
    > "You are a Junior Support Developer. Based on the [Detailed Design] and the [Core Code] generated by the Lead Developer, your task is to generate necessary boilerplate code and write comprehensive Unit Test Cases covering the core logic. Ensure your code is isolated and does not break the main architecture."

## 8. Context Optimization Strategies

To maximize AI comprehension and prevent context dilution (especially important for limited Context Windows), the following principles must be enforced:

1.  **Strict Data Chaining:** Never force the AI to guess the context from scratch. The approved Output of a preceding task must serve as the precise Input for the next. For example, `coder_agent` must generate code *only* based on the PO-approved PRD from `ba_agent`, never from fragmented chat history.
2.  **Context Isolation:** When assigning a task for a specific module (e.g., User Management), only feed the AI the directory structure and Detailed Design *relevant to that specific module*. Avoid stuffing the entire monolithic codebase into the prompt to prevent AI hallucination and context loss.
3.  **Strict Formatting Enforcement:** Always command the AI to output responses in standard formats (Markdown for documentation, JSON for structured data). This allows the CrewAI framework to reliably parse and pass data downstream.
4.  **Reference Injecting:** When generating UI code, explicitly inject [Brand Guidelines] and [Existing UI Components] into the prompt. This forces the AI to reuse established styling instead of hallucinating new CSS classes.
---

## 9. LUỒNG PIPELINE PHÁT TRIỂN (BẢN CHỐT) — Finalized Pipeline

> Phần này chốt lại và thay thế sơ đồ nháp ở Mục 4. Đây là luồng chuẩn được Product Owner phê duyệt.

### 9.1. Bảy bước & agent phụ trách

| Bước | Giai đoạn | Agent phụ trách | Đầu ra |
| :---: | :--- | :--- | :--- |
| 1 | Phân tích yêu cầu | `ba_agent` (Business Analyst) | PRD, User Stories, User Flow |
| 2 | Thiết kế hệ thống | `architect_agent` (System Architect) | Kiến trúc, tech stack, API contract, ERD, coding conventions |
| 3 | Thiết kế chi tiết (Task) | `detail_designer_agent` | Detail Design + sơ đồ Task (dependency, priority) |
| 4 | Viết code | `coder_agent` | Logic code + UI/UX |
| 5 | Test | `tester_agent` | Unit test / test cases (chạy song song) |
| 6 | Review | `reviewer_agent` (agent RIÊNG) | Báo cáo review: đạt/không đạt chuẩn |
| 7 | Nghiệm thu | Product Owner (Anh) | Ký duyệt cuối & triển khai |

### 9.2. Nguyên tắc

*   **Phương án A — mỗi bước một agent riêng:** không gộp vai. Người thiết kế, người code và người review là các agent tách biệt để rõ trách nhiệm và tránh giẫm chân / tự bênh code.
*   **Tách agent Reviewer:** người viết code (`coder_agent`) và người review (`reviewer_agent`) là hai agent khác nhau. Không để agent tự review code của chính mình. Không giao review cho `tester_agent` (model yếu hơn, khó bắt lỗi chuẩn kiến trúc).
*   **Nội dung Review kiểm tra:** đúng coding convention, bám sát Detail Design, không sinh code thừa, pass lint, test cover đúng logic.
*   **Vòng lặp sửa lỗi:** Bước 4 → 5 → 6 là một vòng lặp. Nếu Review KHÔNG đạt → quay lại Bước 4 sửa → test lại → review lại. Chỉ khi **test PASS + review PASS** mới lên Bước 7.
*   **Cổng QA của Product Owner (human_input=True):** đặt tại 3 mốc — (a) sau Bước 1 (duyệt yêu cầu), (b) sau Bước 3 (duyệt kiến trúc & sơ đồ task), (c) Bước 7 (nghiệm thu code). Dù Reviewer là AI, cổng nghiệm thu của con người ở Bước 7 vẫn là chốt chặn cuối cùng.

### 9.3. Sơ đồ luồng chốt

    [ Ý Tưởng / Yêu Cầu ]
             │
             ▼
    1. ba_agent ──────────────> Phân tích yêu cầu (PRD, User Story, Flow)
             │
        [ QA GATE - PO ] ───────> Duyệt yêu cầu nghiệp vụ
             │
             ▼
    2. architect_agent ───────> Thiết kế hệ thống (kiến trúc, API contract, ERD)
             │
             ▼
    3. detail_designer_agent ─> Thiết kế chi tiết + Sơ đồ Task
             │
        [ QA GATE - PO ] ───────> Duyệt kiến trúc & thứ tự thi công
             │
             ▼
    ┌───► 4. coder_agent ─────> Viết code (logic + UI)
    │        │
    │        ▼
    │    5. tester_agent ──> Test / boilerplate (song song)
    │        │
    │        ▼
    │    6. reviewer_agent ───> Review: đúng chuẩn? bám Detail Design?
    │        │
    └──[Không đạt: sửa]──────────┘
             │[test PASS + review PASS]
             ▼
        [ QA GATE - PO ] ───────> 7. NGHIỆM THU & Triển khai

### 9.4. Cấu hình CrewAI (Phương án A — tách riêng từng agent)

Mỗi bước là một agent riêng (thay thế danh sách 3 agent ở Mục 6):

*   `ba_agent`              — role='Business Analyst' (Bước 1)
*   `architect_agent`       — role='System Architect' (Bước 2)
*   `detail_designer_agent` — role='Detail Designer' (Bước 3)
*   `coder_agent`           — role='Developer' (Bước 4)
*   `tester_agent`       — role='Junior Developer' (Bước 5: test + boilerplate)
*   `reviewer_agent`        — role='Code Reviewer / QA Engineer' (Bước 6)

Product Owner (con người) giữ vai nghiệm thu ở Bước 7 và các cổng QA (`human_input=True`).

---

## 9 (EN). FINALIZED DEVELOPMENT PIPELINE

> This section finalizes and supersedes the draft flow in Section 4. This is the PO-approved standard workflow.

### 9.1. Seven Steps & Ownership

| Step | Phase | Agent | Output |
| :---: | :--- | :--- | :--- |
| 1 | Requirements Analysis | `ba_agent` (Business Analyst) | PRD, User Stories, User Flow |
| 2 | System Design | `architect_agent` (System Architect) | Architecture, tech stack, API contracts, ERD, coding conventions |
| 3 | Detailed Design (Tasks) | `detail_designer_agent` | Detail Design + Task map (dependency, priority) |
| 4 | Coding | `coder_agent` | Logic code + UI/UX |
| 5 | Testing | `tester_agent` | Unit tests / test cases (parallel) |
| 6 | Review | `reviewer_agent` (SEPARATE agent) | Review report: pass/fail |
| 7 | Acceptance | Product Owner | Final sign-off & deployment |

### 9.2. Principles

*   **Option A — one agent per step:** no role merging. Designer, coder, and reviewer are separate agents for clear ownership and to avoid overlap / self-bias.
*   **Separate Reviewer agent:** the coder (`coder_agent`) and the reviewer (`reviewer_agent`) are distinct agents. An agent never reviews its own code. `tester_agent` is not used for review (weaker, misses architectural-standard issues).
*   **Review checklist:** coding conventions, adherence to Detail Design, no redundant code, lint passing, tests covering the intended logic.
*   **Fix loop:** Steps 4 → 5 → 6 form a loop. If Review fails → back to Step 4 → re-test → re-review. Only when tests PASS + review PASS does it advance to Step 7.
*   **PO QA Gates (human_input=True):** at 3 milestones — (a) after Step 1, (b) after Step 3, (c) Step 7. The human acceptance gate at Step 7 remains the final, non-removable checkpoint.

### 9.4. CrewAI Configuration (Option A — fully separated agents)

Each step is its own agent (supersedes the 3-agent list in Section 6):

*   `ba_agent`              — role='Business Analyst' (Step 1)
*   `architect_agent`       — role='System Architect' (Step 2)
*   `detail_designer_agent` — role='Detail Designer' (Step 3)
*   `coder_agent`           — role='Developer' (Step 4)
*   `tester_agent`       — role='Junior Developer' (Step 5: tests + boilerplate)
*   `reviewer_agent`        — role='Code Reviewer / QA Engineer' (Step 6)

The Product Owner (human) owns acceptance at Step 7 and the QA gates (`human_input=True`).

---

## 10. QUY ƯỚC CHUNG TOÀN PIPELINE (Global Conventions)

> Áp dụng cho MỌI agent, đảm bảo dữ liệu nối liền mạch giữa các bước (hỗ trợ nguyên tắc Chaining ở Mục 8).

### 10.1. Mã định danh & Truy vết (Traceability IDs)
*   BA (Bước 1) sinh ID cho mọi yêu cầu: `US-xx` (User Story), `FR-xx` (yêu cầu chức năng), `NFR-xx` (yêu cầu phi chức năng).
*   `detail_designer_agent` (Bước 3) khi chia Task đặt ID `T-xx` và **bắt buộc** tham chiếu ngược tới `US-xx`/`FR-xx` mà task đó phục vụ.
*   Nhờ chuỗi ID này, luôn truy được: Task → Yêu cầu → Story, xuyên suốt pipeline.

### 10.2. Độ ưu tiên (Priority)
*   Nguồn ưu tiên bắt nguồn từ nhãn MoSCoW (`Must / Should / Could / Won't`) do BA gắn cho từng User Story.
*   `detail_designer_agent` (Bước 3) dùng nhãn này làm căn cứ cho Priority Mapping và thứ tự thi công.

### 10.3. Ngôn ngữ tài liệu (mặc định — PO có thể đổi)
*   Tài liệu nghiệp vụ & thiết kế (PRD, System Design, Detail Design, Task map): **tiếng Việt** (để PO đọc và duyệt nhanh).
*   Mã nguồn và comment trong code: **tiếng Anh**.

### 10.4. Agent ↔ Model là cấu hình, không phải danh tính
*   Mỗi agent định danh theo **vai trò** (`ba_agent`, `architect_agent`, `detail_designer_agent`, `coder_agent`, `tester_agent`, `reviewer_agent`) — KHÔNG gán cứng vào bất kỳ hãng model nào.
*   Model (LLM) đứng sau mỗi agent chỉ là tham số cấu hình `llm=<model>`, có thể đổi bất cứ lúc nào (cloud hoặc local) mà không cần sửa tên agent, prompt hay logic pipeline.
*   Đổi model = chỉ sửa đúng dòng `llm` của agent đó trong cấu hình CrewAI.


### 10.5. Điểm vào & Thứ tự đọc khi bàn giao (Entry Point & Reading Order)
*   Mỗi tài liệu bàn giao PHẢI mở đầu bằng một **Entry note** — một dòng chỉ rõ agent nhận bắt đầu đọc từ mục nào.
*   Nguyên tắc: agent nhận đọc **phần định hướng công việc trước** (mục tiêu / danh sách việc), rồi tới đặc tả được tham chiếu, cuối cùng đối chiếu quy ước & tiêu chí chấp nhận. Cụ thể theo từng chặng:
    *   `architect_agent` đọc PRD: Tổng quan/Mục tiêu → User Stories (ưu tiên) → FR/NFR → Ràng buộc.
    *   `detail_designer_agent` đọc System Design: Thành phần & Ranh giới → API contract → ERD → Coding Conventions; đọc PRD để lấy Acceptance Criteria.
    *   `coder_agent` đọc Detail Design: **Sơ đồ Task trước** (chọn task theo ưu tiên/phụ thuộc) → đặc tả mà task tham chiếu → Coding Conventions (trong System Design) → Acceptance Criteria (trong PRD).
    *   `tester_agent` đọc Detail Design: **Sơ đồ Task** (lọc task độc lập/song song) → Definition of Done + Acceptance Criteria từng task.
    *   `reviewer_agent` đọc: Coding Conventions + Detail Design + code, đối chiếu Acceptance Criteria/DoD.
*   Luôn theo Context Isolation: chỉ nạp tài liệu của đúng module đang làm.


### 10.6. Bảng theo dõi Task (Task Tracker) & Vòng đời trạng thái
*   **Nguồn sự thật duy nhất** về tiến độ task là một file Task Tracker dùng chung (một file/module, ví dụ `task-tracker.md`), do `detail_designer_agent` khởi tạo từ Sơ đồ Task (mọi task = `Todo`).
*   **Vòng đời trạng thái:** `Todo` → `In-Progress` → `Coded` → `Test-Pass` → `Review-Pass` → `Accepted`. Khi `Test-Fail` / `Review-Fail` → kéo task về `In-Progress` cho `coder_agent` sửa.
*   **Ai cập nhật:** `coder_agent` (`In-Progress`, `Coded`); `tester_agent` (`Test-Pass`/`Test-Fail`); `reviewer_agent` (`Review-Pass`/`Review-Fail`); Product Owner (`Accepted`).
*   **Cấu trúc:** `Task ID | Mô tả | FR/US | Ưu tiên | Phụ thuộc | Trạng thái | Cập nhật bởi | Ghi chú`.
*   Post-Coding Summary và báo cáo test/review là chi tiết từng lượt; nhưng **trạng thái chuẩn luôn nằm ở Task Tracker**.


---

## 10 (EN). GLOBAL CONVENTIONS

> Applies to ALL agents to keep data flowing seamlessly across steps (supports the Chaining principle in Section 8).

### 10.1. Traceability IDs
*   The BA (Step 1) assigns IDs to every requirement: `US-xx` (User Story), `FR-xx` (functional), `NFR-xx` (non-functional).
*   When breaking down tasks (Step 3), `detail_designer_agent` assigns `T-xx` IDs and MUST reference back the `US-xx`/`FR-xx` each task serves.
*   This ID chain guarantees end-to-end traceability: Task → Requirement → Story.

### 10.2. Priority
*   Priority originates from the MoSCoW labels (`Must / Should / Could / Won't`) the BA attaches to each User Story.
*   `detail_designer_agent` (Step 3) uses these labels as the basis for Priority Mapping and execution order.

### 10.3. Document Language (default — PO may change)
*   Business & design documents (PRD, System Design, Detail Design, Task map): **Vietnamese** (for fast PO review).
*   Source code and code comments: **English**.

### 10.4. Agent ↔ Model is Config, Not Identity
*   Each agent is identified by its **role** (`ba_agent`, `architect_agent`, `detail_designer_agent`, `coder_agent`, `tester_agent`, `reviewer_agent`) — NOT hardcoded to any model vendor.
*   The model (LLM) behind each agent is just an `llm=<model>` config parameter, changeable anytime (cloud or local) without renaming agents or altering prompts/pipeline logic.
*   Switching model = edit only that agent's `llm` line in the CrewAI configuration.


### 10.5. Entry Point & Reading Order at Handoff
*   Every handoff document MUST begin with an **Entry note** — one line stating where the receiving agent should start reading.
*   Principle: the receiving agent reads the **work-orienting part first** (goals / work list), then the referenced specs, then checks conventions & acceptance criteria. Per stage:
    *   `architect_agent` reads the PRD: Overview/Goals → User Stories (priority) → FR/NFR → Constraints.
    *   `detail_designer_agent` reads System Design: Components & Boundaries → API contracts → ERD → Coding Conventions; reads the PRD for Acceptance Criteria.
    *   `coder_agent` reads Detail Design: **Task map first** (pick tasks by priority/dependency) → the specs each task references → Coding Conventions (in System Design) → Acceptance Criteria (in PRD).
    *   `tester_agent` reads Detail Design: **Task map** (filter independent/parallel tasks) → each task's Definition of Done + Acceptance Criteria.
    *   `reviewer_agent` reads: Coding Conventions + Detail Design + code, checked against Acceptance Criteria/DoD.
*   Always follow Context Isolation: load only the docs for the module currently in scope.


### 10.6. Task Tracker & Status Lifecycle
*   The **single source of truth** for task progress is a shared Task Tracker file (one per module, e.g. `task-tracker.md`), created by `detail_designer_agent` from the Task map (every task = `Todo`).
*   **Status lifecycle:** `Todo` → `In-Progress` → `Coded` → `Test-Pass` → `Review-Pass` → `Accepted`. On `Test-Fail` / `Review-Fail` → move the task back to `In-Progress` for `coder_agent` to fix.
*   **Who updates:** `coder_agent` (`In-Progress`, `Coded`); `tester_agent` (`Test-Pass`/`Test-Fail`); `reviewer_agent` (`Review-Pass`/`Review-Fail`); Product Owner (`Accepted`).
*   **Columns:** `Task ID | Description | FR/US | Priority | Depends-on | Status | Updated-by | Notes`.
*   Post-Coding Summary and test/review reports are per-run detail; the **authoritative status always lives in the Task Tracker**.
