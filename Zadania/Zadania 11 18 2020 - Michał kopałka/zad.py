# Program realizujący zadanie 1a, 1b
#
#   zad 1a - utworzenie i dodanie QPushButton w pętli do gridLayout
#   zad 1b - przypisanie do przycisku QMessageBox
#
#  Autor: Michał Kopałka
#
#           24.11.2020 | Michał Kopałka     | Utworzenie

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton, QMessageBox
from PyQt5.uic.properties import QtWidgets

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout(self)
        self.name = "Apka"
        self.initUI()

    def initUI(self):
        self.setFixedSize(200, 200)
        self.setGeometry(0, 0, 400, 600)

        for i in range(3):
            for j in range(3):
                button = QPushButton(self)
                button.setText(str(i*3+j+1))
                button.setFixedWidth(50)
                button.setFixedHeight(50)
                button.clicked.connect(self.buttonClicked)
                self.gridLayout.addWidget(button, i, j)
        self.setWindowTitle(self.name)
        self.show()

    def buttonClicked(self):
        msgb = QMessageBox.question(self, "hallo", "Czy napewno chcesz wyjsć?", QMessageBox.Yes | QMessageBox.No)

        if msgb == QMessageBox.Yes:
            sys.exit()
        else:
            pass

app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())