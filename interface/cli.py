from inventory.inventory_reports import InventoryReports


class CLI:
    def __init__(self, inventory_manager, transportation_manager, security_file, db_file):
        self.db_file = db_file
        self.db_file = self.db_file
        self.inventory_manager = inventory_manager
        self.transportation_manager = transportation_manager
        self.security_file = security_file

    def start(self):
        print("Welcome to St. Mary's Logistics Database System")

        while True:
            print("\nPlease select an option:")
            print("1. Add item to inventory")
            print("2. Update item quantity")
            print("3. Add transportation details")
            print("4. Generate inventory report")
            print("5. Register user")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item_to_inventory()
            elif choice == "2":
                self.update_item_quantity()
            elif choice == "3":
                self.add_transportation_details()
            elif choice == "4":
                self.generate_inventory_report()
            elif choice == "5":
                self.register()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    def update_item_quantity(self):
        item_id = int(input("Enter item ID: "))
        new_quantity = int(input("Enter new quantity: "))

        self.inventory_manager.update_quantity(item_id, new_quantity)
        print("Successfully updated")

    def add_item_to_inventory(self):
        name = input("Enter the name of the item: ")
        quantity = int(input("Enter quantity: "))
        location = input("Enter location: ")

        self.inventory_manager.add_item(name, quantity, location)
        print("successfully item added to inventory")

    def add_transportation_details(self):
        vehicle_id = int(input("Enter vehicle ID: "))
        driver_id = int(input("Enter driver ID: "))
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")

        self.transportation_manager.add_transportation(vehicle_id, driver_id, destination, departure_time, arrival_time)
        print("Transportation details added")

    def register(self):
        username = input("username:")
        password = input("password:")
        role = input("role:")
        self.security_file.register_user(username, password, role)

    def generate_inventory_report(self):
        print("Generating inventory report...")
        inventory_reports = InventoryReports(self.db_file)
        inventory_report = inventory_reports.generate_inventory_report()
        if inventory_report:
            output_file = "inventory_report.txt"
            with open(output_file, "w") as file:
                for item in inventory_report:
                    file.write(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Location: {item[3]}\n")
        print("Report Generated", f"The inventory report has been saved to file")
