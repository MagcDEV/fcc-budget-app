class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        print(self.name + amount)

    def withdraw(self, amount, description=""):
        print(self.name + amount)

    def get_balance(self):
        print("balance")

    def transfer(self):
        print("transfer")

    def check_founds(self):
        print("check_founds")


def create_spend_chart(categories):
