"""Command-line interface for BhoomiAI open-source utilities."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .access_control import authorise
from .benchmark_report import write_reports
from .benchmark_runner import calculate_metrics, load_jsonl, run_benchmark
from .content_security import scan_agriculture_content
from .integrated_evaluator import evaluate_case


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bhoomiai", description="BhoomiAI open-source utility CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-content")
    validate.add_argument("path")

    access = subparsers.add_parser("check-access")
    access.add_argument("role")
    access.add_argument("action")

    benchmark = subparsers.add_parser("run-integrated-benchmark")
    benchmark.add_argument("path")
    benchmark.add_argument("--include-results", action="store_true")

    report = subparsers.add_parser("generate-benchmark-report")
    report.add_argument("path")
    report.add_argument("--output-dir", default="artifacts/benchmark")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "validate-content":
        text = Path(args.path).read_text(encoding="utf-8")
        print(json.dumps(scan_agriculture_content(text), indent=2, sort_keys=True))
        return 0

    if args.command == "check-access":
        print(json.dumps(authorise(args.role, args.action), indent=2, sort_keys=True))
        return 0

    if args.command == "run-integrated-benchmark":
        results = run_benchmark(load_jsonl(args.path), evaluate_case)
        payload = {"metrics": calculate_metrics(results)}
        if args.include_results:
            payload["results"] = results
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["metrics"]["incorrect"] == 0 else 1

    if args.command == "generate-benchmark-report":
        results = run_benchmark(load_jsonl(args.path), evaluate_case)
        written = write_reports(results, args.output_dir)
        print(json.dumps({"json": written["json"], "markdown": written["markdown"], "metrics": written["report"]["metrics"]}, indent=2, sort_keys=True))
        return 0 if written["report"]["metrics"]["incorrect"] == 0 else 1

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
