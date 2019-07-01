from PyQt5.QtWidgets import *
import sys

class dataBase(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindow()


    def setWindow(self):
        self.setGeometry(100,200,200,400)
        self.setWindowTitle("Photo Editor 1.2")
        self.show()

app = QApplication(sys.argv)
obj = dataBase()
sys.exit(app.exec())