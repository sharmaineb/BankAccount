accounts_list = []

class BankAccount:
    def __init__(self, full_name, account_number, type_of_account, balance = 0,): # balance set at 0
        self.name = full_name
        self.account = account_number
        self.balance = balance
        self.account_type = type_of_account
        
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

    def add_interest(self): # check the type of bank account: checking/savings
        if self.account_type == "checking":
            interest = self.balance * 0.00083 # add interest to the users balance
            self.balance = self.balance + interest
        else:
            interest = self.balance * 0.01 # a savings account get 1.2% interest (that's 1% per month)
            self.balance = self.balance + interest

    def print_statement(self): # prints a message with the account name, account number, and balance
        print()
        print(  "Name:", self.name) # name
        print(  "Account No.:", self.account ) # account number
        print(  "Balance:", self.balance) # balance

    def new_account(self):
        new_account = {"Name:", self.name, "Balance:", self.balance, "Account Number:", self.account, "Type:", self.account_type}
        accounts_list.append(new_account)

# outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.
shar = BankAccount("Shar", "67982312", "checking")
shar.deposit(7000)
shar.print_statement()
shar.withdraw(550)
shar.print_statement()
shar.add_interest()
shar.print_statement()

ian = BankAccount("Ian", "112163201", "savings")
ian.deposit(10000)
ian.print_statement()
ian.withdraw(1000)
ian.print_statement()
ian.add_interest()
ian.print_statement()

kae = BankAccount("Kaeleen", "671507134", "checking")
kae.deposit(12000)
kae.print_statement()
kae.add_interest()
kae.print_statement()
kae.withdraw(100)
kae.print_statement()

# example code
mitchell = BankAccount("Mitchell", "3141592", "savings")
mitchell.deposit(400000)
mitchell.print_statement()
mitchell.withdraw(150)
mitchell.print_statement()
mitchell.add_interest()
mitchell.print_statement()

# Create a list called: bank. Add all of your accounts to bank. 
bank = [shar, ian, kae, mitchell]





