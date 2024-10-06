import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


users_database = sqlite3.connect('users.db')

df = pd.read_sql_query("SELECT * FROM users", users_database)

users_database.close()

#

total_balance = np.sum(df['Balance'])

print(total_balance)

df.groupby('Age')['Balance'].sum().plot(kind='bar')
plt.title('Account Balance per Age')
plt.xlabel('Age')
plt.ylabel('Balance')
plt.show()