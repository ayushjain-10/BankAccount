class BankAccount:
    def __init__(self, full_name, account_number, balance, account_type):
        self.full_name= full_name
        self.account_number= account_number
        self.balance= balance
        self.account_type= account_type
    
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
        if self.account_type == "checking" or self.account_type == "Checking":
            interest = self.balance * 0.00083
        else:
            interest = self.balance * 0.01
        self.balance+= interest
        print(f"Interest earned this month= {interest}")
        print (f'Account Balance({self.account_type}) with interest: ${self.balance}')

    def print_statement(self):
        account_str = str(self.account_number)
        print(f"Account Name: {self.full_name}")
        print(f"Account Number: ****{account_str[-4:]}")
        print(f"Balance: {self.balance}")
    
    def execute(self, user, deposit, withdraw):
        user.deposit(deposit)
        user.add_interest()
        user.withdraw(withdraw)
        user.print_statement()
        print("---------------")
    
    def interest_loop():
        for account in bank:
            print(f"Username= {bank[account]}")
            account.add_interest()
            print("--------")

    def application():
        while True:
            choice= input("Enter no.= 1. Create Account, 2. Statement, 3. Deposit, 4. Withdraw, or 5. Exit : ")
            if choice== "1":
                name= input("Enter name:")
                account_no= input("Enter account number:")
                account_no = int(account_no)
                bal= input("Enter balance:")
                bal = int(bal)
                User = BankAccount(name, account_no, bal, type)
                bank[User]= name
                account_numbers[User]= account_no
                User.print_statement()
            
            if choice == "2":
                number= 10
                statement= input("Enter account number:")
                for account in account_numbers:
                    if statement == account_numbers[account]:
                        account.print_statement()
                        number+=1
                        break
                if number==10:
                    print("Incoorect account information")
                        
            if choice == "3":
                number_2= 10
                statement= input("Enter account number:")
                deposit_amount= input("How much would you like to deposit?")
                for account in account_numbers:
                    if statement == account_numbers[account]:
                        account.deposit(int(deposit_amount))
                        number_2+=1
                        break
                if number_2==10:
                    print("Incoorect account information")


            if choice == "4":
                number_3= 10
                statement= input("Enter account number:")
                withdraw_amount= input("How much would you like to withdraw?")
                for account in account_numbers:
                    if statement == account_numbers[account]:
                        account.withdraw(int(withdraw_amount))
                        number_3+=1
                        break
                if number_3==10:
                    print("Incoorect account information")
            
            if choice == "5":
                print("Hope you have a great day!")
                break



    

Mitchell = BankAccount("Mitchell", 13141592, 0, "checking")
Mitchell.execute(Mitchell, 400000, 150)

Ayush = BankAccount("Ayush", 34582458, 0, "savings")
Mitchell.execute(Ayush, 400000, 200)

User_3 = BankAccount("User_3", 12345678, 0, "Checking")
Mitchell.execute(User_3, 50000, 600000)

bank= {Mitchell: 'Mitchell', Ayush: 'Ayush', User_3: 'User_3'}
account_numbers= {Mitchell: '13141592', Ayush: '34582458', User_3: '12345678'}


BankAccount.interest_loop()
BankAccount.application()