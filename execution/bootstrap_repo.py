#!/usr/bin/env python3
"""
bootstrap_repo.py
Purpose:
  Bootstrap a repository into the standard Production-Grade Agent Constitution layout
  by creating required directories and pulling canonical starter files from a template repo.

Dependencies:
  - Python 3.8+ (standard library only)

Safety:
  - Idempotent by default (won't overwrite existing files)
  - Supports --dry-run and --overwrite

Updated:
  2026-02-04
"""

import argparse
import os
import sys
import urllib.request
from dataclasses import dataclass
from typing import List, Optional, Tuple


# -----------------------------
# Configuration (edit if needed)
# -----------------------------

DEFAULT_TEMPLATE_OWNER = "MyTownDigitalSolutions"
DEFAULT_TEMPLATE_REPO = "Repo_Setup_Templates"
DEFAULT_REF = "main"  # branch or tag
RAW_BASE = "https://raw.githubusercontent.com"


@dataclass(frozen=True)
class RemoteFile:
    remote_path: str   # path in template repo
    local_path: str    # path in target repo


REQUIRED_DIRS = [
    ".tmp",
    "execution",
    "directives",
    ".agent",
]

# Canonical files to pull from the template repo:
CANONICAL_FILES = [
    RemoteFile("AGENTS.md", "AGENTS.md"),
    RemoteFile("README_TEMPLATE.md", "README_TEMPLATE.md"),
    RemoteFile("directives/DIRECTIVE_TEMPLATE.md", "directives/DIRECTIVE_TEMPLATE.md"),
    RemoteFile("directives/project_init.md", "directives/project_init.md"),
    RemoteFile(".agent/codex_system_prompt.md", ".agent/codex_system_prompt.md"),
]


GITIGNORE_REQUIRED_LINES = [
    ".env",
    ".tmp/",
    ".tmp",
    "token.json",
    "credentials.json",
]


# -----------------------------
# Helpers
# -----------------------------

def eprint(*args) -> None:
    print(*args, file=sys.stderr)


def normpath(path: str) -> str:
    return path.replace("\\", "/")


def ensure_dir(path: str, dry_run: bool) -> None:
    if os.path.isdir(path):
        return
    if dry_run:
        print(f"[DRY-RUN] mkdir {path}")
        return
    os.makedirs(path, exist_ok=True)
    print(f"[OK] Created directory: {path}")


def build_raw_url(owner: str, repo: str, ref: str, remote_path: str) -> str:
    remote_path = normpath(remote_path).lstrip("/")
    return f"{RAW_BASE}/{owner}/{repo}/{ref}/{remote_path}"


def http_get_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "repo-bootstrap/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def safe_write_file(path: str, content: str, overwrite: bool, dry_run: bool) -> Tuple[bool, str]:
    """
    Returns (did_write, reason)
    """
    if os.path.exists(path) and not overwrite:
        return (False, "exists (skipped)")
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        if dry_run:
            print(f"[DRY-RUN] mkdir -p {parent}")
        else:
            os.makedirs(parent, exist_ok=True)

    if dry_run:
        action = "overwrite" if os.path.exists(path) else "create"
        print(f"[DRY-RUN] {action} file: {path} ({len(content)} chars)")
        return (True, "dry-run (would write)")
    else:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        return (True, "written")


def patch_gitignore(gitignore_path: str, dry_run: bool) -> None:
    existing_lines: List[str] = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8", errors="replace") as f:
            existing_lines = [line.rstrip("\n") for line in f.readlines()]

    existing_set = set(line.strip() for line in existing_lines if line.strip())
    to_add = [line for line in GITIGNORE_REQUIRED_LINES if line not in existing_set]

    if not to_add:
        print("[OK] .gitignore already contains required entries.")
        return

    if dry_run:
        print(f"[DRY-RUN] Would append to .gitignore: {to_add}")
        return

    with open(gitignore_path, "a", encoding="utf-8", newline="\n") as f:
        if existing_lines and existing_lines[-1].strip() != "":
            f.write("\n")
        f.write("# Agent bootstrap defaults\n")
        for line in to_add:
            f.write(line + "\n")

    print(f"[OK] Updated .gitignore with: {to_add}")


def render_readme_from_template(template_text: str, project_name: Optional[str]) -> str:
    """
    Minimal templating:
      - Replaces first occurrence of <Project Name> if present
      - Replaces <YYYY-MM-DD> with today's date string if present (kept simple; optional)
    """
    if project_name:
        template_text = template_text.replace("<Project Name>", project_name, 1)
    return template_text


# -----------------------------
# Main
# -----------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap repo structure and governance files from Repo_Setup_Templates."
    )
    parser.add_argument("--owner", default=DEFAULT_TEMPLATE_OWNER, help="Template repo owner/org")
    parser.add_argument("--repo", default=DEFAULT_TEMPLATE_REPO, help="Template repo name")
    parser.add_argument("--ref", default=DEFAULT_REF, help="Template repo ref (branch or tag)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing anything")
    parser.add_argument("--project-name", default=None, help="Project name to inject into README.md")
    parser.add_argument("--write-readme", action="store_true",
                        help="Create README.md from README_TEMPLATE.md (if missing unless --overwrite)")
    parser.add_argument("--patch-gitignore", action="store_true",
                        help="Ensure .gitignore excludes .env, .tmp, and credential files")

    args = parser.parse_args()

    print("=== Repo Bootstrap ===")
    print(f"Template source: {args.owner}/{args.repo}@{args.ref}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'WRITE'} | Overwrite: {args.overwrite}")

    # 1) Ensure dirs
    for d in REQUIRED_DIRS:
        ensure_dir(d, args.dry_run)

    # 2) Fetch and write canonical files
    created = []
    skipped = []
    failed = []

    for rf in CANONICAL_FILES:
        url = build_raw_url(args.owner, args.repo, args.ref, rf.remote_path)
        try:
            text = http_get_text(url)
        except Exception as ex:
            failed.append((rf.local_path, f"fetch failed: {ex}"))
            eprint(f"[ERR] Failed to fetch {url}: {ex}")
            continue

        did_write, reason = safe_write_file(rf.local_path, text, args.overwrite, args.dry_run)
        if did_write:
            created.append((rf.local_path, reason))
            print(f"[OK] {rf.local_path}: {reason}")
        else:
            skipped.append((rf.local_path, reason))
            print(f"[SKIP] {rf.local_path}: {reason}")

    # 3) README.md (optional)
    if args.write_readme:
        # Use README_TEMPLATE.md (local) if present; otherwise fetch it from template (already fetched above)
        readme_template_path = "README_TEMPLATE.md"
        if not os.path.exists(readme_template_path):
            eprint("[ERR] README_TEMPLATE.md not found locally; cannot render README.md.")
        else:
            with open(readme_template_path, "r", encoding="utf-8", errors="replace") as f:
                template = f.read()
            rendered = render_readme_from_template(template, args.project_name)
            did_write, reason = safe_write_file("README.md", rendered, args.overwrite, args.dry_run)
            if did_write:
                created.append(("README.md", reason))
                print(f"[OK] README.md: {reason}")
            else:
                skipped.append(("README.md", reason))
                print(f"[SKIP] README.md: {reason}")

    # 4) .gitignore patch (optional)
    if args.patch_gitignore:
        patch_gitignore(".gitignore", args.dry_run)

    # Summary
    print("\n=== Summary ===")
    if created:
        print("Created/Updated:")
        for p, r in created:
            print(f"  - {p} ({r})")
    if skipped:
        print("Skipped:")
        for p, r in skipped:
            print(f"  - {p} ({r})")
    if failed:
        print("Failed:")
        for p, r in failed:
            print(f"  - {p} ({r})")

    # Exit code
    if failed:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
