# Base class
class Employee:
    def get_salary(self):
        pass


# Subclass for full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def get_salary(self):
        return f"Full-Time Employee Salary: UGX{self.monthly_salary}"


# Subclass for part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def get_salary(self):
        total = self.hours_worked * self.rate_per_hour
        return f"Part-Time Employee Salary: UGX{total}"


# Subclass for interns
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def get_salary(self):
        return f"Intern Salary (Stipend): UGX{self.stipend}"


# Create a list of employees (demonstrating polymorphism)
employees = [FullTimeEmployee(2000), PartTimeEmployee(80, 10), Intern(500)]

# Loop through and print each employee's salary using one method call
for emp in employees:
    print(emp.get_salary())
