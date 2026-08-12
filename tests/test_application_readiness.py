import unittest
from pathlib import Path

from src.benchmark_runner import calculate_metrics, load_jsonl, run_benchmark
from src.integrated_evaluator import evaluate_case


class TestApplicationReadiness(unittest.TestCase):
    def test_expanded_agriculture_benchmark_is_complete_and_green(self):
        benchmark = Path("benchmarks/agriculture_security_cases.jsonl")
        cases = load_jsonl(benchmark)
        self.assertEqual(len(cases), 25)
        self.assertEqual(len({case["id"] for case in cases}), 25)

        categories = {case["category"] for case in cases}
        required = {
            "normal_guidance",
            "content_security",
            "recommendation_safety",
            "privacy",
            "market_integrity",
            "access_control",
            "human_review",
            "weather_integrity",
            "field_verification",
            "multi_step",
        }
        self.assertTrue(required.issubset(categories))

        results = run_benchmark(cases, evaluate_case)
        metrics = calculate_metrics(results)
        self.assertEqual(metrics["incorrect"], 0)
        self.assertEqual(metrics["accuracy"], 1.0)


if __name__ == "__main__":
    unittest.main()
