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
    
    def execute(self, user, deposit, withdraw):
        user.deposit(deposit)
        user.print_statement()
        user.add_interest()
        user.print_statement()
        user.withdraw(withdraw)
        user.print_statement()
        print("---------------")

Mitchell = BankAccount("Mitchell", 13141592, 0)
Mitchell.execute(Mitchell, 400000, 150)

Ayush = BankAccount("Ayush", 34582458, 0)
Mitchell.execute(Ayush, 200000, 10000)

User_3 = BankAccount("User_3", 12345678, 0)
Mitchell.execute(User_3, 50000, 200)


