# Main demonstrujacy i testujacy mozliwosci klas Shelf i Product
#
#   skrypt zapewniający możliwość przetestowania funkcji zaimplementowanych w klasie Shelf
#   pod postacią prostego menu opartego na instrukcji if. TODO( nie umiem w dokumentacje )
#
#   Autorzy: Szymon Krawczyk, Michał Kopałka
#
#    Data utworzenia: 31.10.2020
#
#       Modyfikacje:
#           31.10.2020 | Michał Kopałka     | Utworzenie wyjatkow
#           01.11.2020 | Szymon Krawczyk    | Przeniesienie try do main
#           01.11.2020 | Szymon Krawczyk    | Rozbudowanie main
#           01.11.2020 | Michał Kopałka     | Rozbudowanie main
#

import Shelf
import os

def main():
    anime_shelf = Shelf.Shelf()
    #inicjalizacja pierwszych dwóch produktów TODO ( było nieco zbyt pusto na początku )
    anime_shelf.new_product("Megumin figurine", 99.98, 7)
    anime_shelf.new_product("Holo sticker", 5.55, 17)
    anime_shelf.new_product("Echidna dakimakura", 119.99, 1)

    myinput = 0
    while myinput != 5:
        print("        APLIKACJA SKLEP        ")
        print("1) Wyświetl listę produktów.")
        print("2) Dodaj nowy produkt.")
        print("3) Usuń produkt z listy.")
        print("4) Zmodyfikuj istniejący produkt.")
        print("5) zakończ działanie programu.")
        try:
            myinput = int(input("   Wybierz akcję którą chcesz wykonać: "))
        except ValueError:
            myinput = 0

        if myinput == 1:
            printshelf(anime_shelf)

        elif myinput == 2:
            try:
                myinput1 = input("Nazwa produktu: ")
                myinput2 = float(input("Cena produktu: "))
                myinput3 = int(input("Ilość produktu: "))
                anime_shelf.new_product(myinput1, myinput2, myinput3)

                printshelf(anime_shelf)

            except Shelf.WrongTypeOfVariable:
                input("Zły typ danych, spróbuj ponownie ( naciśnij ENTER )")
            except Shelf.WrongValueOfVariable:
                input("Zła wartość danych, spróbuj ponownie ( naciśnij ENTER )")
            except ValueError:
                input("Zła wartość danych, spróbuj ponownie ( naciśnij ENTER )")

        elif myinput == 3:
            try:
                print(anime_shelf)
                print()
                myinput1 = input("podaj nazwę prduktu ktory chcesz usunąć: ")
                anime_shelf.remove_product(myinput1)
                printshelf(anime_shelf)

            except Shelf.WrongTypeOfVariable:
                input("Zły typ danych, spróbuj ponownie ( naciśnij ENTER )")
            except Shelf.WrongValueOfVariable:
                input("Zła wartość danych, spróbuj ponownie ( naciśnij ENTER )")
            except Shelf.ProductDoesNotExistError:
                input("Podany produkt nie istnieje ( naciśnij ENTER )")
            except ValueError:
                input("Zła wartość danych, spróbuj ponownie ( naciśnij ENTER )")

        elif myinput == 4:
            try:
                print(anime_shelf)
                myinput1 = str(input("podaj nazwę produktu który chcesz zmodyfikować: "))
                if anime_shelf.return_product_index_by_name(myinput1) == -1:
                    input("Wybrany produkt nie istnieje ( naciśnij ENTER )")
                else:
                    myinput2 = int(input("Którą wartość chcesz zmodyfikować? 1)nazwę 2)cenę 3)ilość sztuk(set) 4)ilość sztuk(add) : "))
                    if myinput2 < 1 or myinput2 > 4:
                        input("Wybrano złą wartość ( możliwe opcje: 1, 2, 3, 4 ) ( naciśnij ENTER )")
                    else:
                        myinput3 = input("podaj nową wartość: ")
                        if myinput2 == 1:
                            anime_shelf.change_name(old=myinput1, new=myinput3)
                        if myinput2 == 2:
                            anime_shelf.set_price(name=myinput1, value=float(myinput3))
                        if myinput2 == 3:
                            anime_shelf.set_amount(name=myinput1, value=int(myinput3))
                        if myinput2 == 4:
                            anime_shelf.change_amount(name=myinput1, value=int(myinput3))
                        printshelf(anime_shelf)

            except Shelf.WrongTypeOfVariable:
                input("Zły typ danych, spróbuj ponownie ( naciśnij ENTER )")
                print()
            except Shelf.WrongValueOfVariable:
                input("Zła wartość danych, spróbuj ponownie ( naciśnij ENTER )")
                print()
            except Shelf.ProductDoesNotExistError:
                input("Wybrany produkt nie istnieje ( naciśnij ENTER )")
                print()
            except ValueError:
                input("Zła wartość danych, spróbuj ponownie ( naciśnij ENTER )")
                print()

        elif myinput == 5:
            print()
            input("Dziękujemy za skorzystanie ze sklepiku, zapraszamy ponownie ( naciśnij ENTER )")
        else:
            input("Proszę wybrać opcję z zakresu 1 - 5 ( naciśnij ENTER )")

        print()
        print()
        clear()

def printshelf(shelf):
    print()
    print(shelf)
    input("( naciśnij ENTER )")

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

    # TODO wszystko w miarę w porządku oprócz dodawania produktów o nazwie "123".
    #  wczytywane są one jako string i nie trigerują wyjątku
    #  różnica pomiędzy Product(123, 123, 123) a Product("123", 123, 123)
    # TODO nie zaimplementowałem też metody change_amount... zapomniałem że istnieje.
    #  jest tylko set. ( po co komu change_amount jak ma set? )


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    main()
