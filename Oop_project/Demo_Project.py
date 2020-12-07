import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from Project import Menu
from Project import Status
from Project import Login


class Caltrack(QWidget):
    def __init__(self):
        self.a = 1
        self.b = 1
        super().__init__()
        self.initUI()


    def initUI(self):
        age = QLabel('Age (Years old) ')
        weight = QLabel('Weight (Kg.)')
        height = QLabel('Height (Cm.) ')
        gender = QLabel('Gender ')
        ex_fq = QLabel('Exercise frequency ')
        goal = QLabel('Goal')
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Back to menu")
        cancel_button.clicked.connect(self.back_to_menu)
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
        ok_button.setFont(QFont("Arial", 8))
        ok_button.setStyleSheet("background-color : yellow")
        ok_button.clicked.connect(lambda:self.calculate())
        cancel_button.setFont(QFont("Arial", 8))
        cancel_button.setStyleSheet("background-color : yellow")


        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.weightEdit = QLineEdit()
        self.heightEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(age, 2, 0)
        grid.addWidget(self.ageEdit, 2, 1, 1, 2)

        grid.addWidget(weight, 3, 0)
        grid.addWidget(self.weightEdit, 3, 1, 1, 2)

        grid.addWidget(height, 4, 0)
        grid.addWidget(self.heightEdit, 4, 1, 1, 2)

        hbox = QHBoxLayout()
        self.radio_male = QRadioButton("Male")
        self.radio_male.setFont(QFont("Arial", 8))
        self.radio_male.setStyleSheet("color : yellow")
        self.radio_male.setChecked(True)
        self.radio_male.toggled.connect(lambda:self.isClicked(self.radio_male))
        self.radio_female = QRadioButton("Female")
        self.radio_female.setFont(QFont("Arial", 8))
        self.radio_female.setStyleSheet("color : yellow")
        self.radio_female.toggled.connect(lambda:self.isClicked(self.radio_female))
        hbox.addStretch()
        grid.addWidget(gender, 5, 0)
        grid.addWidget(self.radio_male, 5, 1, 1, 2)
        grid.addWidget(self.radio_female, 5, 2, 1, 2)

        grid.addWidget(ok_button, 10, 1)
        grid.addWidget(cancel_button, 10, 2)

        grid.addWidget(ex_fq, 6, 0)
        self.label = QLabel()
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 150, 150, 30)
        ex_fq_list = ["-", "Never   ", "Seldom  (1-2 times/week)",
                      "Sometimes    (3-5 times/week)", "Often   (6-7 times/week)",
                      "Sportsman    (10-14 times/week)"]
        self.combo_box.setEditable(True)
        self.combo_box.addItems(ex_fq_list)
        self.combo_box.activated.connect(lambda:self.Find())
        grid.addWidget(self.combo_box, 6, 1, 1, 2)

        grid.addWidget(goal, 7, 0)
        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(200, 150, 150, 30)
        goal_list = ["-", "Lose weight", "Maintain", "Gain weight"]
        self.combo_box2.setEditable(True)
        self.combo_box2.addItems(goal_list)
        self.combo_box2.activated.connect(lambda:self.Find2())
        grid.addWidget(self.combo_box2, 7, 1, 1, 2)

        background = QtGui.QImage('background.png')
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(background))

        self.setPalette(palette)
        self.setLayout(grid)
        self.setWindowTitle('CALTRACK DEMO VERSION')
        self.setWindowIcon(QIcon("app-icon.png"))
        self.setFixedSize(400, 600)
        self.show()

    def return_age(self):
        f = open("Age.txt", "w")
        f.write(self.ageEdit.text())
        f.close()

    def return_height(self):
        f = open("Height.txt", "w")
        f.write(self.heightEdit.text())
        f.close()

    def return_weight(self):
        f = open("Weight.txt", "w")
        f.write(self.weightEdit.text())
        f.close()

    def return_ex_fq(self):
        f = open("Ex_fq.txt", "w")
        f.write(self.content)
        f.close()

    def return_goal(self):
        f = open("Goal.txt", "w")
        f.write(self.content_goal)
        f.close()

    def after_calculate(self):
        f = open("Tdee.txt", "w")
        f.write(str(self.tdee))
        f.close()

    def return_gender(self, b):
        f = open("Gender.txt", "w")
        f.write(b.text())
        f.close()

    def read_name(self):
        f = open("Name.txt", "r")
        self.read_name_txt = f.read()
        return self.read_name_txt

    def back_to_menu(self):
        self.start = Menu.Menu_bar()
        self.start.show()
        self.close()

    def calculate(self):
        never_dif_lose = 500
        never_dif_gain = 300
        seldom_dif_lose = 600
        seldom_dif_gain = 350
        sometimes_dif_lose = 700
        sometimes_dif_gain = 400
        often_dif_lose = 800
        often_dif_gain = 420
        sportsman_dif_lose = 820
        sportsman_dif_gain = 500
        try:
            if self.a == 1:
                bmr = 66 + (13.7 * float(self.weightEdit.text())) + (5 * float(self.heightEdit.text())) - (6.8 * int(self.ageEdit.text()))
                if self.content == "Seldom  (1-2 times/week)":
                    tdee = bmr * 1.375
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (seldom_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)

                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (seldom_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Never   ":
                    tdee = bmr * 1.2
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (never_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (never_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Sometimes    (3-5 times/week)":
                    tdee = bmr * 1.55
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (sometimes_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (sometimes_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Often   (6-7 times/week)":
                    tdee = bmr * 1.725
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (often_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (often_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Sportsman    (10-14 times/week)":
                    tdee = bmr * 1.9
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (sportsman_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (sportsman_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

            elif self.b == 1:
                bmr = 65.5 + (9.6 * float(self.weightEdit.text())) + (5 * float(self.heightEdit.text())) - (4.7 * int(self.ageEdit.text()))
                if self.content == "Seldom  (1-2 times/week)":
                    tdee = bmr * 1.375
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (seldom_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (seldom_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Never   ":
                    tdee = bmr * 1.2
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (never_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (never_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Sometimes    (3-5 times/week)":
                    tdee = bmr * 1.55
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (sometimes_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (sometimes_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Often   (6-7 times/week)":
                    tdee = bmr * 1.725
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (often_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = tdee + (often_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                elif self.content == "Sportsman    (10-14 times/week)":
                    tdee = bmr * 1.9
                    if self.content_goal == "Lose weight":
                        self.tdee = tdee - (sportsman_dif_lose)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Maintain":
                        self.tdee = tdee
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee :.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    elif self.content_goal == "Gain weight":
                        self.tdee = (sportsman_dif_gain)
                        reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                                     f"{self.read_name()}'s total daily energy is : {self.tdee:.2f}\n"
                                                     f"[{self.read_name()}'s lowest energy need to take is : {bmr:.2f}]",
                                                     QMessageBox.Ok)
                    else:
                        reply = QMessageBox.question(self, f"Error !", f"Please enter your goal!", QMessageBox.Ok)

                else:
                    pass
            self.return_age()
            self.return_height()
            self.return_weight()
            self.return_ex_fq()
            self.return_goal()
            self.after_calculate()


        except Exception:
            reply = QMessageBox.question(self, f"Total daily energy expenditure",
                                         f"Value Error please try again......",
                                         QMessageBox.Ok)

    def isClicked(self, b):
        if b.text() == "Male":
            if b.isChecked() == True:
                self.a = 1
            else:
                self.a = 0
            self.return_gender(b)

        if b.text() == "Female":
            if b.isChecked() == True:
                self.b = 1
            else:
                self.b = 0
            self.return_gender(b)
    def Find(self):
        self.content = self.combo_box.currentText()
        self.label.setText(self.content)

    def Find2(self):
        self.content_goal = self.combo_box2.currentText()
        self.label.setText(self.content_goal)

def mains():
    app = QApplication(sys.argv)
    ex = Caltrack()
    app.exec_()


if __name__ == '__main__':
    mains()
