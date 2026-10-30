#!/usr/bin/env python3
"""Flag placeholders and internal notes left in final copy. A lexical check only, not a quality or legal review."""
import argparse
import json
import re
import sys

HARD = {
    "待补/待确认/待核": r"待(?:补证?|确认|定|核实?|核验)",
    "未提供类括注": r"[（(][^）)\n]*(?:未提供|未给出|缺失|待提供)[^）)\n]*[）)]",
    "TODO/TBD": r"\b(?:TODO|TBD|FIXME)\b",
    "空占位": r"【\s*】|\[\s*\]|X{3,}|\?{3,}|？{3,}",
}
SOFT = {
    "内部建议口吻": r"(?:^|[，。；\s])(?:建议|备注|注意)[:：]",
    "此处填写": r"此处(?:填|放|写|补)",
    "暂定/拟定": r"暂(?:定|无|不|未)|拟(?:定|用|补)",
    "含括注，请人工确认不是内部说明": r"[（(][^）)\n]{1,40}[）)]",
}


def scan(text: str) -> dict:
    return {
        "hard": [name for name, pattern in HARD.items() if re.search(pattern, text)],
        "soft": [name for name, pattern in SOFT.items() if re.search(pattern, text)],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("texts", nargs="+")
    args = parser.parse_args()
    results = [{"text": text, **scan(text)} for text in args.texts]
    print(json.dumps(results, ensure_ascii=False))
    return 1 if any(item["hard"] for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
