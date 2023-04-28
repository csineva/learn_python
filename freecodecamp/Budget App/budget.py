class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        funds = 0
        for item in self.ledger:
            funds += amount
        return funds

def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(100, "some money")
print(food.ledger)
food.deposit(600, "some more money")
print(food.ledger)
print(food.withdraw(1))