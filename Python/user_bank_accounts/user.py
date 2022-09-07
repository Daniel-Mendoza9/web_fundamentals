from bank_account import BankAccount as ba

class User:

    def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.accounts = {}

def open_bank_account(self, account_name):
    account = ba(0.02, 0)
    self.accounts[account_name] = account

def make_deposit(self, amount, account_name):
    self.accounts[account_name].deposit(amount)
    return self

def make_withdrawal(self, amount, account_name):
    self.accounts[account_name].withdraw(amount)

def transfer_money(self, account_name, amount, other_user, other_account):
    self.accounts[account_name].withdraw(amount)
    other_user.accounts[other_account].deposit(amount)

def display_user_balance(self):
    print(self.first_name + "'s balance:") 
    for k,v in self.accounts.items():
    print(f"{k}: ${v.balance}")
    return self

def display_info(self):
    for k,v in self.__dict__.items():
    print(f"{k}: {v}")

def enroll(self):
    if self.is_rewards_member:
    print('User is already a member.')
    return
    self.is_rewards_member = True
    self.gold_card_points = 200

def spend_points(self, amount):
    if self.gold_card_points >= amount:
    self.gold_card_points -= amount
    else: print(f"{self.first_name} doesn't have enough points!")

cam = User('Cam', 'De Robertis', 'cmderobertis@gmail.com', 28)
# cam.display_info()
# cam.enroll()
# cam.display_info()

bob = User('Bob', 'Weir', 'sea245634@star.bucks', 54)
julia = User('Julia', 'Weir', 'jweir@com.at', 29)

# cam.spend_points(50)
# bob.enroll()
# bob.spend_points(80)
# cam.display_info()
# bob.display_info()
# julia.display_info()
# cam.enroll()
# julia.spend_points(40)

cam.display_info()
bob.open_bank_account('Savings')
cam.open_bank_account('Checking')
cam.make_deposit(500, 'Checking').display_user_balance()
cam.transfer_money('Checking', 400, bob, 'Savings')
bob.display_user_balance()
cam.display_user_balance()