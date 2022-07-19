# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_create_account import Ui_create_account

class CreateAccount(QtWidgets.QWidget):
    def __init__(self):
        super(CreateAccount, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_create_account()
        self.ui.setupUi(self)
