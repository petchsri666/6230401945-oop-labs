import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pathlib import Path

class Sample3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.edit = QTextEdit()
        self.fbox = QFormLayout()
        self.init_ui()
        self.bg_color = ""
        self.font_color = ""
        self.file_path = ""

    def init_ui(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = QMenu('Edit', self)

        color_menu = QMenu("Color", self)
        edit_menu.addMenu(color_menu)

        background_act = QAction("Background color", self)
        background_act.triggered.connect(self.background_update)
        foreground_act = QAction("Foreground color", self)
        foreground_act.triggered.connect(self.foreground_update)
        menubar.addMenu(edit_menu)
        color_menu.addAction(background_act)
        color_menu.addAction(foreground_act)

        font_act = QAction("Font", self)
        font_act.triggered.connect(self.change_font)
        edit_menu.addAction(font_act)

        open_act = QAction('Open', self)
        open_act.setShortcut("Ctrl+O")
        open_act.triggered.connect(self.opening)
        file_menu.addAction(open_act)

        save_act = QAction('Save', self)
        save_act.setShortcut("Ctrl+S")
        save_act.triggered.connect(self.saving)
        file_menu.addAction(save_act)

        self.edit.setFont(QFont("Arial", 16))
        self.setCentralWidget(self.edit)

        self.setLayout(self.fbox)
        self.resize(300, 200)
        self.setWindowTitle("File dialog")
        self.show()

    def saving(self):
        home = str(Path.home())
        name = QFileDialog.getSaveFileName(self, "Save files as...", home)
        if name[0]:
            with open(name[0], "w") as file:
                file.write(self.edit.toPlainText())

    def opening(self):
        home = str(Path.home())
        name = QFileDialog.getOpenFileName(self, "Open file", home)
        if name[0]:
            f = open(name[0], 'r')
            with f:
                data = f.read()
                self.edit.setText(data)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.edit.setFont(font)

    def background_update(self):
        self.bg_color = QColorDialog.getColor()
        try:
            self.edit.setStyleSheet(f"background-color: {self.bg_color.name()}; color: {self.font_color.name()}")
        except:
            self.edit.setStyleSheet(f"background-color: {self.bg_color.name()}")

    def foreground_update(self):
        self.font_color = QColorDialog.getColor()
        try:
            self.edit.setStyleSheet(f"background-color: {self.bg_color.name()}; color: {self.font_color.name()}")
        except:
            self.edit.setStyleSheet(f"background-color: {self.font_color.name()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sample3()
    sys.exit(app.exec_())
