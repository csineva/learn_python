"""
Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
"""


def sequence_sum(start, end, step):
    # print(len(range(start, end + 1, step)))
    return sum(range(start, end + 1, step))


print(sequence_sum(20, 33, 5))  # 45
print(sequence_sum(20, 673388797, 5))  # 45345247259849570
print(sequence_sum(9383, 71418, 2))  # 1253127200
print(sequence_sum(2, 6, 2))  # 12
print(sequence_sum(-1, -5, -3))  # -5
print(sequence_sum(-24, -2, 22))  # -26
