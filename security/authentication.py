from database.database import Database


class Authentication:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def authenticate_user(self, username, password):
        pass
