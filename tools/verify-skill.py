#!/usr/bin/env python3
"""Minimal release checks for ecommerce-visual-copywriting-skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "examples/README.md",
    "references/compliance-rules.md",
    "assets/showcase-output.svg",
    ".claude-plugin/marketplace.json",
]

CHECKS = {
    "SKILL.md": [
        "name: ecommerce-visual-copywriting",
        "description:",
        "不要用于",
        "Step 2",
        "暂停",
        "自审评分",
        "普通食品",
        "references/compliance-rules.md",
    ],
    "README.md": [
        "npx skills add feichanggege/ecommerce-visual-copywriting-skill",
        "装完后，对 Agent 说",
        "效果示例",
        "安全边界",
        "python tools/verify-skill.py",
        "assets/showcase-output.svg",
    ],
    "examples/README.md": [
        "Ordinary Food",
        "Fitness Equipment",
        "Compliance Review",
    ],
    "references/compliance-rules.md": [
        "普通食品",
        "蓝帽子保健食品",
        "运动器材",
        "绝对化用语",
    ],
}

SECRET_PATTERNS = [
    re.compile(r"gho_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)(api[_-]?key|token|cookie|secret|password)\s*[:=]\s*['\"]?[^'\"\s]{8,}"),
    re.compile(r"[A-Z]:\\Users\\[^\\\s]+"),
]

TEXT_SUFFIXES = {".md", ".json", ".py", ".svg", ".txt", ".yml", ".yaml"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read(path: str) -> str:
    full = ROOT / path
    if not full.exists():
        fail(f"missing required file: {path}")
    return full.read_text(encoding="utf-8")


def main() -> int:
    for path in REQUIRED_FILES:
        if not (ROOT / path).exists():
            fail(f"missing required file: {path}")

    for path, needles in CHECKS.items():
        text = read(path)
        for needle in needles:
            if needle not in text:
                fail(f"{path} missing expected text: {needle}")

    for file in ROOT.rglob("*"):
        if ".git" in file.parts or not file.is_file() or file.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = file.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret or private path in {file.relative_to(ROOT)}")

    print("PASS: skill release checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
