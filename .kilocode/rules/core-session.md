<!-- path: promptosaurus/prompts/agents/core/core-session.md -->
# Core Session

## 🔴 CRITICAL: Session Management is MANDATORY

**Session management is not optional. It is required for ALL work.**

There is **no point in time** where you are not governed by session management:
- Starting work: Governed ✓
- Switching modes: Governed ✓
- Resuming work: Governed ✓
- Emergency fixes: Governed ✓
- Hotfixes: Governed ✓
- Quick changes: Governed ✓

**If a session doesn't exist for your branch, CREATE ONE immediately.**
**If a session exists, READ IT before doing anything else.**

Sessions are the **single source of truth** for:
- What work has been done
- What work is in progress
- What the current context is
- How to hand off between modes
- How to recover from interruptions

---

## Overview

Session files provide persistent context across mode switches, enabling continuity throughout the development workflow. Each session is tied to a git branch and tracks mode history, actions taken, and current state.

## Session File Location

- **Directory:** `.promptosaurus/sessions/`
- **Naming:** `session_{YYYYMMDD}_{random}.md` (e.g., `session_20260302_a7x9k2.md`)
- **Format:** Markdown with YAML frontmatter
- **Git:** Session files are gitignored and NOT committed

## Session File Format

```markdown
---
session_id: "session_20260302_a7x9k2"
branch: "feat/PROJ-123-auth-system"
created_at: "2026-03-02T10:30:00Z"
current_mode: "code"
version: "1.0"
---

## Session Overview

**Branch:** feat/PROJ-123-auth-system  
**Started:** 2026-03-02 10:30 UTC  
**Current Mode:** code

## Mode History

| Mode | Entered | Exited | Summary |
|------|---------|--------|---------|
| architect | 10:30 | 11:15 | Designed data models |
| code | 11:15 | - | Implementing models |

## Actions Taken

### 2026-03-02 10:45 - architect mode
- Created User model
- Created Order model
- User approved design

## Context Summary

Currently implementing data models based on architect design. User model complete, working on Order model.

## Notes

- Waiting for user review of Order model
```

---

## Complete Session Example (3-Day Progression)

This example shows how sessions evolve across modes over multiple days.

### Day 1: Architect Phase

```yaml
---
session_id: "session_20260302_k7m9x1"
branch: "feat/PROJ-123-auth-system"
created_at: "2026-03-02T09:00:00Z"
current_mode: "architect"
version: "1.0"
---

## Session Overview

**Branch:** feat/PROJ-123-auth-system  
**Started:** 2026-03-02 09:00 UTC  
**Current Mode:** architect
```
