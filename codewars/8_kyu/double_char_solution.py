# https://www.codewars.com/kata/56b1f01c247c01db92000076
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(s):
    doubled = ''
    for char in s:
        doubled += char * 2  # megduplázzuk az aktuális karaktert és hozzáadjuk a doubled változóhoz
    return doubled

print(double_char('alma'))
print(double_char('Nabukadonozor'))