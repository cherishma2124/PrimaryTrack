a=input("enter gmail") 
b=input("enter password") 
ans="valid" 
if "@" not in a: 
    ans="Invalid" 
if len(b)<8: 
    ans="Invalid" 
print(ans) 

 