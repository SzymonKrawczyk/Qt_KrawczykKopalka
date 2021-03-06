# Plik klasy widoku głównego aplikacji, zarządzający wymianą informacji pomiędzy widokami
#
#  Główna klasa zawierająca okno z buttonem i CentralWidget, który jest podmieniany
#  w zależności który widok aktualnie powinien być wyświetlony.
#  Widoki są bezpośredno zależne od klas TitleView i GameView.
#  Button umożliwia przełączanie się pomiędzy widokami.
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           15.11.2020 | Michał Kopałka     | Utworzenie
#           16.11.2020 | Szymon Krawczyk    | Poprawa kodu; uściślenie wymagań;
#                                           |   doprecyzowanie co do działania i sposobu przekazywania informacji
#                                           |   pomiedzy widokami
#           16.11.2020 | Szymon Krawczyk    | Poprawa komentarzy
#           16.11.2020 | Szymon Krawczyk    | Dodanie przekazywania informacji pomiędzy widokami
#           16.11.2020 | Szymon Krawczyk    | Dodanie tworzenia obiektów widoków w konstruktorze
#           18.11.2020 | Michał Kopałka     | Dodanie przechodzenia między oknami
#           18.11.2020 | Szymon Krawczyk    | Naprawa błędu przy przechodzeniu na wcześniej odwiedzony widok
#           19.11.2020 | Szymon Krawczyk    | Przekazanie self do GameView
#           19.11.2020 | Michał Kopałka     | Wywołanie funkcji checkIfNewRecord() po powrocie do TitleView
#           20.11.2020 | Michał Kopałka     | Dodanie komentarzy
#           20.11.2020 | Szymon Krawczyk    | Dodanie / poprawa komentarzy
#           20.11.2020 | Szymon Krawczyk    | Usunięcie próby zapisu wyniku, jeżeli ktoś wychodzi przez końcem gry
#           02.12.2020 | Michał Kopałka     | Dodanie zmiennej settings przechowującej informację o ustawieniach
#                                           |   ostatniej uruchamianej gry w ramiach jednej sesji
#           02.12.2020 | Michał Kopałka     | Dodanie wczytywania ustawień ze zmiennej settings
#           02.12.2020 | Michał Kopałka     | Dodanie funkcji saveSettings(), loadSettings(), setGameSettings
#

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from GameView import GameView
from TitleView import TitleView
from Settings import Settings


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.GameWindow = GameView(self.startTitleWindow)   # Przekazanie metody która wraca do okna ustawień
        self.TitleWindow = TitleView()
        self.setGeometry(50, 50, 600, 800)
        self.setFixedSize(600, 900)

        self.pushButton = QPushButton('Graj', self)
        self.pushButton.move(225, 825)
        self.pushButton.resize(150, 30)

        self.nameOfTheCentralWidget = ""
        self.pushButton.clicked.connect(self.mainButtonClicked)

        self.settings = Settings()

        self.startTitleWindow()
        self.show()

    # Funkcja inicjalizująca obiekt klasy TitleView a następnie ustawiająca go jako centralny Widget
    def startTitleWindow(self):
        self.setWindowTitle("Python menu")
        self.nameOfTheCentralWidget = "TitleView"
        self.TitleWindow = TitleView()
        self.loadSettings()
        self.setCentralWidget(self.TitleWindow)
        self.pushButton.setText("Graj")
        self.show()

    # funkcja inicjalizująca obiekt klasy GameView na podstawie wyciągniętych parametrów z TitleView i wywołująca
    # funkcję newGame z GameView a następnie ustawiająca obiekt tej klasy pod centralny widget
    def startGameWindow(self):
        self.setWindowTitle("Python game screen")
        self.nameOfTheCentralWidget = "GameView"
        self.GameWindow = GameView(self.startTitleWindow)   # Przekazanie metody która wraca do okna ustawień
        self.setCentralWidget(self.GameWindow)
        self.saveSettings()
        self.setGameSettings()
        self.GameWindow.newGame()
        self.GameWindow.show()
        self.pushButton.setText("Powrót do menu")

    # funkcjia umożliwiająca zmianę widoku w zależności od parametru nameOfTheCentralWidget
    def mainButtonClicked(self):
        if self.nameOfTheCentralWidget == "TitleView":
            self.startGameWindow()
        elif self.nameOfTheCentralWidget == "GameView":
            self.startTitleWindow()

    # funkcjia umożliwiająca zapisanie stanu widgetów z TitleView do zmiennej settings
    def saveSettings(self):
        self.settings.CPS = self.TitleWindow.CPS
        self.settings.cellCount = self.TitleWindow.cellCount
        self.settings.powerups = self.TitleWindow.powerups
        self.settings.closedBox = self.TitleWindow.closedBox
        self.settings.randomWall = self.TitleWindow.randomWall

    # funkcjia umożliwiająca wczytanie parametrów ze zmiennej settings do zainicjalizowania TitleView
    def loadSettings(self):
        self.TitleWindow.CPS = self.settings.CPS
        self.TitleWindow.cellCount = self.settings.cellCount
        self.TitleWindow.powerups = self.settings.powerups
        self.TitleWindow.closedBox = self.settings.closedBox
        self.TitleWindow.randomWall = self.settings.randomWall

    # funkcjia umożliwiająca wczytanie stanu widgetów z TitleView do zainicjalizowania TitleView
    def setGameSettings(self):
        self.GameWindow.CPS = self.TitleWindow.CPS
        self.GameWindow.cellCount = self.TitleWindow.cellCount
        self.GameWindow.powerups = self.TitleWindow.powerups
        self.GameWindow.closedBox = self.TitleWindow.closedBox
        self.GameWindow.randomWall = self.TitleWindow.randomWall



if __name__ == "__main__":
    # Uruchomienie
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())