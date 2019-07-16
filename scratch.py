from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
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
        layout.addWidget(browseButton)
        capimageButton = QPushButton()
        capimageButton.setIcon(QIcon('webcam.png'))
        capimageButton.setToolTip("Capture image from your pc's webcam")
        capimageButton.clicked.connect(self.capImage)
        layout.addWidget(capimageButton)
        capvideoButton = QPushButton()
        capvideoButton.setIcon(QIcon('videocap.png'))
        capvideoButton.setToolTip("Capture video from your pc's webcam")
        capvideoButton.clicked.connect(self.capVideo)
        layout.addWidget(capvideoButton)
        self.resize(300,400)
        self.setLayout(layout)
        self.show()

    def browseImage(self):
        filter = "JPG (*.jpg);;PNG (*.png);;JPEG (*.jpeg)"
        name = QFileDialog.getOpenFileName(self,'Select Images','',filter)
        image = cv2.imread(name[0])
        cv2.imshow('image',image)

    def capImage(self):
        print('capimage')


    def capVideo(self):
        print('capvideo')

if __name__=="__main__":
    app = QApplication([])
    obj = Options()
    app.exec_()

