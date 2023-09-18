# Group 18 case9 Python code
import mysql.connector
 
# Connect to the MySQL database
db = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="das"
)
 
# Create a cursor object to execute SQL queries
cursor = db.cursor()
 
# Function to enter employee data into the Employees table
def enter_employee_data():
   id = input("Enter employee id: ")
   name = input("Enter employee name: ")
   role = input("Enter employee role: ")
 
   # SQL query to insert data into Employees table
   sql = "INSERT INTO Employees (employee_id, employee_name, employee_role) VALUES (%s, %s, %s)"
   values = (id, name, role)
 
   # Execute the query
   cursor.execute(sql, values)
   db.commit()
 
   print("Employee data entered successfully!")
 
# Function to generate a list of all employees and their roles
def generate_employee_list():
   # SQL query to select all employees
   sql = "SELECT employee_id, employee_name, employee_role FROM Employees"
 
   # Execute the query
   cursor.execute(sql)
 
   # Fetch all the records
   employees = cursor.fetchall()
 
   print("Employee List:")
   for employee in employees:
       print(f"ID: {employee[0]}, Name: {employee[1]}, Role: {employee[2]}")
 
# Function to generate a count of employees per role
def generate_employee_count_per_role():
   # SQL query to count employees per role
   sql = "SELECT employee_role, COUNT(*) FROM Employees GROUP BY employee_role"
 
   # Execute the query
   cursor.execute(sql)
 
   # Fetch all the records
   counts = cursor.fetchall()
 
   print("Employee Count per Role:")
   for count in counts:
       print(f"Role: {count[0]}, Count: {count[1]}")
 
# Function to enter asset data into the Assets table
def enter_asset_data():
   id = input("Enter asset id: ")
   name = input("Enter asset name: ")
   asset_type = input("Enter asset type: ")
   location_id = input("Enter location id: ")
 
   # SQL query to insert data into Assets table
   sql = "INSERT INTO assets (asset_id, asset_name, asset_type, location_id) VALUES (%s, %s, %s, %s)"
   values = (id, name, asset_type, location_id)
 
   # Execute the query
   cursor.execute(sql, values)
   db.commit()
 
   print("Asset data entered successfully!")
 
# Function to generate a list of all assets
def generate_assets_list():
   # SQL query to select all assets
   sql = "SELECT asset_id, asset_name, asset_type, location_id FROM assets"
 
   # Execute the query
   cursor.execute(sql)
 
   # Fetch all the records
   assets = cursor.fetchall()
 
   print("Asset List:")
   for asset in assets:
       print(f"ID: {asset[0]}, Name: {asset[1]}, Type: {asset[2]}, Location ID: {asset[3]}")
 
# Function to generate a count of assets per location
def generate_asset_count_per_location():
   # SQL query to count assets per location
   sql = "SELECT location_id, COUNT(*) FROM assets GROUP BY location_id"
 
   # Execute the query
   cursor.execute(sql)
 
   # Fetch all the records
   counts = cursor.fetchall()
 
   print("Asset Count per Location:")
   for count in counts:
       print(f"Location ID: {count[0]}, Count: {count[1]}")
 
# Main program loop
while True:
   print("\n--- Employee and Asset Management System ---")
   print("1. Enter Employee Data")
   print("2. Generate Employee List")
   print("3. Generate Employee Count per Role")
   print("4. Enter Asset Data")
   print("5. Generate Asset List")
   print("6. Generate Asset Count per Location")
   print("7. Exit")
 
   choice = input("Enter your choice (1-7): ")
 
   if choice == "1":
       enter_employee_data()
   elif choice == "2":
       generate_employee_list()
   elif choice == "3":
       generate_employee_count_per_role()
   elif choice == "4":
       enter_asset_data()
   elif choice == "5":
       generate_assets_list()
   elif choice == "6":
       generate_asset_count_per_location()
   elif choice == "7":
       break
   else:
       print("Invalid choice. Please try again.")
 
# Close the database connection
cursor.close()
db.close()