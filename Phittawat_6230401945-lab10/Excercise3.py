import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Excercise3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        btn = QPushButton('OK', self)
        btn.setToolTip('Click to OK')
        btn1 = QPushButton('CANCEL', self)
        btn1.setToolTip('Click to CANCEL')


        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1, 1, 3)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1, 1, 3)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 3)

        grid.addWidget(btn, 8, 2)
        grid.addWidget(btn1, 8, 3)

        self.setLayout(grid)
        self.resize(600, 500)
        self.setWindowTitle(f"Review by {sys.argv[1]}")
        self.show()



def main():
    app = QApplication(sys.argv)
    ex = Excercise3()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
