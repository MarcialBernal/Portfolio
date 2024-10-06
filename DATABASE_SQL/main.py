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

    # Update user count
    update_user_count(len(rows))

# Filter users by age and balance
def filter_users():
    # Get the age filter values
    min_age = int(entry_min_age.get()) if entry_min_age.get() else 0
    max_age = int(entry_max_age.get()) if entry_max_age.get() else 150

    # Get the balance filter values
    min_balance = float(entry_min_balance.get()) if entry_min_balance.get() else 0.0
    max_balance = float(entry_max_balance.get()) if entry_max_balance.get() else float('inf')

    # Get the users based on the filters
    rows = database.filter_users_by_age(min_age, max_age)
    rows = [row for row in rows if min_balance <= row[4] <= max_balance]

    # Clear the table
    for row in tree.get_children():
        tree.delete(row)

    # Insert filtered rows into the table
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Update user count
    update_user_count(len(rows))

# Clear filters and show all users
def clear_filters():
    entry_min_age.delete(0, tk.END)
    entry_max_age.delete(0, tk.END)
    entry_min_balance.delete(0, tk.END)
    entry_max_balance.delete(0, tk.END)
    load_users()  # Load all users again

# Update user count label
def update_user_count(count):
    label_user_count.config(text=f"Total Users: {count}")

# Main window configuration
root = tk.Tk()
root.title("User Management")
root.geometry("1100x800")

# GUI Elements for adding users
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

# GUI Elements for filtering
label_min_age = tk.Label(root, text="Min Age")
label_min_age.grid(row=6, column=0, padx=10, pady=10)

entry_min_age = tk.Entry(root)
entry_min_age.grid(row=6, column=1, padx=10, pady=10)

label_max_age = tk.Label(root, text="Max Age")
label_max_age.grid(row=7, column=0, padx=10, pady=10)

entry_max_age = tk.Entry(root)
entry_max_age.grid(row=7, column=1, padx=10, pady=10)

# GUI Elements for balance filtering
label_min_balance = tk.Label(root, text="Min Balance")
label_min_balance.grid(row=8, column=0, padx=10, pady=10)

entry_min_balance = tk.Entry(root)
entry_min_balance.grid(row=8, column=1, padx=10, pady=10)

label_max_balance = tk.Label(root, text="Max Balance")
label_max_balance.grid(row=9, column=0, padx=10, pady=10)

entry_max_balance = tk.Entry(root)
entry_max_balance.grid(row=9, column=1, padx=10, pady=10)

# Filter button
button_filter = tk.Button(root, text="Apply Filters", command=filter_users, bg="lightblue", width=15)
button_filter.grid(row=10, column=0, padx=10, pady=10)

# Clear filters button
button_clear_filters = tk.Button(root, text="Clear Filters", command=clear_filters, bg="lightgreen", width=15)
button_clear_filters.grid(row=10, column=1, padx=10, pady=10)

# Label to display total users
label_user_count = tk.Label(root, text="Total Users: 0")
label_user_count.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

# Load Users at the app start
load_users()

# Run App
root.mainloop()