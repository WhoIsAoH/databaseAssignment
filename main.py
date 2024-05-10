# main.py

from interface.cli import CLI
from interface.gui import GUI
from inventory.inventory_management import InventoryManagement
from security.authentication import Authentication
from security.authorization import Authorization
from transportation.transportation_management import TransportationManagement
from database.database import Database


def main():
    db_file = 'database/inventory_managements.db'
    table_file = 'database/create_table.sql'
    database = Database(db_file)
    database.create_tables(table_file)

    inventory_manager = InventoryManagement(db_file)
    auth=Authentication(db_file)
    Authorization(db_file)
    transportation_manager = TransportationManagement(db_file)

    interface_of_user = input("Choose interface (CLI or GUI): ").lower()
    if interface_of_user == 'cli':
        cli_interface = CLI(inventory_manager, transportation_manager,auth)
        cli_interface.start()
    elif interface_of_user == 'gui':
        gui_interface = GUI(inventory_manager, transportation_manager, db_file)
        gui_interface.run()
    else:
        print("Invalid choice. Please choose either CLI or GUI.")


if __name__ == "__main__":
    main()
