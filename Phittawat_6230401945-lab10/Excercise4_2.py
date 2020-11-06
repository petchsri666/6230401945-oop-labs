import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Caltrack_into(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap('app-icon_small.png')
        label.setPixmap(pixmap)

        self.welcome = QLabel("Welcome to CALTRACK")
        self.welcome.setFont(QFont("Arial", 12))
        self.welcome.setStyleSheet("background-color : yellow")
        self.welcome.move(100, 80)
        ok_bt = QPushButton("OK")
        ok_bt.setStyleSheet("background-color : yellow")
        ok_bt.setFont(QFont("Arial", 12))


        self.setCentralWidget(label)
        self.resize(300, 300)
        self.setWindowTitle("Caltrack INTRO DEMO")
        self.setWindowIcon(QIcon("app-icon.png"))
        self.show()


def mains():
    app = QApplication(sys.argv)
    ex = Caltrack_into()
    app.exec_()

if __name__ == '__main__':
    mains()

