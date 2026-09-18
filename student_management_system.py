import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="student_db"
)

cursor = connection.cursor()


# Add student
def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    query = """
    INSERT INTO students (student_id, name, age, course)
    VALUES (%s, %s, %s, %s)
    """

    values = (student_id, name, age, course)

    cursor.execute(query, values)
    connection.commit()

    print("Student added successfully!")


# Display students
def display_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        print("\nID | Name | Age | Course")
        print("-" * 30)

        for student in students:
            print(student)


# Search student
def search_student():
    student_id = int(input("Enter Student ID to search: "))

    query = "SELECT * FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:
        print("Student found:", student)
    else:
        print("Student not found.")


# Update student
def update_student():
    student_id = int(input("Enter Student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    query = """
    UPDATE students
    SET name = %s, age = %s, course = %s
    WHERE student_id = %s
    """

    values = (name, age, course, student_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")


# Delete student
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    query = "DELETE FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

cursor.close()
connection.close()