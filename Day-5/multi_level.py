class A:
    def display(self):
        print("Hello")

class B:
    def display(self):
        print("Display from class B")

class C(A, B):
    def display(self):
        super(A,self).display()

c = C()
c.display()

