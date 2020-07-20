class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append([amount, description])

    def withdraw(self, amount, description=""):
        if self.check_founds(amount):
            self.ledger.append([-amount, description])
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        count = 0
        for x in self.ledger:
            balance += self.ledger[count][0]
            count += 1
        return balance

    def transfer(self, amount, category):
        if self.check_founds(amount):
            category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + category.name)
            return True
        else:
            return False

    def check_founds(self, amount):
        if self.get_balance() > amount:
            return True
        else:
            return False

    def __str__(self):
        if len(self.name) % 2 == 0:
            return ("*" * int(((30 - (len(self.name))) / 2)) +
                    self.name + "*" * int(((30 - (len(self.name))) / 2)))
        else:
            return ("*" * int(((30 - (len(self.name))) / 2)) + self.name +
                    "*" * int(((30 - (len(self.name))) / 2) + 1))


queso = Category("Food")

queso.deposit(1000, "un kilo de queso")


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append([amount, description])

    def withdraw(self, amount, description=""):
        if self.check_founds(amount):
            self.ledger.append([-amount, description])
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        count = 0
        for x in self.ledger:
            balance += self.ledger[count][0]
            count += 1
        return balance

    def transfer(self, amount, category):
        if self.check_founds(amount):
            category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + category.name)
            return True
        else:
            return False

    def check_founds(self, amount):
        if self.get_balance() > amount:
            return True
        else:
            return False

    def __str__(self):
        if len(self.name) % 2 == 0:
            return ("*" * int(((30 - (len(self.name))) / 2)) +
                    self.name + "*" * int(((30 - (len(self.name))) / 2)))
        else:
            return ("*" * int(((30 - (len(self.name))) / 2)) + self.name +
                    "*" * int(((30 - (len(self.name))) / 2) + 1))


queso = Category("Food")

queso.deposit(1000, "un kilo de quesoooooooooooooooo")

queso.withdraw(500, "un kilo de jamon")

jamon = Category("Tech")

queso.transfer(200, jamon)

print(queso.get_balance())
print(jamon.get_balance())

print(queso.ledger)
print(jamon.ledger)

print(queso)

count = 1
toPrint = ""
for x in queso.ledger:
    if count < len(queso.ledger):
        toPrint += (x[1])[0:23] + "\n"
    else:
        toPrint += (x[1])[0:23]
    count += 1

print(toPrint)

# def create_spend_chart(categories):
