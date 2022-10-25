class BankAccount:
    def __init__(self, full_name, account_number, balance = 0): # balance starting at 0
        self.name = full_name
        self.account = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount # add amount to the balance
        print("Amount Deposited: $$$ New Balance: $$$") # placeholder

    def withdraw(self, amount, amount_to_withdraw):
        self.balance = self.balance - amount # subtract balance from account
        print("Amount Withdrawn: $$$ New Balance: $$$") # placeholder
        if amount_to_withdraw > self.balance:
            print("Insufficient Funds.")
            # charge overdraft fee of $10

    def get_balance():
        print("Here is your current account balance:")

    def add_interest(self):
        self.balance = self.balance * 0.00083 # add interest to the users balance

    def print_statement(self): # prints a message with the account name, account number, and balance
