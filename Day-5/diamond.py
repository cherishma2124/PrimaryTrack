class A():
    def d1(self):
        return "Im from A"
class B(A):
    def d2(self):
        return "Im from B"
class C(A):
    def d3(self):
        return "Im from C"
class D(B,C):
    def d4(self):
       return "Im from D"
dd = D()
print(dd.d1())
print(dd.d2())
print(dd.d3())
print(dd.d4())