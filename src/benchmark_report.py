"""JSON and Markdown benchmark report generation for BhoomiAI."""

from __future__ import annotations

import json
from pathlib import Path

from .benchmark_runner import calculate_metrics


def build_report(results: list[dict]) -> dict:
    metrics = calculate_metrics(results)
    failures = [
        {
            "id": row.get("id"),
            "category": row.get("category"),
            "expected_decision": row.get("expected_decision"),
            "actual_decision": row.get("actual_decision"),
        }
        for row in results if not row.get("correct")
    ]
    return {"metrics": metrics, "failures": failures, "results": results}


def markdown_report(report: dict) -> str:
    metrics = report["metrics"]
    lines = [
        "# BhoomiAI Benchmark Report",
        "",
        f"- Total cases: {metrics['total']}",
        f"- Correct: {metrics['correct']}",
        f"- Incorrect: {metrics['incorrect']}",
        f"- Accuracy: {metrics['accuracy']:.2%}",
        "",
        "## Category Accuracy",
        "",
        "| Category | Correct | Total | Accuracy |",
        "|---|---:|---:|---:|",
    ]
    for category, bucket in sorted(metrics["categories"].items()):
        lines.append(f"| {category} | {bucket['correct']} | {bucket['total']} | {bucket['accuracy']:.2%} |")
    lines.extend(["", "## Failed Cases", ""])
    failures = report.get("failures") or []
    if not failures:
        lines.append("No failed cases.")
    else:
        for failure in failures:
            lines.append(
                f"- {failure['id']}: expected `{failure['expected_decision']}`, got `{failure['actual_decision']}`"
            )
    return "\n".join(lines) + "\n"


def write_reports(results: list[dict], output_dir: str | Path) -> dict:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    report = build_report(results)
    json_path = output / "benchmark-report.json"
    md_path = output / "benchmark-report.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    md_path.write_text(markdown_report(report), encoding="utf-8")
    return {"json": str(json_path), "markdown": str(md_path), "report": report}
