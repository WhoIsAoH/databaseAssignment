import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('stmarys_logistics.db')
cursor = conn.cursor()

# Create tables for inventory and transportation management
cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY,
                    item_name TEXT,
                    quantity INTEGER,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS shipments (
                    id INTEGER PRIMARY KEY,
                    item_id INTEGER,
                    shipment_type TEXT,
                    quantity INTEGER,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (item_id) REFERENCES inventory(id)
                )''')

# Insert some dummy data into the inventory table
cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", ('Item A', 100))
cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", ('Item B', 200))
conn.commit()


# Function to add new inventory items
def add_inventory_item(item_name, quantity):
    cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", (item_name, quantity))
    conn.commit()
    print(f"Item '{item_name}' with quantity '{quantity}' added to inventory.")


# Function to update stock levels
def update_stock(item_id, quantity_change):
    cursor.execute("UPDATE inventory SET quantity = quantity + ? WHERE id = ?", (quantity_change, item_id))
    conn.commit()
    print(f"Stock level for item with ID '{item_id}' updated by '{quantity_change}'.")


# Function to track incoming and outgoing shipments
def track_shipment(item_id, shipment_type, quantity):
    if shipment_type.lower() == 'incoming':
        update_stock(item_id, quantity)
    elif shipment_type.lower() == 'outgoing':
        update_stock(item_id, -quantity)
    else:
        print("Invalid shipment type")

    # Insert a record into the shipments table
    cursor.execute("INSERT INTO shipments (item_id, shipment_type, quantity) VALUES (?, ?, ?)",
                   (item_id, shipment_type, quantity))
    conn.commit()
    print(f"{shipment_type.capitalize()} shipment of {quantity} units for item with ID {item_id} tracked successfully.")


# Test the track_shipment function
# Example: Track an incoming shipment of 50 units for Item A
track_shipment(1, 'incoming', 50)

# Example: Track an outgoing shipment of 20 units for Item B
track_shipment(2, 'outgoing', 20)


# Function to generate inventory reports
def generate_inventory_report():
    cursor.execute("SELECT * FROM inventory")
    inventory_data = cursor.fetchall()
    for row in inventory_data:
        print(f"Item ID: {row[0]}, Item Name: {row[1]}, Quantity: {row[2]}, Last Updated: {row[3]}")


print("Inventory Report:")
generate_inventory_report()



# transportation

# Create tables for transportation management
cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                    id INTEGER PRIMARY KEY,
                    vehicle_name TEXT,
                    capacity INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS drivers (
                    id INTEGER PRIMARY KEY,
                    driver_name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS transportation_schedule (
                    id INTEGER PRIMARY KEY,
                    item_id INTEGER,
                    vehicle_id INTEGER,
                    driver_id INTEGER,
                    scheduled_date TIMESTAMP,
                    FOREIGN KEY (item_id) REFERENCES inventory(id),
                    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id),
                    FOREIGN KEY (driver_id) REFERENCES drivers(id)
                )''')
# Insert dummy data into vehicles and drivers tables
cursor.execute("INSERT INTO vehicles (vehicle_name, capacity) VALUES (?, ?)", ('Truck A', 500))
cursor.execute("INSERT INTO vehicles (vehicle_name, capacity) VALUES (?, ?)", ('Truck B', 700))
conn.commit()
cursor.execute("INSERT INTO drivers (driver_name) VALUES (?)", ('John Doe',))
cursor.execute("INSERT INTO drivers (driver_name) VALUES (?)", ('Jane Smith',))
conn.commit()

# Function to generate transportation schedule
def generate_transportation_schedule(item_id, vehicle_id, driver_id, scheduled_date):
    cursor.execute(
        "INSERT INTO transportation_schedule (item_id, vehicle_id, driver_id, scheduled_date) VALUES (?, ?, ?, ?)",
        (item_id, vehicle_id, driver_id, scheduled_date))
    conn.commit()
    print(f"Transportation schedule for item with ID {item_id} generated successfully for {scheduled_date}.")


# Test the transportation schedule function
# Example: Generate a transportation schedule for Item A using Truck A and Driver John Doe on 2024-04-28
generate_transportation_schedule(1, 8, 1, '2024-04-28')

# Close the database connection
conn.close()
# Close the database connection
conn.close()
