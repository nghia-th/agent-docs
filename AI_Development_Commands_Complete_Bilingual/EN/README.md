# AI Development Commands — Usage Guide

## Goal
This command pack turns a raw idea into an approved design, then into tasks, code, tests and verification.

## Standard workflow

```text
IDEA
  ↓
ANALYZE IDEA
  ↓
DESIGN
  ↓
REVIEW DESIGN
  ↓
CHANGE REQUEST (if needed)
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

## Golden rule
**Do not let the AI jump directly from IDEA → CODE.**

Use the command files as copy/paste prompts in OpenCode. Replace `[PLACEHOLDER]` values.

## Quick command map

| Purpose | Command |
|---|---|
| Raw idea | `00_CORE/01_IDEA.md` |
| Deep analysis | `00_CORE/02_ANALYZE_IDEA.md` |
| Design | `00_CORE/03_DESIGN.md` |
| Design review | `00_CORE/04_REVIEW_DESIGN.md` |
| Approval | `00_CORE/05_APPROVE_DESIGN.md` |
| Design change | `00_CORE/06_CHANGE_REQUEST.md` |
| Create tasks | `00_CORE/07_CREATE_TASKS.md` |
| Implement task | `02_TASK/01_IMPLEMENT_TASK.md` |
| Bug | `03_BUG/02_INVESTIGATE_BUG.md` |
| Database | `04_DATABASE/01_DESIGN_DATABASE_CHANGE.md` |
| API | `04_API/01_DESIGN_API.md` |
| Security | `05_SECURITY/01_SECURITY_REVIEW.md` |
| Code review | `06_CODE/01_CODE_REVIEW.md` |
| Test plan | `07_TESTING/01_TEST_PLAN.md` |
| Final verification | `08_RELEASE/01_FINAL_VERIFICATION.md` |
