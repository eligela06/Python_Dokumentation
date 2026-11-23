class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}: {self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.balance += amount
            return True

    def withdraw(self, amount):
        if amount > self.balance or amount <= 0:
            return False
        else:
            self.balance -= amount
            return True


class SavingsAccount(BankAccount):
    def __init__(self, owner,rate, balance=0 ):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate /100

class CheckingAccount(BankAccount):
    def __init__(self, owner, overdraft_limit, balance=0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if super().withdraw(amount) > self.overdraft_limit:
            return super().withdraw(amount)
        else:
            return False


acc = BankAccount("Anna", 100)
savings = SavingsAccount("Ben", 1000, 5)
checking = CheckingAccount("Cara", 100, 200)

print(acc.deposit(50))      # True
print(acc.withdraw(200))    # False
print(acc)                  # Anna: $150.00

savings.add_interest()
print(savings.balance)      # 1050.0

print(checking.withdraw(250))  # True
print(checking.balance)        # -150
print(checking.withdraw(100))  # False

accounts = [acc, savings, checking]
print(sum(a.balance for a in accounts))  # 1050.0