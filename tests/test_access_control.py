import unittest

from src.access_control import authorise


class TestAccessControl(unittest.TestCase):
    def test_farmer_can_view_own_farm(self):
        self.assertTrue(authorise("farmer", "view_own_farm")["allowed"])

    def test_farmer_cannot_manage_users(self):
        result = authorise("farmer", "manage_users")
        self.assertFalse(result["allowed"])
        self.assertEqual(result["decision"], "deny")

    def test_unknown_role_fails_closed(self):
        self.assertFalse(authorise("unknown", "view_own_farm")["allowed"])


if __name__ == "__main__":
    unittest.main()
