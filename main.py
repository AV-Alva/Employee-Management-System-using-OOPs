from employee_management import Employee, InvalidSalaryError


def main():

    try:
        # Creating 5 Employee objects

        employee1 = Employee(
            101,
            "Arjun",
            "IT",
            75000,
            "Software Engineer"
        )

        employee2 = Employee(
            102,
            "Meera",
            "HR",
            60000,
            "HR Manager"
        )

        employee3 = Employee(
            103,
            "Rahul",
            "Finance",
            70000,
            "Financial Analyst"
        )

        employee4 = Employee(
            104,
            "Priya",
            "Marketing",
            65000,
            "Marketing Manager"
        )

        employee5 = Employee(
            105,
            "Vikram",
            "IT",
            90000,
            "Technical Lead"
        )

        employees = [
            employee1,
            employee2,
            employee3,
            employee4,
            employee5
        ]

        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")

        # Display all employees
        for employee in employees:
            employee.display_employee()

        # Calculate annual salaries
        print("\n===== ANNUAL SALARIES =====")

        for employee in employees:
            annual_salary = employee.calculate_annual_salary()

            print(
                employee.name,
                "- Annual Salary: ₹",
                annual_salary
            )

        # Update salary
        print("\n===== SALARY UPDATE =====")

        employee1.update_salary(80000)

        employee1.display_employee()

        print(
            "Updated Annual Salary: ₹",
            employee1.calculate_annual_salary()
        )

    except InvalidSalaryError as error:
        print("Salary Error:", error)

    except Exception as error:
        print("Unexpected Error:", error)


if __name__ == "__main__":
    main()