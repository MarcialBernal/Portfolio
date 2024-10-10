"""
This script connects to an SQLite database, retrieves user data, calculates the total balance 
across all users, and visualizes the balance distribution based on users' age.

Libraries used:
    - sqlite3: For interacting with the SQLite database.
    - pandas: To easily manipulate and analyze tabular data.
    - numpy: Used for numerical computations.
    - matplotlib: For creating visual plots.

Steps:
    1. Connect to the 'users.db' SQLite database and retrieve all data from the 'users' table 
       using a SQL query.
    2. Load the data into a pandas DataFrame for easy data manipulation.
    3. Close the database connection after retrieving the data.
    4. Calculate the total balance by summing all values in the 'Balance' column.
    5. Print the total balance.
    6. Group the data by users' age and plot the sum of balances per age group as a bar chart.
    7. Display the bar chart showing 'Account Balance per Age'.

Assumptions:
    - The database contains a 'users' table with columns 'Age' and 'Balance'.
    - The 'Balance' column stores numerical values representing each user's account balance.
"""
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
users_database = sqlite3.connect('users.db')

# Step 2: Retrieve all records from the 'users' table
df = pd.read_sql_query("SELECT * FROM users", users_database)

# Step 3: Close the database connection
users_database.close()

# Step 4: Calculate the total balance across all users
total_balance = np.sum(df['Balance'])

# Step 5: Print the total balance
print(total_balance)

# Step 6: Plot the total balance per age group
df.groupby('Age')['Balance'].sum().plot(kind='bar')

# Step 7: Customize the plot and show it
plt.title('Account Balance per Age')
plt.xlabel('Age')
plt.ylabel('Balance')
plt.show()