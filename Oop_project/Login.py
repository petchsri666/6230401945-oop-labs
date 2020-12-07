import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from Project import Demo_Project
from Project import Menu

class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('CALTRACK')
		self.setFixedSize(300, 400)

		layout = QFormLayout()
		labelImage = QLabel()
		labelImage2 = QLabel()
		labelImage_name = QLabel()
		pixmap2 = QPixmap("CALTRACK2.png")
		pixmap = QPixmap("app-icon_smallest2.png")
		entername = QPixmap("Entername.png")
		labelImage2.setPixmap(pixmap)
		labelImage.setPixmap(pixmap2)
		labelImage_name.setPixmap(entername)

		labelImage2.setAlignment(Qt.AlignCenter)
		labelImage.setAlignment(Qt.AlignCenter)
		labelImage_name.setAlignment(Qt.AlignCenter)
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your name')
		layout.addRow(labelImage)
		layout.addRow(labelImage_name)
		layout.setVerticalSpacing(30)
		layout.addRow(self.lineEdit_username)


		button_login = QPushButton('Login', self)
		button_login.sizeHint()
		button_login.clicked.connect(self.check_password)
		button_login.setStyleSheet("background-color : yellow")
		layout.addRow(button_login)

		button_register = QPushButton('Quit', self)
		button_register.clicked.connect(self.quit_program)
		button_register.sizeHint()
		button_register.setStyleSheet("background-color : yellow")
		layout.addRow(button_register)

		background = QImage("background.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(background))

		self.setPalette(palette)
		self.setLayout(layout)
		self.setWindowIcon(QIcon("app-icon.png"))

	def check_password(self):
		if self.lineEdit_username.text() != "":
			self.write_files_name()
			self.login_button()
		else:
			reply = QMessageBox.question(self, f"Error 479",
										 f"Your value error!",
										 QMessageBox.Ok)
	def quit_program(self):
		app = QApplication
		app.quit()

	def login_button(self):
		self.start = Menu.Menu_bar()
		self.start.show()
		self.close()

	def return_name(self):
		return self.lineEdit_username.text()

	def write_files_name(self):
		f = open("Name.txt", "w")
		f.write(self.return_name())
		f.close()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = LoginForm()
	form.show()
	sys.exit(app.exec_())