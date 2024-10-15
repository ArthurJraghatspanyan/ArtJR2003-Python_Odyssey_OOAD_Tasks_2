# Design a class Employee with private attributes employee_id, name, and salary. Provide methods to set and get these values. Ensure that salary cannot be negative.


class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def getEmployeeID(self):
        return self.__employee_id
    
    def setEmployeeID(self, value):
        if not isinstance(value, int):
            raise TypeError("Type must be int.")
        self.__employee_id = value

    def getName(self):
        return self.__name
    
    def setName(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be str.")
        self.__name = value

    def getSalary(self):
        return self.__salary
    
    def setSalary(self, value):
        if value < 0:
            raise ValueError("Salary can't be negative.")
        self.__salary = value

ob = Employee(1, "Josh", 2000)
print(ob.getSalary())
ob.setSalary(3000)
print(ob.getSalary())
ob.setSalary(-3000)
ob.getSalary()