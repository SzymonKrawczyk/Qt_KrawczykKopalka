# Plik przykładowy
#
#  Główna klasa zawierająca okno z CentralWidget który jest podmieniany
#  w zależności który widok aktóalnie powinien być wyświetlony ( metody
#  startGameWindow i startTitleWindow )
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           15.11.2020 | Michał Kopałka     | Utworzenie
#
#           TODO: upewnić się co do działania przekazywania danych pomiędzy menu a grą
#

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Projekt.Szablony.GameView import GameView
from Projekt.Szablony.TitleView import TitleView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 600, 800)
        self.setFixedSize(600, 800)
        self.startTitleWindow()

    def startGameWindow(self):
        list = self.Window.getSettings()
        #print(list)
        self.Window = GameView()
        self.setWindowTitle("Python game screen")
        self.setCentralWidget(self.Window)
        #self.Window.setGameSettings(list)
        self.show()
        self.Window.newGame()

    def startTitleWindow(self):
        self.Window = TitleView()
        self.setWindowTitle("Python menu")
        self.setCentralWidget(self.Window)
        self.Window.pushButton.clicked.connect(self.startGameWindow)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
