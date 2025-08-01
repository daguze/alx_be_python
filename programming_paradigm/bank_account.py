class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"deposited {amount}, new balance is {self.__account_balance}"
        else:
            return "Deposit amount must be positive"
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print("Current Balance:", self.__account_balance)