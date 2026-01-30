def add(a,b): 
    return a+b
def sub(a,b): 
    return a-b 
def mul(a,b): 
    return a*b 
def div(a,b): 
    return a/b 
def calc(a,b): 
    print("select any optiion:1.Add\n2.Sub\n3.Multiply\n4.Divide\n") 
    op=int(input("select any number from 1-4")) 
    if(op==1): 
        print(add(a,b)) 
    if(op==2): 
        print(sub(a,b)) 
        print(mul(a,b)) 
    if(op==4): 
        print(div(a,b)) 

a=int(input("enter a num:"))
b=int(input("enter another num:"))
calc(a,b)