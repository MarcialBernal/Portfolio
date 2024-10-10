import sqlite3

# Connect to the database
connection = sqlite3.connect('sales.db')
cursor = connection.cursor()

# Sample sales data
sales_data = [
    ('2024-10-09', 'Product A', 10, 5.50, 10 * 5.50),
    ('2024-10-09', 'Product B', 3, 12.99, 3 * 12.99),
    ('2024-10-09', 'Product C', 1, 199.99, 1 * 199.99)
]

# Insert the data into the table
cursor.executemany('''
    INSERT INTO daily_sales (date, product, quantity, price, total)
    VALUES (?, ?, ?, ?, ?)
''', sales_data)

# Commit changes and close the connection
connection.commit()
connection.close()