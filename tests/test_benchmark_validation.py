import tempfile
import unittest
from pathlib import Path

from src.benchmark_validation import load_jsonl, validate_cases


class TestBenchmarkValidation(unittest.TestCase):
    def test_valid_cases(self):
        cases = [{"id": "AG-001", "category": "normal", "scenario": "Synthetic case", "expected_decision": "allow"}]
        result = validate_cases(cases)
        self.assertTrue(result["valid"])
        self.assertEqual(result["case_count"], 1)

    def test_duplicate_ids_fail(self):
        cases = [
            {"id": "AG-001", "category": "a", "scenario": "one", "expected_decision": "allow"},
            {"id": "AG-001", "category": "b", "scenario": "two", "expected_decision": "review"},
        ]
        self.assertFalse(validate_cases(cases)["valid"])

    def test_load_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "cases.jsonl"
            path.write_text('{"id":"AG-001","category":"normal","scenario":"x","expected_decision":"allow"}\n', encoding="utf-8")
            self.assertEqual(len(load_jsonl(path)), 1)


if __name__ == "__main__":
    unittest.main()
