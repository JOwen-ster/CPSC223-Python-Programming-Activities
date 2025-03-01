class NegativeAmountError(Exception):
    def __init__(self, message):
        self.message = message


class InsufficientFundsError(Exception):
    def __init__(self, message):
        self.message = message