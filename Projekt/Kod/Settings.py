# Klasa Settings
#
#   Klasa przechowująca ustawienia rozgrywki potrzebne służące do zapamiętywania stanu Widgetów z TitleView
#
#   Interface publiczny, czyli jak korzystać z klasy:
#
#       Konstruktor:
#           Nie przyjmuje argumentów
#
#       Właściwości:
#           CPS         - określa ilość operacji / kroków / klatek na sekundę [1; 10].
#           cellCount   - określa długość boku pola rozgrywki (ilość komórek) [11; 41 | nieparzysta].
#           powerups    - określa czy ma się pojawiać jedzenie, które po zjedzeniu daje dwukrotne przyspieszenie
#                         gry.
#           closedBox   - określa czy na obrzeżach pola gry mają być ściany.
#           randomWall  - określa czy w polu rozgrywki mają być losowe ściany.
#
#       Metody:
#           str(Settings) - zwraca string wypisujący wszystkie właściwości
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           02.12.2020 | Michał Kopałka     | Utworzenie
#           02.12.2020 | Michał Kopałka     | Dodanie komentarzy
#           02.12.2020 | Michał Kopałka     | Dodanie metody str
#

class Settings:
    """Klasa przechowująca właściwości potrzebne do inicjalizacji TitleView"""

    # Właściwości
    @property
    def CPS(self):
        return self._CPS

    @CPS.setter
    def CPS(self, value):
        if value < 1 or value > 10:
            raise ValueError
        self._CPS = value

    @property
    def cellCount(self):
        return self._cellCount

    @cellCount.setter
    def cellCount(self, value):
        if value % 2 == 0 or value < 11 or value > 41:
            raise ValueError
        self._cellCount = value

    @property
    def powerups(self):
        return self._powerups

    @powerups.setter
    def powerups(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._powerups = value

    @property
    def closedBox(self):
        return self._closedBox

    @closedBox.setter
    def closedBox(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._closedBox = value

    @property
    def randomWall(self):
        return  self._randomWall

    @randomWall.setter
    def randomWall(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._randomWall = value

    # Metody
    def __init__(self):
        self.CPS = 5
        self.cellCount = 25
        self.powerups = False
        self.closedBox = False
        self.randomWall = False

    def __str__(self):
        return (f"CPS = {self.CPS} \n" +
                f"cellCount = {self.cellCount}\n" +
                f"powerups = {self.powerups}\n" +
                f"closedBox = {self.closedBox}\n" +
                f"randomWall = {self.randomWall}\n")
