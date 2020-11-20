import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.col = QColor(0, 0, 0)
        self.square = QFrame(self)
        self.init_ui()

    def init_ui(self):
        redb = QPushButton("RED", self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.set_color)

        greenb = QPushButton("GREEN", self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.set_color)

        blueb = QPushButton("BLUE", self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.set_color)

        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget{ background-color: %s }" % self.col.name())
        self.setGeometry(300, 300, 300, 250)
        self.adjustSize()
        self.setWindowTitle("Toggle Button")
        self.show()

    def set_color(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == "RED":
            self.col.setRed(val)
        elif source.text() == "GREEN":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

def mains():
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

if __name__ == '__main__':
    mains()
