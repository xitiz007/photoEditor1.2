from PyQt5.Qt import QIcon,QLabel,QVBoxLayout,QWidget
class Description(QWidget):
    def __init__(self,image,path):
        super().__init__()
        self.setWindowIcon(QIcon('description.png'))
        self.setWindowTitle("Properties")
        vbox = QVBoxLayout()
        label = QLabel()
        label.setText("Path : " + path)
        vbox.addWidget(label)
        label2 = QLabel()
        label2.setText("Width : " + str(image.width) + " px")
        vbox.addWidget(label2)
        label3 = QLabel()
        label3.setText("Height : " + str(image.height) + " px")
        vbox.addWidget(label3)
        self.setLayout(vbox)
        self.show()
