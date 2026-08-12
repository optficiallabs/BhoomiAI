"""Configurable benchmark quality gates for BhoomiAI."""

from __future__ import annotations


def evaluate_thresholds(metrics: dict, minimum_accuracy: float, category_minimums: dict[str, float]) -> dict:
    failures = []
    accuracy = float(metrics.get("accuracy", 0.0))
    if accuracy < minimum_accuracy:
        failures.append({"type": "overall_accuracy", "actual": accuracy, "required": minimum_accuracy})
    categories = metrics.get("categories") or {}
    for category, required in category_minimums.items():
        if category not in categories:
            failures.append({"type": "missing_category", "category": category, "required": required})
            continue
        actual = float(categories[category].get("accuracy", 0.0))
        if actual < required:
            failures.append({"type": "category_accuracy", "category": category, "actual": actual, "required": required})
    return {"passed": not failures, "failures": failures}
