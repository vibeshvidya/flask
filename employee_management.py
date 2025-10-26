import mysql.connector

# ✅ Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V0daf!ne",
    database="employee_db"
)

cursor = conn.cursor()

# ✅ Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
)
""")

# ✅ Function to insert new employee
def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    sql = "INSERT INTO employees (name, age, department, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, age, department, salary))
    conn.commit()
    print("✅ Employee added successfully.\n")

# ✅ Function to display all employees
def show_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    if not rows:
        print("No employee records found.\n")
        return
    print("\nEmployee Records:")
    print("-" * 70)
    print("{:<8} {:<20} {:<8} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 70)
    for row in rows:
        print("{:<8} {:<20} {:<8} {:<15} {:<10}".format(row[0], row[1], row[2], row[3], row[4]))
    print()

# ✅ Function to update employee details
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    print("What do you want to update?")
    print("1. Name\n2. Age\n3. Department\n4. Salary")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        new_name = input("Enter new name: ")
        cursor.execute("UPDATE employees SET name = %s WHERE emp_id = %s", (new_name, emp_id))
    elif choice == 2:
        new_age = int(input("Enter new age: "))
        cursor.execute("UPDATE employees SET age = %s WHERE emp_id = %s", (new_age, emp_id))
    elif choice == 3:
        new_dept = input("Enter new department: ")
        cursor.execute("UPDATE employees SET department = %s WHERE emp_id = %s", (new_dept, emp_id))
    elif choice == 4:
        new_salary = float(input("Enter new salary: "))
        cursor.execute("UPDATE employees SET salary = %s WHERE emp_id = %s", (new_salary, emp_id))
    else:
        print("❌ Invalid choice.\n")
        return

    conn.commit()
    print("✅ Employee details updated successfully.\n")

# ✅ Function to delete employee record
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("❌ No employee found with that ID.\n")
    else:
        print("✅ Employee deleted successfully.\n")

# ✅ Main Menu
while True:
    print("=== Employee Management System ===")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        show_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice, please try again.\n")

# ✅ Close connection
cursor.close()
conn.close()
