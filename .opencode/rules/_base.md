# Always-on base behaviors for all modes and tools.
# EDIT THIS FILE to change global assistant behavior.

## ⚠️ STARTUP CHECKLIST - COMPLETE BEFORE ANY WORK

### 1. Check Git Branch (REQUIRED FIRST STEP)

**ALWAYS run this command FIRST before any work:**
```bash
git branch --show-current
```

**If on `main` branch:**
- ❌ STOP all work immediately
- DO NOT proceed with any changes
- If sufficient context exists: suggest creating a feature branch with appropriate naming
- If insufficient context: ask the user for a branch name
- Wait for user confirmation before creating/checkout out a feature branch

**If on feature branch:**
- ✓ Proceed to Step 2

---

### 🔴 2. Session Management (MANDATORY - REQUIRED FOR ALL WORK)

**For complete session management guidance, see: `core-session.md`**

**There is NO scenario where you skip session management. Sessions govern all work without exception.**

#### MANDATORY STEPS (do not skip any):

**1. MUST check for existing session:**
```bash
ls -la .prompty/session/session_*.md 2>/dev/null
```

**2. MUST handle existing session or create new:**
- If session exists for your branch: MUST read it entirely
  - Read YAML frontmatter to verify branch matches
  - Read entire Context Summary to understand current state
  - Update `current_mode` field to current mode
  - Add timestamp entry to Mode History if switching modes
- If no session exists: MUST create one immediately
  - Location: `.prompty/session/session_{YYYYMMDD}_{RANDOM}.md`
  - Include YAML frontmatter with branch name
  - Initialize Mode History, Actions Taken, and Context Summary sections
- Never proceed without a valid session

**3. MANDATORY VERIFICATION (before doing any work):**
```
- [ ] Session file exists in .prompty/session/: YES
- [ ] Session file has YAML frontmatter: YES
- [ ] Session branch matches current branch: YES
- [ ] Session has Mode History section: YES
- [ ] Session has Actions Taken section: YES
- [ ] Session has Context Summary: YES
- [ ] You have read Context Summary: YES
- [ ] You understand what work has been done before: YES
```

**If ANY check is false → STOP and fix it immediately. Do not proceed.**

**4. MANDATORY SESSION UPDATES (during work):**
- Update: `current_mode` field to match current task
- Record: All work in Actions Taken with timestamps
- Update: Context Summary after completing work
- Before switching modes: Update Mode History with exit time and summary

#### ENFORCEMENT:

Sessions are not "nice to have" — they are **MANDATORY infrastructure**.

**There are NO exceptions. NO bypasses. NO "I'll do it later."**

**Every single piece of work is governed by session management.**

If you proceed without session management:
- ❌ Context is lost between mode switches
- ❌ Work is undocumented
- ❌ Team cannot hand off work
- ❌ Progress is invisible
- ❌ Recovery from interruption is impossible

---

## Feature Branch Naming Convention

### REQUIRED FORMAT: `{type}/{ticket-id}-{description}`

**Branch Types:**
- `feat/` - New feature
- `bugfix/` - Normal bug fix (can wait for next release)
- `hotfix/` - Urgent bug fix requiring immediate deployment

**Ticket ID:** Required for tracking
- Jira format: `PROJ-123`
- GitHub issue: `#456`
- If no ticket: create one before branching

**Description:** Kebab-case, 3-5 words

### Valid Examples:

✓ **Correct:**
- `feat/PROJ-123-add-user-authentication`
- `bugfix/PROJ-124-fix-null-pointer-exception`
- `hotfix/PROJ-999-critical-security-vulnerability`

✗ **Incorrect (DO NOT USE):**
- `my-branch` (no ticket, no type)
- `feature-123` (type not prefix, no ticket)
- `bugfix_something_here` (underscores, no ticket)
- `fix/PROJ-123-issue` (use bugfix/ or hotfix/, not fix/)
- `john-fix-auth` (includes author name)

### Branch Creation:

If you're on `main` and need to create a branch:

```bash
# Ensure main is up-to-date
git checkout main
git pull origin main

# Create feature branch with correct naming
git checkout -b feat/PROJ-123-feature-description
# or for a bug fix:
git checkout -b bugfix/PROJ-124-fix-description
# or for urgent fix:
git checkout -b hotfix/PROJ-999-urgent-issue

# Verify correct branch
git branch --show-current
# Should show: feat/PROJ-123-... or bugfix/PROJ-124-... or hotfix/PROJ-999-...
```

### When to use which type:

- `feat/` - Always for new features
- `bugfix/` - Normal bug fixes following standard review process
- `hotfix/` - Critical production bugs, security issues, data loss - requires immediate deployment

### Branch Validation Checklist:

After creating or checking out a feature branch:

```bash
# 1. Confirm correct branch
git branch --show-current
# Output should match: feat/PROJ-123-..., bugfix/PROJ-124-..., or hotfix/PROJ-999-...

# 2. Confirm base is main (no pre-existing commits)
git log --oneline main..HEAD
# Output should be empty for fresh branch

# 3. Confirm main is up-to-date
git log -1 --oneline main
# Verify this is latest commit from origin

# 4. Status check
git status
# Should show: On branch feat/PROJ-123-..., nothing to commit
```

### Anti-Patterns (what NOT to do):

- ❌ Creating branches from non-main source
- ❌ Using `fix/` as type (use `bugfix/` or `hotfix/`)
- ❌ Creating branches without a ticket ID
- ❌ Branch names longer than 60 characters
- ❌ Using other types like `chore/`, `docs/`, `spike/` (not part of your convention)

---

## General Development Rules

You are a senior software engineer embedded in this codebase.
You have filesystem access — use it proactively.

### Read Before You Write

Before changing any file:
- Read it and the files it imports
- Understand the existing pattern before introducing a new one
- Check core-conventions.md for naming, style, and error handling rules

### Scope Discipline

- Make the smallest change that satisfies the requirement
- Do not refactor code outside the stated scope without asking
- If you spot something worth fixing nearby, mention it — don't fix it silently
- Do not add dependencies without flagging them explicitly

### Plan Before Acting on Large Changes

If a task touches more than 3 files or involves a design decision:
- Write a short plan first
- Wait for confirmation before making any changes

### Questions

- Ask one focused question at a time — never a list of blockers
- If you are unsure about scope or approach, ask before acting

### Terminal Commands

- Run read-only commands freely: cat, ls, grep, git log, git diff
- Ask before: installs, writes, deletes, migrations, deployments
- Show the command before running anything that cannot be undone

### Error Handling

- If a tool call fails, explain what happened and what you tried
- Do not silently retry — report what went wrong

### Code Quality

- Follow core-conventions.md exactly
- Prefer explicit over clever; readable over terse
- Add TODO comments for any judgment calls the user should review
- Never hardcode secrets, URLs, or environment-specific values
- Flag anything hacky or temporary with a comment

---

# Project coding standards - base conventions for all projects.
# For language-specific rules, see: core-conventions-ts.md, core-conventions-py.md, etc.
# All mode-specific rules inherit from this file.

## Repository Structure

Repository type: {{single-language | multi-language-folder | mixed-collocation}}

### If single-language:
Include: core-conventions-[LANG].md where [LANG] matches your primary language

### If multi-language-folder:
Define each language area:
- /frontend      → include: core-conventions-ts.md
- /backend       → include: core-conventions-py.md
- /shared        → include: core-conventions-go.md

### If mixed-collocation:
File extension determines which rules apply:
- *.ts, *.tsx   → TypeScript rules
- *.py           → Python rules
- *.go           → Go rules

## Shared Conventions

These conventions apply to all languages and projects:

### Naming Conventions

Files:               {{kebab-case | snake_case | PascalCase}}
Variables:           {{camelCase | snake_case}}
Constants:           {{UPPER_SNAKE | PascalCase}}
Classes/Types:       {{PascalCase}}
Functions:           {{camelCase | snake_case}}
Database tables:     {{snake_case | PascalCase}}
Environment vars:    UPPER_SNAKE_CASE always

## File & Folder Structure

src/
└── {{your structure here}}

Rule: One export per file unless it is a barrel (index.ts).
Rule: Co-locate tests with source (auth.ts → auth.test.ts).

### Class Organization Rules

Rule: One class per file. Each class must be in its own dedicated file.
Rule: Filename must be the snake_case version of the class name.
  - Example: `class ConfigHandler` → `config_handler.py`
  - Example: `class SelectionState` → `selection_state.py`
  - Example: `class SingleSelectState` → `single_select_state.py`
  - Example: `class RenderStage` → `render_stage.py`
  - Example: `class CommandFactory` → `command_factory.py`

This rule ensures:
- Clear file-to-class mapping for maintainability
- Easier navigation in IDEs
- Consistent naming across the codebase
- Simplified imports and dependency tracking

### SOLID Principles for OOP Components

All OOP components must follow SOLID principles:

**S - Single Responsibility Principle (SRP)**
- Each class has one reason to change
- A class should do one thing and do it well
- Split large classes into smaller, focused ones

**O - Open/Closed Principle (OCP)**
- Open for extension, closed for modification
- Use inheritance, composition, or interfaces to extend behavior
- Avoid modifying existing working code to add features

**L - Liskov Substitution Principle (LSP)**
- Subtypes must be substitutable for their base types
- Derived classes should extend behavior without changing contracts
- Breaking parent behavior in subclasses violates LSP

**I - Interface Segregation Principle (ISP)**
- Clients should not depend on interfaces they don't use
- Split large interfaces into smaller, focused ones
- Prefer multiple small interfaces over one large interface

**D - Dependency Inversion Principle (DIP)**
- Depend on abstractions, not concrete implementations
- High-level modules should not depend on low-level modules
- Both should depend on abstractions (interfaces/abstract classes)

## Error Handling

Pattern: {{throw | return Result<T, E> | return [data, error]}}

- Never swallow errors silently
- Always include context: Error("failed to fetch user: " + userId)
- Log at the boundary where the error is handled, not where it is thrown
- Use typed errors, not generic Error or Exception

## Imports & Dependencies

- Prefer standard library over third-party where equivalent
- No circular imports
- Group imports: stdlib → third-party → internal (blank line between groups)
- Flag any new dependency before adding it

## Testing

Testing conventions are language-specific. See your language's conventions file for:
- Test framework recommendations
- Coverage targets
- Test style patterns
- Mocking approaches

## Database

Database:            {{DATABASE}}           e.g., PostgreSQL, DynamoDB
ORM/Query:           {{ORM}}                e.g., Prisma, SQLAlchemy, GORM

## Git & PR Conventions

Branch naming:       feat|fix|chore|docs / ticket-id - short-description
Commit style:        {{Conventional Commits | free-form}}
PR size:             {{MAX_LINES}} lines changed (soft limit)

## Deployment

Target:              {{DEPLOYMENT_TARGET}}  e.g., AWS Lambda, Vercel, GKE

---

# Language-Specific Conventions

For language-specific rules, include the appropriate file:
- `core-conventions-ts.md` - TypeScript/JavaScript
- `core-conventions-py.md` - Python
- `core-conventions-go.md` - Go
- `core-conventions-java.md` - Java
- `core-conventions-rust.md` - Rust
- `core-conventions-sql.md` - SQL

These files contain language-specific patterns for:
- Error handling patterns
- Type system usage
- Testing frameworks and patterns
- Module/dependency management

## Session Context Management

All modes must follow the session management protocol defined in `core-session.md`:

1. **Check for session on startup** - Look for existing session for current branch
2. **Create session if needed** - New session if none exists for current branch
3. **Update on mode switch** - Record exit from current mode, entry to new mode
4. **Record actions** - Log significant actions with timestamps
5. **Maintain context** - Keep Context Summary current

Session files provide continuity across mode switches and persist workflow state.
See `core-session.md` for complete protocol and file format specifications.

---

# Session Context Management

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

- **Directory:** `.prompty/session/`
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
**Status:** In Progress (Day 1 of 3)

## Mode History

| Mode | Entered | Exited | Summary |
|------|---------|--------|---------|
| architect | 09:00 | 17:30 | Designed auth flow, created 8 tasks |

## Actions Taken

### 2026-03-02 09:15 - architect mode
- **Task:** Review existing auth in codebase
- **Finding:** Current JWT implementation doesn't validate refresh tokens
- **Decision:** Design new token refresh flow with rotation

### 2026-03-02 11:00 - architect mode  
- **Deliverable:** Task breakdown for auth system
  - `PROJ-123-1`: Refactor JWT validation (S)
  - `PROJ-123-2`: Implement token refresh endpoint (M)
  - `PROJ-123-3`: Add refresh token rotation (M)
  - `PROJ-123-4`: Integration tests for token flow (M)
  - `PROJ-123-5`: Security audit of implementation (S)
- **Status:** User approved all 5 tasks
- **File:** `docs/AUTH_DESIGN.md` created with full design

### 2026-03-02 15:30 - architect mode
- **Deliverable:** Sequence diagram for refresh token flow
- **File:** `docs/AUTH_SEQUENCE.md`
- **Review:** Ready for Code mode

## Context Summary

Completed architecture phase for JWT refresh token redesign. Designed new token rotation system to address security gaps in current implementation. Identified 5 implementation tasks (total ~1.5 weeks). User approved architecture. Ready to implement Task 1 (JWT validation refactor).

**Deliverables Created:**
- `docs/AUTH_DESIGN.md` - Full design specification
- `docs/AUTH_SEQUENCE.md` - Sequence diagrams

**Next Steps:**
- Switch to Code mode
- Create `feat/PROJ-123-1-jwt-validation` branch
- Implement JWT validation refactor

## Notes
- User concerned about backwards compatibility with existing tokens — added migration strategy to design doc
- Requires security review before merging (flagged in PROJ-123-5)
```

### Day 2: Code Phase (Mode Switch)

When switching modes, update Mode History and create continuation:

```yaml
---
session_id: "session_20260302_k7m9x1"
branch: "feat/PROJ-123-auth-system"
created_at: "2026-03-02T09:00:00Z"
current_mode: "code"
version: "1.0"
---

## Session Overview

**Branch:** feat/PROJ-123-auth-system  
**Started:** 2026-03-02 09:00 UTC  
**Current Mode:** code  
**Status:** In Progress (Day 2)

## Mode History

| Mode | Entered | Exited | Summary |
|------|---------|--------|---------|
| architect | 09:00 | 17:30 | Designed auth flow, created 8 tasks |
| code | 09:30 | - | Implementing Task 1: JWT validation |

## Actions Taken

[Previous architect actions from Day 1...]

### 2026-03-03 09:30 - code mode
- **Task:** PROJ-123-1 - Refactor JWT validation
- **Work:** Created new JWT validation module
- **File:** `src/auth/jwt_validator.py` - 150 LOC
- **Status:** Core validation logic complete, tests pending

### 2026-03-03 14:00 - code mode
- **Work:** Added comprehensive test coverage
- **Files:** `tests/unit/auth/test_jwt_validator.py` - 280 LOC (8 test cases)
- **Coverage:** 92% on validator module
- **Status:** All tests passing locally

### 2026-03-03 16:45 - code mode
- **Review:** Self-review complete, flagged one edge case
- **Decision:** Requested user approval before merging
- **Blockers:** None

## Context Summary

Completed implementation of JWT validation refactor (PROJ-123-1). All 8 unit tests passing with 92% coverage. Code follows core-py.md patterns. Identified and addressed one edge case with expired token refresh. Ready for Code Review mode or user approval.

**Deliverables:**
- `src/auth/jwt_validator.py` - New validation module
- `tests/unit/auth/test_jwt_validator.py` - Complete test suite

**Next Steps (waiting on user):**
- Approve changes
- Switch to Review mode for code review
- OR continue with Task 2
```

### Day 3: Code Review Phase

```yaml
---
session_id: "session_20260302_k7m9x1"
branch: "feat/PROJ-123-auth-system"
created_at: "2026-03-02T09:00:00Z"
current_mode: "review"
version: "1.0"
---

## Mode History

| Mode | Entered | Exited | Summary |
|------|---------|--------|---------|
| architect | 09:00 | 17:30 | Designed auth flow, created 8 tasks |
| code | 09:30 | 16:45 | Implemented Task 1: JWT validation |
| review | 17:00 | - | Code review of JWT validation |

## Actions Taken

[Previous actions...]

### 2026-03-03 17:00 - review mode
- **Task:** Code review of PROJ-123-1
- **Files reviewed:** 
  - `src/auth/jwt_validator.py` (150 LOC)
  - `tests/unit/auth/test_jwt_validator.py` (280 LOC)
- **Status:** Initial review in progress

### 2026-03-03 17:45 - review mode
- **Findings:** 2 blockers, 1 suggestion, all tests passing
- **Blockers:**
  1. Missing error handling for malformed tokens
  2. No timeout for validation (potential DoS)
- **Suggestion:** Add logging for failed validations
- **Verdict:** Needs changes before merge

## Context Summary

Completed code review of PROJ-123-1. Found 2 blocking issues (error handling, timeout) and 1 suggestion (logging). Code quality is good, tests are comprehensive. Ready to report findings to developer.

**Next Steps:**
- Report findings to developer
- Switch to Code mode for fixes
- Re-review after fixes

## Notes
- Token validation logic is solid, issues are edge cases
- Developer should address blockers before next review
```

---

## Session Management Procedure

### On Mode Startup (REQUIRED)

1. **Determine current git branch:**
   - Run: `git branch --show-current`
   - If on `main` branch:
     - If sufficient context exists: suggest creating a feature branch
     - If insufficient context: ask user for branch name
   - If on feature branch: use that branch name

2. **Check for existing session:**
   - List files in `.prompty/session/`
   - Read each file's YAML frontmatter
   - Look for `branch:` field matching current branch
   - Find most recent session if multiple exist

3. **If no session exists:**
   - Create `.prompty/session/` directory if needed
   - Create new session file using format above
   - Set `current_mode` to current mode
   - Record branch name and timestamp

4. **If session exists:**
   - Read the session file
   - Update `current_mode` to current mode
   - Append to Mode History if different from previous mode
   - Read Context Summary to understand current state

### On Mode Switch

1. **Before switching:**
   - Update current session file
   - Add exit timestamp to current mode in Mode History
   - Record summary of work done in current mode
   - Update Context Summary

2. **After switch:**
   - New mode reads session file (follows startup procedure)

### Recording Actions

Record significant actions in "Actions Taken" section:
- File creations/modifications
- Important decisions
- User approvals or rejections
- Completion of major tasks

Use format: `### {ISO8601 timestamp} - {mode} mode`

---

## When to CREATE vs UPDATE Session

### Create NEW session when:
- First time working on this branch
- Previous session is > 1 week old
- Starting completely new feature
- Session file corrupted or unreadable

### Update existing session when:
- Continuing work on same branch
- Switching modes (update `current_mode` field)
- Recording new actions
- Completing work phase

### Session Rotation Guidelines:
- Check age: `ls -l .prompty/session/`
- If oldest session is 1+ week old, consider archive
- Keep last session for 30 days for historical reference
- Archive old sessions: `mv session_*.md .prompty/session/archive/`

---

## Best Practices

1. **Always check for existing session first** - Don't create duplicates
2. **Update session after significant work** - Keep context current
3. **Be concise in summaries** - Capture essence without verbosity
4. **Use UTC timestamps** - Consistent timezone handling (ISO8601 format)
5. **Link related files** - Reference created/modified files in actions
6. **Track decisions** - Record when user approves/rejects something
7. **Read Context Summary** - Always understand prior work before proceeding

## Integration with Modes

All modes MUST:
1. Check for session on startup
2. Create session if none exists
3. Update session on mode switch
4. Record significant actions
5. Maintain Context Summary

This ensures continuity when switching between modes (e.g., Architect → Code → Test → Review).

## Session Troubleshooting

### Session file not found
```bash
# Check if directory exists
ls -la .prompty/session/

# If directory doesn't exist, create it
mkdir -p .prompty/session/

# Create new session
# (Follow session file format from above)
```

### Multiple sessions for same branch
```bash
# Check which sessions exist
ls -la .prompty/session/

# Read each session's branch field
for file in .prompty/session/session_*.md; do
  echo "=== $file ===" && head -5 "$file"
done

# Delete duplicates, keep most recent
# Sessions are safe to delete (gitignored)
```

### Session branch doesn't match current branch
```bash
# Check current branch
git branch --show-current

# Check session branch
grep "^branch:" .prompty/session/session_*.md

# If mismatch:
# Option 1: Create new session for current branch
# Option 2: Update session file's branch field
```

### Session context is unclear
```bash
# Read the Context Summary section carefully
# If still unclear:
# - Ask user for clarification
# - Review Actions Taken section
# - Check Mode History
# - Read related files mentioned in actions
```

### Session file is corrupted
```bash
# If YAML frontmatter is broken:
# Option 1: Carefully edit and fix YAML
# Option 2: Create new session (old one is still readable as backup)

# Check YAML syntax
head -10 .prompty/session/session_*.md
# Should see lines: ---, session_id:, branch:, created_at:, current_mode:, version:, ---
```

---

# Python Conventions

Language:             python           e.g., Python 3.11+
Runtime:              3.14            e.g., CPython 3.11, PyPy
Package Manager:      uv        e.g., poetry, pip, uv
Linter:               ruff, pyright             e.g., Ruff, flake8
Formatter:           ruff          e.g., Ruff, Black
Abstract Class Style: interface  e.g., abc, interface

## Python-Specific Rules

### Type Hints
- Type hints required on all public functions (use `pyright` or `mypy` to enforce)
- Use `dataclasses` or `pydantic` for data shapes, not raw dicts
- Use `T | None` instead of `typing.Optional[T]`. This is the standard for modern python
- Use `typing.TypeAlias` for complex type aliases

### Error Handling
- Use exception hierarchies — don't raise generic `Exception`
- Use `Result` pattern from `returns` library or custom Result type
- Never swallow errors silently — always log or re-raise with context
- Use `contextlib.contextmanager` for resource management

### Async
- Use `asyncio` — no mixing sync/async without explicit bridging
- Use `asyncpg` for async database access, not synchronous drivers
- Use `httpx` for async HTTP requests

### Imports
- Use absolute imports (no relative `..` imports)
- Group imports: stdlib → third-party → local (blank lines between)
- **NEVER use import forwarding** — do not re-export imported symbols (e.g., `from module import X` then exposing `X` at package level). This is an anti-pattern and NOT allowed. Define public API explicitly.

### Code Structure & Patterns

#### Constants & Configuration (CRITICAL)
- **NO constants allowed inside or outside of classes** — never define `CONSTANT = value` at module level OR as class constants
- **For values changeable at runtime**: use a YAML configuration file
- **For fixed configuration**: use internal class variables (not constants) or `pydantic-settings` with environment variable support
- **Never have const values outside of a class** — always use a settings file (`pydantic-settings`) for configurable values
- When asked to create constants, redirect to the appropriate configuration approach

#### Dynamic Attribute Access
- **AVOID `setattr` and `getattr`** unless absolutely necessary — these bypass type checking and make code harder to reason about
- Before using: ask yourself if there's a type-safe alternative (dataclass, pydantic model, explicit properties)
- If present: ask the user if they are creating core/framework code or generally reusable code — only acceptable for core framework code that MUST handle dynamic structures

#### Module Structure
- **ALL modules MUST have `__init__.py`** — every package directory must include an `__init__.py` file
- Verify `__init__.py` exists before adding new modules
- No implicit namespace packages allowed

#### Type Casting
- **DO NOT use type casting** (`typing.cast`, `isinstance` + cast patterns) UNLESS working with data primitives like `int`, `str`, `float`, `bool`
- Primitive conversions (e.g., `int()`, `str()`, `float()`) are acceptable
- Use proper type narrowing with `isinstance` checks instead of casting for complex types
- Design APIs to return correct types rather than requiring casts

#### Type Checking Enforcement
- **ENFORCE the use of `pyright`** while coding — run continuously during development
- Treat type errors as blocking issues
- All code must pass pyright strict mode before commit
- No commits with type errors or `Any` types without explicit justification

### Testing

#### Coverage Targets
Line:           80          e.g., 80%
Branch:         70        e.g., 70%
Function:       90       e.g., 90%
Statement:      85      e.g., 85%
Mutation:       80       e.g., 80%
Path:           60           e.g., 60%

#### Test Types

##### Unit Tests
- One function or method in isolation
- Mock all external dependencies (database, API calls, filesystem)
- Use `pytest` fixtures for setup/teardown
- Use `pytest.mark.parametrize` for table-driven tests
- Use `pytest.raises` for exception testing

##### Integration Tests
- Test at service or module boundary
- Use real database (testcontainers) or in-memory alternatives
- Test API endpoints, database queries, file operations
- Clean up test data after each test

##### Mutation Tests
- Use `mutmut` or `pytest-mutmut` to verify test quality
- Run after unit tests pass
- Aim to kill mutations in core business logic

##### Property-Based Tests
- Use `hypothesis` for generative testing
- Test edge cases automatically generated

#### Framework & Tools
Framework:         hybrid       e.g., pytest
Mocking library:   {{MOCKING_LIBRARY}}             e.g., unittest.mock, pytest-mock
Coverage tool:    {{COVERAGE_TOOL}}             e.g., pytest-cov, coverage.py
Mutation tool:    {{MUTATION_TOOL}}        e.g., mutmut, pytest-mutmut

#### Scaffolding

```bash
# Install
pip install pytest pytest-cov pytest-mock hypothesis mutmut

# Run tests
pytest                          # Run all tests
pytest --cov                    # With coverage
pytest --cov --cov-branch       # Line + branch coverage
pytest --cov-report=html        # HTML report

# Mutation testing
mutmut run
mutmut report

# Configuration (pyproject.toml)
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --strict-markers"

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if __name__ == .__main__.:",
    "raise NotImplementedError",
]
```

##### CI Integration
```yaml
# GitHub Actions example
- name: Run tests
  run: pytest --cov --cov-branch --cov-report=xml

- name: Mutation tests
  run: |
    pip install mutmut
    mutmut run
    mutmut html > mutation_report.html
```

### Code Style
- Follow PEP 8 (enforced by Ruff)
- Use f-strings for string formatting
- Use `dataclasses` for simple data containers
- Use `pydantic` for complex validation
- Unless the code is a framework layer or there is a strong necessity - DO NOT use setattr or getattr.

### Python Styling and Conventions

#### Properties Over Direct Access
- **Use properties** for attribute access control - never access fields directly when get/set logic is needed
- Use `@property` decorator with getters/setters instead of `get_x()` / `set_x()` methods
- Use `@property.deleter` when cleanup logic is needed on attribute deletion
- Prevent setting when inappropriate by raising `AttributeError` or `TypeError` in setters

```python
# GOOD - property with controlled access
class Temperature:
    def __init__(self, celsius: float = 0.0) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @celsius.deleter
    def celsius(self) -> None:
        self._celsius = 0.0

# BAD - direct field access or getter/setter methods
class Temperature:
    def __init__(self) -> None:
        self.celsius = 0.0  # Direct access - no validation

    def get_celsius(self) -> float:  # Old-style getter
        return self._celsius

    def set_celsius(self, value: float) -> None:  # Old-style setter
        self._celsius = value
```

#### Public/Protected/Private Scoping
- Use single underscore `_` prefix for protected/internal attributes and methods
- Use double underscore `__` prefix for private attributes (name mangling when needed)
- Protected methods should not be called from outside the class hierarchy

```python
class DataProcessor:
    def __init__(self) -> None:
        self.public_field: str = "visible"
        self._internal_state: dict = {}  # Protected
        self.__private_cache: dict = {}  # Private (name mangled)

    def public_method(self) -> None:
        """Part of public API."""
        pass

    def _helper_method(self) -> None:
        """Protected - for subclass use only."""
        pass

    def __internal_cleanup(self) -> None:
        """Private - internal use only."""
        pass
```

#### Decorators and Design Patterns
- Use `@staticmethod` for functions that don't access instance state
- Use `@classmethod` for factory methods and alternate constructors
- Use `@property` for computed attributes without side effects
- Use `@functools.cached_property` for expensive computations that should be cached
- Use `@functools.wraps` when creating decorators
- Use `@contextlib.contextmanager` for creating context managers

```python
from functools import cached_property, wraps
from contextlib import contextmanager
from typing import Iterator

class ExpensiveComputation:
    @cached_property
    def heavy_result(self) -> dict:
        """Computed once and cached."""
        return self._expensive_operation()

    @staticmethod
    def utility_function(x: int) -> int:
        """Doesn't need self."""
        return x * 2

    @classmethod
    def from_config(cls, config: dict) -> "ExpensiveComputation":
        """Factory method."""
        return cls(**config)

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        print("Before call")
        return func(*args, **kwargs)
    return wrapper
```

#### Asynchrony and Async Constructs
- Use `async`/`await` for I/O-bound operations
- Use `asyncio` for concurrency - never mix sync/async without explicit bridging
- Use `async with` for async context managers
- Use `async for` for async iterators
- Never use `time.sleep()` in async code - use `await asyncio.sleep()`

```python
import asyncio
from contextlib import asynccontextmanager

class AsyncResource:
    async def fetch(self) -> bytes:
        """Async operation."""
        await asyncio.sleep(0.1)  # Never use time.sleep() in async code
        return b"data"

    async def __aenter__(self) -> "AsyncResource":
        """Async context manager entry."""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.disconnect()

@asynccontextmanager
async def managed_resource() -> Iterator[AsyncResource]:
    """Async context manager using decorator."""
    resource = AsyncResource()
    await resource.connect()
    try:
        yield resource
    finally:
        await resource.disconnect()
```

#### Context Managers (sync and async)
- **ALWAYS use context managers** for resource management (files, connections, locks)
- Use `contextlib.contextmanager` for simple sync context managers
- Use `contextlib.asynccontextmanager` for async context managers
- Never manually manage `connect()`/`disconnect()` or `open()`/`close()` without context managers
- Use `contextlib.closing()` for objects with close() but no context manager

```python
from contextlib import contextmanager, asynccontextmanager, closing
from typing import Iterator
import sqlite3

@contextmanager
def database_connection(db_path: str) -> Iterator[sqlite3.Connection]:
    """Sync context manager for database connections."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

# Usage - always use context managers
with database_connection("app.db") as conn:
    conn.execute("SELECT * FROM users")

# For objects with close() but no context manager
from urllib.request import urlopen
with closing(urlopen("https://example.com")) as response:
    data = response.read()
```

#### No Nested Class/Function Definitions
- **NEVER nest class or function definitions** unless:
  1. It is a documented design decision
  2. It is marked with `#design-decision-override` comment
  3. It solves a specific scoping or closure problem that cannot be solved otherwise
- Define classes and functions at module level for testability and readability
- Use factories or partial functions instead of closures when state capture is needed

```python
# BAD - nested function (hard to test, unclear scope)
def process_data(data: list) -> list:
    def transform(item: int) -> int:
        return item * 2
    return [transform(x) for x in data]

# GOOD - module-level function (testable, clear scope)
def transform(item: int) -> int:
    return item * 2

def process_data(data: list) -> list:
    return [transform(x) for x in data]

# Acceptable - nested with explicit design decision override
def create_handler(config: dict):
    #design-decision-override: closure captures config without exposing it
    def handler(event: dict) -> None:
        if event["type"] in config["allowed_types"]:
            process_event(event, config["handler_type"])
    return handler
```

### Abstract Classes and Interfaces

Selected Style: **interface**

{{#if ABSTRACT_CLASS_STYLE == "abc"}}
#### Using Abstract Base Classes (abc module)
- Inherit from `abc.ABC` for abstract base classes
- Use `@abstractmethod` decorator for methods that must be implemented
- Use `@abstractclassmethod` and `@abstractstaticmethod` where appropriate
- Type checkers will catch incomplete implementations at static analysis time

```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, id: str) -> Entity | None:
        """Retrieve entity by ID. Must be implemented by subclasses."""
        ...

class SqlRepository(Repository):
    def get(self, id: str) -> Entity | None:
        # Concrete implementation
        return self.session.query(Entity).get(id)
```
{{/if}}

{{#if ABSTRACT_CLASS_STYLE == "interface"}}
#### Using NotImplementedError (Informal Interfaces)
- Raise `NotImplementedError` in methods that must be overridden
- Document expected behavior in docstrings
- Rely on runtime checks and duck typing
- Simpler for cases where strict enforcement isn't needed

```python
class Repository:
    def get(self, id: str) -> Entity | None:
        """Retrieve entity by ID. Must be overridden by subclasses."""
        raise NotImplementedError(f"{self.__class__.__name__} must implement get()")

class SqlRepository(Repository):
    def get(self, id: str) -> Entity | None:
        # Concrete implementation
        return self.session.query(Entity).get(id)
```
{{/if}}
