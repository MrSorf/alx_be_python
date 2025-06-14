class BankAccount:
    def __init__(self, account_balance, balance):
        self.account_balance = account_balance
        self.balance = 0
    
    def deposit(self, amount):
         account_balance += amount
         return account_balance
    
    def withdraw(self, amount):
        account_balance = 100
        if amount <= account_balance:
            return account_balance - amount 
        else: 
            print("Insufficient funds!")

    def display_balance(self, account_balance):
        print(f"Your balance is: ${account_balance}")
        







