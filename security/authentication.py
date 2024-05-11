from database.database import Database
from security.encryption import Encryption


class Authentication:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def register_user(self, username, password, role):
        hashed_password = Encryption.hashed_password(password)
        self.db.cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hashed_password, role))
        self.db.conn.commit()
        print("User registered successfully")

    def authenticate_user(self, username, password, role):
        self.db.cursor.execute(
            "SELECT password, role FROM users WHERE username = ?",
            (username,))
        user_data = self.db.cursor.fetchone()
        if user_data:
            hashed_password, role = user_data
            if Encryption.verify_password(password, hashed_password):
                return role
        return None

    def check_role_access(self, param, param1, param2):
        pass
