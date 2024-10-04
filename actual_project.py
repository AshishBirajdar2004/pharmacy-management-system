import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for Treeview
import mysql.connector

# Database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashish@2004",  
    database="pharmeasy"
)

cursor = db_connection.cursor()

# Function to insert a new customer
def insert_customer():
    customer_name = entry_customer_name.get()
    phone_number = entry_phone_number.get()
    address = entry_address.get()
    
    query = "INSERT INTO Customers (customer_name, phone_number, address) VALUES (%s, %s, %s)"
    values = (customer_name, phone_number, address)
    
    cursor.execute(query, values)
    db_connection.commit()
    messagebox.showinfo("Success", "Customer added successfully!")
    clear_entries()

# Function to insert a new medicine
def insert_medicine():
    medicine_name = entry_medicine_name.get()
    manufacturer = entry_manufacturer.get()
    category_id = entry_category_id.get()
    expiry_date = entry_expiry_date.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    
    query = """INSERT INTO Medicines (medicine_name, manufacturer, category_id, expiry_date, quantity, price) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (medicine_name, manufacturer, category_id, expiry_date, quantity, price)

    cursor.execute(query, values)
    db_connection.commit()
    messagebox.showinfo("Success", "Medicine added successfully!")
    clear_entries()

# Function to retrieve all customers
def retrieve_customers():
    # Clear previous data in the customer Treeview
    for row in customer_tree.get_children():
        customer_tree.delete(row)
    
    query = "SELECT * FROM Customers"
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Insert data into the customer Treeview
    for row in results:
        customer_tree.insert("", tk.END, values=row)

# Function to retrieve all medicines
def retrieve_medicines():
    # Clear previous data in the medicine Treeview
    for row in medicine_tree.get_children():
        medicine_tree.delete(row)
    
    query = "SELECT * FROM Medicines"
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Insert data into the medicine Treeview
    for row in results:
        medicine_tree.insert("", tk.END, values=row)

# Function to update customer phone number
def update_customer():
    customer_name = entry_customer_name.get()
    new_address = entry_new_address.get()
    new_phone_number = entry_new_phone_number.get()
    
    query = "UPDATE Customers SET phone_number = %s, address= %s WHERE customer_name = %s"
    values = (new_phone_number,new_address,customer_name)
    
    cursor.execute(query, values)
    db_connection.commit()
    messagebox.showinfo("Success", "Customer phone number updated!")
    clear_entries()

# Function to update medicine price
def update_medicine_price():
    medicine_name = entry_medicine_name.get()
    new_price = entry_new_price.get()
    new_qty = entry_new_qty.get()

    query = "UPDATE Medicines SET price = %s, quantity=%s WHERE medicine_name = %s"
    values = (new_price, new_qty, medicine_name)

    cursor.execute(query, values)
    db_connection.commit()
    messagebox.showinfo("Success", "Medicine details updated!")
    clear_entries()

# Function to delete a customer
def delete_customer():
    customer_name = entry_delete_customer_name.get()
    query = "DELETE FROM Customers WHERE customer_name = %s"
    cursor.execute(query, (customer_name,))
    db_connection.commit()
    messagebox.showinfo("Success", "Customer deleted!")
    clear_entries()

# Function to delete a medicine
def delete_medicine():
    medicine_name = entry_delete_medicine_name.get()
    query = "DELETE FROM Medicines WHERE medicine_name = %s"
    cursor.execute(query, (medicine_name,))
    db_connection.commit()
    messagebox.showinfo("Success", "Medicine deleted!")
    clear_entries()

# Function to find medicines low in stock
def find_low_stock():
    query = "SELECT medicine_name, quantity FROM Medicines WHERE quantity < %s"
    low_stock_threshold = int(entry_low_stock.get())
    cursor.execute(query, (low_stock_threshold,))
    results = cursor.fetchall()
    display_results(results)

# Function to list medicines expiring soon
def find_expiring_medicines():
    query = "SELECT medicine_name, expiry_date FROM Medicines WHERE expiry_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL %s MONTH)"
    months = int(entry_expiry_months.get())
    cursor.execute(query, (months,))
    results = cursor.fetchall()
    display_results(results)

# Function to generate total sales and revenue report
def get_sales_report():
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    query = """SELECT COUNT(sale_id) AS total_sales, SUM(total_price) AS total_revenue
               FROM Sales
               WHERE sale_date BETWEEN %s AND %s"""
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    display_results(results)

# Function to display query results
def display_results(results):
    # Clear existing table rows
    for row in tree.get_children():
        tree.delete(row)
    
    for row in results:
        tree.insert("", tk.END, values=row)

# Function to clear all entry fields
def clear_entries():
    entry_customer_name.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_medicine_name.delete(0, tk.END)
    entry_manufacturer.delete(0, tk.END)
    entry_category_id.delete(0, tk.END)
    entry_expiry_date.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_new_phone_number.delete(0, tk.END)
    entry_new_address.delete(0, tk.END)
    entry_new_price.delete(0, tk.END)
    entry_new_qty.delete(0, tk.END)
    entry_delete_customer_name.delete(0, tk.END)
    entry_delete_medicine_name.delete(0, tk.END)

# Creating the GUI
root = tk.Tk()
root.title("Pharmacy Management System")

# Configuring the root window to expand with the Notebook
root.grid_rowconfigure(0, weight=1)  # Make the first row expandable
root.grid_columnconfigure(0, weight=1)  # Make the first column expandable

# Create a Notebook for tabs
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky='nsew',)  # Use sticky for filling in all directions
style = ttk.Style()
style.configure('TNotebook.Tab', padding=[10, 10], font=('Helvetica', 12), background='yellow')



# Create the first tab for input forms
form_tab = ttk.Frame(notebook)
notebook.add(form_tab, text='EDIT DATA')

# Customer Section
tk.Label(form_tab, text="Customer Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_customer_name = tk.Entry(form_tab)
entry_customer_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_tab, text="Phone Number").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_phone_number = tk.Entry(form_tab)
entry_phone_number.grid(row=1, column=1)

tk.Label(form_tab, text="Address").grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_address = tk.Entry(form_tab)
entry_address.grid(row=2, column=1)

tk.Button(form_tab, text="Add Customer", command=insert_customer).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Medicine Section
tk.Label(form_tab, text="Medicine Name").grid(row=5, column=0, padx=10, pady=5, sticky='w')
entry_medicine_name = tk.Entry(form_tab)
entry_medicine_name.grid(row=5, column=1)

tk.Label(form_tab, text="Manufacturer").grid(row=6, column=0, padx=10, pady=5, sticky='w')
entry_manufacturer = tk.Entry(form_tab)
entry_manufacturer.grid(row=6, column=1)

tk.Label(form_tab, text="Category ID").grid(row=7, column=0, padx=10, pady=5, sticky='w')
entry_category_id = tk.Entry(form_tab)
entry_category_id.grid(row=7, column=1)

tk.Label(form_tab, text="Expiry Date").grid(row=8, column=0, padx=10, pady=5, sticky='w')
entry_expiry_date = tk.Entry(form_tab)
entry_expiry_date.grid(row=8, column=1)

tk.Label(form_tab, text="Quantity").grid(row=9, column=0, padx=10, pady=5, sticky='w')
entry_quantity = tk.Entry(form_tab)
entry_quantity.grid(row=9, column=1)

tk.Label(form_tab, text="Price").grid(row=10, column=0, padx=10, pady=5, sticky='w')
entry_price = tk.Entry(form_tab)
entry_price.grid(row=10, column=1)

tk.Button(form_tab, text="Add Medicine", command=insert_medicine).grid(row=11, column=0, columnspan=2, padx=10, pady=5)

# Update Section
tk.Label(form_tab, text="Customer Name").grid(row=0, column=2, padx=10, pady=5, sticky='w')
entry_customer_name = tk.Entry(form_tab)
entry_customer_name.grid(row=0, column=3)

tk.Label(form_tab, text="New Phone Number").grid(row=1, column=2, padx=10, pady=5, sticky='w')
entry_new_phone_number = tk.Entry(form_tab)
entry_new_phone_number.grid(row=1, column=3)

tk.Label(form_tab, text="New address").grid(row=2, column=2, padx=10, pady=5, sticky='w')
entry_new_address = tk.Entry(form_tab)
entry_new_address.grid(row=2, column=3)

tk.Button(form_tab, text="Update Customer", command=update_customer).grid(row=3, column=2, columnspan=2, padx=10, pady=5)

tk.Label(form_tab, text="Medicine Name").grid(row=5, column=2, padx=10, pady=5, sticky='w')
entry_customer_name = tk.Entry(form_tab)
entry_customer_name.grid(row=5, column=3)

tk.Label(form_tab, text="New Quantity").grid(row=6, column=2, padx=10, pady=5, sticky='w')
entry_new_qty = tk.Entry(form_tab)
entry_new_qty.grid(row=6, column=3)

tk.Label(form_tab, text="New Price").grid(row=7, column=2, padx=10, pady=5, sticky='w')
entry_new_price = tk.Entry(form_tab)
entry_new_price.grid(row=7, column=3)

tk.Button(form_tab, text="Update Medicine", command=update_medicine_price).grid(row=11, column=2, columnspan=2, padx=10, pady=5)

# Delete Section
tk.Label(form_tab, text="Delete Customer Name").grid(row=0, column=4, padx=10, pady=5, sticky='w')
entry_delete_customer_name = tk.Entry(form_tab)
entry_delete_customer_name.grid(row=0, column=5)

tk.Button(form_tab, text="Delete Customer", command=delete_customer).grid(row=3, column=4, columnspan=2, padx=10, pady=5)

tk.Label(form_tab, text="Delete Medicine Name").grid(row=5, column=4, padx=10, pady=5, sticky='w')
entry_delete_medicine_name = tk.Entry(form_tab)
entry_delete_medicine_name.grid(row=5, column=5)

tk.Button(form_tab, text="Delete Medicine", command=delete_medicine).grid(row=11, column=4, columnspan=2, padx=10, pady=5)

separator = tk.Frame(form_tab, height=2, bd=1, relief="sunken", background="black")
separator.grid(row=4, column=0, columnspan=6, sticky="ew", padx=10, pady=50)

# Create a second tab for displaying customers
display_tab = ttk.Frame(notebook)
notebook.add(display_tab, text='DISPLAY DATA')

# Retrieve Customers
tk.Button(display_tab, text="Retrieve Customers", command=retrieve_customers).grid(pady=10,row=0,column=0)

# Treeview for displaying customers
customer_tree = ttk.Treeview(display_tab, columns=("ID", "Name", "Address", "Phone Number"), show='headings')
customer_tree.heading("ID", text="Customer ID")
customer_tree.heading("Name", text="Customer Name")
customer_tree.heading("Phone Number", text="Phone Number")
customer_tree.heading("Address", text="Address")
customer_tree.grid(pady=10, row=1, column=0, sticky='nsew')

# Retrieve Medicines
tk.Button(display_tab, text="Retrieve Medicines", command=retrieve_medicines).grid(row=2, column=0, columnspan=2)

# Treeview for displaying customers
medicine_tree = ttk.Treeview(display_tab, columns=("ID", "Name", "Mfg", "Category","Exp","Qty","price"), show='headings')
medicine_tree.heading("ID", text="Medicine ID")
medicine_tree.heading("Name", text="Medicine Name")
medicine_tree.heading("Mfg", text="Manufacturer")
medicine_tree.heading("Category", text="Category")
medicine_tree.heading("Exp", text="Expiry Date")
medicine_tree.heading("Qty", text="quantity")
medicine_tree.heading("price", text="price")
medicine_tree.grid(pady=10, row=3, column=0, sticky='nsew')

# Set column width
medicine_tree.column("ID", width=80)
medicine_tree.column("Name", width=100)
medicine_tree.column("Mfg", width=150)
medicine_tree.column("Category", width=80)
medicine_tree.column("Exp", width=100)
medicine_tree.column("Qty", width=80)
medicine_tree.column("price", width=80)

########################################################################
info_tab = ttk.Frame(notebook)
notebook.add(info_tab, text='INVENTORY & SALES')

# Tabs using Notebook
sub_notebook = ttk.Notebook(info_tab)
sub_notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Create a tab for each function
low_stock_tab = ttk.Frame(sub_notebook)
expiry_tab = ttk.Frame(sub_notebook)
sales_report_tab = ttk.Frame(sub_notebook)
sub_notebook.add(low_stock_tab, text="Low Stock")
sub_notebook.add(expiry_tab, text="Expiring Medicines")
sub_notebook.add(sales_report_tab, text="Sales Report")

# Low stock tab UI
ttk.Label(low_stock_tab, text="Enter Low Stock Threshold:").grid(row=0, column=0, padx=10, pady=10)
entry_low_stock = ttk.Entry(low_stock_tab)
entry_low_stock.grid(row=0, column=1, padx=10, pady=10)
ttk.Button(low_stock_tab, text="Find Low Stock", command=find_low_stock).grid(row=0, column=2, padx=10, pady=10)

# Expiring medicines tab UI
ttk.Label(expiry_tab, text="Enter Months to Check Expiry:").grid(row=0, column=0, padx=10, pady=10)
entry_expiry_months = ttk.Entry(expiry_tab)
entry_expiry_months.grid(row=0, column=1, padx=10, pady=10)
ttk.Button(expiry_tab, text="Find Expiring Medicines", command=find_expiring_medicines).grid(row=0, column=2, padx=10, pady=10)

# Sales report tab UI
ttk.Label(sales_report_tab, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
entry_start_date = ttk.Entry(sales_report_tab)
entry_start_date.grid(row=0, column=1, padx=10, pady=10)
ttk.Label(sales_report_tab, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
entry_end_date = ttk.Entry(sales_report_tab)
entry_end_date.grid(row=1, column=1, padx=10, pady=10)
ttk.Button(sales_report_tab, text="Get Sales Report", command=get_sales_report).grid(row=2, column=1, padx=10, pady=10)

# Treeview to display results
tree = ttk.Treeview(info_tab, columns=("col1", "col2", "col3", "col4"), show="headings")
tree.heading("col1", text="Column 1")
tree.heading("col2", text="Column 2")
tree.heading("col3", text="Column 3")
tree.heading("col4", text="Column 4")
tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Start the GUI loop
root.mainloop()

# Close the database connection when done
cursor.close()
db_connection.close()
