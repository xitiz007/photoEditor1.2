from PyQt5.QtWidgets import QLabel,QApplication,QAction,QMainWindow,QPushButton,QFileDialog
from PyQt5.Qt import QIcon,QPixmap,QImage
from PyQt5 import QtCore,QtGui
from PIL import Image,ImageOps
import description

class Editor(QMainWindow):
    def __init__(self,path):
        super().__init__()
        self.path = path
        self.setWindowTitle('Photo Editor 1.2')
        self.setWindowIcon(QIcon('icon.png'))
        self.width = 900
        self.height = 500
        self.label = QLabel(self)
        self.label.resize(self.width, self.height)
        self.image = Image.open(path)
        self.showImage()
        self.ui()
        self.keyPressEvent(self)
        self.show()

    def showImage(self):
        self.image = self.image.convert("RGBA")
        data  = self.image.tobytes('raw','RGBA')
        img = QImage(data,self.image.size[0],self.image.size[1],QImage.Format_RGBA8888)
        self.pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(self.pixmap.scaled(self.label.size(),QtCore.Qt.IgnoreAspectRatio))
        self.label.setGeometry(200,100,900,500)

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
        label.move(600,50)

        zoomOutButton = QPushButton(self)
        zoomOutButton.setToolTip("Zoom Out")
        zoomOutButton.setIcon(QIcon('zoomout.png'))
        zoomOutButton.move(570,650)
        zoomOutButton.pressed.connect(self.zoomOut)
        zoomInButton = QPushButton(self)
        zoomInButton.setToolTip("Zoom In")
        zoomInButton.setIcon(QIcon('zoomin.png'))
        zoomInButton.move(680,650)
        zoomInButton.pressed.connect(self.zoomIn)

        mirrorbutton = QPushButton(self)
        mirrorbutton.setIcon(QIcon('mirror.png'))
        mirrorbutton.setToolTip("Mirror Image")
        mirrorbutton.move(790,650)
        mirrorbutton.pressed.connect(self.mirrorButton)

        descriptionbutton = QPushButton(self)
        descriptionbutton.setIcon(QIcon('description.png'))
        descriptionbutton.setToolTip("Properties of image")
        descriptionbutton.move(1110,100)
        descriptionbutton.setMaximumWidth(30)
        descriptionbutton.pressed.connect(self.descriptionButton)

        leftrotate = QPushButton(self)
        leftrotate.setIcon(QIcon('rotateLeft.png'))
        leftrotate.setToolTip("Rotate Left(90)")
        leftrotate.move(350,650)
        leftrotate.pressed.connect(self.leftRotate)

        rightrotate = QPushButton(self)
        rightrotate.setIcon(QIcon('rotateRight.png'))
        rightrotate.setToolTip("Rotate Right(-90)")
        rightrotate.move(460,650)
        rightrotate.pressed.connect(self.rightRotate)

    def leftRotate(self):
        self.image = self.image.rotate(90)
        self.showImage()

    def rightRotate(self):
        self.image = self.image.rotate(-90)
        self.showImage()

    def descriptionButton(self):
        self.object = description.Description(self.image,self.path)

    def newMenu(self):
        print("New Menu")

    def saveMenu(self):
        filter = "JPG (*.jpg);;PNG (*.png);;JPEG (*.jpeg)"
        fileName = QFileDialog.getSaveFileName(self,"Save Image",filter=filter)
        self.image = self.image.convert("RGB")
        self.image.save(fileName[0])

    def exitMenu(self):
        print("Exit Menu")

    def keyPressEvent(self, event):
        pass

    def zoomIn(self):
        if self.width < 900 and self.height < 500:
            self.width += 50
            self.height += 50
            self.label.resize(self.width, self.height)
            self.label.setPixmap(self.pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))

    def zoomOut(self):
        if self.width > 500:
            self.width -= 50
            self.height -= 50
            self.label.resize(self.width, self.height)
            self.label.setPixmap(self.pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))

    def mirrorButton(self):
        self.image = ImageOps.mirror(self.image)
        self.showImage()

if __name__ == '__main__':
    app = QApplication([])
    obj = Editor('C:/Users/kshit/OneDrive/तस्विरहरू/Saved pictures/fabian-grohs-dC6Pb2JdAqs-unsplash.jpg')
    app.exec_()
