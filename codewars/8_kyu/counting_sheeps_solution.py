# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).


def count_sheeps(sheep: list):
    return sheep.count(True)  # count metódussal megszámoljuk a list True elemeit.


print(count_sheeps([True, False, True, False]))
