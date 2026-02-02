file=open("notes.txt","r")
content=file.read()
print(content)
file.close()

#other method
# with open("notes.txt","r")as file:
#    while True:
#       line=file.readline()
#       if not line:
#          break
#       print(line.strip())

