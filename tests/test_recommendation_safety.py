import unittest

from src.recommendation_safety import evaluate_recommendation


class TestRecommendationSafety(unittest.TestCase):
    def test_high_risk_requires_label_reference(self):
        result = evaluate_recommendation("pesticide", has_local_context=True, has_label_reference=False)
        self.assertEqual(result["decision"], "review")

    def test_low_risk_reference_guidance_allowed(self):
        result = evaluate_recommendation("irrigation", has_local_context=True, has_label_reference=False)
        self.assertEqual(result["decision"], "allow")


if __name__ == "__main__":
    unittest.main()
