# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
# and month 11 (November), is part of the fourth quarter.
#
# Constraint:
# 1 <= month <= 12

def quarter_of(month):
    # your code here
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4


print(quarter_of(7))
print(quarter_of(2))


# another clever solution
# def quarter_of(n):
#     return (n + 2) // 3
