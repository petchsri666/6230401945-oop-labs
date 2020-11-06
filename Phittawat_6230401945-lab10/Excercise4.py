import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *


class Caltrack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        name = QLabel('Name ')
        age = QLabel('Age ')
        weight = QLabel('Weight ')
        height = QLabel('Height ')
        gender = QLabel('Gender ')
        ex_fq = QLabel('Exercise frequency ')
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        name.setFont(QFont("Arial", 8))
        name.setStyleSheet("color : yellow")
        age.setFont(QFont("Arial", 8))
        age.setStyleSheet("color : yellow")
        weight.setFont(QFont("Arial", 8))
        weight.setStyleSheet("color : yellow")
        height.setFont(QFont("Arial", 8))
        height.setStyleSheet("color : yellow")
        gender.setFont(QFont("Arial", 8))
        gender.setStyleSheet("color : yellow")
        ex_fq.setFont(QFont("Arial", 8))
        ex_fq.setStyleSheet("color : yellow")
        ok_button.setFont(QFont("Arial", 8))
        ok_button.setStyleSheet("background-color : yellow")
        cancel_button.setFont(QFont("Arial", 8))
        cancel_button.setStyleSheet("background-color : yellow")

        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        weightEdit = QLineEdit()
        heightEdit = QLineEdit()
        genderEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1, 1, 2)

        grid.addWidget(age, 2, 0)
        grid.addWidget(ageEdit, 2, 1, 1, 2)

        grid.addWidget(weight, 3, 0)
        grid.addWidget(weightEdit, 3, 1, 1, 2)

        grid.addWidget(height, 4, 0)
        grid.addWidget(heightEdit, 4, 1, 1, 2)

        grid.addWidget(gender, 5, 0)
        grid.addWidget(genderEdit, 5, 1, 1, 2)

        grid.addWidget(ok_button, 9, 1)
        grid.addWidget(cancel_button, 9, 2)

        grid.addWidget(ex_fq, 6, 0)
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 150, 150, 30)
        ex_fq_list = ["-", "Never", "Seldom", "Sometimes", "Often", "Sportsman"]
        self.combo_box.setEditable(True)
        self.combo_box.addItems(ex_fq_list)
        #self.combo_box.activated.connect(self.do_someting)
        grid.addWidget(self.combo_box, 6, 1, 1, 2)

        background = QtGui.QImage('background.png')
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(background))

        self.setPalette(palette)
        self.setLayout(grid)
        self.setWindowTitle('CALTRACK DEMO VERSION')
        self.setWindowIcon(QIcon("app-icon.png"))
        self.resize(300, 300)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def mains():
    app = QApplication(sys.argv)
    ex = Caltrack()
    app.exec_()


if __name__ == '__main__':
    mains()
