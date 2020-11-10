import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class CheckDemo(QWidget):
    def __init__(self, parent = None):
        super(CheckDemo, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        fbox = QFormLayout()
        layout = QHBoxLayout()
        label_name = QLabel("Name")
        label_lib = QLabel("Library")
        self.edit_name = QLineEdit()
        fbox.addRow(label_name, self.edit_name)
        self.b1 = QCheckBox("PyQt")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda:self.chk_state(self.b1))

        self.b2 = QCheckBox("PyGame")
        self.b2.toggled.connect(lambda:self.chk_state(self.b2))

        self.b3 = QCheckBox("PyTorch")
        self.b3.toggled.connect(lambda:self.chk_state(self.b3))

        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        layout.addWidget(self.b3)
        layout.addStretch()
        fbox.addRow(QLabel("Library"), layout)

        layout = QHBoxLayout()
        layout.addStretch(1)
        submit = QPushButton("Submit")
        submit.clicked.connect(lambda:self.chk_click())
        layout.addWidget(submit)
        layout.addWidget(QPushButton("Cancel"))
        fbox.addRow(layout)
        self.setLayout(fbox)
        self.setWindowTitle("checkbox demo")
        self.show()

    def chk_state(self, b):
        if b.isChecked() == True:
            print(b.text()+" is selected")
        else:
            print(b.text()+" is deselected")

    def chk_click(self):
        print(f"Name is {self.edit_name.text()}")

def maiin():
    app = QApplication(sys.argv)
    ex = CheckDemo()
    sys.exit(app.exec_())

if __name__ == '__main__':
    maiin()
