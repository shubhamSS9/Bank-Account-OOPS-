class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self, amount):
        self.balance+=amount
    
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient Fund")
            # return self.balance
        
    def display(self):
        print(f"Your total balance is {self.balance}")

my_account=BankAccount()

my_account.deposit(300)
my_account.withdraw(600)
my_account.display()
