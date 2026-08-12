"""Run BhoomiAI integrated benchmark, thresholds, reports and regression checks."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.benchmark_regression import compare_to_baseline
from src.benchmark_report import write_reports
from src.benchmark_runner import calculate_metrics, load_jsonl, run_benchmark
from src.benchmark_thresholds import evaluate_thresholds
from src.integrated_evaluator import evaluate_case

BENCHMARK = ROOT / "benchmarks" / "agriculture_security_cases.jsonl"
BASELINE = ROOT / "benchmarks" / "baseline_v0.2.0.json"
THRESHOLDS = ROOT / "config" / "benchmark_thresholds.json"
OUTPUT = ROOT / "artifacts" / "benchmark"


def main() -> int:
    cases = load_jsonl(BENCHMARK)
    results = run_benchmark(cases, evaluate_case)
    metrics = calculate_metrics(results)
    config = json.loads(THRESHOLDS.read_text(encoding="utf-8"))
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    thresholds = evaluate_thresholds(metrics, float(config.get("minimum_accuracy", 1.0)), config.get("category_minimums") or {})
    regression = compare_to_baseline(results, baseline)
    written = write_reports(results, OUTPUT)
    payload = {"metrics": metrics, "thresholds": thresholds, "regression": regression, "reports": {"json": written["json"], "markdown": written["markdown"]}}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if thresholds["passed"] and regression["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
