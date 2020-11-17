# Klasa QWidgetu widoku ekranu tytułowego z ustawieniami
#
#   TODO Opis pliku, klas i metod w nim zawieranych
#
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
#
#         TODO: dodanie liczników na końcu każdego slidera ( o dziwo przy projektowaniu nie przyszło mi to do głowy )
#         TODO: zrobienie porządnej instrukcji ( ale lorem ipsum też spoczko )
#         TODO: ewentualna poprawa tytułu ( jak się nie da bez wgrywania dziwnych czcionek to zastąpić label imageView )
#         TODO: posprzątać bałagan w nazwach zmiennych ( lub nie )
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class TitleView(QWidget):

    # Ilość ruchów na sekundę (szybkość gry) - musi być w przedziale
    @property
    def CPS(self):
        return self.horizontalSlider_2.value()

    # Ilość komórek na ekranie gry (bok) - musi być nieparzysty i w przedziale
    @property
    def cellCount(self):
        return self.horizontalSlider.value()

    # Opcja - czy generować powerUpy
    @property
    def powerups(self):
        return self.checkBox_3.isChecked()

    # Opcja - czy obszar gry ma być otoczony ścianą
    @property
    def closedBox(self):
        return self.checkBox_2.isChecked()

    # Opcja - czy generować losową ścianę w środku gry
    @property
    def randomWall(self):
        return self.checkBox.isChecked()

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

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_5.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setMinimum(13)
        self.horizontalSlider.setMaximum(51)
        self.horizontalSlider.setSliderPosition(31)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("bok")
        self.horizontalLayout_6.addWidget(self.horizontalSlider)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(5)
        self.horizontalSlider_2.setSliderPosition(3)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("cps")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_2)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 45))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

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

        font2 = QtGui.QFont()
        font2.setPointSize(16)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 521, 221))
        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setFont(font2)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox_2.setText(_translate("Form", "Zamknięty obszar gry"))
        self.checkBox.setText(_translate("Form", "Losowe ściany - przeszkody"))
        self.checkBox_3.setText(_translate("Form", "Super-food"))
        self.label_4.setText(_translate("Form", "długość boku planszy "))
        self.label_3.setText(_translate("Form", "Szybkość rozgrywki"))
        self.pushButton.setText(_translate("Form", "Graj"))
        self.label.setText(_translate("Form", "(PYTHON)^2"))
        self.label_2.setText(_translate("Form", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mollis lacus id mi vulputate suscipit. Vestibulum eu odio est. "
                                                "In convallis augue vitae nulla condimentum, non pharetra orci dictum. Nullam vehicula ligula id eros mattis lobortis. Nulla "
                                                "dignissim ex ac erat euismod efficitur. Etiam consectetur nibh a tempor posuere. In sed metus id nibh rhoncus vulputate. "
                                                "Nam aliquam ante in odio ornare cursus. Donec varius dolor vitae augue condimentum varius. Nunc sed lacinia eros. Ut "
                                                "ornare mauris a odio gravida, gravida mattis eros bibendum."))
