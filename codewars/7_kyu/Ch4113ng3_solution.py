# https://www.codewars.com/kata/59e9f404fc3c49ab24000112
# Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"

def nerdify(txt: str):

    replace_dict = {  # mit-mire dictionary
        'a': '4',
        'A': '4',
        'e': '3',
        'E': '3',
        'l': '1',
    }

    nerdified_string = ''  # ide írjuk bele a karaktereket

    for char in txt:
        if char in replace_dict:                    # ha az aktuális karakter megegyezik a dict valamelyik kulcsával
            nerdified_string += replace_dict[char]  # akkor kicseréljük a hozzátartozó értékre és beleírjuk a nerdified_string változóba
        else:
            nerdified_string += char                # ha nincs a kulcsok között, akkor csak simán beleírjuk a nerdified_string változóba

    return nerdified_string

print(nerdify('feladat'))