# https://www.codewars.com/kata/587731fda577b3d1b0001196
# Write simple .camelCase method for strings.
# All words must have their first letter capitalized without spaces.
#
# For instance:
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord

def camel_case(s: str):
    words = s.split()  # a stringet szavak listájára bontjuk
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())  # a szavak listáján ciklussal átiterálva minden szót nagybetűssé alakítunk, majd hozzáfűzzük a capitalized_words listához
    return ''.join(capitalized_words)  # a capitalized_word lista elemeit egy stringbe összefűzzük


print(camel_case('alma a fa alatt'))


# clever version:
# def camel_case(string):
#     return string.title().replace(" ", "")