from PyQt5.QtWidgets import QLabel,QApplication,QAction,QMainWindow
from PyQt5.Qt import QIcon,QPixmap,Qt
from PyQt5 import QtCore,QtGui

class Editor(QMainWindow):
    def __init__(self,path):
        super().__init__()
        self.setWindowTitle('Photo Editor 1.2')
        self.setWindowIcon(QIcon('icon.png'))
        label = QLabel(self)
        label.resize(900, 500)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap.scaled(label.size(),QtCore.Qt.IgnoreAspectRatio))
        label.setGeometry(200,100,900,500)
        self.ui()
        self.keyPressEvent(self)
        self.show()

    def ui(self):
        menu = self.menuBar()
        filemenu = menu.addMenu('File')
        newmenu = QAction('New',self)
        newmenu.setShortcut("Ctrl+N")
        newmenu.triggered.connect(self.newMenu)
        savemenu = QAction('Save',self)
        savemenu.setShortcut("Ctrl+S")
        savemenu.triggered.connect(self.saveMenu)
        exitmenu = QAction('Exit',self)
        exitmenu.setShortcut("Ctrl+X")
        exitmenu.triggered.connect(self.exitMenu)
        filemenu.addAction(newmenu)
        filemenu.addAction(savemenu)
        filemenu.addAction(exitmenu)

        label = QLabel(self)
        label.setText("Photo Editor 1.2")
        label.setFont(QtGui.QFont('SansSerif',8,QtGui.QFont.Bold))
        label.move(550,50)

    def newMenu(self):
        print("New Menu")

    def saveMenu(self):
        print("Save menu")

    def exitMenu(self):
        print("Exit Menu")

    def keyPressEvent(self, event):
        pass

if __name__=='__main__':
    app = QApplication([])
    obj = Editor('C:/Users/kshit/OneDrive/तस्विरहरू/Saved pictures/fabian-grohs-dC6Pb2JdAqs-unsplash.jpg')
    app.exec_()
