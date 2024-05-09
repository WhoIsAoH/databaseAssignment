from database.database import Database


class Authorization:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def check_role_access(self, username, role, resource):
        pass
