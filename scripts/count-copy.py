#!/usr/bin/env python3
"""Count copy lengths using the skill's internal layout convention, not platform rules."""
import argparse
import json


def count(text: str, language: str) -> int:
    return len(text.split()) if language == "en" else sum(not char.isspace() for char in text)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("zh", "en"), default="zh")
    parser.add_argument("texts", nargs="+")
    args = parser.parse_args()
    print(json.dumps([
        {"text": text, "count": count(text, args.language), "unit": "words" if args.language == "en" else "characters"}
        for text in args.texts
    ], ensure_ascii=False))


if __name__ == "__main__":
    main()
