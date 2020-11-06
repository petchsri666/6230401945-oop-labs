import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Excercise1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('Click to exit')
        btn.resize(btn.sizeHint())
        btn.move(100, 100)


        self.label_1 = QLabel(f'My name is {sys.argv[1]}', self)
        self.label_1.setFont(QFont("Arial", 8))
        self.label_1.move(100, 80)
        self.resize(300, 200)
        self.setWindowTitle('Excercise 1')
        self.show()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerpoint)
        self.move(qtRectangle.topLeft())

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, "What",
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Excercise1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()