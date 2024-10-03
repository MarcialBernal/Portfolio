import tkinter as tk
from tkinter import messagebox, ttk
import database  # Import the database module
from populate_db import populate_users

# Add user to the database
def add_user():
    name = entry_name.get()
    lastname = entry_lastname.get()
    age = entry_age.get()
    balance = entry_balance.get()
    
    if name and lastname and age and balance:
        try:
            database.add_user(name, lastname, int(age), float(balance))
            messagebox.showinfo("Success", "User added successfully")
            entry_name.delete(0, tk.END)
            entry_lastname.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            entry_balance.delete(0, tk.END)
            load_users()  # Update user list
        except Exception as e:
            messagebox.showerror("Error", f"Error adding user: {e}")
    else:
        messagebox.showwarning("Error", "All fields are required")

# Load all users
def load_users():
    rows = database.load_users()  # Call the user loading function in the database module
    
    # Check if the table is empty
    if not rows:  # If there are no rows
        populate_users()  # Call the function to add test data
        rows = database.load_users()  # Reload after adding
        
    # Clear the table
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert rows into the table
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Calculate and display the total number of users and their percentage
    total_users = len(rows)  # Total users in the database
    label_percentage.config(text=f"Total Users: {total_users}, Percentage: 100.00%")  # Update the label

# Filter users by age range
def filter_by_age(min_age, max_age):
    rows = database.filter_users_by_age(min_age, max_age)  # Call the filtering function in the database module
    
    # Clear the table
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert filtered rows into the table
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Calculate and display the total number of filtered users and their percentage
    total_users = database.load_users()  # Load all users
    percentage = (len(rows) / len(total_users) * 100) if total_users else 0
    label_percentage.config(text=f"Total Users: {len(rows)}, Percentage: {percentage:.2f}%")  # Update the label

# Filter users by balance
def filter_by_balance(is_less_than):
    rows = database.filter_users_by_balance(is_less_than)  # Call the filtering function in the database module
    
    # Clear the table
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert filtered rows into the table
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Calculate and display the total number of filtered users and their percentage
    total_users = database.load_users()  # Load all users
    percentage = (len(rows) / len(total_users) * 100) if total_users else 0
    label_percentage.config(text=f"Total Users: {len(rows)}, Percentage: {percentage:.2f}%")  # Update the label

# Clear filters and load all users
def clear_filters():
    load_users()  # Load all users without any filters
    
    
# Main window configuration
root = tk.Tk()
root.title("User Management")
root.geometry("1100x800")

# GUI Elements
label_name = tk.Label(root, text="Name")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_lastname = tk.Label(root, text="Lastname")
label_lastname.grid(row=1, column=0, padx=10, pady=10)

entry_lastname = tk.Entry(root)
entry_lastname.grid(row=1, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age")
label_age.grid(row=2, column=0, padx=10, pady=10)

entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=10)

label_balance = tk.Label(root, text="Balance")
label_balance.grid(row=3, column=0, padx=10, pady=10)

entry_balance = tk.Entry(root)
entry_balance.grid(row=3, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Add User", command=add_user)
button_add.grid(row=4, column=1, padx=10, pady=10)

# Table to display users
columns = ("ID", "Name", "Lastname", "Age", "Balance")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Lastname", text="Lastname")
tree.heading("Age", text="Age")
tree.heading("Balance", text="Balance")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Add a label to display the total number of users and percentage
label_percentage = tk.Label(root, text="Total Users: 0, Percentage: 0%")
label_percentage.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Age filter Button
button_age_18_25 = tk.Button(root, text="Filter Age from 18-25", command=lambda: filter_by_age(18, 25))
button_age_18_25.grid(row=6, column=0, padx=10, pady=10)

button_age_26_35 = tk.Button(root, text="Filter Age from 26-35", command=lambda: filter_by_age(26, 35))
button_age_26_35.grid(row=6, column=1, padx=10, pady=10)

button_age_36_plus = tk.Button(root, text="Filter Age from 36+", command=lambda: filter_by_age(36, 150))
button_age_36_plus.grid(row=7, column=0, padx=10, pady=10)

# Balance filter Button
button_balance_less_10000 = tk.Button(root, text="Filter Bank Balance < 10,000", command=lambda: filter_by_balance(True))
button_balance_less_10000.grid(row=7, column=1, padx=10, pady=10)

button_balance_greater_10000 = tk.Button(root, text="Filter Bank Balance >= 10,000", command=lambda: filter_by_balance(False))
button_balance_greater_10000.grid(row=8, column=0, padx=10, pady=10)

# Clear filters Button
button_clear_filters = tk.Button(root, text="Clear Filters", command=clear_filters)
button_clear_filters.grid(row=8, column=1, padx=10, pady=10)

# Load Users at the app start
load_users()

# Run App
root.mainloop()