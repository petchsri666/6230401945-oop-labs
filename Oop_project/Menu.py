import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from Project import Demo_Project
from Project import Status
from Project import Track_cal

class Menu_bar(QWidget):
    def __init__(self):
        self.a = 1
        self.b = 1
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QFormLayout()

        pixmap = QPixmap("app-icon_smallestttt.png")
        pixmap2 = QPixmap("CALTRACK-MENU.png")
        labelImage = QLabel()
        labelImage2 = QLabel()
        labelImage.setPixmap(pixmap)
        labelImage2.setPixmap(pixmap2)
        labelImage.setAlignment(Qt.AlignCenter)
        labelImage2.setAlignment(Qt.AlignCenter)
        calculate_button = QPushButton("CALCULATE")
        calculate_button.setFont(QFont("Arial", 8))
        calculate_button.setStyleSheet("background-color : yellow")
        calculate_button.clicked.connect(self.to_calculate)
        status_button = QPushButton("STATUS")
        status_button.setFont(QFont("Arial", 8))
        status_button.setStyleSheet("background-color : yellow")
        status_button.clicked.connect(self.to_status)
        track_cal = QPushButton("TRACK CALORIES")
        track_cal.setFont(QFont("Arial", 8))
        track_cal.setStyleSheet("background-color : yellow")
        track_cal.clicked.connect(self.to_track)
        back_to_menu = QPushButton("BACK TO MENU")
        back_to_menu.setFont(QFont("Arial", 8))
        back_to_menu.setStyleSheet("background-color : yellow")

        grid.addRow(labelImage)
        grid.addRow(labelImage2)
        grid.addRow(calculate_button)
        grid.addRow(status_button)
        grid.addRow(track_cal)
        #grid.addRow(back_to_menu)
        grid.setVerticalSpacing(25)

        background = QImage("background.png")
        palette = QPalette()
        palette.setBrush(10, QBrush(background))

        self.setLayout(grid)
        self.setPalette(palette)
        self.setWindowTitle('CALTRACK')
        self.setWindowIcon(QIcon("app-icon.png"))
        self.setFixedSize(300, 400)
        self.show()

    def to_calculate(self):
        self.start = Demo_Project.Caltrack()
        self.start.show()
        self.close()

    def to_status(self):
        self.start = Status.Caltrack()
        self.start.show()
        self.close()

    def to_track(self):
        self.start = Track_cal.Caltrack()
        self.start.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu_bar()
    app.exec_()