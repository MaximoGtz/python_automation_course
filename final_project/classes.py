import abstract, random
class SavingsAccount(abstract.Schema):
   def __init__(self, user_name, balance):
      self.user_name = user_name
      self.balance = balance
      account_number = self.create_account_number()
      self.account_number = account_number
      print("Account created succesfully!", end=' ')   
      print("Account number: ", account_number)
      print("Initial balance: $", balance)

   def info(self):
      print("Account: ", self.account_number)
      print("Owner: ", self.user_name)
      print("Balance: $", self.balance)
   @staticmethod
   def create_account_number():
    return random.randint(10000, 99999)
   def deposit(self, quantity):
      self.balance += quantity

class User(abstract.Schema):
   def __init__(self, name):
      self.name = name
      self.accounts = []
   def info(self):
      print("User details")
      print("Name: ", self.name)
      print("Accounts ({}) :".format(len(self.accounts)))
      total_money=0
      for account in self.accounts:
         account.info()
         total_money += account.balance
      print("Total money: $", total_money)
   def create_account(self, initial_deposit):
      account = SavingsAccount(self.name, initial_deposit)
      self.accounts.append(account)
      print("Print account created succesfully!")
      account.info()
   def get_accounts(self):
      return self.accounts

class Database(abstract.Schema):
   def __init__(self, users):
      self._users = users
   def info(self):
      if not self._users:
         print("There are no users in the database.")
      else:
         print("Database information:")
         for user in self._users:
            user.info()
   def get_users(self):
      return self._users
               
            



      


