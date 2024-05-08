class CLI:
    def __init__(self, inventory_manager, transportation_manager):
        self.inventory_manager = inventory_manager
        self.transportation_manager = transportation_manager

    def start(self):
        print("Greeting to St. Mary's Logistics Database System")

        while True:
            print("\nPlease select an option:")
            print("i. Add item to inventory")
            print("ii. Update item quantity")
            print("iii. Add transportation details")
            print("iv. Generate inventory report")
            print("v. Exit")

            option = input("Enter your choice: ")

            if option == "i":
                self.add_item_to_inventory()
            elif option == "ii":
                self.update_item_quantity()
            elif option == "iii":
                self.add_transportation_details()
            elif option == "iv":
                self.generate_inventory_report()
            elif option == "v":
                print("Exit...")
                break
            else:
                print("Invalid option")

    def add_item_to_inventory(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        location = input("Enter location: ")

        self.inventory_manager.add_item(name, quantity, location)
        print("Item added to inventory")

    def update_item_quantity(self):
        item_id = int(input("Enter item ID: "))
        new_quantity = int(input("Enter new quantity: "))

        self.inventory_manager.update_quantity(item_id, new_quantity)
        print("Quantity updated")

    def add_transportation_details(self):
        vehicle_id = int(input("Enter vehicle ID: "))
        driver_id = int(input("Enter driver ID: "))
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")

        self.transportation_manager.add_transportation(vehicle_id, driver_id, destination, departure_time, arrival_time)
        print("Transportation details added")

    def generate_inventory_report(self):
        print("Generating inventory report...")
        # Call the method from InventoryReports class to generate the report
