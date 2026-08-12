"""Baseline regression comparison for BhoomiAI benchmarks."""

from __future__ import annotations


def compare_to_baseline(results: list[dict], baseline: dict) -> dict:
    current_by_id = {str(row.get("id")): row for row in results}
    baseline_cases = baseline.get("cases") or {}
    newly_failing = []
    missing = []
    changed = []

    for case_id, prior in baseline_cases.items():
        current = current_by_id.get(case_id)
        if current is None:
            missing.append(case_id)
            continue
        previous_correct = bool(prior.get("correct"))
        current_correct = bool(current.get("correct"))
        if previous_correct and not current_correct:
            newly_failing.append(case_id)
        if str(prior.get("actual_decision")) != str(current.get("actual_decision")):
            changed.append(case_id)

    new_cases = sorted(set(current_by_id) - set(baseline_cases))
    passed = not newly_failing and not missing
    return {
        "passed": passed,
        "newly_failing": newly_failing,
        "missing_baseline_cases": missing,
        "changed_decisions": changed,
        "new_cases": new_cases,
    }
