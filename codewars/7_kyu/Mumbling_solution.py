# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s: str):
    output = []
    for index, char in enumerate(s, 1):   # szükségünk lesz a karakterre meg egy növekvő ciklusváltozóra --> enumerate()
        temp = char * index               # ideiglenes változóba rakjuk a karakter szorzatát az index-el
        output.append(temp.capitalize())  # nagy kezdőbetűsre alakítjuk és beleírjuk az output listába

    return '-'.join(output)  # az output lista elemeit összeolvasztjuk köztük a '-' karakterrel

print(accum('alma'))
print(accum('megkerülhetetlenül'))