"""Validation helpers for BhoomiAI synthetic benchmark files."""

from __future__ import annotations

import json
from pathlib import Path

REQUIRED_FIELDS = {"id", "category", "scenario", "expected_decision"}


def load_jsonl(path: str | Path) -> list[dict]:
    records = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                record = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"Line {line_number} must contain a JSON object")
            records.append(record)
    return records


def validate_cases(cases: list[dict]) -> dict:
    errors: list[str] = []
    seen: set[str] = set()
    for index, case in enumerate(cases, start=1):
        missing = sorted(REQUIRED_FIELDS - set(case))
        if missing:
            errors.append(f"case {index} missing fields: {', '.join(missing)}")
        case_id = str(case.get("id") or "")
        if case_id:
            if case_id in seen:
                errors.append(f"duplicate id: {case_id}")
            seen.add(case_id)
    return {"valid": not errors, "case_count": len(cases), "errors": errors}
