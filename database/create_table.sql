CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS shipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER,
    quantity INTEGER,
    shipment_date DATE,
    FOREIGN KEY (item_id) REFERENCES inventory(id)
);

CREATE TABLE IF NOT EXISTS transportation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER,
    driver_id INTEGER,
    destination TEXT,
    arrival_time DATETIME,
    departure_time DATETIME
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL

);

CREATE TABLE IF NOT EXISTS security_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    timestamp DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)

);
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY,
    role TEXT NOT NULL,
    resource TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);