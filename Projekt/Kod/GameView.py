# Klasa QWidgetu gry
#
#   TODO Opis pliku, klas i metod w nim zawieranych
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#  Plik początkowo wygenerowany:
#   -*- coding: utf-8 -*-
#   Form implementation generated from reading ui file 'gameView2.ui'
#
#   Created by: PyQt5 UI code generator 5.15.1
#
#
#           11.11.2020 | Szymon Krawczyk    | Utworzenie
#           12.11.2020 | Szymon Krawczyk    | Rysowanie v1:
#                                           |   Rysowanie bezpośrednio na GameView, usunięcie myCanvas
#                                           |       (prostsze rozwiązanie na chwilę obecną)
# TODO cleanup!!!

#   Legenda oznaczeń wewnątrz macierzy komórek
#       0-puste
#       1-jedzenie
#       2-super jedzenie
#       7-ściana


import sys
from random import randrange

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class GameView(QWidget):

    # Właściwości

    # Nowy kierunek ruchu
    @property
    def newDirection(self):
        return self._newDirection

    @newDirection.setter
    def newDirection(self, value):
        if value != "N" and value != "E" and value != "W" and value != "S" and value != "":
            raise ValueError
        self._newDirection = value

    # Ilość ruchów na sekundę (szybkość gry) - musi być w przedziale <1; 10>
    @property
    def CPS(self):
        return self._CPS

    @CPS.setter
    def CPS(self, value):
        if value < 1 or value > 10:
            raise ValueError
        self._CPS = value

    # Ilość komórek na ekranie gry (bok) - musi być nieparzystyi w przedziale <11; 31>
    @property
    def cellCount(self):
        return self._cellCount

    @cellCount.setter
    def cellCount(self, value):
        if value % 2 == 0 or value < 11 or value > 41:
            raise ValueError
        self._cellCount = value

    # Opcja - czy generować powerUpy
    @property
    def powerups(self):
        return self._powerups

    @powerups.setter
    def powerups(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._powerups = value

    # Opcja - czy obszar gry ma być otoczony ścianą
    @property
    def closedBox(self):
        return self._closedBox

    @closedBox.setter
    def closedBox(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._closedBox = value

    # Opcja - czy generować losową ścianę w środku gry
    @property
    def randomWall(self):
        return self._randomWall

    @randomWall.setter
    def randomWall(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._randomWall = value

    def __init__(self):
        super().__init__()

        # Deklaracja pól
        self.newDirection = ""
        self.CPS = 1
        self.cellCount = 21
        self.powerups = True
        self.closedBox = True
        self.randomWall = True
        self.__gameMatrix = []
        self.__paintFlag = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimeout)

        # UI wygenerowane automatycznie
        self.width = 600
        self.height = 800
        self.setFixedSize(self.width, self.height)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 440, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scoreHigh = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.scoreHigh.setFont(font)
        self.scoreHigh.setObjectName("scoreHigh")
        self.verticalLayout_2.addWidget(self.scoreHigh)

        self.scoreCurrent = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.scoreCurrent.setFont(font)
        self.scoreCurrent.setObjectName("scoreCurrent")

        self.verticalLayout_2.addWidget(self.scoreCurrent)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # self.myCanvas = QtWidgets.QWidget(self)
        self.cellWidth = int(500 / self.cellCount)
        self.myCanvasSize = self.cellWidth * self.cellCount
        self.myCanvasPaddingX = (self.width-self.myCanvasSize)/2
        self.myCanvasPaddingY = 100
        # self.myCanvas.setGeometry(QtCore.QRect(int(tempPaddingX), 100, self.myCanvasSize, self.myCanvasSize))
        # self.myCanvas.setObjectName("myCanvas")

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 610, 239, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.arrRight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrRight.setObjectName("arrRight")
        self.arrRight.clicked.connect(self.arrRightClicked)
        self.gridLayout.addWidget(self.arrRight, 1, 2, 1, 1)

        self.arrUp = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrUp.setObjectName("arrUp")
        self.arrUp.clicked.connect(self.arrUpClicked)
        self.gridLayout.addWidget(self.arrUp, 0, 1, 1, 1)

        self.arrLeft = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrLeft.setObjectName("arrLeft")
        self.arrLeft.clicked.connect(self.arrLeftClicked)
        self.gridLayout.addWidget(self.arrLeft, 1, 0, 1, 1)

        self.arrDown = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrDown.setObjectName("arrDown")
        self.arrDown.clicked.connect(self.arrDownClicked)
        self.gridLayout.addWidget(self.arrDown, 2, 1, 1, 1)

        # Ustawienie pól i elementów UI domyślnie
        self.hardReset()

    def hardReset(self):
        self.label_3.setText("HIGH SCORE")
        self.label_4.setText("SCORE")
        self.scoreHigh.setText("999999")
        self.scoreCurrent.setText("000009")
        self.arrRight.setText(">")
        self.arrUp.setText("^")
        self.arrLeft.setText("<")
        self.arrDown.setText("v")

        self.newDirection = ""
        self.CPS = 1
        self.cellCount = 21
        self.powerups = True
        self.closedBox = True
        self.randomWall = True
        self.__gameMatrix = []

        self.cellWidth = int(500 / self.cellCount)
        self.myCanvasSize = self.cellWidth * self.cellCount
        self.myCanvasPaddingX = (self.width - self.myCanvasSize) / 2
        self.myCanvasPaddingY = 100

        self.__paintFlag = True
        self.timer.stop()

    def newGame(self):
        self.timer.stop()

        self.__gameMatrix = []
        for i in range(self._cellCount):
            temp = []
            for j in range(self._cellCount):
                temp.append(0)
            self.__gameMatrix.append(temp)

        if self.closedBox:
            for i in range(self._cellCount):
                self.__gameMatrix[i][0] = 7
                self.__gameMatrix[0][i] = 7
                self.__gameMatrix[i][self.cellCount-1] = 7
                self.__gameMatrix[self.cellCount-1][i] = 7

        if self.randomWall:
            randY1 = randrange(3, int(self.cellCount/2))
            randY2 = randrange(int(self.cellCount/2)+1, self.cellCount-3)
            for i in range(self._cellCount-6):
                self.__gameMatrix[i+3][randY1] = 7
                self.__gameMatrix[i+3][randY2] = 7

        self.timer.start(int(1000/self.CPS))

    def onTimeout(self):
        self.__paintFlag = True
        self.update()

    def paintEvent(self, e):
        if self.__paintFlag:
            print("paint")

            # Kolory TODO self?
            backgroundColor = QColor(153, 204, 255)
            wallColor = QColor(0, 0, 0)

            # Dla uproszczenia i skrócenia dalszej części
            width = self.myCanvasSize
            x0 = int(self.myCanvasPaddingX)
            xn = int(x0 + width)
            y0 = int(self.myCanvasPaddingY)
            yn = int(y0 + width)

            painter = QPainter(self)

            painter.setBrush(backgroundColor)
            painter.setPen(Qt.NoPen)  # rysowanie bez krawędzi
            painter.drawRect(x0, y0, width, width)

            for i in range(self._cellCount):
                for j in range(self._cellCount):
                    if self.__gameMatrix[i][j] == 7:
                        painter.setBrush(wallColor)
                    elif self.__gameMatrix[i][j] == 1:
                        # kolor = czerwony
                        pass
                    elif self.__gameMatrix[i][j] == 2:
                        # kolor = pomarańczowy
                        pass
                    else:
                        painter.setBrush(backgroundColor)
                    painter.drawRect(int(x0+(i*self.cellWidth)), int(y0+(j*self.cellWidth)), int(self.cellWidth), int(self.cellWidth))

        self.__paintFlag = False

    def arrRightClicked(self):
        self.newDirection = "E"
        print(self.newDirection)

    def arrUpClicked(self):
        self.newDirection = "N"
        print(self.newDirection)

    def arrLeftClicked(self):
        self.newDirection = "W"
        print(self.newDirection)

    def arrDownClicked(self):
        self.newDirection = "S"
        print(self.newDirection)


# test
# TODO Usunąć
app = QApplication(sys.argv)
interface = GameView()
interface.show()
interface.newGame()
sys.exit(app.exec_())
