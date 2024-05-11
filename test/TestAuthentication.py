import os
import unittest
from database.database import Database
from security.authentication import Authentication


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.db_file = "test_db.db"
        self.db = Database(self.db_file)
        self.auth = Authentication(self.db_file)

    def tearDown(self):
        self.db.conn.close()
        os.remove(self.db_file)

    def test_register_user(self):
        self.auth.register_user("test_user", "password123", "user")

        self.assertIsNotNone(self.auth.authenticate_user("test_user", "password123", "user"))

    def test_authenticate_user(self):

        self.auth.register_user("test_user", "password123", "user")

        # Authenticate the user with correct credentials
        role = self.auth.authenticate_user("test_user", "password123", "user")
        self.assertEqual(role, "user")

        # Authenticate the user with incorrect password
        role = self.auth.authenticate_user("test_user", "wrong_password", "user")
        self.assertIsNone(role)

    def test_check_role_access(self):
        self.db.cursor.execute("INSERT INTO roles (role, resource) VALUES ('user', 'resource1')")
        self.db.conn.commit()

        self.assertTrue(self.auth.check_role_access("test_user", "user", "resource1"))

        self.assertFalse(self.auth.check_role_access("test_user", "user", "resource2"))


if __name__ == '__main__':
    unittest.main()
