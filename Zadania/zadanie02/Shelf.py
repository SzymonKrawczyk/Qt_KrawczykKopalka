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
#
#       Modyfikacje:
#           31.10.2020 | Michał Kopałka     | Utworzenie wyjatkow
#           01.11.2020 | Szymon Krawczyk    | Przeniesienie wyjatkow do osobnego pliku
#           01.11.2020 | Szymon Krawczyk    | Usuniecie blokow try
#


import Product
from MyExceptions import WrongTypeOfVariable
from MyExceptions import WrongValueOfVariable
from MyExceptions import ProductAlreadyExistsError
from MyExceptions import ProductDoesNotExistError


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
        if not isinstance(name, str):
            raise WrongTypeOfVariable()
        else:
            index = -1
            for i in range(len(self.products)):
                if self.products[i].name.lower() == name.lower():
                    index = i
                    break
            return index

    def new_product(self, name, price=-1.0, amount=-1):
        if self.return_product_index_by_name(name) != -1:
            raise ProductAlreadyExistsError()

        product = Product.Product(name, price, amount)  # mozliwe WrongTypeOfVariable oraz WrongValueOfVariable
        self.products.append(product)

    def remove_product(self, name):
        i = self.return_product_index_by_name(name)
        if i == -1:
            raise ProductDoesNotExistError
        self.products.pop(i)

    def change_name(self, old, new):
        index_old = self.return_product_index_by_name(old)
        index_new = self.return_product_index_by_name(new)
        if index_old == -1:
            raise ProductDoesNotExistError
        if index_new != -1:
            raise ProductAlreadyExistsError
        self.products[index_old].set_name(new)      # mozliwe WrongTypeOfVariable

    def set_price(self, name, value):
        i = self.return_product_index_by_name(name)
        if i == -1:
            raise ProductDoesNotExistError
        self.products[i].set_price(value)           # mozliwe WrongTypeOfVariable oraz WrongValueOfVariable

    def set_amount(self, name, value):
        i = self.return_product_index_by_name(name)
        if i == -1:
            raise ProductDoesNotExistError
        self.products[i].set_amount(value)          # mozliwe WrongTypeOfVariable oraz WrongValueOfVariable

    def change_amount(self, name, value):
        i = self.return_product_index_by_name(name)
        if i == -1:
            raise ProductDoesNotExistError
        self.products[i].change_amount(value)       # mozliwe WrongTypeOfVariable oraz WrongValueOfVariable
