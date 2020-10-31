# Klasa Shelf
#
#   Klasa przechowuje informacje o produktach skladajacych sie z nazwy, ceny i ilosci
#
#       return_product_index_by_name - metoda pomocnicza do znajdywania indexow produktow po nazwie
#       new_product - dodaje nowy produkt do listy
#       remove_product - usuwa produkt z listy
#       change_name - ustawia nazwe produktu na nowa
#       set_price - ustawia nowa cene produktu
#       set_amount - ustawia nowa ilosc produktu
#       change_amount - dodaje wartosc do starej ilosci produktu
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#   Data utworzenia: 31.10.2020

import Product


class Shelf:
    """Klasa przechowuje informacje o produktach i zarzadzajaca nimi """

    # Zmienne
    products = []

    def __init__(self):
        self.products = []

    def __str__(self):

        temp = "Products: \n"

        for i in range(len(self.products)):
            temp += f"{i+1}) {self.products[i]}\n"

        return temp

    def return_product_index_by_name(self, name):

        # TODO: wyjatek gdy niepoprawny typ danych

        index = -1
        for i in range(len(self.products)):
            if self.products[i].name.lower() == name.lower():
                index = i
                break
        return index

    def new_product(self, name, price=-1.0, amount=-1):

        # if self.return_product_index(name) != -1:
        # TODO: wyrzuc wyjatek "produkt juz istnieje"
        self.products.append(Product.Product(name, price, amount))

    def remove_product(self, name):

        i = self.return_product_index_by_name(name)
        # if i == -1:
        # TODO: wyrzuc wyjatek "produkt nie istnieje"

        self.products.pop(i)

    def change_name(self, old, new):

        index_old = self.return_product_index_by_name(old)
        # if index_old == -1:
        # TODO: wyrzuc wyjatek "produkt nie istnieje"

        index_new = self.return_product_index_by_name(new)  # sprawdzenie czy juz taki jest
        # if index_new == -1:
        # TODO: wyrzuc wyjatek "produkt nie istnieje"

        self.products[index_old].set_name(new)

    def set_price(self, name, value):

        i = self.return_product_index_by_name(name)
        # if i == -1:
        # TODO: wyrzuc wyjatek "produkt nie istnieje"
        self.products[i].set_price(value)

    def set_amount(self, name, value):

        i = self.return_product_index_by_name(name)
        # if i == -1:
        # TODO: wyrzuc wyjatek "produkt nie istnieje"
        self.products[i].set_amount(value)

    def change_amount(self, name, value):

        i = self.return_product_index_by_name(name)
        # if i == -1:
        # TODO: wyrzuc wyjatek "produkt nie istnieje"
        self.products[i].change_amount(value)