from PyQt5.QtWidgets import *
from ui import Ui_MainWindow
import server


class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton_2.clicked.connect(server.receive())


app = QApplication([])
pencere = window()
pencere.show()
app.exec_()
