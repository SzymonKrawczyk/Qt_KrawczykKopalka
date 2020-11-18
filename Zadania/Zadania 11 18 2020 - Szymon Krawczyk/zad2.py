import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Moja aplikacja'

        self.x = 3  # wiersze
        self.y = 3  # kolumny
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)

        gridLayout = QGridLayout(self)
        for i in range(self.x):
            for j in range(self.y):
                tempName = str(self.y * i + j + 1)
                gridLayout.addWidget(QPushButton(tempName, self), i, j)

        self.setWindowTitle(self.name)
        self.show()


app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())
