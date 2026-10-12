# Employee Management System using Python OOP

## 📌 Project Overview

The **Employee Management System** is a Python-based application developed to demonstrate fundamental **Object-Oriented Programming (OOP)** concepts.

The system creates and manages employee records containing information such as:

- Employee ID
- Name
- Department
- Salary
- Designation

The application allows users to display employee information, update employee salaries, and calculate annual salaries.

This project demonstrates how real-world entities such as employees can be represented using **classes and objects in Python**.

---

## 🎯 Objectives

The main objectives of this project are:

- Understand classes and objects in Python
- Understand the `__init__()` constructor
- Work with instance attributes
- Create and use instance methods
- Create multiple objects from the same class
- Update object attributes using methods
- Perform calculations using object data
- Organize Python code using packages and modules
- Implement exception handling
- Implement basic logging

---

## 🧠 OOP Concepts Used

### 1. Class

A class acts as a blueprint for creating objects.

In this project, the `Employee` class represents an employee.

```python
class Employee:
    pass
```

---

### 2. Object

An object is an instance of a class.

Five employee objects are created in this project.

```python
employee1 = Employee(
    101,
    "Arjun",
    "IT",
    75000,
    "Software Engineer"
)
```

Each object contains its own employee information.

---

### 3. Constructor

The `__init__()` method is a constructor that is automatically executed when an Employee object is created.

```python
def __init__(self, employee_id, name, department, salary, designation):
    self.employee_id = employee_id
    self.name = name
    self.department = department
    self.salary = salary
    self.designation = designation
```

---

### 4. Instance Attributes

Every employee object contains its own attributes:

- `employee_id`
- `name`
- `department`
- `salary`
- `designation`

For example:

```python
self.name = name
self.salary = salary
```

---

### 5. Instance Methods

The Employee class contains methods that perform operations on employee objects.

#### Display Employee Information

```python
display_employee()
```

Displays complete employee details.

#### Update Salary

```python
update_salary(new_salary)
```

Updates the employee's monthly salary.

#### Calculate Annual Salary

```python
calculate_annual_salary()
```

Calculates annual salary using:

```text
Annual Salary = Monthly Salary × 12
```

---

## 📁 Project Structure

```text
employee_management_system/
│
├── employee_management/
│   ├── __init__.py
│   ├── employee.py
│   └── exceptions.py
│
├── logs/
│   └── employee.log
│
├── main.py
├── README.md
└── .gitignore
```

### File Description

**`employee.py`**

Contains the `Employee` class and methods for managing employee information.

**`exceptions.py`**

Contains custom exceptions such as `InvalidSalaryError`.

**`__init__.py`**

Marks `employee_management` as a Python package and exposes the required classes.

**`main.py`**

Acts as the entry point of the application. It creates employee objects and demonstrates the functionality of the system.

**`logs/employee.log`**

Stores application activity such as employee creation, salary updates, and errors.

---

## ✨ Features

The Employee Management System supports the following functionality:

- Create employee objects
- Store employee details
- Display employee information
- Update employee salary
- Calculate annual salary
- Validate salary values
- Handle invalid salary errors
- Log important application activities
- Manage multiple employees

---

## 👥 Sample Employees

The application creates at least five employee objects.

| Employee ID | Name | Department | Designation | Monthly Salary |
|---|---|---|---|---:|
| 101 | Arjun | IT | Software Engineer | ₹75,000 |
| 102 | Meera | HR | HR Manager | ₹60,000 |
| 103 | Rahul | Finance | Financial Analyst | ₹70,000 |
| 104 | Priya | Marketing | Marketing Manager | ₹65,000 |
| 105 | Vikram | IT | Technical Lead | ₹90,000 |

---

## ⚙️ How the Program Works

The basic program flow is:

```text
Start
  ↓
Import Employee Class
  ↓
Create Employee Objects
  ↓
Store Objects in Employee List
  ↓
Display Employee Details
  ↓
Calculate Annual Salaries
  ↓
Update Employee Salary
  ↓
Display Updated Information
  ↓
Handle Errors
  ↓
Write Activities to Log File
  ↓
End
```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project

```bash
cd employee_management_system
```

### Step 3: Check Python Installation

```bash
python --version
```

### Step 4: Run the Application

```bash
python main.py
```

---

## 💻 Sample Output

```text
===== EMPLOYEE MANAGEMENT SYSTEM =====

Employee ID : 101
Name        : Arjun
Department  : IT
Designation : Software Engineer
Salary      : ₹75000

Employee ID : 102
Name        : Meera
Department  : HR
Designation : HR Manager
Salary      : ₹60000

===== ANNUAL SALARIES =====

Arjun - Annual Salary: ₹900000
Meera - Annual Salary: ₹720000
Rahul - Annual Salary: ₹840000
Priya - Annual Salary: ₹780000
Vikram - Annual Salary: ₹1080000

===== SALARY UPDATE =====

Salary updated successfully for Arjun.

Updated Monthly Salary: ₹80000
Updated Annual Salary: ₹960000
```

---

## ⚠️ Exception Handling

The project contains a custom exception called:

```python
class InvalidSalaryError(Exception):
    pass
```

It prevents invalid salary values from being accepted.

For example:

```python
if new_salary <= 0:
    raise InvalidSalaryError(
        "New salary must be greater than zero."
    )
```

This prevents salaries such as:

```text
₹0
-₹10,000
```

from being accepted.

---

## 📝 Logging

Python's `logging` module is used to record important application activities.

Examples include:

- Employee creation
- Salary updates
- Invalid salary attempts
- Application errors

Logs are stored inside:

```text
logs/employee.log
```

Example:

```text
Employee created: 101 - Arjun
Salary updated for 101: 75000 -> 80000
```

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming
- Python Packages and Modules
- Exception Handling
- Python Logging
- Git
- GitHub
- Visual Studio Code

---

## 📚 Learning Outcomes

After completing this project, you should understand:

- How to create Python classes
- How to create multiple objects
- How constructors work
- How `self` refers to the current object
- How instance attributes store object-specific information
- How instance methods operate on object data
- How object attributes can be updated
- How calculations can be performed using object attributes
- How packages and modules organize Python projects
- How custom exceptions improve error handling
- How logging can track application activities
- How to push a Python project to GitHub

---

## 🔮 Future Enhancements

The project can be extended with features such as:

- Add new employees dynamically
- Delete employees
- Search employees by employee ID
- Update employee department or designation
- Calculate bonuses
- Store employee information in a file
- Connect the application to a database
- Build a menu-driven CLI
- Create a GUI or web interface

---

## 👩‍💻 Author

**Amrutha Varshini Alva**

Created as part of a Python OOP learning project.

---

## 📄 License

This project is created for educational and learning purposes.
