def patt(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or i==j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
n=int(input("enter a num:"))
patt(n)