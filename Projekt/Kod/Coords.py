# Klasa Coords
#
#   Klasa przechowująca współrzędne x, y jako liczby całkowite
#
#   Interface publiczny, czyli jak korzystać z klasy:
#
#       Konstruktor:
#           Klasa przymuje dwa argumenty typu int reprezentujące wartości współrzędnych x i y.
#           W przypadku niepodania argumentów, domyślne wartości to (0; 0)
#
#       Właściwości:
#           x   - przechowuje wartość współrzędnej x
#           y   - przechowuje wartość współrzędnej y
#
#       Metody:
#           copyCoords(Coords)  - kopiuje wartości pól obiektu typu Coords przekazanego w argumencie
#           Coords == Coords    - True, jeżeli wartości pól x, y są takie same
#           str(Coords)         - zwraca string w postaci: (x, y)
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           06.11.2020 | Szymon Krawczyk    | Utworzenie
#           29.11.2020 | Szymon Krawczyk    | Dodanie komentarzy
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
        return self.x == other.x and self.y == other.y

    def copyCoords(self, coordsObj):  # Metoda kopiująca
        self.x = coordsObj.x
        self.y = coordsObj.y
