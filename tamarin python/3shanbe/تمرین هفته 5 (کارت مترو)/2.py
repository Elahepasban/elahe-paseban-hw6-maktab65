class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, dmoney):
        self.balance += dmoney
        return self.balance

    def withdrawal(self, wmoney):
        if wmoney > self.balance:
            print(f"balance is not enough. your balance is {self.balance}")
        else:
            self.balance -= wmoney
            return self.balance

    def fees_bank(self):
        self.balance -= (0.05 * self.balance)
        return self.balance

    def display(self, dmoney, wmoney):
        return f'account_number: {self.account_number}, Name: {self.name}, balance: {self.balance},' \
               f' deposit: {dmoney}, withdrawal: {wmoney}'


person = BankAccount(1, "ell", 250)
print(person.deposit(50))
print(person.withdrawal(48))
print(person.fees_bank())
print(person.display(50, 48))
