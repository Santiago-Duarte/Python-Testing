class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = []

    def add_account(self, account):
        self.account.append(account)

    def get_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.account)
        return total_balance
    
    