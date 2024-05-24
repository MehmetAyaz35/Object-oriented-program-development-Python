# define a class
class Employee:            # In Python 2, the use of parentheses was required when defining a class, but it is not necessary in Python 3. Both syntaxes are valid in Python 3. class Employee: or class Employee():
    # define an attribute
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")