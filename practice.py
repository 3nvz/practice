class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def set_balance(self, balance):
        if isinstance(balance, int) and balance > 0 and balance < 100000:
            self._balance = balance
        else:
            raise Exception("Balance must be positive")
    
    def get_balance(self):
        return self._balance
    

bA1 = BankAccount("John")
bA1.set_balance(-100)
print(bA1.get_balance())

