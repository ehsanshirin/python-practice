class BankAccount :
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount
        print(self.balance)

    def withdraw (self,amount):
        if amount <= 0:
            print('Invalid withdrawal amount')
            return
        if amount > self.balance:
            print('Insufficient funds')
            return
        self.balance -= amount
        print(self.balance)


    def info(self):
        print(f'Owner: {self.owner}')
        print(f'Balance: {self.balance}')

acc1 = BankAccount('Sara')
acc1.deposit(50)
acc1.withdraw(20)
acc1.info()