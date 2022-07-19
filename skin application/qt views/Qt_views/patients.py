# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_patients import Ui_patients

class Patients(QtWidgets.QWidget):
    def __init__(self):
        super(Patients, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_patients()
        self.ui.setupUi(self)
