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
#           07.11.2020 | Szymon Krawczyk     | Zmiana drugiego okna na klasę Interface służącą jako demo
#                                            |   rysowania dynamicznie generowanych linii
#           07.11.2020 | Szymon Krawczyk     | Dodanie dynamiki przycisku głównego
#


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox
from zmiana_widoku.Ui_zmiana_widoku import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.main_win = QMainWindow()
        self.flag = 0

        # Podstawienie sobie pod ui naszego wygenerowanego interfaceu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Podstawienie sobie pod stackedWidget naszego pierwszego "okienka"
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        # Odpowiednie funkcje dla przycisków ( zauważ że niezależnie czy przycisk należy do głównego okna
        # czy jest elementem stackedWidget odwołujemy się do niego tak samo )
        # mainPushButton jest w głównym oknie, reszta w stackedWidget
        self.ui.mainPushButton.clicked.connect(self.mainPushButtonClicked)
        self.ui.Screen1pushButton.clicked.connect(self.screen1PushButtonClicked)
        self.ui.screen2pushButton.clicked.connect(self.screen2PushButtonClicked)
        self.ui.mainPushButton.setText("Zagraj")

    def show(self):
        self.main_win.show()

    # zmiany widoku widgetu
    def mainPushButtonClicked(self):
        if self.flag == 1:
            self.flag = 0
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
            self.ui.mainPushButton.setText("Zagraj")
        else:
            self.flag = 1
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.ui.mainPushButton.setText("Ekran główny")
            self.ui.page_2.reset()

    def screen2PushButtonClicked(self):
        self.flag = 0
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.mainPushButton.setText("Zagraj")

    def screen1PushButtonClicked(self):
        self.flag = 1
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.mainPushButton.setText("Ekran główny")
        self.ui.page_2.reset()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
