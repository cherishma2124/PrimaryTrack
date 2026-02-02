import bill_functions

name=input("Enter Name:")
phnum=input("Enter Phone Number:")
city=input("Enter City:")
restaurant=input("Enter Restaurant:")

bill1=int(input("Enter bill 1:"))
bill2=int(input("Enter bill 2:"))
bill3=int(input("Enter bill 3:"))

maskedphnum=phnum[:2]+"******"+phnum[-2:]
totalbill=bill_functions.add(bill1,bill2,bill3)


print("\n")
list=bill_functions.display(Name=name.title().strip(), PhoneNumber=maskedphnum, City=city.title().strip(), Restaurant=restaurant.title().strip(), TotalBill=totalbill)

for i in list:
    print(i)