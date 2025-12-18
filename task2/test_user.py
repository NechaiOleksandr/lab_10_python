import unittest
from user import User
from admin import Admin

class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_user = User("Олександр", "Тестовий", "test@mail.com", "Tester123")

    def test_user_initialization(self):
        self.assertEqual(self.test_user.firstName, "Олександр")
        self.assertEqual(self.test_user.lastName, "Тестовий")
        self.assertEqual(self.test_user.loginAttempts, 0)
        self.assertFalse(self.test_user.newsletter)

    def test_increment_login_attempts(self):
        self.test_user.increment_login_attempts()
        self.test_user.increment_login_attempts()
        self.assertEqual(self.test_user.loginAttempts, 2)

    def test_reset_login_attempts(self):
        self.test_user.increment_login_attempts()
        self.test_user.reset_login_attempts()
        self.assertEqual(self.test_user.loginAttempts, 0)

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.test_admin = Admin("Олександр", "Адмінов", "admin@mail.com", "SuperTestAdmin")

    def test_admin_privileges_exists(self):
        from admin import Privileges
        self.assertIsInstance(self.test_admin.priv, Privileges)

    def test_default_privileges_list(self):
        expected_privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
            "Allowed to modify settings"
        ]
        self.assertEqual(self.test_admin.priv.privileges, expected_privileges)

if __name__ == '__main__':
    unittest.main()