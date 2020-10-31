# Odwracanie string
#
#  Autor: Szymon Krawczyk
#   Data utworzenia: 31.10.2020
#

def reverse_string(string):
    strlen = len(string)
    temp = ""
    for i in range(strlen):
        temp += string[strlen-(i+1)]
    return temp


# test
print(reverse_string("String testowy"))
print(reverse_string("!dlrow olleH"))
