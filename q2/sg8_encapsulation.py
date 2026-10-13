class BankAccount:
  def __init__(self, account_number, balance):
    self.__accN = account_number
    self.__bal = float(balance)

  def set_account_number(account_number):
    self.__accN = account_number

  def set_balance(self, balance):
    if balance > 0:
      self.__bal = balance
      return balance
    else:
      return "Balance must not be negative!"

  
  def get_account_number(self):
    return self.__accN
    
  
  def get_balance(self):
    return self.__bal

k = BankAccount(98612, 5000)

print("Output:")
print(f"Account 1")
print(f"Account Number {k.get_account_number()}")
print(f"Balance {k.get_balance()}")

balance1 = int(input("Change the balance to: "))
print(k.set_balance(balance1))

print(f"Account Number {k.get_account_number()}")
print(f"Balance {k.get_balance()}")
