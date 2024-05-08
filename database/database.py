import sqlite3


class Database:

    def __init__(self, db_file):
        self.cursor = None  # Fix here
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_tables(self, create_table_file):
        with open(create_table_file, 'r') as f:
            schema = f.read()
            self.cursor.executescript(schema)
        self.conn.commit()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor

    def fetch_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
