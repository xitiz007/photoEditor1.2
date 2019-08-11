from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
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

class Captureimage:
    def __init__(self,root):
        root.title('Capture Image')
        root.geometry("250x300")

if __name__=="__main__":
    root = Tk()
    app = QApplication([])
    obj = Options()
    app.exec_()

