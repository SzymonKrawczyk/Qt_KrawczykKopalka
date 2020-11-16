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
#

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from GameView import GameView
from TitleView import TitleView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.GameWindow = GameView()
        self.TitleWindow = TitleView()
        self.setGeometry(50, 50, 600, 800)
        self.setFixedSize(600, 800)
        self.startTitleWindow()
        self.show()

    def startTitleWindow(self):
        self.setWindowTitle("Python menu")
        self.setCentralWidget(self.TitleWindow)
        self.TitleWindow.pushButton.clicked.connect(self.startGameWindow)
        # self.show()

    def startGameWindow(self):
        self.setWindowTitle("Python game screen")
        self.setCentralWidget(self.GameWindow)
        # TODO fix TitleWindow sliders
        self.GameWindow.CPS = self.TitleWindow.CPS
        self.GameWindow.cellCount = self.TitleWindow.cellCount
        self.GameWindow.powerups = self.TitleWindow.powerups
        self.GameWindow.closedBox = self.TitleWindow.closedBox
        self.GameWindow.randomWall = self.TitleWindow.randomWall
        self.GameWindow.newGame()
        self.GameWindow.show()


# Uruchomienie
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
