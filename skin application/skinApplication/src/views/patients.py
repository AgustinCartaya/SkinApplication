from .view_object import *
from .ui.ui_patients import Ui_patients

class Patients(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()

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


    s_change_view = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_add_new_patient.clicked.connect(self.add_new_patient)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def back(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.LOGIN_VIEW, None)

    def add_new_patient(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.ADD_PATIENT_VIEW, None)
