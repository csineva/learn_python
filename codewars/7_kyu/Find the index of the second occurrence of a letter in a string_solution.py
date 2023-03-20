# https://www.codewars.com/kata/63f96036b15a210058300ca9
# In this kata, you need to write a function that takes a string and a letter as input and then
# returns the index of the second occurrence of that letter in the string. If there is no such letter in the string,
# then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.
#
# Examples:
# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1

def second_symbol(s: str, symbol):
    pointer = s.find(symbol)  # az első keresés eredményét a pointer változóba mentjük
    if pointer == -1:         # ha a pointer érték -1 (nincs találat), akkor visszatérünk vele
        return pointer
    else:
        return s.find(symbol, pointer + 1)  # egyébként meghívjuk a find metódust, megadva, hogy pointer + 1 indextől keresse meg a második előfordulást.
                                            # Ha talál, akkor return, ha nem, akkor is (mert akkor -1 lesz a find visszatérési értéke és az nekünk pont kapóra jön)

print(second_symbol('alma', 'a'))
print(second_symbol('alma', 'l'))
print(second_symbol('lóhalálában', 'l'))