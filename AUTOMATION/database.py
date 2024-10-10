import sqlite3

# Connect to or create the SQLite database
connection = sqlite3.connect('sales.db')

# Create a cursor object
cursor = connection.cursor()

# Create the daily sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        total REAL NOT NULL
    )
''')

# Commit changes and close the connection
connection.commit()
connection.close()