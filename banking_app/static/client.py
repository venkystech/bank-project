class Client:
    def __init__(self, name, deposit):
        self.account = {
            'account_number': randint(10000, 99999),
            'name': name,
            'holdings': deposit
        }

    def withdraw(self, amount):
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            print(f"Withdrawal successful! Remaining balance: {self.account['holdings']}")
        else:
            print("Insufficient balance!")

    def deposit(self, amount):
        self.account['holdings'] += amount
        print(f"Deposit successful! New balance: {self.account['holdings']}")

