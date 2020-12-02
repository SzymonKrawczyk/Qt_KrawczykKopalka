# Klasa QWidgetu widoku ekranu tytułowego z ustawieniami
#
#  Klasa slużąca za interface do ustawienia wartości parametrów w GameView,
#  umożliwia odczyt (i tylko odczyt) parametrów ze sliderów oraz checkBoxów, slidery są ograniczone
#  zgodnie z wymaganiami stawianymi przez GameView
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#  Plik początkowo wygenerowany:
#   -*- coding: utf-8 -*-
#   Form implementation generated from reading ui file 'TitleView1.ui'
#
#   Created by: PyQt5 UI code generator 5.15.1
#
#
#           15.11.2020 | Michał Kopałka     | Utworzenie wersji preAlpha
#           16.11.2020 | Szymon Krawczyk    | Dodanie właściwości jako wartości checkboxów i sliderów
#           16.11.2020 | Szymon Krawczyk    | Poprawa komentarzy
#           17.11.2020 | Szymon Krawczyk    | Zmiana wartości minimalnej wielkości planszy w celu uniknięcia błędu
#           18.11.2020 | Michał Kopałka     | Zmiana UI - dodanie spinBox przy każdym ze sliderów
#           18.11.2020 | Michał Kopałka     | Powiązanie wartości sliderów ze spinBox
#           20.11.2020 | Michał Kopałka     | Dodanie komentarzy
#           20.11.2020 | Szymon Krawczyk    | Poprawa komentarzy
#           20.11.2020 | Szymon Krawczyk    | Usunięcie testowania
#           20.11.2020 | Szymon Krawczyk    | Stworzenie prostej instrukcji gry
#           29.11.2020 | Szymon Krawczyk    | Zmiana czcionki tekstu zasad
#           02.12.2020 | Michał Kopałka     | Dodanie metody setSettings
#           02.12.2020 | Michał Kopałka     | Dodanie setterów
#           02.12.2020 | Michał Kopałka     | Usunięcie metody setSettings ( przeniesienie jej do MainViewUI )
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication

class TitleView(QWidget):

    # Ilość ruchów na sekundę (szybkość gry) - musi być w przedziale
    @property
    def CPS(self):
        return self.horizontalSlider_2.value()

    @CPS.setter
    def CPS(self, value):
        if value < 1 or value > 10:
            raise ValueError
        self.horizontalSlider_2.setValue(value)

    # Ilość komórek na ekranie gry (bok) - musi być nieparzysty i w przedziale
    @property
    def cellCount(self):
        return (self.horizontalSlider.value()*2)+1


    @cellCount.setter
    def cellCount(self, value):
        if value % 2 == 0 or value < 11 or value > 41:
            raise ValueError
        self.horizontalSlider.setValue(int((value - 1) / 2))


    # Opcja - czy generować powerUpy
    @property
    def powerups(self):
        return self.checkBox_3.isChecked()

    @powerups.setter
    def powerups(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self.checkBox_3.setChecked(value)

    # Opcja - czy obszar gry ma być otoczony ścianą
    @property
    def closedBox(self):
        return self.checkBox_2.isChecked()

    @closedBox.setter
    def closedBox(self,value):
        if not isinstance(value, bool):
            raise ValueError
        self.checkBox_2.setChecked(value)

    # Opcja - czy generować losową ścianę w środku gry
    @property
    def randomWall(self):
        return self.checkBox.isChecked()

    @randomWall.setter
    def randomWall(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self.checkBox.setChecked(value)


    def __init__(self):
        super().__init__()

        # UI wygenerowane automatycznie
        self.setObjectName("Form")
        self.resize(600, 800)
        self.setMinimumSize(QtCore.QSize(600, 800))
        self.setMaximumSize(QtCore.QSize(600, 800))

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 360, 601, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(40, 20, 40, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_5.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(162, 0))
        self.label_4.setMaximumSize(QtCore.QSize(162, 16777215))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)

        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMaximumSize(QtCore.QSize(45, 16777215))
        self.spinBox.setMinimum(11)
        self.spinBox.setMaximum(41)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 31)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(267, 16777215))

        # setSingle Step nie działa tak jak powinno więc ustawiłem zakres na 5-25 gdzie
        # wartość slidera odpowiada (value*2)+1
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setPageStep(3)
        self.horizontalSlider.setSliderPosition(12)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_6.addWidget(self.horizontalSlider)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(162, 0))
        self.label_3.setMaximumSize(QtCore.QSize(162, 16777215))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)

        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setMaximumSize(QtCore.QSize(45, 16777215))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setProperty("value", 5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_7.addWidget(self.spinBox_2)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_2.setMaximumSize(QtCore.QSize(267, 16777215))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setSliderPosition(5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_2)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 30, 519, 49))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(35)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        font2 = QtGui.QFont()
        font2.setFamily("Calibri")
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 521, 241))
        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # zablokowana możliwość wpisania np 12 w pole z długością boku
        self.spinBox.lineEdit().setReadOnly(True)
        self.spinBox_2.lineEdit().setReadOnly(True)

        self.horizontalSlider.valueChanged.connect(self.slider1ValueChanged)
        self.horizontalSlider_2.valueChanged.connect(self.slider2ValueChanged)
        self.spinBox.valueChanged.connect(self.spinBox1ValueChanged)
        self.spinBox_2.valueChanged.connect(self.spinBox2ValueChanged)

    # funkcje zapewniające integralność sliderów ze spinboxami
    def slider1ValueChanged(self):
        self.spinBox.setValue((self.horizontalSlider.value() * 2) + 1)

    def slider2ValueChanged(self):
        self.spinBox_2.setValue(self.horizontalSlider_2.value())

    def spinBox1ValueChanged(self):
        self.horizontalSlider.setValue(int((self.spinBox.value() - 1) / 2))

    def spinBox2ValueChanged(self):
        self.horizontalSlider_2.setValue(self.spinBox_2.value())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox_2.setText(_translate("Form", "Zamknięty obszar gry"))
        self.checkBox.setText(_translate("Form", "Losowe ściany - przeszkody"))
        self.checkBox_3.setText(_translate("Form", "Super-food"))
        self.label_4.setText(_translate("Form", "Długość boku planszy "))
        self.label_3.setText(_translate("Form", "Szybkość rozgrywki"))
        self.label.setText(_translate("Form", "(PYTHON)^2"))
        tempStr = "Gra Snake zrealizowana w Python"\
                  + "\nZbieraj jedzenie w celu zdobywania punktów, jednak uważaj, ponieważ z każdym kolejnym " \
                  + "posiłkiem wąż robi się coraz dłuższy!" \
                    "\nGra kończy się, gdy wąż spróbuje zjeść siebie lub ścianę"\
                  + "\n"\
                    "\nCzerwone koła = zwykłe jedzenie.."\
                    "\nZłote romby = jedzenie warte 5x ilośc punktów i dajace przyspieszenie na 10s!"\
                  + "\n"\
                  + "\nIm trudniejsza rozgrywka (ściany, szybkość), tym większy mnożnik punktów!"\
                  + "\nSterowanie: przyciski na ekranie / WSAD / Strzałki"\
                  + "\n"\
                  + "\nDostosuj ustawienia gry do swoich umiejętności"
        self.label_2.setText(_translate("Form", tempStr))
