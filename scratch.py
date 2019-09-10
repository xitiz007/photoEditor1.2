from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QIntValidator
from PyQt5 import QtCore
from tkinter import *
import cv2
import os

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
        filter = "AVI (*.avi)"
        name = QFileDialog.getSaveFileName(self,'Save Video','',filter)
        path = name[0]
        if(path):
            video = cv2.VideoCapture(0)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            videoWriter = cv2.VideoWriter(path,fourcc,23,(640,480))
            if video.isOpened():
                while (True):
                    tof , frame = video.read()
                    cv2.imshow('Video',frame)
                    videoWriter.write(frame)
                    key = cv2.waitKey(1)
                    if key==27 :
                        break
                videoWriter.release()
                video.release()
                cv2.destroyAllWindows()



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
        button.clicked.connect(self.browseDirectory)
        vbox.addWidget(button)
        self.path = QTextEdit()
        self.path.setDisabled(True)
        self.path.setToolTip("Path")
        self.path.setMaximumHeight(40)
        vbox.addWidget(self.path)
        hbox = QHBoxLayout()
        self.width = QLineEdit()
        self.width.setValidator(QIntValidator())
        self.width.setToolTip("Width")
        self.width.setMinimumHeight(30)
        hbox.addWidget(self.width)
        self.height = QLineEdit()
        self.height.setToolTip("Height")
        self.height.setMinimumHeight(30)
        self.height.setValidator(QIntValidator())
        hbox.addWidget(self.height)
        vbox.addLayout(hbox)
        hbox2 = QHBoxLayout()
        label2 = QLabel()
        label2.setText("Image Extension:")
        self.radioButton1 = QRadioButton()
        self.radioButton1.setChecked(True)
        self.radioButton1.setText(".JPG")
        self.radioButton2 = QRadioButton()
        self.radioButton2.setText(".PNG")
        self.checkBox = QCheckBox()
        self.checkBox.setText("B&W")
        self.checkBox.setToolTip("Black & White")
        saveButton = QPushButton()
        saveButton.setToolTip("Select where to save")
        saveButton.setIconSize(QtCore.QSize(40,40))
        saveButton.setIcon(QIcon('save.png'))
        saveButton.clicked.connect(self.saveButtonClicked)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.radioButton1)
        hbox2.addWidget(self.radioButton2)
        hbox2.addWidget(self.checkBox)
        vbox.addLayout(hbox2)
        vbox.addWidget(saveButton)
        convertButton = QPushButton()
        convertButton.setText("Convert")
        convertButton.setMinimumHeight(30)
        convertButton.clicked.connect(self.convertButtonClicked)
        vbox.addWidget(convertButton)

        self.setWindowIcon(QIcon('script.png'))
        self.setWindowTitle("Photo Scripting")
        self.setLayout(vbox)
        self.show()

    def convertButtonClicked(self):
        try:
            if(self.file and self.saveFile):
                path = self.file
                path = path.replace('\\','/')
                for files in os.listdir(self.file):
                    if(files.endswith(".jpg") or files.endswith(".png") or files.endswith(".jpeg")):
                        name=""
                        image = cv2.imread(path+'/'+files)
                        if(self.checkBox.isChecked()):
                            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                        image = cv2.resize(image,(int(self.width.text()),int(self.height.text())))
                        if(self.radioButton1.isChecked()):
                            name = files[:files.index('.')] + ".jpg"
                        elif(self.radioButton2.isChecked()):
                             name = files[:files.index('.')] + ".png"
                        cv2.imwrite(self.saveFile+'/'+name,image)



        except:
            print("Error")

    def browseDirectory(self):
        self.file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.file = self.file.replace('/','\\')
        self.path.setText(self.file)

    def saveButtonClicked(self):
        self.saveFile = str(QFileDialog.getExistingDirectory(self, "Select  Directory"))

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
