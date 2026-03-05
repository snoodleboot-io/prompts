# Kilo Code Agents

This directory contains the agent instructions for Kilo Code.

## Structure

- **`AGENTS.md`** (this file) — User guide for understanding the agents
- **`.opencode/rules/_base.md`** — Core behaviors, conventions, and session management (always loaded)
- **`.opencode/rules/{MODE}.md`** — Mode-specific behaviors for each agent

## Available Agents

### Core Agents (Built-in)

These agents are built into Kilo Code and are always available:

| Agent | Purpose |
|-------|---------|
| **Architect** | Scaffold projects, create task breakdowns, design data models |
| **Code** | Feature implementation and boilerplate generation |
| **Ask** | Q&A, decision logs, and documentation lookup |
| **Orchestrator** | CI/CD, DevOps, and PR descriptions |
| **Debug** | Root cause analysis, log analysis, and problem solving |

### Custom Agents

These agents are defined in `.kilocodemodes` and can be customized:

| Agent | Purpose |
|-------|---------|
| **Test** | Write comprehensive tests with coverage-first approach |
| **Refactor** | Improve code structure while preserving behavior |
| **Document** | Generate documentation, READMEs, and changelogs |
| **Explain** | Code walkthroughs and onboarding assistance |
| **Migration** | Handle dependency upgrades and framework migrations |
| **Review** | Code, performance, and accessibility reviews |
| **Security** | Security reviews for code and infrastructure |
| **Compliance** | SOC 2, ISO 27001, GDPR, HIPAA, PCI-DSS compliance |
| **Enforcement** | Reviews code against established coding standards |
| **Planning** | Develops PRDs and works with architects to create ARDs |

## Usage

Switch between agents based on the task at hand. Each agent has specialized
behaviors and will suggest switching when appropriate.

## Configuration

The `.opencode/rules/` directory contains the instruction files that define
agent behaviors. The `opencode.json` file references these instructions:

```json
{
  "instructions": [
    "AGENTS.md",
    ".opencode/rules/_base.md",
    ".opencode/rules/{MODE}.md"
  ]
}
```

Replace `{MODE}` with the agent you want to use (architect, code, ask, etc.).
