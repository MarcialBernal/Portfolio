import os
import sqlite3

# Remove the database file if it exists
if os.path.exists('users.db'):
    os.remove('users.db')

# Create a new database and table
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        lastname TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance REAL NOT NULL
                    )''')
    
    conn.commit()
    conn.close()

# Call the function to create the database
create_database()