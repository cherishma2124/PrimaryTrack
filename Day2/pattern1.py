def patt(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")
n=int(input("enter a num:"))
patt(n)