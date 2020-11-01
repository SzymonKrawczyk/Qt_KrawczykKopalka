# Main demonstrujacy i testujacy mozliwosci klas Shelf i Product
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#   Data utworzenia: 31.10.2020
#
#       Modyfikacje:
#           31.10.2020 | Michał Kopałka     | Utworzenie wyjatkow
#           01.11.2020 | Szymon Krawczyk    | Przeniesienie try do main
#           01.11.2020 | Szymon Krawczyk    | Rozbudowanie main
#

import Shelf


def main():
    anime_shelf = Shelf.Shelf()

    print("Dodawanie produktów.")
    myinput = input("Nacisnij Enter aby dodać produkt, next aby przejść dalej: ")
    while myinput != "next":
        try:
            myinput1 = input("Nazwa produktu: ")
            myinput2 = float(input("Cena produktu: "))
            myinput3 = int(input("Ilość produktu: "))
            anime_shelf.new_product(myinput1, myinput2, myinput3)

            print()
            print("Obecna zawartosc półki:")
            print(anime_shelf)

            myinput = input("Nacisnij Enter aby dodać produkt, next aby przejść dalej: ")

        except Shelf.WrongTypeOfVariable:
            print("Zły typ danych, spróbuj ponownie")
            print()
        except Shelf.WrongValueOfVariable:
            print("Zła wartość danych, spróbuj ponownie")
            print()
        except ValueError:
            print("Zła wartość danych, spróbuj ponownie")
            print()


    # TODO dokonczyc main wedlug wzoru wyzej
    # anime_shelf.new_product("Megumin figurine", 99.98, 7)
    # anime_shelf.new_product("Holo sticker", 5.55, 17)
    # anime_shelf.new_product(112, 123, 123)
    # anime_shelf.new_product("HEJ", "asd", 123)
    # print(anime_shelf)
    #
    # anime_shelf.change_name("MegumiN figurine", "Megumin figure")
    # anime_shelf.set_amount("megumin figure", 2)
    # anime_shelf.set_price("megumin figure", 130.49)
    # print(anime_shelf)
    #
    # anime_shelf.remove_product("megumin figure")
    # anime_shelf.change_amount("HoLo StIcKeR", 25)
    # print(anime_shelf)


if __name__ == '__main__':
    main()