from database.database import Database


class InventoryReports:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def generate_inventory_report(self):

        try:
            self.db.cursor.execute("SELECT * FROM inventory")
            return self.db.cursor  # Return the cursor object directly

        except Exception as e:
            print(f"Error generating inventory report: {e}")
            return None
