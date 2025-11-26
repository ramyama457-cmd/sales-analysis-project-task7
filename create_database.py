import sqlite3
import os

# Remove existing database file if it exists
if os.path.exists("sales_data.db"):
    os.remove("sales_data.db")

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date DATE NOT NULL
)
''')

# Insert sample data
sample_data = [
    ('Laptop', 5, 999.99, '2024-01-15'),
    ('Mouse', 20, 25.50, '2024-01-15'),
    ('Laptop', 3, 999.99, '2024-01-16'),
    ('Keyboard', 15, 75.00, '2024-01-16'),
    ('Mouse', 10, 25.50, '2024-01-17'),
    ('Monitor', 8, 299.99, '2024-01-17'),
    ('Keyboard', 12, 75.00, '2024-01-18'),
    ('Monitor', 5, 299.99, '2024-01-18')
]

cursor.executemany('''
INSERT INTO sales (product, quantity, price, sale_date)
VALUES (?, ?, ?, ?)
''', sample_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully with sample data!")