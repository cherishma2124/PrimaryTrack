class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def display(self):
        print(f"Hello, I am {self.name} and my age is {self.age}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
s1 = Student(name,age)
s1.display()