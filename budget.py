class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append([amount, description])

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
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
        if self.check_funds(amount):
            category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + category.name)
            return True
        else:
            return False

    def check_funds(self, amount):
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


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
business.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
food.withdraw(100)
entertainment.withdraw(20)
business.withdraw(10)
entertainment.withdraw(30)

def create_spend_chart(categories):
    percList = []
    totalCount = 0
    for x in categories:
        count = 0
        for y in x.ledger:
            if y[0] < 0:
                count += abs(y[0])
        totalCount += count
    for x in categories:
        count = 0
        for y in x.ledger:
            if y[0] < 0:
                count += abs(y[0])
        percList.append([int((0.10 * round((count / totalCount) / 0.10)) * 100), x.name])
    return percList

print(create_spend_chart([business, food, entertainment]))

expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(expected)
