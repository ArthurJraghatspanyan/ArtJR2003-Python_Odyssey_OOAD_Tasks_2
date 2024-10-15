# Create a class Student with private attributes name, roll_number, and grades. Implement methods to add grades, calculate the average grade, and display the student’s information. Ensure that the grades are between 0 and 100.

class Student:
    def __init__(self, name, roll_number, grades):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []
        self.__grades.append(grades)

    def getName(self):
        return self.__name
    
    def setName(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be str.")
        self.__name = value

    def getRollNumber(self):
        return self.__roll_number
    
    def setRollNumber(self, value):
        if not isinstance(value, int):
            raise TypeError("Type must be int.")
        self.__roll_number = value

    def getGrades(self):
        return self.__grades
    
    def setGrades(self, value):
        if not 0 < value < 100:
            raise ValueError("Grades must be between 0 and 100.")
        self.__grades.append(value)

    def avg_grade(self):
        summary = 0
        for i in self.__grades:
            summary += i
        return summary // len(self.__grades)
    
    def student_info(self):
        print(f"Student's name is {self.getName()}, roll number is {self.getRollNumber()} and average grade is {self.avg_grade()}")

student = Student("Jane", 1, 95)
student.setGrades(94)
student.setGrades(90)
student.setGrades(98)

student.student_info()

student2 = Student("Bob", 2, 85)
student2.setGrades(97)
student2.setGrades(90)
student2.setGrades(87)

student2.student_info()