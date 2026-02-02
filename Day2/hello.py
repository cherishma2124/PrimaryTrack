text = "User ID:12345"
id = text.split(":")[1]
print(id)


name = "Yerramada Cherishma"
parts = name.split()
initials = parts[0][0] + parts[1][0]
print(initials.upper())


name="   abc  "
print(name.strip())

msg="the trip was amazing "
print(len(msg.split()))

marks,attendance=89,90
if(marks>=50 and attendance>=75):
   print("Eligible for writing exam")
else:
   print("Not eligible")


recharge,gb=200,5
if recharge>250 and gb==5:
    print("Bonus ")
else:
    print("No bonus")


bill=2000
day="sunday"
member="Gold"
if bill>1000 and (day=="saturday" or day=="sunday") and member=="gold":
    bill=bill*0.8
    print(bill)
else:
    print(bill)

password="abc"
for i in range(3):
    pwd=input("Enter password:")
    if pwd != password:
        print(f"Login failed")
    else:
        print("login successfull")
        break
print("Thankyou")


l = []
while True:
    a = input("Enter item: ")
    if a == "done":
        break
    else:
        l.append(a)
print(l)



def greet(name):
    print(f"Hi {name} ! Good morning")
greet("cherry")

def add_all(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(add_all(1,2,3,3))


def printdata(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
printdata(name="cherry",age=89)

#profile generator
def profile(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += f"{key} : {value}\n"
    return result

name = input("Enter name: ")
age = input("Enter Age: ")
phoneno = input("Enter phonenumber: ")
print(profile(Name=name, Age=age, PH=phoneno))