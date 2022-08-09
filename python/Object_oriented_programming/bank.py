class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password
    def deposit(self, password, amount_to_deposit):
        if password != self.password:
            print("incorrect password")
            return None
        if amount_to_deposit < 0:
            print("you can not deposit a negative amount")
            return None
        self.balance += amount_to_deposit
        return self.balance
    
    def withdraw(self, password, amount_to_withdraw):
        if password != self.password:
            print("incorrect password")
            return None
        if amount_to_withdraw == 0:
            print("Not balance in your account")
            return None
        if amount_to_withdraw > self.balance:
            print("you can not withdraw more than you balance")
            return None
        self.balance -= amount_to_withdraw
        return self.balance

myaccount = Account("ahmed", 234000, 1234)


print(myaccount.deposit(1234, 3000))