import sqlite3

DB_NAME = "bolibahi.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Customer Udhaar (Credit) Ledger
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            phone TEXT,
            balance REAL DEFAULT 0.0
        )
    """)
    
    # Shop Inventory
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT UNIQUE NOT NULL,
            stock_qty REAL DEFAULT 0.0,
            unit TEXT DEFAULT 'pcs'
        )
    """)
    
    # Seed sample data
    cursor.execute("INSERT OR IGNORE INTO customers (name, phone, balance) VALUES ('Ramesh', '+919876543210', 250.0)")
    cursor.execute("INSERT OR IGNORE INTO inventory (item_name, stock_qty, unit) VALUES ('sugar', 50.0, 'kg'), ('soap', 30.0, 'pcs')")
    
    conn.commit()
    conn.close()

def update_udhaar(customer_name: str, amount: float):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT balance, phone FROM customers WHERE LOWER(name) = LOWER(?)", (customer_name,))
    row = cursor.fetchone()
    
    if row:
        new_balance = row[0] + amount
        phone = row[1]
        cursor.execute("UPDATE customers SET balance = ? WHERE LOWER(name) = LOWER(?)", (new_balance, customer_name))
    else:
        new_balance = amount
        phone = None
        cursor.execute("INSERT INTO customers (name, balance) VALUES (?, ?)", (customer_name.capitalize(), new_balance))
        
    conn.commit()
    conn.close()
    return new_balance, phone

def deduct_inventory(item_name: str, qty: float):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET stock_qty = MAX(0, stock_qty - ?) WHERE LOWER(item_name) = LOWER(?)", (qty, item_name))
    conn.commit()
    conn.close()
