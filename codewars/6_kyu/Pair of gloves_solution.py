# https://www.codewars.com/kata/58235a167a8cb37e1a0000db
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine
# the number of pair of gloves you can constitute from the gloves you have in your drawer.
#
# Given an array describing the color of each glove, return the number of pairs you can constitute,
# assuming that only gloves of the same color can form pairs.
#
# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2
# (1 red pair + 1 blue pair)
#
# input = ["red", "red", "red", "red", "red", "red"]
# result = 3
# (3 red pairs)

def number_of_pairs(gloves):
    gloves_dict = {}  #ebbe a dictionary-be pakolgatjuk a kesztyűket

    for glove in gloves:
        if glove not in gloves_dict:
            gloves_dict[glove] = 1  # ha a dict-ben még nincs, akkor belerakjuk 1-es értékkel, pl: gloves_dict['red'] = 1
        else:
            gloves_dict[glove] += 1  # ha már benne van a dict-ben, akkor hozzáadunk az értékhez 1-et

    counter = 0
    for glove in gloves_dict:
        counter += gloves_dict[glove] // 2  # A dict minden elemét 2-vel elosztva és az egész részeket összedva a counterben megkapjuk a kesztyűpárok számát

    return counter  # visszatérünk, mint a terminátor

print(number_of_pairs(['red', 'red', 'blue', 'blue', 'blue', 'yellow', 'white']))


# another smart solution
# def number_of_pairs(gloves):
#     unique = set(gloves)
#     return sum(gloves.count(i)//2 for i in unique)