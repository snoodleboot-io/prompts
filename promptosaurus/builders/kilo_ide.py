"""
builders/kilo_ide.py
Kilo Code IDE builder - outputs .kilocode/rules-{mode}/ structure.

Output layout:
  {output}/.kilocode/rules/                 ← core files (always loaded)
  {output}/.kilocode/rules-{mode}/           ← per-mode directories with files
  {output}/.kilocodemodes                ← all mode definitions (for IDE)
  {output}/.kiloignore                  ← ignore patterns

This format is used by the KiloCode IDE extensions (VSCode/JetBrains).
"""

from pathlib import Path
from typing import Any

from promptosaurus.builders.kilo import KiloCodeBuilder
from promptosaurus.registry import registry


class KiloIDEBuilder(KiloCodeBuilder):
    """Builder for Kilo Code .kilocode/rules-{mode}/ directory structure (IDE format)."""

    def build(
        self, output: Path, config: dict[str, Any] | None = None, dry_run: bool = False
    ) -> list[str]:
        """
        Write the Kilo .kilocode/rules-{mode}/ structure under `output`.
        Returns a list of action strings for display.
        """
        actions: list[str] = []

        # Get selected language from config
        selected_language = config.get("defaults", {}).get("language", "") if config else ""
        language_file = (
            self.LANGUAGE_FILE_MAP.get(selected_language.lower()) if selected_language else None
        )

        # 1. Create AGENTS.md user guide
        actions.append(self._create_agents_md(output, dry_run))

        # 2. Create core files in .kilocode/ (for IDE compatibility - legacy location)
        # These are in .kilocode/ directly for IDE
        for filename in self.BASE_FILES:
            source_path = registry.prompt_path(filename)
            if source_path.exists():
                destination = output / ".kilocode" / filename
                actions.append(self._copy(source_path, destination, dry_run, config))

        # 2a. Create core files in .kilocode/rules/ (new location - core files without core- prefix)
        for filename in self.BASE_FILES:
            source_path = registry.prompt_path(filename)
            if source_path.exists():
                # Remove "core-" prefix from filename
                new_filename = filename
                if filename.startswith("core-"):
                    new_filename = filename[5:]  # Remove "core-" prefix
                destination = output / ".kilocode" / "rules" / new_filename
                actions.append(self._copy(source_path, destination, dry_run, config))

        # 2b. Add language-specific conventions to .kilocode/rules/ if selected
        if language_file:
            source_path = registry.prompt_path(language_file)
            if source_path.exists():
                # Remove "core-" prefix from filename for .kilocode/rules/
                new_filename = language_file
                if language_file.startswith("core-"):
                    new_filename = language_file[5:]  # Remove "core-" prefix
                # Copy to legacy location for IDE compatibility
                destination = output / ".kilocode" / language_file
                actions.append(self._copy(source_path, destination, dry_run, config))
                # Copy to new .kilocode/rules/ location with renamed file
                destination_rules = output / ".kilocode" / "rules" / new_filename
                actions.append(self._copy(source_path, destination_rules, dry_run, config))

        # 3. Create per-mode directories with their subagent files (custom modes only)
        for mode_key in self.custom_modes:
            if mode_key in registry.mode_files:
                mode_dir = output / ".kilocode" / f"rules-{mode_key}"
                for filename in registry.mode_files[mode_key]:
                    source_path = registry.prompt_path(filename)
                    if source_path.exists():
                        destination = mode_dir / filename
                        actions.append(self._copy(source_path, destination, dry_run, config))

        # 4. Generate .kilocodemodes manifest
        actions.append(self._write_manifest(output / ".kilocodemodes", dry_run))

        # 5. Build .kiloignore
        actions.extend(self._build_ignore(output, dry_run))

        return actions

    def _get_agents_md_content(self) -> str:
        """Get the AGENTS.md content for IDE format."""
        return """# Kilo Code Agents

This directory contains the agent instructions for Kilo Code (IDE format).

## Structure

- **`AGENTS.md`** (this file) — User guide for understanding the agents
- **`.kilocode/rules/`** — Core behaviors and conventions (always loaded)
- **`.kilocode/rules-{mode}/`** — Mode-specific behaviors for each agent

## Core Instructions

The `.kilocode/rules/` directory contains core files that are always loaded:
- `system.md` — Core system behaviors
- `conventions.md` — General conventions
- `session.md` — Session management
- `{language}.md` — Language-specific conventions (if configured)

**Important:** Always load the core files from `.kilocode/rules/` for any task, as they contain the foundational behaviors and conventions for this project.

## Available Agents

Each agent has its own directory under `.kilocode/rules-{mode}/`:

| Mode | Directory | Purpose |
|------|-----------|---------|
| **test** | `.kilocode/rules-test/` | Write comprehensive tests with coverage-first approach |
| **refactor** | `.kilocode/rules-refactor/` | Improve code structure while preserving behavior |
| **document** | `.kilocode/rules-document/` | Generate documentation, READMEs, and changelogs |
| **explain** | `.kilocode/rules-explain/` | Code walkthroughs and onboarding assistance |
| **migration** | `.kilocode/rules-migration/` | Handle dependency upgrades and framework migrations |
| **review** | `.kilocode/rules-review/` | Code, performance, and accessibility reviews |
| **security** | `.kilocode/rules-security/` | Security reviews for code and infrastructure |
| **compliance** | `.kilocode/rules-compliance/` | SOC 2, ISO 27001, GDPR, HIPAA, PCI-DSS compliance |
| **enforcement** | `.kilocode/rules-enforcement/` | Reviews code against established coding standards |
| **planning** | `.kilocode/rules-planning/` | Develops PRDs and works with architects to create ARDs |

> **Note:** The architect, code, ask, debug, and orchestrator modes are built-in to Kilo and are not generated here.

## Usage

Switch between agents based on the task at hand. Each agent has specialized
behaviors and will suggest switching when appropriate.

## Configuration

The KiloCode IDE extensions automatically load the appropriate mode instructions
from the `.kilocode/` directory based on the current mode selection.
"""
