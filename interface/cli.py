def generate_inventory_report():
    print("Generating inventory report...")


class CLI:
    def __init__(self, inventory_manager, transportation_manager, auth):
        self.inventory_manager = inventory_manager
        self.transportation_manager = transportation_manager
        self.auth = auth

    def start(self):
        print("Greeting to St. Mary's Logistics Database System")

        while True:
            print("\nPlease select an option:")
            print("1. Add item to inventory")
            print("2. Add transportation details")
            print("3. Update item quantity")
            print("4. register")
            print("5. Generate inventory report")
            print("6. Exit")

            option = input("Enter your choice: ")

            if option == "1":
                self.add_item_to_inventory()
            elif option == "2":
                self.update_item_quantity()
            elif option == "3":
                self.add_transportation_details()
            elif option == "4":
                generate_inventory_report()
            elif option == "5":
                self.user_register()
            elif option == "6":
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

    def user_register(self):
        username = input("username:")
        password = input("password:")
        role = input("role")
        self.auth.authenticate_user(username, password, role)
