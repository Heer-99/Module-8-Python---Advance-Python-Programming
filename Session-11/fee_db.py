
# ==========================================
# Task 1: Tuition Fee Database
# ==========================================

import pymysql
from getpass import getpass


# Enter MySQL Password
password = getpass("Enter MySQL Password: ")


# Connect to MySQL Server
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=password
)

# Create Cursor
cursor = connection.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS tuition_fee_db")

# Close First Connection
cursor.close()
connection.close()


# Connect to Tuition Fee Database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=password,
    database="tuition_fee_db"
)

# Create Cursor
cursor = connection.cursor()

# Create Students Table
query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    class_name VARCHAR(50),
    monthly_fee DECIMAL(10,2)
)
"""

cursor.execute(query)

# Display Message
print("Table ready")


# ==========================================
# Task 2: Add Student
# ==========================================

# Function to Add Student
def add_student(name, class_name, monthly_fee):

    query = """
    INSERT INTO students (name, class_name, monthly_fee)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, class_name, monthly_fee))

    connection.commit()

    print("Student added successfully!")


# ==========================================
# Task 3: View and Search Students
# ==========================================

# Function to Display Students
def display_students(rows):

    print("\n{:<5} {:<15} {:<15} {:<15}".format(
        "ID", "Name", "Class", "Monthly Fee"
    ))

    print("-" * 50)

    for row in rows:

        print("{:<5} {:<15} {:<15} ₹{:<14}".format(
            row[0], row[1], row[2], row[3]
        ))


# Function to View All Students
def view_students():

    query = "SELECT * FROM students"

    cursor.execute(query)

    rows = cursor.fetchall()

    if rows:
        display_students(rows)
    else:
        print("No students found")


# Function to Search Students by Class
def search_by_class(class_name):

    query = "SELECT * FROM students WHERE class_name = %s"

    cursor.execute(query, (class_name,))

    rows = cursor.fetchall()

    if rows:
        display_students(rows)
    else:
        print("No students found")


# ==========================================
# Task 4: Update Fee
# ==========================================

# Function to Update Student Fee
def update_fee(student_id, monthly_fee):

    query = """
    UPDATE students
    SET monthly_fee = %s
    WHERE id = %s
    """

    cursor.execute(query, (monthly_fee, student_id))

    if cursor.rowcount == 0:
        print("No such student")
    else:
        connection.commit()
        print("Student fee updated successfully!")


# Function to Delete Student
def delete_student(student_id):

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    if cursor.rowcount == 0:
        print("No such student")
    else:
        connection.commit()
        print("Student deleted successfully!")


# ==========================================
# Menu Loop
# ==========================================

while True:

    print("\n===== Tuition Fee Menu =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search by class")
    print("4. Update fee")
    print("5. Delete student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        class_name = input("Enter class name: ")
        monthly_fee = float(input("Enter monthly fee: "))

        add_student(name, class_name, monthly_fee)

    elif choice == "2":

        view_students()

    elif choice == "3":

        class_name = input("Enter class name to search: ")

        search_by_class(class_name)

    elif choice == "4":

        student_id = int(input("Enter student ID: "))
        monthly_fee = float(input("Enter new monthly fee: "))

        update_fee(student_id, monthly_fee)

    elif choice == "5":

        student_id = int(input("Enter student ID: "))

        delete_student(student_id)

    elif choice == "0":

        print("Exiting program...")
        break

    else:

        print("Invalid choice! Please try again.")


# Close Connection
cursor.close()
connection.close()
