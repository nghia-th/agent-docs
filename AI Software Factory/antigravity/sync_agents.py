#!/usr/bin/env python3
"""Sync doc-01..doc-06 into antigravity/.agents/agents/*.md.

Each agent file = its own frontmatter (kept as-is) + "# Core Instructions" + the doc text.
Usage:
    python3 antigravity/sync_agents.py          # regenerate all agent files
    python3 antigravity/sync_agents.py --check  # only report files that are out of sync (exit 1 if any)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # folder that holds doc-0X files
AGENTS = Path(__file__).resolve().parent / ".agents" / "agents"
MAP = {
    "ba-agent": "doc-01_agent_BusinessAnalyst.md",
    "architect-agent": "doc-02_agent_System Architect.md",
    "detail-designer-agent": "doc-03_agent_Detail Design.md",
    "coder-agent": "doc-04_agent_code.md",
    "tester-agent": "doc-05_agent_test.md",
    "reviewer-agent": "doc-06_agent_Reviewer.md",
}

def build(agent: str, doc: str) -> str:
    target = AGENTS / f"{agent}.md"
    old = target.read_text(encoding="utf-8")
    end = old.index("\n---\n", 4) + 5                 # end of the frontmatter block
    body = (ROOT / doc).read_text(encoding="utf-8")
    return old[:end] + "\n# Core Instructions\n\n" + body

def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for agent, doc in MAP.items():
        new = build(agent, doc)
        target = AGENTS / f"{agent}.md"
        if target.read_text(encoding="utf-8") != new:
            stale.append(agent)
            if not check:
                target.write_text(new, encoding="utf-8")
    if check:
        print("Out of sync:", ", ".join(stale) if stale else "none")
        return 1 if stale else 0
    print("Updated:", ", ".join(stale) if stale else "nothing (already in sync)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
