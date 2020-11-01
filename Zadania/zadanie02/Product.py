# Klasa Product
#
#   Klasa przechowuje informacje o produkcie skladajacym sie z nazwy, ceny i ilosci
#
#       set_name - ustawia nowa nazwe
#       set_price - ustawia nowa cene
#       set_amount - ustawia nowa ilosc
#       change_amount - dodaje wartosc do starej ilosci
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#   Data utworzenia: 31.10.2020
#
#       Modyfikacje:
#           31.10.2020 | Michał Kopałka     | Utworzenie wyjatkow
#           01.11.2020 | Szymon Krawczyk    | Przeniesienie wyjatkow do osobnego pliku
#           01.11.2020 | Szymon Krawczyk    | Usuniecie blokow try
#


from MyExceptions import WrongTypeOfVariable
from MyExceptions import WrongValueOfVariable


class Product:
    """Klasa przechowuje informacje o produktcie"""

    # Zmienne
    name = ""
    price = -1.0
    amount = -1

    def __init__(self, name=None, price=None, amount=None):
        if not isinstance(name, str):
            raise WrongTypeOfVariable()
        if not isinstance(price, (int, float)):
            raise WrongTypeOfVariable()
        if not isinstance(amount, int):
            raise WrongTypeOfVariable()

        if price < 0:
            raise WrongValueOfVariable()
        if amount < 0:
            raise WrongValueOfVariable()

        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"\"{self.name}\", ${self.price}, Amount: {self.amount}"

    def set_name(self, value):
        if not isinstance(value, str):
            raise WrongTypeOfVariable()
        else:
            self.name = value

    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise WrongTypeOfVariable()
        if value < 0:
            raise WrongValueOfVariable()
        self.price = value

    def set_amount(self, value):
        if not isinstance(value, int):
            raise WrongTypeOfVariable()
        if value < 0:
            raise WrongValueOfVariable()
        self.amount = value

    def change_amount(self, value):
        if not isinstance(value, int):
            raise WrongTypeOfVariable()
        if (self.amount+value) < 0:
            raise WrongValueOfVariable()
        self.amount += value
