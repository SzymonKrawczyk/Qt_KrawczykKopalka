# Klasy wyjatkow do klas Product i Shelf
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#   Data utworzenia: 31.10.2020
#
#       Modyfikacje:
#           01.11.2020 | Szymon Krawczyk    | Przeniesienie wyjatkow do osobnego pliku
#           01.11.2020 | Szymon Krawczyk    | Uproszczenie wyjatkow
#

class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongTypeOfVariable(Exception):
    """Klasa służąca do wyświetlania błędu przy podaniu złego typu dla zmiennej name"""
    pass


class WrongValueOfVariable(Exception):
    """Klasa służąca do wyświetlania błędu przy podaniu wartości mniejszej od 0 dla zmiennej price"""
    pass


class ProductAlreadyExistsError(Exception):
    """Klasa służąca do wyświetlania błędu przy probie dodania już istniejącego produktu"""
    pass


class ProductDoesNotExistError(Exception):
    """Klasa służąca do wyświetlania błędu przy probie odwołania się do nie istniejącego produktu"""
    pass
