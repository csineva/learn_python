# String ends with
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text: str, ending):
    return text.endswith(ending)  # nahbakker, de leizzadtam :D

print(solution('alma', 'ma'))
print(solution('alma', 'holnap'))
print(solution('alma', 'al'))

#  egy másik jópofa megoldás :D
# solution = str.endswith