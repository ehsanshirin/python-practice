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


    def transfer(self, amount, target_account):
        if amount <= 0:
            print('Invalid transfer amount')
            return
        if amount > self.balance:
            print('Insufficient funds for transfer')
            return
        self.balance -= amount
        target_account.balance += amount


        print (f'{self.owner} transferred {amount} to {target_account.owner}')
        print(f'{self.owner} balance: {self.balance}')
        print(f'{target_account.owner} balance: {target_account.balance}')


acc1 = BankAccount('Ali')
acc2 = BankAccount('Sara')

acc1.deposit(100)
acc2.deposit(50)

acc1.transfer(30,acc2)

acc1.info()
acc2.info()