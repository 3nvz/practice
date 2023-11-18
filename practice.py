class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0


    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if isinstance(balance, int) and balance > 0 and balance < 100000:
            self._balance = balance
        else:
            raise Exception("Balance must be positive")
    

bA1 = BankAccount("ljol")
bA1.balance = 100
print(bA1.balance)

