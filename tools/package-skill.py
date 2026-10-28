#!/usr/bin/env python3
"""Build a minimal, self-contained skill folder ZIP for manual installation/upload."""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "ecommerce-visual-copywriting"
RUNTIME_PATHS = ("SKILL.md", "SKILL.en.md", "LICENSE", "agents", "references", "examples", "scripts")


def package(output: Path, root: Path = ROOT) -> int:
    files = []
    for relative in RUNTIME_PATHS:
        path = root / relative
        if not path.exists():
            raise ValueError(f"missing runtime resource: {relative}")
        files.extend(sorted(path.rglob("*")) if path.is_dir() else [path])
    files = [path for path in files if path.is_file()]
    if output.resolve().is_relative_to(root.resolve()) and output.resolve() in [path.resolve() for path in files]:
        raise ValueError("output must not overwrite a runtime resource")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, f"{SKILL_NAME}/{path.relative_to(root).as_posix()}")
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / f"{SKILL_NAME}.zip")
    args = parser.parse_args()
    try:
        count = package(args.output)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print(f"PASS: packaged {count} runtime files ({args.output.stat().st_size:,} bytes) into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
