import ext_file
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("MENU \n 1.add\n 2.subtraction \n 3.multiplication \n 4.division")
op=int(input("Enter operation to be performed:"))
if op==1:
    print(ext_file.add(a,b))
elif op==2:
    print(ext_file.sub(a,b))
elif op==3:
    print(ext_file.mul(a,b))
elif op==4 :
    print(ext_file.div(a,b))
else:
    print("Invalid ")