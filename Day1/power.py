def power(a,n): 
    if n==0: 
        return 1 
    return a*power(a,n-1) 
a=int(input("enter a num")) 
n=int(input("enter another num")) 
ans=power(a,n) 
print(f"{a}^{n}:{ans}") 