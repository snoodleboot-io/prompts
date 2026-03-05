
When the user asks to implement a feature or task:

1. Before writing any code:
   - Restate the goal in your own words to confirm understanding
   - Read the relevant source files — do not assume their contents
   - Identify all files that will need to change
   - Propose the implementation approach with tradeoffs noted
   - Flag any assumptions you are making
   - Wait for the user to confirm before proceeding

2. After confirmation:
   - Implement following core-conventions.md exactly
   - Match the patterns used in existing code in the same layer
   - Add inline comments for non-obvious logic
   - Add a TODO comment for any judgment call the user should review
   - Implement one file at a time

3. After implementation:
   - List any follow-up work created (tech debt, missing tests, related changes)
   - List the tests that should be written or updated

Output order: plan → confirmation → implementation → follow-up list.

---


When the user asks to generate boilerplate, scaffolding, or structural code
(components, routes, services, models, repositories, hooks, middleware, etc.):

1. Before generating, read an existing file from the same layer of the codebase
   to understand the established pattern. Do not invent a new pattern.

2. Generate structure and signatures only — do not implement business logic.
   Use "// TODO: implement" placeholders where logic needs to be filled in.

3. All generated code must:
   - Follow core-conventions.md exactly for naming and structure
   - Include typed interfaces and signatures — no any or unknown without narrowing
   - Include a test file skeleton alongside the implementation

4. Ask the user for the following if not provided:
   - Type (component, route, service, model, repository, hook, middleware)
   - Name (PascalCase)
   - Purpose (one sentence)

5. Do not implement logic — structure and signatures only.

---


When the user asks to check code against house style, audit style, or
when you are about to write new code in an unfamiliar part of the codebase:

1. Before writing any code in an unfamiliar module, read 2-3 existing files
   from the same layer to understand the established patterns.

2. When auditing code for style, check against core-conventions.md and
   against patterns observed in the rest of the codebase. Report:
   - Every deviation from core-conventions.md
   - Any patterns that don't match how similar code is written elsewhere
   - Severity: MUST FIX (will confuse maintainers) or NIT (minor preference)

3. When writing new code, match the patterns you observed — do not introduce
   a new pattern without asking first.

4. If asked to summarize house style for a new contributor, read 3-4
   representative source files and produce a brief style guide covering:
   - File and folder naming
   - Error handling pattern
   - Async style
   - Module structure (imports, exports)
   - Testing patterns
