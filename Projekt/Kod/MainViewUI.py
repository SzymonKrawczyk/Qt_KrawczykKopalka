# Plik widoku głównego aplikacji, zarządzający wymianą informacji pomiędzy widokami
#
#  Główna klasa zawierająca okno z CentralWidget który jest podmieniany
#  w zależności który widok aktóalnie powinien być wyświetlony ( metody
#  startGameWindow i startTitleWindow )
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
#


import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic.properties import QtWidgets

from GameView import GameView
from TitleView import TitleView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.GameWindow = GameView(self)
        self.TitleWindow = TitleView()
        self.setGeometry(50, 50, 600, 800)
        self.setFixedSize(600, 900)

        self.pushButton = QPushButton('Graj', self)
        self.pushButton.move(225, 825)
        self.pushButton.resize(150, 30)

        self.nameOfTheCentralWidget = ""
        self.pushButton.clicked.connect(self.mainButtonClicked)

        self.startTitleWindow()
        self.show()

    def startTitleWindow(self):
        self.setWindowTitle("Python menu")
        self.nameOfTheCentralWidget = "TitleView"
        self.TitleWindow = TitleView()
        self.setCentralWidget(self.TitleWindow)
        self.pushButton.setText("Graj")
        #self.show()

    def startGameWindow(self):
        self.setWindowTitle("Python game screen")
        self.nameOfTheCentralWidget = "GameView"
        self.GameWindow = GameView(self)
        self.setCentralWidget(self.GameWindow)
        self.GameWindow.CPS = self.TitleWindow.CPS
        self.GameWindow.cellCount = self.TitleWindow.cellCount
        self.GameWindow.powerups = self.TitleWindow.powerups
        self.GameWindow.closedBox = self.TitleWindow.closedBox
        self.GameWindow.randomWall = self.TitleWindow.randomWall
        self.GameWindow.newGame()
        self.GameWindow.show()
        self.pushButton.setText("Powrót do menu")

    def mainButtonClicked(self):
        if self.nameOfTheCentralWidget == "TitleView":
            self.startGameWindow()
        elif self.nameOfTheCentralWidget == "GameView":
            # self.GameWindow.endGame()
            self.startTitleWindow()


# Uruchomienie
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
