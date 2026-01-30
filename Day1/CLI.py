import sys 
print("Prog name:",sys.argv[0]) 
if len(sys.argv)>2: 
    for i in range(1,len(sys.argv)): 
        print(f"arg{i}:",sys.argv[i]) 

 