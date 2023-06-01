"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

# def move_zeros(lst):
#     zeros = []
#     result = []
#
#     for number in lst:
#         if not number:
#             zeros.append(0)
#         else:
#             result.append(number)
#
#     return result + zeros

# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


def move_zeros(lst):
    for number in lst:
        if number == 0:
            lst.append(lst.pop(lst.index(0)))
    return lst

# not_mine, interesting
# def move_zeros(a):
#     a.sort(key=lambda v: v == 0)
#     return a


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))