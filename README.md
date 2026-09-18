# Student Management System

A simple console-based Student Management System built using **Python and MySQL**.

## Features

* Add student
* Display all students
* Search student by ID
* Update student details
* Delete student
* Exit the application

## Technologies Used

* Python
* MySQL
* MySQL Connector/Python

## Database

Database name:

`student_db`

Table name:

`students`

The `students` table contains:

* `student_id`
* `name`
* `age`
* `course`

## How It Works

The Python program connects to the MySQL database using `mysql.connector`.

Users interact with the application through a menu:

1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

The application uses SQL `INSERT`, `SELECT`, `UPDATE`, and `DELETE` operations to manage student records.

## How to Run

1. Install Python.
2. Install MySQL.
3. Create the `student_db` database and `students` table.
4. Install the MySQL Connector package:

```bash
pip install mysql-connector-python
```

5. Update the MySQL password in `student_management_system.py`.
6. Run the program:

```bash
py student_management_system.py
```

## Project Purpose

This project was created to practice **Python, SQL, database connectivity, CRUD operations, and basic project development**.
