# Klasa Snake
#
#   Klasa przechowująca informacje o wężu i implementująca poruszanie się węża po macierzy xy
#   TODO dodać informacje o obsłudze klasy
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           06.11.2020 | Szymon Krawczyk    | Utworzenie
#           11.11.2020 | Szymon Krawczyk    | Poprawienie setterów - wyrzucanie wyjątków
#           14.11.2020 | Szymon Krawczyk    | Usunięcie testowania działania
#           14.11.2020 | Szymon Krawczyk    | Poprawa błędu krytycznego w poruszaniu ogonem gdy jest pusty
#           16.11.2020 | Szymon Krawczyk    | Usunięcie właściwości przechowujących kolory
#
from PyQt5.QtGui import QColor

from Coords import Coords


class Snake:
    """Klasa przechowująca informacje o wężu"""

    # Pola i właściwości

    # Głowa węża
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        if not isinstance(value, Coords):
            raise ValueError
        self._head = value

    # Tablica z ogonem
    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        if not isinstance(value, list):
            raise ValueError
        self._tail = value

    # Obecny kierunek ruchu
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if value != "N" and value != "E" and value != "W" and value != "S" and value != "":
            raise ValueError
        self._direction = value

    # # Kolor głowy węża
    # @property
    # def headColor(self):
    #     return self._headColor
    #
    # @headColor.setter
    # def headColor(self, value):
    #     if not isinstance(value, QColor):
    #         raise ValueError
    #     self._headColor = value
    #
    # # Kolor ogonu węża
    # @property
    # def tailColor(self):
    #     return self._tailColor
    #
    # @tailColor.setter
    # def tailColor(self, value):
    #     if not isinstance(value, QColor):
    #         raise ValueError
    #     self._tailColor = value

    # Metody
    def __init__(self):
        self.head = Coords()
        self.tail = []
        self.direction = ""
        # self.headColor = QColor(0, 100, 0)
        # self.tailColor = QColor(0, 128, 0)

    # True, jeżeli wąż "się zjadł"; w pozostałych przypadkach False
    def checkTailCollision(self):
        error = False
        for i in self.tail:
            if i == self.head:
                error = True
                break
        return error

    # Ruch 'normalny' ciała węża - ostatnia pozycja przyjmuję pozycję wcześniejszej itd + ruch głowy
    def tailMove(self):
        n = len(self.tail)-1
        if n >= 0:
            for element in range(n):
                self.tail[n-element].copyCoords(self.tail[n-(element+1)])
            self.tail[0].copyCoords(self.head)
        self.headMove()

    # Ruch ciała węża po jedzeniu - brak ruchu, zwiększenie ciała w pozycji głowy i ruch głowy
    def tailMoveEating(self):
        temp = Coords()
        temp.copyCoords(self.head)
        self.tail.insert(0, temp)
        self.headMove()

    # Ruch głowy w zależności od kierunku
    def headMove(self):
        if self.direction == "N":
            self.head.y -= 1
        elif self.direction == "E":
            self.head.x += 1
        elif self.direction == "W":
            self.head.x -= 1
        elif self.direction == "S":
            self.head.y += 1
