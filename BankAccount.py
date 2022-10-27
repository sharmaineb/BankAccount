class BankAccount:
    def __init__(self, full_name, account_number, balance = 0): # balance starting at 0
        self.name = full_name
        self.account = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount # add amount to the balance
        print()
        print(f"Amount Deposited: ${amount} New Balance: ${self.balance}") 

    def withdraw(self, amount):
        self.balance = self.balance - amount # subtract balance from account
        print(f"Amount Withdrawn: ${amount} New Balance: ${self.balance}") 
        if amount > self.balance:
            print("Insufficient Funds.")
            print()
            self.balance = self.balance - 10 # charge overdraft fee of $10
        else:
            return self.balance

    def get_balance(self):
        print("Here is your current account balance:")
        return self.balance

    def add_interest(self):
        self.balance = self.balance * 0.00083 # add interest to the users balance

    def print_statement(self): # prints a message with the account name, account number, and balance
        print()
        print(  "Name:", self.name)
        print(  "Account No.:", self.account ) # account number
        print(  "Balance:", self.balance)

# outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.
mitchell = BankAccount("Mitchell", "3141592")
mitchell.deposit(400000)
mitchell.print_statement()
mitchell.withdraw(150)
mitchell.print_statement()