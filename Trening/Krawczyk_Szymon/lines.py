# Rysowanie 50 losowych linii z zachowaniem poprzednich
#
#   źródło: https://stackoverflow.com/questions/47982140/pyqt5-add-line-one-by-one-using-a-pause/47995280#47995280
#
#       Co określony czas wywołuje się onTimeout które wywołuje update, które wywołuje paintEvent
#       które wywołuje drawstepbystep
#
#       Modyfikacje:
#           06 11 2020 - Szymon Krawczyk:
#                           dodanie komentarzy
#                           dodanie zachowania narysowanych poprzednich linii
#                           usunięcie flagi możliwości rysowania (self.paint) w ramach eksperymentu - działa
#

import sys
from random import random

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication


LINES = []
# losowanie koordynatów dla 50 linii
for i in range(50):
    LINES.append([int(500*random()), int(500*random()), int(500*random()), int(500*random())])


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.cursor = 0
        self.show()
        self.indexes = []

        # self.paint = True

        # timer wykonuje self.onTimeout co 500ms
        timer = QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(500)

    def onTimeout(self):  # zmienia flagę możliwości rysowania na true; wykonuje się co 500ms
        # self.paint = True
        self.update()  # wywołuje paintEvent

    def paintEvent(self, e):    # żądanie odświeżenia obrazu
        # if self.paint:  # jeżeli jest flaga możliwości rysowania, wykonaj drawstepbystep
        painter = QPainter(self)
        self.drawstepbystep(painter)

    def drawstepbystep(self, painter): # podczas każdego wykonania wyświetla kolejną linię na podstawie wartosci z listy

        if self.cursor < len(LINES):  # dodaje nową linię do narysowania, jeżeli jest taka możliwość
            self.indexes.append(self.cursor)
            self.cursor += 1

        for i in self.indexes:  # gdy nie ma nowych linii, wyświetla te, które są już wyświetlone
            painter.drawLine(LINES[i][0], LINES[i][1], LINES[i][2], LINES[i][3])

        # self.paint = False  # zmiana informacji o możliwości rysowania na false,
                            # będzie można rysować gdy wywoła się onTimeout


app = QApplication(sys.argv)
interface = Interface()
sys.exit(app.exec_())
