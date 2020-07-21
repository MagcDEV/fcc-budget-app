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
            balance += x[0]
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
        count = 1
        toPrint = ""
        for x in self.ledger:
            if count < len(self.ledger):
                toPrint += (x[1] + "                       ")[0:23] + ("                       " +
                                                                       str("{:.2f}".format(x[0])))[-7:] + "\n"
            else:
                toPrint += (x[1] + "                       ")[0:23] + ("                       " +
                                                                       str("{:.2f}".format(x[0])))[-7:]
            count += 1

        if len(self.name) % 2 == 0:
            return ("*" * int(((30 - (len(self.name))) / 2)) +
                    self.name + "*" * int(((30 - (len(self.name))) / 2))) + "\n" + toPrint + "\n" + "Total: " + str("{:.2f}".format(self.get_balance()))
        else:
            return ("*" * int(((30 - (len(self.name))) / 2)) + self.name +
                    "*" * int(((30 - (len(self.name))) / 2) + 1)) + "\n" + toPrint + "\n" + "Total: " + str("{:.2f}".format(self.get_balance()))


queso = Category("Food")

queso.deposit(2000, "initial deposit")

queso.deposit(1000, "un kilo de queso")

queso.withdraw(500, "un kilo de jamon")

jamon = Category("Tech")

queso.transfer(200, jamon)

print(queso)

# def create_spend_chart(categories):
