import tkinter as tk
from tkinter import messagebox
from inventory.inventory_reports import InventoryReports


class GUI:
    def __init__(self, inventory_manager, transportation_manager, db_file):
        self.conn = None
        self.cursor = None
        self.inventory_manager = inventory_manager
        self.transportation_manager = transportation_manager
        self.db_file = db_file

        self.root = tk.Tk()
        self.root.title("St. Mary's Logistics Database System")

        # Create GUI components
        self.label = tk.Label(self.root, text="Welcome to St. Mary's Logistics Database System", padx=30, pady=30,
                              fg="black")
        self.label.pack()

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        self.add_item_button = tk.Button(self.menu_frame, text="Add Item to Inventory", command=self.add_item_window)
        self.add_item_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_quantity_button = tk.Button(self.menu_frame, text="Update Item Quantity",
                                                command=self.update_quantity_window)
        self.update_quantity_button.grid(row=0, column=1, padx=5, pady=5)

        self.add_transportation_button = tk.Button(self.menu_frame, text="Add Transportation Details",
                                                   command=self.add_transportation_window)
        self.add_transportation_button.grid(row=1, column=0, padx=5, pady=5)

        self.generate_report_button = tk.Button(self.menu_frame, text="Generate Inventory Report",
                                                command=self.generate_report)
        self.generate_report_button.grid(row=1, column=1, padx=5, pady=5)

    def run(self):
        self.root.mainloop()

    def add_item_window(self):
        add_item_window = tk.Toplevel(self.root)
        add_item_window.title("Add Item to Inventory")

        name_label = tk.Label(add_item_window, text="Item Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_item_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        quantity_label = tk.Label(add_item_window, text="Quantity:")
        quantity_label.grid(row=1, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(add_item_window)
        quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        location_label = tk.Label(add_item_window, text="Location:")
        location_label.grid(row=2, column=0, padx=5, pady=5)
        location_entry = tk.Entry(add_item_window)
        location_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = tk.Button(add_item_window, text="Add",
                               command=lambda: self.add_item(name_entry.get(), quantity_entry.get(),
                                                             location_entry.get(), add_item_window))
        add_button.grid(row=3, columnspan=2, padx=5, pady=5)

    def add_item(self, name, quantity, location, window):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be greater than zero")
            else:
                self.inventory_manager.add_item(name, quantity, location)
                messagebox.showinfo("Success", "Item added to inventory")
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a positive integer")

    def update_quantity_window(self):
        update_quantity_window = tk.Toplevel(self.root)
        update_quantity_window.title("Update Item Quantity")

        item_id_label = tk.Label(update_quantity_window, text="Item ID:")
        item_id_label.grid(row=0, column=0, padx=5, pady=5)
        item_id_entry = tk.Entry(update_quantity_window)
        item_id_entry.grid(row=0, column=1, padx=5, pady=5)

        quantity_label = tk.Label(update_quantity_window, text="New Quantity:")
        quantity_label.grid(row=1, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(update_quantity_window)
        quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        update_button = tk.Button(update_quantity_window, text="Update",
                                  command=lambda: self.update_quantity(item_id_entry.get(), quantity_entry.get(),
                                                                       update_quantity_window))
        update_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def update_quantity(self, item_id, new_quantity, window):
        try:
            item_id = int(item_id)
            new_quantity = int(new_quantity)
            if new_quantity <= 0:
                messagebox.showerror("Error", "Quantity must be greater than zero")
            else:
                self.inventory_manager.update_quantity(item_id, new_quantity)
                messagebox.showinfo("Success", "Quantity updated")
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Item ID and Quantity must be numbers")

    def add_transportation_window(self):
        add_transportation_window = tk.Toplevel(self.root)
        add_transportation_window.title("Add Transportation Details")

        driver_id_label = tk.Label(add_transportation_window, text="Driver ID:")
        driver_id_label.grid(row=1, column=0, padx=5, pady=5)
        driver_id_entry = tk.Entry(add_transportation_window)
        driver_id_entry.grid(row=1, column=1, padx=5, pady=5)

        vehicle_id_label = tk.Label(add_transportation_window, text="Vehicle ID:")
        vehicle_id_label.grid(row=0, column=0, padx=5, pady=5)
        vehicle_id_entry = tk.Entry(add_transportation_window)
        vehicle_id_entry.grid(row=0, column=1, padx=5, pady=5)

        departure_time_label = tk.Label(add_transportation_window, text="Departure Time:")
        departure_time_label.grid(row=3, column=0, padx=5, pady=5)
        departure_time_entry = tk.Entry(add_transportation_window)
        departure_time_entry.grid(row=3, column=1, padx=5, pady=5)

        arrival_time_label = tk.Label(add_transportation_window, text="Arrival Time:")
        arrival_time_label.grid(row=4, column=0, padx=5, pady=5)
        arrival_time_entry = tk.Entry(add_transportation_window)
        arrival_time_entry.grid(row=4, column=1, padx=5, pady=5)

        destination_label = tk.Label(add_transportation_window, text="Destination:")
        destination_label.grid(row=2, column=0, padx=5, pady=5)
        destination_entry = tk.Entry(add_transportation_window)
        destination_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = tk.Button(add_transportation_window, text="Add",
                               command=lambda: self.add_transportation(vehicle_id_entry.get(), driver_id_entry.get(),
                                                                       destination_entry.get(),
                                                                       departure_time_entry.get(),
                                                                       arrival_time_entry.get(),
                                                                       add_transportation_window))
        add_button.grid(row=5, columnspan=2, padx=5, pady=5)

    def add_transportation(self, vehicle_id, driver_id, destination, departure_time, arrival_time, window):
        try:
            vehicle_id = int(vehicle_id)
            driver_id = int(driver_id)
            if departure_time >= arrival_time:
                messagebox.showerror("Error", "Departure time must be before arrival time")
            else:
                self.transportation_manager.add_transportation(vehicle_id, driver_id, destination, departure_time,
                                                               arrival_time)
                messagebox.showinfo("Success", "Transportation details added")
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Vehicle ID and Driver ID must be integers")

    def generate_report(self):
        print("Generating inventory report...")
        inventory_reports = InventoryReports(self.db_file)
        inventory_report = inventory_reports.generate_inventory_report()

        if inventory_report:
            output_file = "inventory_report.txt"
            with open(output_file, "w") as file:
                for item in inventory_report:
                    file.write(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Location: {item[3]}\n")

            report_window = tk.Toplevel(self.root)
            report_window.title("Inventory Report")

            with open(output_file, "r") as file:
                report_text = file.read()
                report_label = tk.Label(report_window, text=report_text)
                report_label.pack()

            messagebox.showinfo("Report Generated", f"The inventory report has been saved to {output_file}")
        else:
            messagebox.showinfo("Empty Inventory", "The inventory is empty.")
