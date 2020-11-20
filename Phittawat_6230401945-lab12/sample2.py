import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.init_value2 = 50
        self.button = None
        self.slieder = QSlider(Qt.Horizontal, self)
        self.slieder2 = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        self.init_ui()

    def init_ui(self):
        fromlayout = QFormLayout()
        self.sliederss(self.slieder, self.label)
        fromlayout.addRow(self.label, self.slieder)

        self.sliederss(self.slieder2, self.label2)
        fromlayout.addRow(self.label2, self.slieder2)

        grid = QHBoxLayout()
        self.add_button = QPushButton("ADD")
        self.add_button.clicked.connect(self.toggle_state)
        self.sub_button = QPushButton("SUBTRACT")
        self.sub_button.clicked.connect(self.toggle_state)
        self.mul_button = QPushButton("MULTIPLY")
        self.mul_button.clicked.connect(self.toggle_state)
        self.div_button = QPushButton("DIVIDE")
        self.div_button.clicked.connect(self.toggle_state)
        grid.addWidget(self.add_button)
        grid.addWidget(self.sub_button)
        grid.addWidget(self.mul_button)
        grid.addWidget(self.div_button)
        fromlayout.addRow(None, grid)

        self.label3 = QLabel("Result")
        self.label3_edit = QLineEdit()
        self.label3_edit.setMinimumSize(100, 25)
        self.label3_edit.setStyleSheet("color : yellow ; background-color : gray")
        self.label3_edit.setFont(QFont("Arial", 25))
        self.label3_edit.setAlignment(Qt.AlignRight)
        self.label3_edit.setEnabled(False)
        fromlayout.addRow(self.label3, self.label3_edit)

        self.setLayout(fromlayout)
        self.adjustSize()
        self.setWindowTitle("Simple Calculator")
        self.show()

    def sliederss(self, sliederf, labelf):
        sliederf.setMinimum(0)
        sliederf.setMaximum(100)
        sliederf.setValue(50)
        sliederf.setTickPosition(QSlider.TicksRight)
        sliederf.setTickInterval(5)
        sliederf.setGeometry(100, 40, 300, 50)
        sliederf.valueChanged[int].connect(self.changed_value)

        labelf.setText(str(self.init_value))
        labelf.setFont(QFont("Arial", 20))
        labelf.setStyleSheet("color : blue")
        labelf.setGeometry(10, 40, 300, 50)

    def changed_value(self, value):
        sender = self.sender()
        update_value = value
        if sender == self.slieder:
            self.label.setText(str(update_value))
            self.init_value = update_value
            self.val = value
        elif sender == self.slieder2:
            self.label2.setText(str(update_value))
            self.init_value2 = update_value
            self.val2 = value
        self.caculate()

    def caculate(self):
        if self.button == 0:
            sum = int(self.init_value + self.init_value2)
            self.label3_edit.setText(str(sum))
        elif self.button == 1:
            sum = int(self.init_value - self.init_value2)
            self.label3_edit.setText(str(sum))
        elif self.button == 2:
            sum = int(self.init_value * self.init_value2)
            self.label3_edit.setText(str(sum))
        elif self.button == 3:
            try:
                sum = int(self.init_value / self.init_value2)
                self.label3_edit.setText(str(sum))
            except:
                self.label3_edit.setText("Cant divide by 0!")

    def toggle_state(self):
        sender = self.sender()
        if sender.text() == "ADD":
            self.add_button.setStyleSheet("background-color : green")
            self.button = 0
        else:
            self.add_button.setStyleSheet("background-color : white")
        if sender.text() == "SUBTRACT":
            self.sub_button.setStyleSheet("background-color : green")
            self.button = 1
        else:
            self.sub_button.setStyleSheet("background-color : white")
        if sender.text() == "MULTIPLY":
            self.mul_button.setStyleSheet("background-color : green")
            self.button = 2
        else:
            self.mul_button.setStyleSheet("background-color : white")
        if sender.text() == "DIVIDE":
            self.div_button.setStyleSheet("background-color : green")
            self.button = 3
        else:
            self.div_button.setStyleSheet("background-color : white")
        self.caculate()

def mains():
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

if __name__ == '__main__':
    mains()
