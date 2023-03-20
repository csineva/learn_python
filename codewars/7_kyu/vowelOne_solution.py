# https://www.codewars.com/kata/580751a40b5a777a200000a1
# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.
#
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
#
# Examples:
# vowelOne "abceios" -- "1001110"
# vowelOne "aeiou, abc" -- "1111100100"

def vowel_one(s):
    vovels = 'aeiouAEIOU'  # magánhangzók
    encoded_string = ''  #tároló
    for char in s:
        if char in vovels:         # ha az aktuális karakter a vovel stringben van, akkor magánhangzó
            encoded_string += '1'  # tehát beleírunk egy 1-est a tárolóba
        else:
            encoded_string += '0'  # amúgy meg egy 0-át

    return encoded_string

print(vowel_one('elore megyunk nem hatra'))