from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QIntValidator
from PyQt5 import QtCore
from tkinter import *
import cv2

class Options(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Photo Editor 1.2')
        self.setWindowIcon(QIcon('icon.png'))
        layout = QVBoxLayout()
        browseButton = QPushButton()
        browseButton.setIcon(QIcon('browse.png'))
        browseButton.setToolTip('Load image from your pc')
        browseButton.clicked.connect(self.browseImage)
        browseButton.setMinimumHeight(50)
        browseButton.setIconSize(QtCore.QSize(40,40))
        layout.addWidget(browseButton)
        capimageButton = QPushButton()
        capimageButton.setIcon(QIcon('webcam.png'))
        capimageButton.setToolTip("Capture image from your pc's webcam")
        capimageButton.clicked.connect(self.capImage)
        capimageButton.setMinimumHeight(50)
        capimageButton.setIconSize(QtCore.QSize(40, 40))
        layout.addWidget(capimageButton)
        capvideoButton = QPushButton()
        capvideoButton.setIcon(QIcon('videocap.png'))
        capvideoButton.setToolTip("Capture video from your pc's webcam")
        capvideoButton.clicked.connect(self.capVideo)
        capvideoButton.setMinimumHeight(50)
        capvideoButton.setIconSize(QtCore.QSize(40, 40))
        layout.addWidget(capvideoButton)
        scriptingButton = QPushButton()
        scriptingButton.setToolTip("Photo Scripting")
        scriptingButton.setMinimumHeight(50)
        scriptingButton.setIcon(QIcon('script.png'))
        scriptingButton.setIconSize(QtCore.QSize(40, 40))
        scriptingButton.clicked.connect(self.photoScript)
        layout.addWidget(scriptingButton)
        self.resize(300,350)
        self.setLayout(layout)
        self.show()

    def browseImage(self):
        filter = "JPG (*.jpg);;PNG (*.png);;JPEG (*.jpeg)"
        name = QFileDialog.getOpenFileName(self,'Select Images','',filter)
        image = cv2.imread(name[0])
        cv2.imshow('image',image)

    def capImage(self):
        obj = Captureimage(root)
        root.mainloop()

    def capVideo(self):
        print('capvideo')

    def photoScript(self):
        self.obj2 = photoScript()

class Captureimage:
    def __init__(self,root):
        root.title('Capture Image')
        root.geometry("250x300")

class photoScript(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()

        label = QLabel()
        label.setText("Convert multiple images from one format to another")
        vbox.addWidget(label)
        button = QPushButton()
        button.setToolTip("Select Directory")
        button.setIcon(QIcon('browse.png'))
        button.setIconSize(QtCore.QSize(40,40))
        vbox.addWidget(button)
        path = QTextEdit()
        path.setDisabled(True)
        path.setToolTip("Path")
        path.setMaximumHeight(40)
        vbox.addWidget(path)
        hbox = QHBoxLayout()
        width = QLineEdit()
        width.setValidator(QIntValidator())
        width.setToolTip("Width")
        width.setMinimumHeight(30)
        hbox.addWidget(width)
        height = QLineEdit()
        height.setToolTip("Height")
        height.setMinimumHeight(30)
        height.setValidator(QIntValidator())
        hbox.addWidget(height)
        vbox.addLayout(hbox)
        hbox2 = QHBoxLayout()
        checkbox1 = QCheckBox()
        checkbox1.setText(".JPG")
        checkbox2 = QCheckBox()
        checkbox2.setText(".PNG")
        group = QButtonGroup()
        group.addButton(checkbox1)
        group.addButton(checkbox2)
        hbox2.addItem(checkbox1)
        hbox2.addItem(checkbox2)
        vbox.addLayout(hbox2)

        self.setWindowIcon(QIcon('script.png'))
        self.setWindowTitle("Photo Scripting")
        self.setLayout(vbox)
        self.show()


def call():
    global root
    root = Tk()
    app = QApplication([])
    obj = Options()
    app.exec_()

if __name__=="__main__":
    root = Tk()
    app = QApplication([])
    obj = Options()
    app.exec_()
