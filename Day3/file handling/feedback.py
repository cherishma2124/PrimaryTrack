feedback=input("please provide your feedback :")
with open("notes.txt","a") as file:
    file.write(feedback+"\n")
print("thank you for ur feedback")
