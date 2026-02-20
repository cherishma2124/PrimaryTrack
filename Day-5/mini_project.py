class BankAccount:
    def __init__(self, name, account_number, account_type):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
        else:
            self.balance += amount
            print(f"Rs {amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Rs {amount} withdrawn successfully")

    def display_details(self):
        print("Account Details")
        print(f"Name          : {self.name}")
        print(f"Account No    : {self.account_number}")
        print(f"Account Type  : {self.account_type}")
        print(f"Balance       : Rs {self.balance}")
   

print("Welcome to Bank Application")

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
account_type = input("Enter account type (Savings/Current): ")

account = BankAccount(name, account_number, account_type)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_details()

    elif choice == "4":
        print("Thank you for using the Bank Application")
        break

    else:
        print("Invalid choice. Please try again.")
