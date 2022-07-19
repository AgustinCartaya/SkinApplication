# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_login import Ui_login

class Login(QtWidgets.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_login()
        self.ui.setupUi(self)
