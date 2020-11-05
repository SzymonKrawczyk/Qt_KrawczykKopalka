# Plik z przykładowym oknem zmieniającym zawartość po kliknięciu na przycisk
#
#   Do zminienia zawartości okna wykorzystałem stackedWidget. pozwala on na zdefiniowanie sobie mniejszego "okna" w
#   głównym oknie i zmienianie jego zawartości. (ustawiamy sobie na ten przykład elementy page_1, page_2, page_3... )
#   W przykładzie zmieniłem kolor tła więc dokładnie możesz zobaczyć zasięg widgetu. (nic nie stoi na przeszkodzie by
#   zajmował całe okno) Minusem jest to że wszystkie elementy, które tak wrzucimy do naszego widgetu
#   traktowane są jak element jednego okna a więc też ich obsługa powinna być realizowana w jednej klasie.
#   Tak dla jasności wykorzystałem Qt Designe.
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#           05.11.2020 | Michał Kopałka      | Utworzenie
#
#


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox
from Projekt.Szablony.Ui_zmiana_widoku import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.main_win = QMainWindow()

        # Podstawienie sobie pod ui naszego wygenerowanego interfaceu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Podstawienie sobie pod stackedWidget naszego pierwszego "okienka"
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        # Odpowiednie funkcje dla przycisków ( zauważ że niezależnie czy przycisk należy do głównego okna
        # czy jest elementem stackedWidget odwołujemy się do niego tak samo )
        # mainPushButton jest w głównym oknie, reszta w stackedWidget
        self.ui.mainPushButton.clicked.connect(self.mainPushButtonClicked)
        self.ui.Screen1pushButton.clicked.connect(self.Screen1PushButtonClicked)
        self.ui.screen2pushButton.clicked.connect(self.screen2PushButtonClicked)

    def show(self):
        self.main_win.show()

    # zmiany widoku widgetu
    def mainPushButtonClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
    def  Screen1PushButtonClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    def screen2PushButtonClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()