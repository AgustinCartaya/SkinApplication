# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_add_patient import Ui_add_patient

class AddPatient(QtWidgets.QWidget):
    def __init__(self):
        super(AddPatient, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_add_patient()
        self.ui.setupUi(self)
