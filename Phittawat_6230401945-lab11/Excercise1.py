import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class FromLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label_simplefrom = QLabel("Simple From")
        label_simplefrom.setFont(QFont("Rhinos rocks", 18))
        label_simplefrom.setStyleSheet("color : blue")
        label_simplefrom.setStyleSheet("background-color : red")
        label_name = QLabel("Name")
        edit_name = QLineEdit()
        edit_name.setMinimumWidth(250)

        fbox = QFormLayout()
        fbox.addWidget(label_simplefrom)
        fbox.addRow(label_name, edit_name)
        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        hbox.addWidget(radio_male)
        hbox.addWidget(radio_female)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Summit"))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.setLayout(fbox)
        self.setWindowTitle("Simple from")
        self.show()

def maiin():
    app = QApplication(sys.argv)
    from_layout = FromLayout()
    sys.exit(app.exec_())

if __name__ == '__main__':
    maiin()