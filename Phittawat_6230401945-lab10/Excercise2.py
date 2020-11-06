import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Excercise2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.resize(800, 500)
        self.setWindowTitle("Excercise 2")
        self.show()

        menubar = self.menuBar()

        flie_menu = menubar.addMenu("File")

        imp_menu = QMenu("Edit", self)
        imp_act = QAction("Copy", self)
        imp_act2 = QAction("Paste", self)

        imp_menu.addAction(imp_act)
        imp_menu.addAction(imp_act2)

        new_act = QAction("New", self)

        flie_menu.addAction(new_act)
        flie_menu.addMenu(imp_menu)


        exit_act = QAction(QIcon("icon.png"), "Exit", self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.setStatusTip("Exit application")
        save_act = QAction(QIcon("icon.png"), "Save", self)
        save_act.setShortcut("Ctrl+S")
        save_act.setStatusTip("Save application")
        self.statusBar().addPermanentWidget(QLabel(f"By {sys.argv[1]}"), 1)
        exit_act.triggered.connect(QApplication.instance().quit)

        flie_menu.addAction(save_act)
        flie_menu.addAction(exit_act)

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
    ex = Excercise2()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
