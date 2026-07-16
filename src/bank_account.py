from datetime import datetime
from src.exeptions import WithdrowalTimeRestrictionError

class BankAccount:

    def __init__(self, balance, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction("Cuenta creada")

    def log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(
                f"Depósito: {amount}, Nuevo saldo: {self.balance}"
            )
        return self.balance
    
    def withdraw(self, amount):

        now = datetime.now()
        if now.hour < 8 or now.hour >= 17:
            raise WithdrowalTimeRestrictionError("Withdrawals are only allowed between 8 AM and 5 PM.")

        if now.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            raise WithdrowalTimeRestrictionError("Withdrawals are not allowed on weekends.")

        if amount > 0:
            self.balance -= amount
            self.log_transaction(
                f"Retiro: {amount}, Nuevo saldo: {self.balance}"
            )
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target_account):
        try:
            if amount <= self.balance:
                self.withdraw(amount)
                target_account.deposit(amount)
            else:
                raise ValueError("Insufficient funds for transfer.")
        except Exception as e:
            self.log_transaction(f"Error during transfer: {e}")
        return self.balance
    
    