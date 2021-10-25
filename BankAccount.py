class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name= full_name
        self.account_number= account_number
        self.balance= balance
    
    def deposit(self, amount):
      self.balance += amount
      print(f'Amount deposited: ${amount} New Balance: ${self.balance}')
    
    def withdraw(self, amount):
        if amount> self.balance:
            print("Insufficient funds")
            self.balance-=10
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount} New Balance: ${self.balance}')

    def get_balance(self):
      print (f'Account Balance: ${self.balance}')
      return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance+= interest
        print (f'Account Balance with interest: ${self.balance}')

    def print_statement(self):
        account_str = str(self.account_number)
        print(f"Account Name: {self.full_name}")
        print(f"Account Number: ****{account_str[-4:]}")
        print(f"Balance: {self.balance}")

Mitchell = BankAccount("Mitchell", 13141592, 0)
Mitchell.deposit(400000)
Mitchell.print_statement()
Mitchell.add_interest()
Mitchell.print_statement()
Mitchell.withdraw(150)
Mitchell.print_statement()

