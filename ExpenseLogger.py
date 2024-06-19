import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

# Dictionary to store expenses categorized by type
expense_records = {}

def log_expense():
    """Logs an expense entry with date, category, and amount."""
    date = date_entry.get()
    category = category_combobox.get()
    amount = amount_entry.get()

    # Check if category and amount are provided
    if not category or not amount:
        messagebox.showwarning("Input Error", "Please enter both category and amount.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid amount.")
        return

    if category not in expense_records:
        expense_records[category] = []

    expense_records[category].append((date, amount))

    # Reset input fields after logging the expense
    category_combobox.set('')
    amount_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Expense logged successfully!")

def print_expenses():
    """Prints all logged expenses to the console."""
    for category, expenses_list in expense_records.items():
        print(f"Category: {category}")
        for expense in expenses_list:
            print(f"    Date: {expense[0]}, Amount: {expense[1]}")
    print("\n")

def clear_expenses():
    """Clears all the logged expenses."""
    global expense_records
    expense_records = {}
    messagebox.showinfo("Success", "All expenses cleared!")

# Setting up the main application window
app = tk.Tk()
app.title("Expense Tracker")

# Date input
ttk.Label(app, text="Date:").grid(row=0, column=0, padx=10, pady=10)
date_entry = DateEntry(app, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=10, pady=10)

# Category input
ttk.Label(app, text="Category:").grid(row=1, column=0, padx=10, pady=10)
categories = ["Rent", "Food/Supermarket", "Food/Restaurant", "Holidays", "Leisure/Entertainment", "Gas", "Purchases", "Investments"]
category_combobox = ttk.Combobox(app, values=categories, state="readonly")
category_combobox.grid(row=1, column=1, padx=10, pady=10)

# Expense amount input
ttk.Label(app, text="Amount: (€)").grid(row=2, column=0, padx=10, pady=10)
amount_entry = ttk.Entry(app, width=20)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons for logging, printing, and clearing expenses
log_button = ttk.Button(app, text="Log Expense", command=log_expense)
log_button.grid(row=3, column=0, columnspan=2, pady=10)

print_button = ttk.Button(app, text="Print Expenses", command=print_expenses)
print_button.grid(row=4, column=0, columnspan=2, pady=10)

clear_button = ttk.Button(app, text="Clear Expenses", command=clear_expenses)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
app.mainloop()