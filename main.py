# main.py

from interface.cli import CLI
from interface.gui import GUI
from inventory.inventory_management import InventoryManagement
from security.authentication import Authentication
from security.authorization import Authorization
from transportation.transportation_management import TransportationManagement
from database.database import Database


def main():
    db_file = 'database/inventory_management.db'
    table_file = 'database/create_table.sql'
    database = Database(db_file)
    database.create_tables(table_file)

    inventory_manager = InventoryManagement(db_file)
    security_manager = Authentication(db_file)
    authorization_manager = Authorization(db_file)
    transportation_manager = TransportationManagement(db_file)

    # Start the user interface (CLI or GUI)
    user_interface = input("Choose interface (CLI or GUI): ").lower()
    if user_interface == 'cli':
        cli_interface = CLI(inventory_manager, transportation_manager)
        cli_interface.start()
    elif user_interface == 'gui':
        gui_interface = GUI(inventory_manager, transportation_manager, db_file)
        gui_interface.run()
    else:
        print("Invalid choice. Please choose either CLI or GUI.")


if __name__ == "__main__":
    main()
