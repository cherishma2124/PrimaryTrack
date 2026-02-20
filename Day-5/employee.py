class Employee : 
    def __init__(self,name,age,dept,empId,salary,exp) :
        self.name = name
        self.age = age
        self.dept = dept
        self.empId = empId
        self.salary = salary
        self.exp = exp
    def display(self): 
        print("Employee Details : ")
        print(f"Employee Name : {self.name}")
        print(f"Employee Age : {self.age}")
        print(f"Employee Departement : {self.dept}")
        print(f"Employee ID : {self.empId}")
        print(f"Employee Salary : {self.salary}")
        print(f"Employee Experience : {self.exp}")

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
dept = input("Enter Your Department: ")
empId = int(input("Enter Your Employee ID: "))
salary = int(input("Enter Your Salary: "))
exp = int(input("Enter Your Experience: "))

e1 = Employee(name, age, dept, empId, salary, exp)

e1.display()
