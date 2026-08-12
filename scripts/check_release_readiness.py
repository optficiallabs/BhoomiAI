"""Release-readiness checks for BhoomiAI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.benchmark_validation import load_jsonl, validate_cases

REQUIRED_FILES = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md",
    "CHANGELOG.md", "ROADMAP.md", "RELEASE_NOTES_v0.1.0.md", "pyproject.toml",
    "benchmarks/agriculture_security_cases.jsonl",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:", ", ".join(missing))
        return 1

    benchmark = ROOT / "benchmarks" / "agriculture_security_cases.jsonl"
    result = validate_cases(load_jsonl(benchmark))
    if not result["valid"]:
        print("Benchmark validation failed:", result["errors"])
        return 1

    compile_result = subprocess.run([sys.executable, "-m", "compileall", "-q", "src", "scripts"], cwd=ROOT)
    if compile_result.returncode:
        return compile_result.returncode

    test_result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], cwd=ROOT)
    return test_result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
