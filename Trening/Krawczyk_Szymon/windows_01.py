# Trening okienkowy 2
#
#   Szymon Krawczyk
#

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)   # klasa zawsze sie wykona

        self.setWindowTitle("Ekusploshion w Qt")
        self.setFixedSize(QSize(600, 600))

        # font jako osobny obiekt
        myfont = QFont("Calibri", 20)
        myfont.setBold(True)
        myfont.setItalic(True)

        mylabel = QLabel("Megumin is the greatest explosion archwizard!")
        mylabel.setFont(QFont("Calibri", 20, 600))  # font tworzony i podawany jako orgument

        self.setCentralWidget(mylabel)
        mylabel.setAlignment(Qt.AlignHCenter)

        button = QPushButton("EKUSPLOSHION!!!", self)
        button.clicked.connect(self.buttonaction)   # ustawienie metody wlaczanej po nacisnieciu

        button2 = QPushButton("EXPLOSION!!!!!", self)
        button2.clicked.connect(self.buttonaction2)

        # Box
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)
        hbox.addWidget(button2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

        vbox.setGeometry(QtCore.QRect(100, 200, 300, 150))

    @staticmethod
    def buttonaction(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("EKUSPLOSHION!")
        msg.setText("BOOM! BOOM!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Abort)

        msg.exec_()
        print("BOOM!")

    @staticmethod
    def buttonaction2(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("EXPLOSION!")
        msg.setText("BOOOOOOM!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Abort)

        msg.exec_()
        print("BOOOOOOM!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
