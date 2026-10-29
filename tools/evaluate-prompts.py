#!/usr/bin/env python3
"""Check saved agent responses; no API calls and no model-generated test results."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def validate_cases(cases: object) -> list[dict]:
    if not isinstance(cases, list) or not cases:
        raise ValueError("cases must be a non-empty JSON array")
    names = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("each case must be an object")
        name = case.get("name")
        if not isinstance(name, str) or not name or name in names:
            raise ValueError("case names must be non-empty and unique")
        names.add(name)
        for field in ("prompt",):
            if not isinstance(case.get(field), str) or not case[field].strip():
                raise ValueError(f"{name}: {field} must be non-empty text")
        if not isinstance(case.get("expected_behavior"), list) or not case["expected_behavior"] or not all(
            isinstance(item, str) and item.strip() for item in case["expected_behavior"]
        ):
            raise ValueError(f"{name}: expected_behavior must be a non-empty text array")
        for field in ("must_include", "must_not_include", "must_include_final"):
            if field == "must_include_final" and field not in case:
                continue
            values = case.get(field)
            if not isinstance(values, list) or not values:
                raise ValueError(f"{name}: {field} must be a non-empty array")
            for value in values:
                alternatives = value if isinstance(value, list) and field != "must_not_include" else [value]
                if not alternatives or not all(isinstance(item, str) and item.strip() for item in alternatives):
                    raise ValueError(f"{name}: invalid {field} matcher")
        if not isinstance(case.get("final_copy_required"), bool):
            raise ValueError(f"{name}: final_copy_required must be boolean")
    return cases


def evaluate(cases: list[dict], responses: object) -> list[str]:
    validate_cases(cases)
    if not isinstance(responses, list):
        raise ValueError("responses must be a JSON array")
    by_name = {}
    for item in responses:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            raise ValueError("each response needs a name")
        if item["name"] in by_name:
            raise ValueError(f"duplicate response: {item['name']}")
        if not isinstance(item.get("response"), str) or not item["response"].strip():
            raise ValueError(f"{item['name']}: response must be non-empty text")
        if not isinstance(item.get("final_copy"), str):
            raise ValueError(f"{item['name']}: final_copy must be text, empty only for blocked/strategy outputs")
        by_name[item["name"]] = item
    known = {case["name"] for case in cases}
    if set(by_name) - known:
        raise ValueError(f"unknown response names: {sorted(set(by_name) - known)}")
    failures = []
    for case in cases:
        name = case["name"]
        item = by_name.get(name)
        if item is None:
            failures.append(f"{name}: missing response")
            continue
        answer, final = item["response"].casefold(), item["final_copy"].casefold()
        if case["final_copy_required"] and not final.strip():
            failures.append(f"{name}: final_copy is required")
        # Prevent checking an unrelated or selectively rewritten final-copy field.
        if item["final_copy"].strip() and item["final_copy"] not in item["response"]:
            failures.append(f"{name}: final_copy must be an exact excerpt of response")
        for matcher in case["must_include"]:
            alternatives = matcher if isinstance(matcher, list) else [matcher]
            if not any(value.casefold() in answer for value in alternatives):
                failures.append(f"{name}: missing required marker {matcher!r}")
        # Required visible sources/conditions cannot be satisfied by analysis alone.
        for matcher in case.get("must_include_final", []):
            alternatives = matcher if isinstance(matcher, list) else [matcher]
            if not any(value.casefold() in final for value in alternatives):
                failures.append(f"{name}: missing required final-copy marker {matcher!r}")
        # Forbidden claims are checked ONLY in publishable copy, not quoted risk analysis.
        for value in case["must_not_include"]:
            if value.casefold() in final:
                failures.append(f"{name}: forbidden final-copy phrase {value!r}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=Path(__file__).resolve().parents[1] / "test-prompts.json")
    parser.add_argument("--responses", type=Path, required=True)
    args = parser.parse_args()
    try:
        cases = json.loads(args.cases.read_text(encoding="utf-8"))
        responses = json.loads(args.responses.read_text(encoding="utf-8"))
        failures = evaluate(cases, responses)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"PASS: {len(cases)} saved responses met lexical expectations; semantic/visual review is separate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
