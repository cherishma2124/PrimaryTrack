import re

password = input("Enter password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")