# Klasa QWidgetu gry Snake
#
#   Interface publiczny, czyli jak korzystać z klasy:
#       Właściwości:
#           newDirection    - pozwala na zmianę kierunku poruszania się węża, jeżeli nie jest to kierunek przeciwny
#                             do obecnego. Przyjmuje wartości "N", "E", "W", "S", ""
#           CPS             - określa ilość operacji / kroków / klatek na sekundę [1; 10].
#                             Po zmianie należy wywołać newGame()
#           cellCount       - określa długość boku pola rozgrywki (ilość komórek) [11; 41 | nieparzysta].
#                             Po zmianie należy wywołać newGame()
#           powerups        - określa czy ma się pojawiać jedzenie, które po zjedzeniu daje dwukrotne przyspieszenie
#                             gry. Po zmianie należy wywołać newGame()
#           closedBox       - określa czy na obrzeżach pola gry mają być ściany. Po zmianie należy wywołać newGame()
#           randomWall      - określa czy w polu rozgrywki mają być losowe ściany. Po zmianie należy wywołać newGame()
#
#       Metody:
#           newGame()       - rozpoczyna nową grę z obecnymi ustawieniami
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
#           14.11.2020 | Szymon Krawczyk    | Wyczyszczenie kodu
#           14.11.2020 | Szymon Krawczyk    | Usunięcie metody hardReset na próbę (nie wydaje się potrzebna)
#           14.11.2020 | Szymon Krawczyk    | Dodanie poruszania się węża
#           14.11.2020 | Szymon Krawczyk    | Rysowanie v2: Rysowanie węża i jego ogonu
#           16.11.2020 | Szymon Krawczyk    | Przeniesienie kolorów z klasy Snake tutaj
#           16.11.2020 | Szymon Krawczyk    | Dodanie funkcjonalności 'zawijania' się planszy
#                                           |   (teleportacji z jednej strony na drugą)
#           16.11.2020 | Szymon Krawczyk    | Poprawa błędu krytycznego - wielkość rysowania przy zmianie długości boku
#           17.11.2020 | Szymon Krawczyk    | Dodanie spawnowania jedzenia na wolnych miejscach
#           17.11.2020 | Szymon Krawczyk    | Poprawa efektywności rysowania; zmiana rysowania jedzenia na koła
#           17.11.2020 | Szymon Krawczyk    | Przeniesienie kolorów węża jako stałe poza klasą (usunąć?)
#           17.11.2020 | Szymon Krawczyk    | Dodanie funkcjonalności przyspieszenia gry i zmiany koloru węża
#           18.11.2020 | Michał Kopałka     | Dodanie obsługi klawiszy
#           18.11.2020 | Michał Kopałka     | Dodanie okna informującego o przegranej grze
#           18.11.2020 | Michał Kopałka     | Dodanie funkcji endGame zatrzymującej wszystkie QTimery i onPress keyboard
#           18.11.2020 | Szymon Krawczyk    | Usunięcie endGame()
#           18.11.2020 | Szymon Krawczyk    | Dodanie grania ponownej gry po przegraniu
#           18.11.2020 | Szymon Krawczyk    | Poprawa generacji losowych ścian
#           19.11.2020 | Szymon Krawczyk    | Dodanie strzałek jako sterowania alternatywnego
#           19.11.2020 | Szymon Krawczyk    | Dodanie możliwości powrotu do menu / rozpoczęcia nowej gry po zakończeniu
#           19.11.2020 | Szymon Krawczyk    | Dodanie możliwości wygrania poprzez zajęcie wężem wszystkich pól poza 2
#           19.11.2020 | Szymon Krawczyk    | Poprawienie systemu zakańczania gry
#           19.11.2020 | Szymon Krawczyk    | Dodanie balansu ustawień i wyniku -> trudniej = większy mnożnik punktów
#           19.11.2020 | Szymon Krawczyk    | Dodanie komentarzy
#           19.11.2020 | Michał Kopałka     | Dodanie odczytu i zapisu highscore z pliku
#           19.11.2020 | Michał Kopałka     | Przeniesienie sprawdzania i zapisu wyniku do osobnej funkcji
#           20.11.2020 | Michał Kopałka     | Zmiana sposobu rysowania super jedzenia
#           20.11.2020 | Michał Kopałka     | Dodanie gradientu do ogona
#           20.11.2020 | Michał Kopałka     | Dodanie przekazywania metody powrotu do menu jako parametr konstruktora
#

#   Legenda oznaczeń wewnątrz macierzy komórek
#       0-puste
#       1-jedzenie
#       2-super jedzenie
#       7-ściana
#

from random import randrange

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow

from Snake import Snake
import keyboard

# Stałe kolorów
NORMAL_HEADCOLOR = QColor(0, 100, 0)
NORMAL_TAILCOLOR = QColor(0, 128, 0)
BOOST_TAILCOLOR = QColor(252, 172, 71)
BOOST_HEADCOLOR = QColor(245, 138, 27)


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

    # Ilość ruchów na sekundę (szybkość gry) - musi być w przedziale
    @property
    def CPS(self):
        return self._CPS

    @CPS.setter
    def CPS(self, value):
        if value < 1 or value > 10:
            raise ValueError
        self._CPS = value

    # Ilość komórek na ekranie gry (bok) - musi być nieparzysty i w przedziale
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

    def __init__(self, exitMethod = None):
        super().__init__()

        # Deklaracja pól i wartości domyślne
        self.newDirection = ""
        self.CPS = 2
        self.cellCount = 21
        self.powerups = True
        self.closedBox = True
        self.randomWall = True

        self.gameMatrix = []    # Plansza / obszar gry
        self.paintFlag = True   # Flaga pomocnicza; jeśli True to rysuje się plansza

        self.Python = Snake()   # Obiekt klasy Snake
        # Kolory inicjalizowane domyślnie kolorami podstawowymi
        self.snakeTailColor = NORMAL_TAILCOLOR
        self.snakeHeadColor = NORMAL_HEADCOLOR

        self.score = 0
        self.gameOver = False   # Pole z informacją czy gracz nadal żyje

        self.boost = False                  # Pole z informacją czy gracz ma boosta / powerupa
        self.boostTimer = QTimer(self)      # Pomocniczy QTimer odliczający czas do wyłączenia boosta
        self.boostTimer.timeout.connect(self.manageBoost)

        self.timer = QTimer(self)   # Główny QTimer który wywołuje każdy kolejny krok gry (silnik)
        self.timer.timeout.connect(self.onTimeout)
        self.timerHelp = False      # Ponieważ (na potrzeby implementacji boosta) wykonuje się dwukrotna ilość kroków
                                    # na sekundę, to pole pomocnicze redukuje ilość kroków o połowę
                                    # (gdy jest aktywny boost, wykonują się wszystkie kroki niezależnie
                                    # od wartości tego pola)

        # TODO Działa, ale czy poprawne? Więcej informacji przy metodzie gameOverWindow
        #if not isinstance(parent, QMainWindow):
        #    raise ValueError
        #self.parentW = parent
        self.exitMetod = exitMethod

        self.MAX_SNAKE_LEN = 0

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

        # Dynamiczna zmiana wielkości komórek, planszy i wyśrodkowania jej w zależności od ilości komórek
        self.cellWidth = int((self.width-100) / self.cellCount)
        self.myCanvasSize = int(self.cellWidth * self.cellCount)
        self.myCanvasPaddingX = (self.width-self.myCanvasSize)/2
        self.myCanvasPaddingY = 100

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

        self.label_3.setText("HIGH SCORE")
        self.label_4.setText("SCORE")
        self.highscore = 7  # TODO pobieranie highscore z pliku
        self.scoreHigh.setText(self.intToScoreStr(self.highscore))
        self.scoreCurrent.setText(self.intToScoreStr(self.score))
        self.arrRight.setText(">")
        self.arrUp.setText("^")
        self.arrLeft.setText("<")
        self.arrDown.setText("v")

    def newGame(self):
        self.timer.stop()
        self.gameOver = False

        # Poprawa wielkości rysowania przy zmianie długości boku
        self.cellWidth = int((self.width - 100) / self.cellCount)
        self.myCanvasSize = int(self.cellWidth * self.cellCount)
        self.myCanvasPaddingX = (self.width - self.myCanvasSize) / 2

        self.score = 0
        self.newDirection = ""
        self.Python.direction = ""
        self.Python.tail = []
        self.Python.head.x = int(self.cellCount/2)
        self.Python.head.y = int(self.cellCount/2)

        try:
            with open("highscore.ini") as file:
                fileContent = file.readline()
                fileContent = fileContent.rstrip('\n')
            self.highscore = float(fileContent)
        except IOError:
            print("highscore.ini file not found")
            self.highscore = 0
        except Exception:
            print("highscore.ini file is empty")
            self.highscore = 0

        self.scoreHigh.setText(self.intToScoreStr(self.highscore))
        self.scoreCurrent.setText(self.intToScoreStr(self.score))

        self.gameMatrix = []
        for i in range(self.cellCount):
            temp = []
            for j in range(self.cellCount):
                temp.append(0)
            self.gameMatrix.append(temp)

        if self.closedBox:
            for i in range(self.cellCount):
                self.gameMatrix[i][0] = 7
                self.gameMatrix[0][i] = 7
                self.gameMatrix[i][self.cellCount-1] = 7
                self.gameMatrix[self.cellCount-1][i] = 7

        if self.randomWall:
            randY1 = randrange(2, int(self.cellCount/2-1))
            randY2 = randrange(int(self.cellCount/2)+2, self.cellCount-2)
            for i in range(self.cellCount-4):
                self.gameMatrix[i+2][randY1] = 7
                self.gameMatrix[i+2][randY2] = 7

        self.gameOver = False
        self.timer.start(int(1000/(self.CPS*2)))

        # Obliczanie maksymalnej długości węża
        self.MAX_SNAKE_LEN = 0
        for i in self.gameMatrix:
            for j in i:
                if j == 0:
                    self.MAX_SNAKE_LEN += 1
        # print(self.MAX_SNAKE_LEN)

        self.spawnFood(1)
        if self.powerups:
            self.manageBoost()  # m.in. dodaje super jedzenie na plaszę

        # Obsługa klawiatury
        keyboard.on_press_key("a", lambda _: self.arrLeftClicked())
        keyboard.on_press_key("left arrow", lambda _: self.arrLeftClicked())

        keyboard.on_press_key("d", lambda _: self.arrRightClicked())
        keyboard.on_press_key("right arrow", lambda _: self.arrRightClicked())

        keyboard.on_press_key("w", lambda _: self.arrUpClicked())
        keyboard.on_press_key("up arrow", lambda _: self.arrUpClicked())

        keyboard.on_press_key("s", lambda _: self.arrDownClicked())
        keyboard.on_press_key("down arrow", lambda _: self.arrDownClicked())

    # Silnik
    def onTimeout(self):
        # Wykonuje się co drugie wywołanie (timerHelp) lub co każde, jeżeli jest boost
        if self.timerHelp or self.boost:

            self.paintFlag = True

            self.gameOver = self.checkCollision()
            foodCheck = self.checkFoodCollision()
            if not self.gameOver:
                self.moveSnake(foodCheck)
            else:
                self.gameOverHandler()

            self.update()

        self.timerHelp = not self.timerHelp

    # Sprawdzanie kolizji
    def checkCollision(self):
        if self.gameMatrix[self.Python.head.x][self.Python.head.y] == 7:
            return True

        for i in range(len(self.Python.tail)):
            if self.Python.tail[i].x == self.Python.head.x and self.Python.tail[i].y == self.Python.head.y:
                return True

        return False

    def checkFoodCollision(self):
        temp = self.gameMatrix[self.Python.head.x][self.Python.head.y]
        scoreMultiplayer = 1 * (float(self.CPS) / 10)
        if self.CPS >= 5:
            scoreMultiplayer += (float(self.CPS) / 10) * 2
        if self.randomWall:
            scoreMultiplayer += 1
        if self.closedBox:
            scoreMultiplayer += 1
        if temp == 1:
            self.spawnFood(1)
            self.score += 1 * scoreMultiplayer
            self.scoreCurrent.setText(self.intToScoreStr(self.score))
        elif temp == 2:
            self.score += 5 * scoreMultiplayer
            self.scoreCurrent.setText(self.intToScoreStr(self.score))

        self.gameMatrix[self.Python.head.x][self.Python.head.y] = 0
        return temp

    # Dekoracja liczby
    @staticmethod
    def intToScoreStr(value):
        STR_SCORE_LEN = 10
        valueT = int(value)
        lenT = len(str(valueT))
        return "0" * (STR_SCORE_LEN - lenT) + str(valueT)

    def spawnFood(self, value):
        try:
            tempX, tempY = self.findFreePosition()
            self.gameMatrix[tempX][tempY] = int(value)
        except InterruptedError:  # Wygrana
            self.gameOver = True

    # Szukanie wolnej pozycji dla jedzenia
    def findFreePosition(self):
        # Sprawdzanie czy wygrana
        tempCounter = self.MAX_SNAKE_LEN - (len(self.Python.tail) + 1 + 2)
        # print("Wolne: " + str(tempCounter))
        if tempCounter <= 1:
            raise InterruptedError

        while True:
            # print("los")
            freeX = randrange(0, self.cellCount-1)
            freeY = randrange(0, self.cellCount-1)
            error = False

            if self.gameMatrix[freeX][freeY] != 0:
                error = True
            elif freeX == self.Python.head.x and freeY == self.Python.head.y:
                error = True
            else:
                for i in self.Python.tail:
                    if freeX == i.x and freeY == i.y:
                        error = True
                        break

            if not error:
                return freeX, freeY

    # Poruszanie się węża
    def moveSnake(self, situation):

        # Zakaz pójścia węża 'w tył'
        tbool1 = self.newDirection == "N" and self.Python.direction == "S"
        tbool2 = self.newDirection == "E" and self.Python.direction == "W"
        tbool3 = self.newDirection == "W" and self.Python.direction == "E"
        tbool4 = self.newDirection == "S" and self.Python.direction == "N"
        if not (tbool1 or tbool2 or tbool3 or tbool4):
            self.Python.direction = self.newDirection

        if situation == 0:
            self.Python.tailMove()
        elif situation == 1:
            self.Python.tailMoveEating()
        elif situation == 2:
            self.startBoost(10000)
            self.Python.tailMoveEating()

        if not self.closedBox:
            self.movementCorrection()

    # Włącza boost i odliczanie do jego wyłączenia; zmiana koloru węża
    def startBoost(self, duration):
        self.snakeTailColor = BOOST_TAILCOLOR
        self.snakeHeadColor = BOOST_HEADCOLOR
        self.boost = True
        self.boostTimer.start(duration)

    # Wyłącza boost i odliczanie, spawnuje super jedzenie; zmiana koloru węża
    def manageBoost(self):
        self.boostTimer.stop()
        self.snakeTailColor = NORMAL_TAILCOLOR
        self.snakeHeadColor = NORMAL_HEADCOLOR
        self.boost = False
        self.spawnFood(2)

    # "Teleportacja" na przeciwną stroną planszy, jeżeli wąż wyjdzie poza
    def movementCorrection(self):
        if self.Python.head.x < 0:
            self.Python.head.x = self.cellCount-1
        elif self.Python.head.y < 0:
            self.Python.head.y = self.cellCount-1
        elif self.Python.head.x > self.cellCount-1:
            self.Python.head.x = 0
        elif self.Python.head.y > self.cellCount-1:
            self.Python.head.y = 0

    # Rysowanie
    def paintEvent(self, e):
        if self.paintFlag:
            # print("paint")

            # Kolory TODO self?
            backgroundColor = QColor(153, 204, 255)
            wallColor = QColor(0, 0, 0)
            foodNormalColor = QColor(255, 0, 0)
            foodSuperColor = QColor(255, 165, 0)


            # Dla uproszczenia i skrócenia dalszej części
            width = self.myCanvasSize
            x0 = int(self.myCanvasPaddingX)
            y0 = int(self.myCanvasPaddingY)

            painter = QPainter(self)

            painter.setBrush(backgroundColor)
            painter.setPen(Qt.NoPen)  # rysowanie bez krawędzi
            painter.drawRect(x0, y0, width, width)  # tło

            for i in range(self.cellCount):
                for j in range(self.cellCount):

                    if self.gameMatrix[i][j] == 7:
                        painter.setBrush(wallColor)
                        painter.drawRect(
                            int(x0 + (i * self.cellWidth))
                            , int(y0 + (j * self.cellWidth))
                            , int(self.cellWidth)
                            , int(self.cellWidth))

                    elif self.gameMatrix[i][j] == 1:
                        painter.setBrush(foodNormalColor)
                        painter.drawEllipse(
                            int(x0 + 3 + (i * self.cellWidth))
                            , int(y0 + 3 + (j * self.cellWidth))
                            , int(self.cellWidth)-6
                            , int(self.cellWidth)-6)

                    elif self.gameMatrix[i][j] == 2:
                        painter.setBrush(foodSuperColor)

                        #TODO: usunąć jeden ze sposobów rysowania (teraz rąb zasłania kółko)
                        painter.drawEllipse(
                            int(x0 + 3 + (i * self.cellWidth))
                            , int(y0 + 3 + (j * self.cellWidth))
                            , int(self.cellWidth)-6
                            , int(self.cellWidth)-6)

                        points = [
                            QPoint(x0+(i*self.cellWidth), y0+((j+0.5)*self.cellWidth)),
                            QPoint(x0+((i+0.5)*self.cellWidth), y0+((j+1.0)*self.cellWidth)),
                            QPoint(x0+((i+1.0)*self.cellWidth), y0+((j+0.5)*self.cellWidth)),
                            QPoint(x0+((i+0.5)*self.cellWidth), y0+(j*self.cellWidth))
                        ]
                        painter.drawPolygon(QPolygon(points))

            # Rysowanie węża
            painter.setBrush(self.snakeTailColor)
            for i in range(len(self.Python.tail)):

                if self.snakeTailColor == BOOST_TAILCOLOR:
                    tailColor = self.snakeTailColor
                else:
                    tailColor = self.snakeTailColor
                    tailColor.setRed(i * 5)
                    tailColor.setGreen(128-(i*2))
                    tailColor.setBlue(i * 5)
                painter.setBrush(tailColor)

                painter.drawRect(
                    int(x0 + 2 + (self.Python.tail[i].x * self.cellWidth)),
                    int(y0 + 2 + (self.Python.tail[i].y * self.cellWidth)),
                    int(self.cellWidth)-4,
                    int(self.cellWidth)-4
                    )

            painter.setBrush(self.snakeHeadColor)
            painter.drawRect(
                int(x0+1+(self.Python.head.x * self.cellWidth))
                , int(y0+1+(self.Python.head.y * self.cellWidth))
                , int(self.cellWidth)-2
                , int(self.cellWidth)-2
            )

        self.paintFlag = False

    def arrRightClicked(self):
        self.newDirection = "E"

    def arrUpClicked(self):
        self.newDirection = "N"

    def arrLeftClicked(self):
        self.newDirection = "W"

    def arrDownClicked(self):
        self.newDirection = "S"

    def gameOverHandler(self):
        newHighScore = False
        if self.score > self.highscore:
            newHighScore = True

        self.checkIfNewRecord()
        self.gameOverWindow(newHighScore)

    def checkIfNewRecord(self):
        if self.score > self.highscore:
            self.highscore = self.score
            try:
                highScoreFile = open("highscore.ini", "w")
                highScoreFile.write(str(self.highscore))
                highScoreFile.close()
            except IOError:
                print("highscore.ini file not found")

    # TODO Działa, jednak czy jest to poprawne rozwiązanie? Czy GameView powinien wiedzieć jakie metody
    #  ma klasa go wykorzystująca?
    #  Do usunięcia? Do zmiany?
    def gameOverWindow(self, value):
        strT = "\n"
        if value:
            strT = "\nNowy najlepszy wynik!\n"

        if self.exitMetod != None:
            choice = QMessageBox.information(self, "Koniec", "Wynik: " + str(int(self.score)) + strT + "Powrót do menu?"
                                             , QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if choice == QMessageBox.Yes:
                self.exitMetod()  # TODO Poprawne w myśl dobrego programowania?
            else:
                self.newGame()
        else:
            choice = QMessageBox.information(self, "Koniec", "Wynik: " + str(int(self.score)) + strT + "!"
                                             ,QMessageBox.Ok, QMessageBox.Ok)
            if choice == QMessageBox.Ok:
                self.newGame()
