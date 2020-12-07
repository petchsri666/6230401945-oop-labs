import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from Project import Demo_Project
from Project import Login
from Project import Menu


class Caltrack(QWidget):
    def __init__(self):
        self.a = 1
        self.b = 1
        super().__init__()
        self.initUI()

    def initUI(self):
        name = QLabel('Name ')
        age = QLabel('Age ')
        weight = QLabel('Weight ')
        height = QLabel('Height ')
        gender = QLabel('Gender ')
        ex_fq = QLabel('Exercise frequency ')
        goal = QLabel('Goal')
        cal_in = QLabel('Calories')
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.ok_button)
        cancel_button = QPushButton("Edit Profile")
        cancel_button.clicked.connect(self.edit_profile)
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
        goal.setFont(QFont("Arial", 8))
        goal.setStyleSheet("color : yellow")
        cal_in.setFont(QFont("Arial", 8))
        cal_in.setStyleSheet("color : yellow")
        ok_button.setFont(QFont("Arial", 8))
        ok_button.setStyleSheet("background-color : yellow")
        cancel_button.setFont(QFont("Arial", 8))
        cancel_button.setStyleSheet("background-color : yellow")
        status_pic = QPixmap("STATUS_PIC.png")
        label_status = QLabel()
        label_status.setPixmap(status_pic)
        label_status.setAlignment(Qt.AlignCenter)

        self.nameEdit = QLineEdit()
        self.nameEdit.setText(self.get_name())
        self.nameEdit.setEnabled(False)
        self.ageEdit = QLineEdit()
        self.ageEdit.setText(self.get_age())
        self.ageEdit.setEnabled(False)
        self.weightEdit = QLineEdit()
        self.weightEdit.setText(self.get_weight())
        self.weightEdit.setEnabled(False)
        self.heightEdit = QLineEdit()
        self.heightEdit.setText(self.get_height())
        self.heightEdit.setEnabled(False)
        self.genderEdit = QLineEdit()
        self.genderEdit.setText(self.get_gender())
        self.genderEdit.setEnabled(False)
        self.calEdit = QLineEdit()
        self.calEdit.setText(self.get_tdee())
        self.calEdit.setEnabled(False)


        grid = QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(label_status, 0, 1, 1, 1)

        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1, 1, 2)

        grid.addWidget(age, 2, 0)
        grid.addWidget(self.ageEdit, 2, 1, 1, 2)

        grid.addWidget(weight, 3, 0)
        grid.addWidget(self.weightEdit, 3, 1, 1, 2)

        grid.addWidget(height, 4, 0)
        grid.addWidget(self.heightEdit, 4, 1, 1, 2)

        hbox = QHBoxLayout()
        hbox.addStretch()
        grid.addWidget(gender, 5, 0)
        grid.addWidget(self.genderEdit, 5, 1, 1, 2)

        grid.addWidget(cal_in, 8, 0)
        grid.addWidget(self.calEdit, 8, 1, 1, 2)

        grid.addWidget(ok_button, 9, 1)
        grid.addWidget(cancel_button, 9, 2)

        grid.addWidget(ex_fq, 6, 0)
        self.label = QLabel()
        self.excercise_fre_edit = QLineEdit()
        self.excercise_fre_edit.setText(self.get_ex_fq())
        self.excercise_fre_edit.setEnabled(False)
        grid.addWidget(self.excercise_fre_edit, 6, 1, 1, 2)

        grid.addWidget(goal, 7, 0)
        self.goal_edit = QLineEdit()
        self.goal_edit.setText(self.get_goal())
        self.goal_edit.setEnabled(False)
        grid.addWidget(self.goal_edit, 7, 1, 1, 2)

        background = QtGui.QImage('background.png')
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(background))

        self.setPalette(palette)
        self.setLayout(grid)
        self.setWindowTitle('CALTRACK Status')
        self.setWindowIcon(QIcon("app-icon.png"))
        self.setFixedSize(400, 500)
        self.show()

    def get_name(self):
        f = open("Name.txt", "r")
        self.read_name_txt = f.read()
        return self.read_name_txt

    def get_age(self):
        f = open("Age.txt", "r")
        self.read_age_txt = f.read()
        return self.read_age_txt

    def get_height(self):
        f = open("Height.txt", "r")
        self.read_height_txt = f.read()
        return self.read_height_txt

    def get_weight(self):
        f = open("Weight.txt", "r")
        self.read_weight_txt = f.read()
        return self.read_weight_txt

    def get_gender(self):
        f = open("Gender.txt", "r")
        self.read_gender_txt = f.read()
        return self.read_gender_txt

    def get_ex_fq(self):
        f = open("Ex_fq.txt", "r")
        self.read_ex_txt = f.read()
        return self.read_ex_txt

    def get_goal(self):
        f = open("Goal.txt", "r")
        self.read_goal_txt = f.read()
        return self.read_goal_txt

    def get_tdee(self):
        f = open("Tdee.txt", "r")
        self.read_tdee_txt = f.read()
        return self.read_tdee_txt

    def ok_button(self):
        self.start = Menu.Menu_bar()
        self.start.show()
        self.close()

    def edit_profile(self):
        self.start = Demo_Project.Caltrack()
        self.start.show()
        self.close()

def mains():
    app = QApplication(sys.argv)
    ex = Caltrack()
    app.exec_()


if __name__ == '__main__':
    mains()
