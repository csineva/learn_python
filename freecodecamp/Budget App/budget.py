class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        details = f'{self.name:*^30}\n'
        for item in self.ledger:
            details += f'{item["description"]: <23.23}{item["amount"]: >7.2f}\n'
        details += f'Total: {self.get_balance():.2f}'

        return details

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        funds = 0
        for item in self.ledger:
            funds += item["amount"]
        return funds

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    withdraws_dict = {}
    sum_withdraws = 0
    longest_category = 0
    for category in categories:
        if len(category.name) > longest_category: longest_category = len(category.name)
        withdraws = abs(sum([item["amount"] for item in category.ledger if item["amount"] < 0]))
        withdraws_dict[category.name] = [withdraws]
        sum_withdraws += withdraws
    for category in withdraws_dict:
        percent = int((withdraws_dict[category][0] * 100 / sum_withdraws) // 10)
        withdraws_dict[category].append(percent)

    percents = []
    percents.append([f'{percent:>3}| ' for percent in range(0, 101, 10)][::-1])
    for percent in withdraws_dict:
        percents.append(["o  " if o <= withdraws_dict[percent][1] else "" for o in range(11)][::-1])

    final = "Percentage spent by category\n"
    print_percents = []
    for index in range(11):
        row = ""
        for percent in percents:
            row += f'{percent[index]:>3}'
        final += f'{row}\n'
    final += f'{" " * 4}{"-" * 10}\n'

    for index in range(longest_category):
        row = "     "
        for key in withdraws_dict:
            try:
                # row += ""
                row += f'{key[index]:3}'
            except IndexError:
                row += f'   '
        final += f'{row}\n'

    return final[:-1]

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
create_spend_chart([business, food, entertainment])
