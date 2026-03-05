
When the user asks to scaffold a new project or set up a project structure:

1. Ask these questions before generating anything — one at a time:
   - What is the project's purpose in one sentence?
   - What is the primary language and framework?
   - What external services or APIs will it integrate with?
   - Is this a monorepo, a single service, or a library?
   - What environments will it run in (local, staging, prod)?
   - Any known constraints (license, compliance, patterns to follow)?

2. After all answers are collected:
   - Propose a folder structure with a brief rationale for each top-level directory
   - List config files to create (tsconfig, .env.example, Dockerfile, CI workflow, etc.)
   - Draft a README.md skeleton with placeholder sections
   - Ask for confirmation before generating any files

3. Do not generate any code or files until the user has confirmed the plan.

---


When the user asks to break down a feature, epic, or requirements document:

1. First identify any ambiguities or missing requirements and ask about them before proceeding.

2. Break the work into discrete, independently deliverable tasks.

3. For each task output:
   - Title: verb-first (e.g., "Add rate limiting to /auth endpoint")
   - Description: what and why, not how
   - Acceptance criteria: bulleted, testable statements
   - Dependencies: which tasks must be completed first
   - Size estimate: XS / S / M / L / XL
   - Type: feat / fix / chore / spike

4. Flag any tasks that require architectural decisions before starting.

5. Suggest a logical delivery sequence.

6. Output as a structured list, not a narrative.

Size guide:
- XS: under 1 hour, trivial change
- S: half day, well-understood
- M: 1-2 days, some complexity
- L: 3-5 days, multiple moving parts
- XL: over 1 week — flag this and ask the user to break it down further

Spikes have a timebox. If acceptance criteria cannot be written, the task is not ready.

---


When the user asks to design a data model, schema, or database structure:

1. Ask these questions before producing anything:
   - What are the core entities and their relationships?
   - What are the most common read patterns?
   - What are the most common write patterns?
   - Are there soft-delete, audit trail, or versioning requirements?
   - Any known scale constraints (rows, request volume, geography)?

2. After answers are collected, produce:
   - Entity definitions: name, fields, types, nullability, defaults, constraints
   - Relationship diagram in Mermaid ERD format
   - Index recommendations based on the stated query patterns
   - Denormalization or caching recommendations with rationale
   - Migration file skeleton (up + down)
   - Open questions or tradeoffs that need a decision before implementing

3. Do NOT generate ORM code — schema design only until the user approves.

4. Use the database from core-conventions.md.

Mermaid ERD format:
```
erDiagram
    USER {
        uuid id PK
        string email
        timestamp created_at
    }
    ORDER {
        uuid id PK
        uuid user_id FK
        string status
    }
    USER ||--o{ ORDER : "places"
```
