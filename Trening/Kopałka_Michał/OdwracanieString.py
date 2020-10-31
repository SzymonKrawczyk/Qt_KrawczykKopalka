#----------------------------------------------------------
#
#   Michał Kopałka
#       Zmiany:
#           wersja orginalna    -    31.10.2020
#
#       Funkcjonalność:
#           skrypt prezentujący działanie funkcji odwracającej kolejność występowania
#           znaków w ciągu znakowym string na przykładnie stringa "ziemnaiczek"
#
#----------------------------------------------------------

def reverseString(string):
    reversedstring = ""

    i = len(string) - 1
    while i >= 0:
        reversedstring = reversedstring + string[i]
        # print(slowo[i])
        i = i - 1
    return reversedstring


def main():
    string = "ziemniaczek"
    print(f"Nasz string: {string}")
    print(f"Nasz string po odwróceniu: {reverseString(string)}")


if __name__ == "__main__":
    main()
