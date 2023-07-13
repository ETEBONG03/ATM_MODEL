from ACCOUNT import Account
class Current_account(Account):
    def __init__(self):
        Account.__init__(self)

current_account = Current_account()
current_account.deposit(50000)