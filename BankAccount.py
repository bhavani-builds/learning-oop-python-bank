class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: {self.__balance}")


# Create object
account = BankAccount("123456789", 5000)

# Perform operations
account.check_balance()
account.deposit(2000)
account.check_balance()
account.withdraw(1500)
account.check_balance()