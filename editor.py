from PyQt5.QtWidgets import QLabel,QApplication,QAction,QMainWindow,QPushButton,QFileDialog,QInputDialog,QSlider
from PyQt5.Qt import QIcon,QPixmap,QImage,Qt
from PyQt5 import QtCore,QtGui
from PIL import Image,ImageOps,ImageFilter,ImageDraw,ImageFont
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
        self.imageShow = self.image.convert("RGBA")
        data  = self.imageShow.tobytes('raw','RGBA')
        img = QImage(data,self.imageShow.size[0],self.imageShow.size[1],QImage.Format_RGBA8888)
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

        blackNwhite = QPushButton(self)
        blackNwhite.setText("Black n White")
        blackNwhite.move(1220,500)
        blackNwhite.pressed.connect(self.BlackNWhite)

        detailButton = QPushButton(self)
        detailButton.setText("Detail")
        detailButton.move(1220,550)
        detailButton.pressed.connect(self.Detail)

        resize = QPushButton(self)
        resize.setText("Resize")
        resize.move(1220,100)
        resize.pressed.connect(self.Resize)

        crop = QPushButton(self)
        crop.setText("Crop")
        crop.move(1220,150)
        crop.pressed.connect(self.Crop)

        doubleExposureButton = QPushButton(self)
        doubleExposureButton.setText("Double Exposure")
        doubleExposureButton.move(1220,200)
        doubleExposureButton.pressed.connect(self.DoubleExposure)

        pasteImage = QPushButton(self)
        pasteImage.setText("Paste Image")
        pasteImage.move(1220,250)
        pasteImage.pressed.connect(self.PasteImage)

        addText = QPushButton(self)
        addText.setText("Add Text")
        addText.move(1220,300)
        addText.pressed.connect(self.AddText)

        negativeButton = QPushButton(self)
        negativeButton.setText("Negative")
        negativeButton.move(1220,450)
        negativeButton.pressed.connect(self.negative)

        bLabel = QLabel(self)
        bLabel.setText("Brightness")
        bLabel.move(30,90)
        self.brightnessSlider = QSlider(self)
        self.brightnessSlider.setOrientation(Qt.Horizontal)
        self.brightnessSlider.setTickInterval(1)
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.move(30,120)
        self.brightnessSlider.valueChanged.connect(self.BrightnessSlider)

        cLabel = QLabel(self)
        cLabel.setText("Contrast")
        cLabel.move(30,210)
        self.contrastSlider = QSlider(self)
        self.contrastSlider.setOrientation(Qt.Horizontal)
        self.contrastSlider.setTickInterval(1)
        self.contrastSlider.setMinimum(0)
        self.contrastSlider.setMaximum(100)
        self.contrastSlider.move(30,240)
        self.contrastSlider.valueChanged.connect(self.BrightnessSlider)

        blLabel = QLabel(self)
        blLabel.setText("Blur")
        blLabel.move(30,330)
        self.blurSlider = QSlider(self)
        self.blurSlider.setOrientation(Qt.Horizontal)
        self.blurSlider.setTickInterval(1)
        self.blurSlider.setMinimum(0)
        self.blurSlider.setMaximum(100)
        self.blurSlider.move(30,360)
        self.blurSlider.valueChanged.connect(self.BlurSlider)

    def BrightnessSlider(self):
        pass

    def ContrastSlider(self):
        pass

    def BlurSlider(self):
        pass

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

    def BlackNWhite(self):
        self.image = self.image.convert('L')
        self.showImage()

    def Resize(self):
        width , pressed = QInputDialog.getInt(self,"Width","Width",1,1,int(self.image.width),1)
        if pressed:
            height , pressed = QInputDialog.getInt(self,"Height","Height",1,1,int(self.image.height),1)
            if pressed:
                self.image = self.image.resize((width,height),Image.ANTIALIAS)
                self.showImage()

    def negative(self):
        self.image = ImageOps.invert(self.image)
        self.showImage()

    def Crop(self):
        topX , pressed = QInputDialog.getInt(self,"Coordinate","TopX",1,1,int(self.image.width),1)
        if pressed:
            topY, pressed = QInputDialog.getInt(self, "Coordinate", "TopY", 1, 1, int(self.image.height), 1)
            if pressed:
                bottomX, pressed = QInputDialog.getInt(self, "Coordinate", "BottomX", 1, 1, int(self.image.width), 1)
                if pressed:
                    bottomY, pressed = QInputDialog.getInt(self, "Coordinate", "BottomY", 1, 1, int(self.image.height),1)
                    if pressed:
                        self.image = self.image.crop((topX,topY,bottomX,bottomY))
                        self.showImage()

    def Detail(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.showImage()

    def DoubleExposure(self):
        filter = "JPG (*.jpg);;PNG (*.png);;JPEG (*.jpeg)"
        name = QFileDialog.getOpenFileName(self, 'Select Image', '', filter)
        try:
            image = Image.open(name[0])
            if self.image.width > image.width :
                self.image = self.image.resize((image.width , image.height),Image.ANTIALIAS)
            else:
                image = image.resize((self.image.width,self.image.height),Image.ANTIALIAS)
            R,G,B = self.image.split()
            r,g,b = image.split()
            self.image = Image.merge("RGB",(R,g,B))
            self.showImage()
        except:
            pass

    def PasteImage(self):
        filter = "JPG (*.jpg);;PNG (*.png);;JPEG (*.jpeg)"
        name = QFileDialog.getOpenFileName(self, 'Select Images', '', filter)
        try:
            image = Image.open(name[0])
            x , pressed = QInputDialog.getInt(self,"Coordinate","X",1,1,self.image.width,1)
            if pressed:
                y, pressed = QInputDialog.getInt(self, "Coordinate", "Y", 1, 1, self.image.height, 1)
                if pressed:
                    self.image.paste(image,(x,y))
                    self.showImage()
        except:
            pass

    def AddText(self):
        text , pressed = QInputDialog.getText(self,"Text","Text")
        if pressed:
            X , pressed = QInputDialog.getInt(self,"Position","X",1,1,self.image.width,1)
            if pressed:
                Y, pressed = QInputDialog.getInt(self, "Position", "Y", 1, 1, self.image.height, 1)
                if pressed:
                    size , pressed = QInputDialog.getInt(self,"Size","Font Size",200,1,99999,1)
                    if pressed:
                        red, pressed = QInputDialog.getInt(self, "RGB", "Red Channel", 255, 1, 255, 1)
                        if pressed:
                            green, pressed = QInputDialog.getInt(self, "RGB", "Green Channel", 255, 1, 255, 1)
                            if pressed:
                                blue, pressed = QInputDialog.getInt(self, "RGB", "Blue Channel", 255, 1, 255, 1)
                                if pressed:
                                    draw = ImageDraw.Draw(self.image)
                                    font = ImageFont.truetype("ABeeZee-Regular.otf", size)
                                    draw.text((100, 100), "Hello World", (red, green, blue), font=font)
                                    self.showImage()

if __name__ == '__main__':
    app = QApplication([])
    obj = Editor('C:/Users/kshit/OneDrive/तस्विरहरू/Saved pictures/fabian-grohs-dC6Pb2JdAqs-unsplash.jpg')
    app.exec_()
