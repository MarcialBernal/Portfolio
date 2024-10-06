import sqlite3
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to the database
def connect_db():
    connection = sqlite3.connect('users.db')
    return connection

# Function to add a user
def add_user(name, lastname, age, balance):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, lastname, age, balance) VALUES (?, ?, ?, ?)", (name, lastname, age, balance))
    connection.commit()
    connection.close()

# Function to generate and add 100 random users
def populate_users(num_users=100):
    for _ in range(num_users):
        name = fake.first_name()
        lastname = fake.last_name()
        age = fake.random_int(min=18, max=80)  # Random age between 18 and 80
        balance = round(fake.random_number(digits=5) + fake.random.random(), 2)  # Random balance

        add_user(name, lastname, age, balance)

if __name__ == "__main__":
    populate_users()
    print("100 random users have been added to the database.")