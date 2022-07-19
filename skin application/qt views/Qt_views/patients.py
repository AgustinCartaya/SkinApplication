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

        self.ui.bt_add_new_patient.set_position(2)

        # organizer

        self.ui.bt_organizer_1.select(True)
        self.ui.bt_organizer_3.select(True)
        self.ui.bt_organizer_5.select(True)

        g1 = [self.ui.bt_organizer_1, self.ui.bt_organizer_2]
        g2 = [self.ui.bt_organizer_3, self.ui.bt_organizer_4]
        g3 = [self.ui.bt_organizer_5, self.ui.bt_organizer_6]

        self.ui.bt_organizer_1.add_group(g1)
        self.ui.bt_organizer_2.add_group(g1)
        self.ui.bt_organizer_3.add_group(g2)
        self.ui.bt_organizer_4.add_group(g2)
        self.ui.bt_organizer_5.add_group(g3)
        self.ui.bt_organizer_6.add_group(g3)


