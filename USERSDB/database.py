import sqlite3

# Connection to the database
def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

# Create users table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        lastname TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance REAL NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Add user
def add_user(name, lastname, age, balance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, lastname, age, balance) VALUES (?, ?, ?, ?)", (name, lastname, age, balance))
    conn.commit()
    conn.close()

# Load all users
def load_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Filter users by age
def filter_users_by_age(min_age, max_age):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE age BETWEEN ? AND ?", (min_age, max_age))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Filter users by balance
def filter_users_by_balance(is_less_than):
    conn = connect_db()
    cursor = conn.cursor()
    if is_less_than:
        cursor.execute("SELECT * FROM users WHERE balance < 10000")
    else:
        cursor.execute("SELECT * FROM users WHERE balance >= 10000")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Create the table at startup
create_table()