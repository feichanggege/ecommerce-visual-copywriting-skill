#!/usr/bin/env python3
"""Release checks for ecommerce-visual-copywriting-skill v3."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "SKILL.en.md",
    "README.md",
    "README.en.md",
    "LICENSE",
    "agents/openai.yaml",
    "examples/README.md",
    "references/compliance-rules.md",
    "references/platform-playbooks.md",
    "references/output-contracts.md",
    "assets/showcase-output.svg",
    "assets/showcase/musang-king-durian-main.jpg",
    "assets/showcase/figure-multi-angle.png",
    "assets/showcase/figure-desktop-scene.png",
    "assets/showcase/lumina-pendant-lamp.png",
    "assets/showcase/thumbs/musang-king-durian-main-thumb.jpg",
    "assets/showcase/thumbs/figure-multi-angle-thumb.jpg",
    "assets/showcase/thumbs/figure-desktop-scene-thumb.jpg",
    "assets/showcase/thumbs/lumina-pendant-lamp-thumb.jpg",
    "test-prompts.json",
    ".claude-plugin/marketplace.json",
]

CHECKS = {
    "SKILL.md": [
        "name: ecommerce-visual-copywriting",
        "证据账本",
        "一次性交付模式",
        "Reference Fidelity",
        "Negative Prompt",
        "references/platform-playbooks.md",
        "五维 Pass/Fail",
    ],
    "SKILL.en.md": [
        "Evidence ledger",
        "One-shot",
        "Reference Fidelity",
        "Negative Constraints",
        "Pass/Fail",
    ],
    "README.md": [
        "npx skills add feichanggege/ecommerce-visual-copywriting-skill",
        "E-commerce Visual Copywriting",
        "证据账本",
        "多平台 Playbook",
        "assets/showcase-output.svg",
        "安全边界",
    ],
    "README.en.md": [
        "Quick Start",
        "Evidence Ledger",
        "Reference Fidelity",
        "Platforms",
        "Safety",
    ],
    "agents/openai.yaml": [
        "display_name:",
        "short_description:",
    ],
    "references/platform-playbooks.md": [
        "Amazon",
        "Shopify",
        "TikTok Shop",
        "Temu",
        "Shopee / Lazada",
    ],
    "references/compliance-rules.md": [
        "证据状态",
        "普通食品/饮料",
        "平台规则的时效性",
    ],
    "references/output-contracts.md": [
        "证据账本",
        "Storyboard",
        "审查/改稿报告",
        "跨境本地化交付",
    ],
}

SECRET_PATTERNS = [
    re.compile(r"gho_[A-Za-z0-9_]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
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


def check_skill_frontmatter() -> None:
    text = read("SKILL.md")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter is not closed")
    frontmatter = parts[1]
    keys = set(re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, re.MULTILINE))
    expected = {"name", "description"}
    if keys != expected:
        fail(f"SKILL.md frontmatter keys must be exactly {sorted(expected)}, got {sorted(keys)}")
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name_match or name_match.group(1).strip() != "ecommerce-visual-copywriting":
        fail("SKILL.md name is invalid")
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not description_match or len(description_match.group(1).strip()) < 80:
        fail("SKILL.md description is too short")
    if len(text.splitlines()) > 500:
        fail("SKILL.md exceeds the 500-line progressive-loading target")


def main() -> int:
    for path in REQUIRED_FILES:
        if not (ROOT / path).exists():
            fail(f"missing required file: {path}")

    check_skill_frontmatter()

    for path, needles in CHECKS.items():
        text = read(path)
        for needle in needles:
            if needle not in text:
                fail(f"{path} missing expected text: {needle}")

    try:
        prompts = json.loads(read("test-prompts.json"))
    except json.JSONDecodeError as exc:
        fail(f"test-prompts.json is invalid JSON: {exc}")
    names = {item.get("name") for item in prompts if isinstance(item, dict)}
    expected_prompts = {
        "standard_storyboard_gate",
        "amazon_one_shot_localization",
        "ordinary_food_claim_boundary",
        "audit_minimum_change",
        "reference_fidelity_lock",
        "shopify_cross_border_localization",
    }
    if not expected_prompts.issubset(names):
        fail("test-prompts.json is missing v3 coverage")

    for file in ROOT.rglob("*"):
        if ".git" in file.parts or not file.is_file() or file.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = file.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret or private path in {file.relative_to(ROOT)}")

    print("PASS: v3 skill release checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
