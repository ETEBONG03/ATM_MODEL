class Account:
    def __init__(self):
        self.name = "Etebong"
        self.account_balance = 10000

    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance)

    def withdraw(self, amount):
        self.account_balance -= amount
        print(self.account_balance)

    def check_balance(self):
        print(self.account_balance)
