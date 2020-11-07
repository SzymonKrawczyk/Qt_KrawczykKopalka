# Rysowanie 50 losowych linii z zachowaniem poprzednich
#
#   źródło: https://stackoverflow.com/questions/47982140/pyqt5-add-line-one-by-one-using-a-pause/47995280#47995280
#
#       Co określony czas wywołuje się onTimeout które wywołuje update, które wywołuje paintEvent
#       które wywołuje drawstepbystep
#
#       Modyfikacje:
#           06.11.2020 | Szymon Krawczyk     | Dodanie komentarzy
#           06.11.2020 | Szymon Krawczyk     | Dodanie zachowania narysowanych poprzednich linii
#           06.11.2020 | Szymon Krawczyk     | Usunięcie flagi możliwości rysowania (self.paint)
#                                            |    w ramach eksperymentu - działa
#           07.11.2020 | Szymon Krawczyk     | Dodanie metody resetującej
#           07.11.2020 | Szymon Krawczyk     | Usprawnienie kodu odpowiedzialnego za rysowanie
#           07.11.2020 | Szymon Krawczyk     | Poprawa komentarzy
#

import sys
from random import random

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.cursor = 0
        self.show()
        self.reset()

        # timer wykonuje self.onTimeout co 500ms
        timer = QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(500)

    def reset(self):
        self.cursor = 0
        self.LINES = []
        # losowanie koordynatów dla 50 linii
        for i in range(50):
            self.LINES.append([int(500 * random()), int(500 * random()), int(500 * random()), int(500 * random())])

    def onTimeout(self):  # zmienia flagę możliwości rysowania na true; wykonuje się co 500ms
        self.update()  # wywołuje paintEvent

    def paintEvent(self, e):    # żądanie odświeżenia obrazu
        painter = QPainter(self)
        self.drawstepbystep(painter)

    def drawstepbystep(self, painter): # podczas każdego wykonania wyświetla kolejną linię na podstawie wartosci z listy

        if self.cursor < len(self.LINES):  # dodaje nową linię do narysowania, jeżeli jest taka możliwość
            self.cursor += 1

        for i in range(0, self.cursor):  # gdy nie ma nowych linii, wyświetla te, które są już wyświetlone
            painter.drawLine(self.LINES[i][0], self.LINES[i][1], self.LINES[i][2], self.LINES[i][3])
