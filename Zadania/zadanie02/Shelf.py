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


class ProductAlreadyExistError(Exception):
    """Klasa służąca do wyświetlania błędu przy prubie dodania już istniejącego produktu"""
    def __init__(self, variable):
        self.message = "Produkt: " + variable + " już istnieje"
        print(self.message)
        super().__init__(self.message)

class ProductDoNotExistError(Exception):
    """Klasa służąca do wyświetlania błędu przy prubie odwołania się do nie istniejącego produktu"""
    def __init__(self, variable):
        self.message = "Produkt: " + variable + " nie istnieje"
        print(self.message)
        super().__init__(self.message)


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

        # TODO: nie jestem pewny czy o coś takiego mogło ci chodzić ( wykorzystałem sobie już istniejący wyjątek z Product.py )

        if not isinstance(name, str):
            raise Product.WrongTypeOfVariableInNameError(name)
        else:
            index = -1
            for i in range(len(self.products)):
                if self.products[i].name.lower() == name.lower():
                    index = i
                    break
            return index

    def new_product(self, name, price=-1.0, amount=-1):
        if self.return_product_index_by_name(name) != -1:
           raise ProductAlreadyExistError(name)

        product = Product.Product(name, price, amount)
        self.products.append(product)



    def remove_product(self, name):
        try:
            i = self.return_product_index_by_name(name)
            if i == -1:
                raise ProductDoNotExistError
            self.products.pop(i)
        except Exception:
            pass

    def change_name(self, old, new):
        try:
            index_old = self.return_product_index_by_name(old)
            index_new = self.return_product_index_by_name(new)
            if index_old == -1:
                raise ProductDoNotExistError
            if index_new == -1:
                raise ProductAlreadyExistError
            self.products[index_old].set_name(new)
        except Exception:
            pass

    def set_price(self, name, value):
        try:
            i = self.return_product_index_by_name(name)
            if i == -1:
                raise ProductDoNotExistError
            self.products[i].set_price(value)
        except Exception:
            pass

    def set_amount(self, name, value):
        try:
            i = self.return_product_index_by_name(name)
            if i == -1:
                raise ProductDoNotExistError
            self.products[i].set_amount(value)
        except Exception:
            pass

    def change_amount(self, name, value):
        try:
            i = self.return_product_index_by_name(name)
            if i == -1:
                raise ProductDoNotExistError
            self.products[i].change_amount(value)
        except Exception:
            pass
