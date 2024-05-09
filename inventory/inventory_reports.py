from database.database import Database


class InventoryReports:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def generate_inventory_report(self):
        try:
            self.db.cursor.execute("SELECT * FROM inventory")
            inventory_data = self.db.cursor.fetchall()

            if not inventory_data:
                print("Inventory is empty.")
                return

            print("Inventory Report:")
            for item in inventory_data:
                print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Location: {item[3]}")

        except Exception as e:
            print(f"Error generating inventory report: {e}")


# Example usage:
if __name__ == "__main__":
    db_file = "database/inventory_management.db"
    inventory_reports = InventoryReports(db_file)
    inventory_reports.generate_inventory_report()
