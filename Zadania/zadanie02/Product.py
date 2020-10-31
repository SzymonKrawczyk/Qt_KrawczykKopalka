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



class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongTypeOfVariableInNameError(Exception):
    """Klasa służąca do wyświetlania błędu przy podaniu złego typu dla zmiennej name"""
    def __init__(self, variable):
        self.typeOFVariable = type(variable).__name__
        self.message = "Zły typ danych dla zmiennej name. Oczekiwano str a dostano: " + self.typeOFVariable
        print(self.message)
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message)


class WrongTypeOfVariableInPriceError(Error):
    """Klasa służąca do wyświetlania błędu przy podaniu złego typu dla zmiennej price"""
    def __init__(self, variable):
        self.typeOFVariable = type(variable).__name__
        self.message = "Zły typ danych dla zmiennej price. Oczekiwano int/float a dostano :" + self.typeOFVariable
        print(self.message)
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message)


class WrongTypeOfVariableInAmountError(Error):
    """Klasa służąca do wyświetlania błędu przy podaniu złego typu dla zmiennej amount"""
    def __init__(self, variable):
        self.typeOFVariable = type(variable).__name__
        self.message = "Zły typ danych dla zmiennej amount. Oczekiwano int a dostano: " + self.typeOFVariable
        print(self.message)
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message)


class WrongValueOfVariablePriceError(Error):
    """Klasa służąca do wyświetlania błędu przy podaniu wartości mniejszej od 0 dla zmiennej price"""
    def __init__(self, variable):
        self.variable = variable
        self.message = "Zmienna price nie może mieć wartości ujemnej. Próbowana przypisać wartość:"
        print(f"{self.message} {self.variable}")
        super().__init__(self.message)


class WrongValueOfVariableAmountError(Error):
    """Klasa służąca do wyświetlania błędu przy podaniu wartości mniejszej od 0 dla zmiennej amount"""
    def __init__(self, variable):
        self.variable = variable
        self.message = "Zmienna Amount nie może mieć wartości ujemnej. Próbowana przypisać wartość:"
        print(f"{self.message} {self.variable}")
        super().__init__(self.message)


class Product:
    """Klasa przechowuje informacje o produktcie"""

    # Zmienne
    name = ""
    price = -1.0
    amount = -1

    def __init__(self, name=None, price=None, amount=None):

        if not isinstance(name, str):

            raise WrongTypeOfVariableInNameError(name)
        if not isinstance(price, (int, float)):
            raise WrongTypeOfVariableInPriceError(price)
        if not isinstance(amount, int):
            raise WrongTypeOfVariableInAmountError(amount)

        if price < 0:
            raise WrongValueOfVariablePriceError(price)
        if amount < 0:
            raise WrongValueOfVariableAmountError(amount)

        self.name = name
        self.price = price
        self.amount = amount


        # try:
        #     if not isinstance(name, str):
        #         raise WrongTypeOfVariableInNameError(name)
        #     if not isinstance(price, (int, float)):
        #         raise WrongTypeOfVariableInPriceError(price)
        #     if not isinstance(amount, int):
        #         raise WrongTypeOfVariableInAmountError(amount)
        #
        #     if price < 0:
        #         raise WrongValueOfVariablePriceError(price)
        #     if amount < 0:
        #         raise WrongValueOfVariableAmountError(amount)
        #
        #     self.name = name
        #     self.price = price
        #     self.amount = amount
        # except WrongTypeOfVariableInNameError:
        #     print("hej2")
        # except Exception:
        #     pass

    def __str__(self):

        return f"\"{self.name}\", ${self.price}, Amount: {self.amount}"

    def set_name(self, value):
        if not isinstance(value, str):
            raise WrongTypeOfVariableInNameError(value)
        else:
            self.name = value

    def set_price(self, value):
        try:
            if not isinstance(value, (int, float)):
                raise WrongTypeOfVariableInPriceError(value)
            if value < 0:
                raise WrongValueOfVariablePriceError(value)

            self.price = value
        except Exception:
            pass

    def set_amount(self, value):
        try:
            if not isinstance(value, int):
                raise WrongTypeOfVariableInAmountError(value)
            if value < 0:
                raise WrongValueOfVariableAmountError(value)
            self.amount = value
        except Exception:
            pass

    def change_amount(self, value):
        try:
            if not isinstance(value, int):
                raise WrongTypeOfVariableInAmountError(value)
            if (self.amount+value) < 0:
                raise WrongValueOfVariableAmountError(self.amount+value)
            self.amount += value
        except Exception:
            pass


