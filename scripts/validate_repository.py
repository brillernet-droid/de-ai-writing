#!/usr/bin/env python3
"""Validate the public de-ai-writing repository before release."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SKILL.md",
    "agents/openai.yaml",
    "references/ai-lexicon.md",
    "references/ai-structure-patterns.md",
    "references/ai-formatting-artifacts.md",
    "examples/academic-safe.md",
    "examples/business-copy.md",
    "examples/translation-naturalise.md",
    "docs/positioning.md",
    "docs/promotion-kit.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AKID[A-Za-z0-9]{13,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[\"'][^\"']{8,}[\"']"),
]

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def iter_text_files():
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or path.is_dir():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
            continue
        yield path


def check_secrets() -> None:
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret in {path.relative_to(ROOT)}")


def check_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                fail(f"broken link in {path.relative_to(ROOT)} -> {target}")


def check_skill_frontmatter() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    if "name: de-ai-writing" not in text:
        fail("SKILL.md frontmatter must keep name: de-ai-writing")
    if "description:" not in text.split("---", 2)[1]:
        fail("SKILL.md frontmatter missing description")


def main() -> int:
    check_required_files()
    check_skill_frontmatter()
    check_markdown_links()
    check_secrets()
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

