#Implement a class called BankAccount that represents a bank account.The class should have private attributes for account number, account holder name, and account balance. Include methods to deposits money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class and test deposit and withdrawal functionality.

# python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
  def_init_(self): 
     self.balance=0
    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

   def deposit(self):
     amount=float(input("Enter amount to be Deposited:"))
     self.balance += amount
     print("\n Amount Deposited:",amount)

  def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn:"))
    if self.balance>=amount:
       self.balance-=amount
       print("\n You Withdrew:", amount)
    else:
      print("\n Insufficient blance")

  def display(self):
    print("\n Net Available Balance=",self.blance)

  # Driver code

  # Creating an objects of class
  s = Bank_Account()

  # Calling functions that class object
  s.deposit(5000)
  s.withdraw(2000)
  s.display()
       