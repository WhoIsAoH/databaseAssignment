from database.database import Database


class Authorization:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def check_role_access(self, username, role, resource):
        self.db.cursor.execute(
            "SELECT COUNT(*) FROM roles WHERE role = ? AND resource = ?",
            (role, resource))
        access_count = self.db.cursor.fetchone()[0]
        return access_count > 0
