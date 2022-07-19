# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from login import Login
from create_account import CreateAccount
from add_patient import AddPatient
from patients import Patients

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_style_sheet()
        self.load_ui()


    def load_ui(self):
#        self.setCentralWidget(Login())
#        self.setCentralWidget(CreateAccount())
#        self.setCentralWidget(AddPatient())
        self.setCentralWidget(Patients())

    def load_style_sheet(self):
        _file = open("styles.css")
        self.setStyleSheet( _file.read())


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
