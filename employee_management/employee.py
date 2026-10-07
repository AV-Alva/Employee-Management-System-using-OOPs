import logging
from .exceptions import InvalidSalaryError


logging.basicConfig(
    filename="logs/employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Employee:
    """Represents an employee in the organization."""

    def __init__(
        self,
        employee_id,
        name,
        department,
        salary,
        designation
    ):
        if salary <= 0:
            raise InvalidSalaryError("Salary must be greater than zero.")

        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

        logging.info(
            f"Employee created: {self.employee_id} - {self.name}"
        )

    def display_employee(self):
        """Display employee information."""

        print("\n-----------------------------")
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Designation :", self.designation)
        print("Salary      : ₹", self.salary)
        print("-----------------------------")

    def update_salary(self, new_salary):
        """Update the employee's monthly salary."""

        if new_salary <= 0:
            logging.error(
                f"Invalid salary update attempted for {self.employee_id}"
            )
            raise InvalidSalaryError(
                "New salary must be greater than zero."
            )

        old_salary = self.salary
        self.salary = new_salary

        logging.info(
            f"Salary updated for {self.employee_id}: "
            f"{old_salary} -> {new_salary}"
        )

        print(
            f"Salary updated successfully for {self.name}."
        )

    def calculate_annual_salary(self):
        """Calculate and return annual salary."""

        return self.salary * 12