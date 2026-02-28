#!/usr/bin/env python3
"""
Semantic Version Calculator for CI/CD Pipeline.

Versioning Rules:
- feat/* branches: Patch increment with dev prerelease (e.g., 0.1.0 → 0.1.1.dev1)
- main branch: Stable release (uses current minor, increments patch)
- PR to main: Minor increment with rc prerelease (e.g., 0.1.x → 0.2.0rc1)

The base version (MAJOR.MINOR) is read from pyproject.toml.
The patch version is calculated based on git history and run number.
"""

import os
import re
import subprocess


def get_base_version() -> tuple[int, int, int]:
    """Read the base version from pyproject.toml."""
    try:
        with open("pyproject.toml") as f:
            content = f.read()
            match = re.search(r'^version\s*=\s*"(\d+)\.(\d+)\.(\d+)"', content, re.MULTILINE)
            if match:
                return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except FileNotFoundError:
        pass
    return (0, 1, 0)  # Default version


def get_git_commit_count() -> int:
    """Get the number of commits in the current branch."""
    try:
        result = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return int(result.stdout.strip())
    except (subprocess.CalledProcessError, ValueError):
        return 0


def get_branch_name() -> str:
    """Get the current branch name from environment or git."""
    # First check GITHUB_REF
    github_ref = os.environ.get("GITHUB_REF", "")
    if github_ref.startswith("refs/heads/"):
        return github_ref.replace("refs/heads/", "")
    if github_ref.startswith("refs/pull/"):
        return "pull-request"

    # Fallback to git command
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "unknown"


def calculate_version() -> tuple[str, bool]:
    """
    Calculate the semantic version based on branch and context.

    Returns:
        Tuple of (version_string, is_prerelease)
    """
    major, minor, patch = get_base_version()
    branch = get_branch_name()
    run_number = int(os.environ.get("GITHUB_RUN_NUMBER", "1"))
    short_sha = os.environ.get("GITHUB_SHA", "unknown")[:7]

    is_prerelease = True

    if branch == "main":
        # Main branch: stable release, increment patch
        # Use run_number to ensure unique versions
        new_patch = patch + run_number
        version = f"{major}.{minor}.{new_patch}"
        is_prerelease = False

    elif branch.startswith("feat/"):
        # Feature branch: patch increment with dev prerelease
        # Format: MAJOR.MINOR.PATCH.devN+SHA
        new_patch = patch + 1
        version = f"{major}.{minor}.{new_patch}.dev{run_number}"

    elif branch == "pull-request":
        # Pull request: minor increment with rc prerelease
        # Format: MAJOR.(MINOR+1).0rcN
        new_minor = minor + 1
        version = f"{major}.{new_minor}.0rc{run_number}"

    else:
        # Other branches: patch with local version identifier
        new_patch = patch + 1
        version = f"{major}.{minor}.{new_patch}.dev{run_number}+{short_sha}"

    return version, is_prerelease


def main():
    """Main entry point - outputs version for GitHub Actions."""
    version, is_prerelease = calculate_version()

    # Output for GitHub Actions
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"version={version}\n")
            f.write(f"is_prerelease={str(is_prerelease).lower()}\n")

    print(f"Calculated version: {version}")
    print(f"Is prerelease: {is_prerelease}")

    return version


if __name__ == "__main__":
    main()
