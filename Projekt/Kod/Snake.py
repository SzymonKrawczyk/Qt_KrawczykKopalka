# Klasa Snake
#
#   Klasa przechowująca informacje o wężu
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           06.11.2020 | Szymon Krawczyk    | Utworzenie
#           11.11.2020 | Szymon Krawczyk    | Poprawienie setterów - wyrzucanie wyjątków
#

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

    # TODO właściwość koloru ogona i głowy - QColor ?
    # Metody
    def __init__(self):
        self.head = Coords()
        self.tail = []
        self.direction = ""

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
        if self._direction == "N":
            self.head.y -= 1
        elif self._direction == "E":
            self.head.x += 1
        elif self._direction == "W":
            self.head.x -= 1
        elif self._direction == "S":
            self.head.y += 1


# Test
# TODO Usunąć
temp = Snake()
temp.direction = "E"
temp.head.x = 1
temp.head.y = 1
for i in range(0, 10):
    print(i)
    temp.tailMoveEating()
    print(f"H {temp.head}")
    for j in temp.tail:
        print(j)
    print()
print()
print()
temp.direction = "S"
for i in range(0, 10):
    temp.tailMove()
    print(f"H {temp.head}")
    for j in temp.tail:
        print(j)
    print()
