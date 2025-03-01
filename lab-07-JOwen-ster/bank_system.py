import bank_exceptions


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise bank_exceptions.NegativeAmountError(F"Amount cannot be negative: ${amount}")
        self.balance += amount
        return self.get_balance()

    def withdraw(self, amount):
        if amount < 0:
            raise bank_exceptions.NegativeAmountError(F"Amount cannot be negative: ${amount}")
        elif amount > self.balance:
            raise bank_exceptions.InsufficientFundsError(F"Insufficient funds. You tried to withdraw ${amount}, but your balance is only {self.get_balance()}.")
        self.balance -= amount
        return self.get_balance()

    def get_balance(self):
        return F"${self.balance}"