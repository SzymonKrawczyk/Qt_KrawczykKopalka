# Klasa Coords
#
#   Klasa przechowująca współrzędne x, y jako liczby całkowite
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           06.11.2020 | Szymon Krawczyk    | Utworzenie
#

class Coords:
    """Klasa przechowująca współrzędne x, y w liczbach całkowitych"""

    # Właściwości
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = int(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = int(value)

    # Metody
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def copyCoords(self, coordsObj): # Metoda kopiująca
        self.x = coordsObj.x
        self.y = coordsObj.y
