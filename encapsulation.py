class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner              # public attribute
        self.__balance = 0.0            # private attribute
        if initial_balance > 0:
            self.deposit(initial_balance)

    
    def deposit(self, amount):
        """Add funds. Rejects non-positive or non-numeric amounts."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        """Remove funds, subject to validation and a sufficient-balance check."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def display_balance(self):
        """Read-only view of the protected state."""
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.__balance:,.2f}")
        return self.__balance

    #Controlled read-only access via property
    @property
    def balance(self):
        """Expose the balance for reading only — no setter is defined."""
        return self.__balance


# Example
if __name__ == "__main__":
    account = BankAccount("Rhiana", 100.0)
    account.display_balance()
    # Account owner: Rhiana
    # Current balance: $100.00

    account.deposit(250.50)
    account.withdraw(50.50)
    account.display_balance()
    # Account owner: Rhiana
    # Current balance: $300.00

    print(account.balance)      # 300.0  -- reading works

    # direct modification attempt
    try:
        account.balance = 999999    # no setter defined -> AttributeError
    except AttributeError as e:
        print(f"Blocked: {e}")

    try:
        account.__balance = 999999  # creates a NEW unrelated attribute
    except AttributeError as e:
        print(f"Blocked: {e}")
    print(account.balance)      # still 300.0 -- the real balance is untouched