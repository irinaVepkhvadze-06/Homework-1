class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary,)
        self.department = department

    @property
    def salary(self):
        return self._Employee__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._Employee__salary = value
        else: raise ValueError("Salary must be positive number")

    @salary.deleter
    def salary(self):
        print("Salary record deleted")

    def get_info(self):
        print(f"Name: {self.name}, Department: {self.department}, Salary: {self.salary} ")


Employee1 = Manager("John", 3000, "It")
print(Employee1.salary)

Employee1.get_info()
