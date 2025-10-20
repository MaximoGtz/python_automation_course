import abstract
class SavingsAccount(abstract.Schema):
   def __init__(self, user_name, balance):
      self.user_name = user_name
      self.balance = balance

class User(abstract.Schema):
   pass

