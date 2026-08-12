import unittest

from src.secure_logging import redact_record


class TestSecureLogging(unittest.TestCase):
    def test_redacts_sensitive_fields_recursively(self):
        record = {"farmer_name": "Synthetic Farmer", "crop": "rice", "location": {"latitude": 1.0}}
        redacted = redact_record(record)
        self.assertEqual(redacted["farmer_name"], "[REDACTED]")
        self.assertEqual(redacted["location"]["latitude"], "[REDACTED]")
        self.assertEqual(redacted["crop"], "rice")


if __name__ == "__main__":
    unittest.main()
