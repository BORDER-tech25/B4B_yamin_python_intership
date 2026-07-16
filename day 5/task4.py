class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary updated successfully.")
        else:
            print("Salary cannot be decreased.")


emp = Employee(30000)

print("Current Salary:", emp.get_salary())

emp.set_salary(35000)
print("Updated Salary:", emp.get_salary())

emp.set_salary(25000)
print("Final Salary:", emp.get_salary())