class BankAccount:
    bank_name = 'PyBank'
    accounts_count = 0

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError
        self.history = []
        self.owner = owner
        self._balance = balance
        BankAccount.accounts_count += 1
        
    def deposit(self, amount):
        self._check_amount(amount)
        self._balance += amount
        self.history.append(f'deposit {amount}')

    def withdraw(self, amount):
        self._check_amount(amount)
        if amount > self._balance:
            raise ValueError
        self._balance -= amount
        self.history.append(f'withdraw {amount}')

    def get_balance(self):
        return self._balance

    def __repr__(self):
        return f'BankAccount(owner={self.owner!r}, balance={self._balance!r})'

    def _check_amount(self, amount):
        if amount <= 0:
            raise ValueError
        if not isinstance(amount, (int, float)):
            raise TypeError
