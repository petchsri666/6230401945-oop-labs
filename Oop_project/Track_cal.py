import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from Project import Menu

class Caltrack(QWidget):
    def __init__(self):
        self.counter_col = 1
        self.counter_row = 0
        self.sum = 0
        super().__init__()
        self.initUI()


    def initUI(self):
        food = QLabel("Food")
        food.setFont(QFont("Arial", 8))
        food.setStyleSheet("color : yellow")
        self.food_edit = QLineEdit()
        calrolies = QLabel("Calories of food")
        calrolies.setFont(QFont("Arial", 8))
        calrolies.setStyleSheet("color : yellow")
        self.calories_edit = QLineEdit()
        tdee_label = QLabel(f"Total daily energy expenditure: {self.get_tdee():.2f}")
        tdee_label.setFont(QFont("Arial", 8))
        tdee_label.setStyleSheet("color : yellow")
        total_food = QLabel("Total Calories")
        total_food.setFont(QFont("Arial", 8))
        total_food.setStyleSheet("color : yellow")
        self.total_food_show = QLineEdit()
        self.total_food_show.setEnabled(False)
        self.total_food_show.setMinimumSize(100, 150)
        self.total_food_show.setStyleSheet("background-color : black")
        self.total_food_cal = QLabel(f"Total calories of foods: {self.sum:.2f}")
        self.total_food_cal.setFont(QFont("Arial", 8))
        self.total_food_cal.setStyleSheet("color : yellow")
        self.calories_left = QLabel(f"Calories left: ")
        self.calories_left.setFont(QFont("Arial", 8))
        self.calories_left.setStyleSheet("color : yellow")
        ok_button = QPushButton("OK")
        ok_button.setFont(QFont("Arial", 8))
        ok_button.setStyleSheet("background-color : yellow")
        ok_button.clicked.connect(lambda: self.calculate_food())
        back_to_menu = QPushButton("BACK TO MENU")
        back_to_menu.clicked.connect(self.back_to_menu)
        back_to_menu.setFont(QFont("Arial", 8))
        back_to_menu.setStyleSheet("background-color : yellow")

        self.table = QTableWidget()
        self.table.setRowCount(100)
        self.table.setColumnCount(2)
        self.table.setEnabled(True)

        self.table.setItem(0, 0, QTableWidgetItem("Foods"))
        self.table.setItem(0, 1, QTableWidgetItem("Calories"))

        formlayout = QFormLayout()
        formlayout.addWidget(food)
        formlayout.addWidget(self.food_edit)
        formlayout.setSpacing(20)
        formlayout.addWidget(calrolies)
        formlayout.addWidget(self.calories_edit)
        formlayout.addWidget(tdee_label)
        formlayout.addWidget(self.total_food_cal)
        formlayout.addWidget(self.calories_left)
        formlayout.addWidget(total_food)
        formlayout.addWidget(self.table)
        formlayout.addWidget(ok_button)
        formlayout.addWidget(back_to_menu)

        background = QtGui.QImage('background.png')
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(background))

        self.setPalette(palette)
        self.setLayout(formlayout)
        self.setWindowTitle('TRACK CAL')
        self.setWindowIcon(QIcon("app-icon.png"))
        self.setFixedSize(400, 600)
        self.show()

    def calculate_food(self):
        self.dict_food()
        self.total_food_show.setText(str(self.dict))
        self.set_data()
        self.sum_calories()

    def sum_calories(self):
        try:
            if self.calories_edit.text() == int or float:
                for row, item_list in enumerate(self.dict):
                    self.sum = float(self.dict[item_list]) + self.sum
                    self.total_food_cal.setText(f"Total calories of foods: {self.sum}")
                    self.calories_left_def()
            else:
                reply = QMessageBox.question(self, f"Error 499",
                                             f"Your value error!",
                                             QMessageBox.Ok)
        except Exception:
            reply = QMessageBox.question(self, f"Error 500",
                                         f"Your value error!",
                                         QMessageBox.Ok)
    def calories_left_def(self):
        tdee = self.read_tdee_txt
        cal_left = tdee - self.sum
        self.calories_left.setText(f"Calories left: {cal_left:.2f}")

    def get_tdee(self):
        f = open("Tdee.txt", "r")
        self.read_tdee_txt = float(f.read())
        return self.read_tdee_txt

    def set_data(self):
        try:
            if self.calories_edit.text() == int or float:
                for row, item_list in enumerate(self.dict):
                    newitem1 = QTableWidgetItem(self.dict[item_list])
                    newitem2 = QTableWidgetItem(item_list)
                    self.table.setItem(self.counter_col, self.counter_row, newitem2)
                    self.counter_row += 1
                    self.table.setItem(self.counter_col, self.counter_row, newitem1)
                    self.counter_col += 1
                    self.counter_row = 0
            else:
                reply = QMessageBox.question(self, f"Error 501",
                                             f"Your value error!",
                                             QMessageBox.Ok)
        except Exception:
            reply = QMessageBox.question(self, f"Error 502",
                                         f"Your value error!",
                                         QMessageBox.Ok)

    def dict_food(self):
            self.dict = {}
            self.dict[self.food_edit.text()] = self.calories_edit.text()

    def back_to_menu(self):
        self.start = Menu.Menu_bar()
        self.start.show()
        self.close()

def mains():
    app = QApplication(sys.argv)
    ex = Caltrack()
    app.exec_()


if __name__ == '__main__':
    mains()
