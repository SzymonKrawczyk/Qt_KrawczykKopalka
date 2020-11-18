import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Moja aplikacja'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle(self.name)

        buttonMsg = QPushButton('Exit', self)
        buttonMsg.resize(150, 25)
        buttonMsg.move(100, 150)
        buttonMsg.clicked.connect(self.showMsg)

        self.show()

    def showMsg(self):

        choice = QMessageBox.question(self, 'Warning', 'Czy na pewno chcesz wyjść z aplikacji?'
                                      , QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('Do zobaczenia')
            sys.exit(0)
        elif choice == QMessageBox.No:
            print('Jednak nie wyłączamy')
        else:
            print('Coś się ewidentnie popsuło')


app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())
