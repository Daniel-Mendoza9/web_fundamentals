class BankAccount:

    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1 + self.int_rate
        return self

    @classmethod
    def print_all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

acc1 = BankAccount()
acc2 = BankAccount()

acc1.deposit(50).deposit(50).deposit(50).withdraw(75).yield_interest().display_account_info()
acc2.deposit(400).deposit(600).withdraw(75).withdraw(75).withdraw(75).withdraw(75).yield_interest().display_account_info()

BankAccount.print_all_info()