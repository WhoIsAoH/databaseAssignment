import sqlite3

from database.database import Database


class InventoryManagement:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.db = Database(db_file)

    def add_item(self, name, quantity, location):
        self.db.cursor.execute("INSERT INTO inventory (name, quantity, location) VALUES (?, ?, ?)",
                               (name, quantity, location))
        self.db.conn.commit()



    def update_quantity(self, item_id, new_quantity):
        self.db.cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?", (new_quantity, item_id))
        self.db.conn.commit()

