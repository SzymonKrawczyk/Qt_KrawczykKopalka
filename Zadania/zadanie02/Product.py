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

class Product:
    """Klasa przechowuje informacje o produktcie"""

    # Zmienne
    name = ""
    price = -1.0
    amount = -1

    def __init__(self, name=None, price=None, amount=None):

        # TODO: gdy niepoprawny typ danych, wartosci domyslne / wyjatek?
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):

        return f"\"{self.name}\", ${self.price}, Amount: {self.amount}"

    def set_name(self, value):

        # TODO: wyjatek gdy niepoprawny typ danych
        self.name = value

    def set_price(self, value):

        # TODO: wyjatek gdy niepoprawny typ danych
        # TODO jesli cena < 0.0, wyjatek
        self.price = value

    def set_amount(self, value):

        # TODO: wyjatek gdy niepoprawny typ danych
        # TODO jesli ilosc < 0, wyjatek
        self.amount = value

    def change_amount(self, value):

        # TODO: wyjatek gdy niepoprawny typ danych
        # TODO jesli ilosc po zmianie < 0, wyjatek
        self.amount += value
