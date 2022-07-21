from .view_object import *
from .ui.ui_patients import Ui_patients
from .ui.promoted.button import Button

import src.util.util as util
from src.objects.patient_list import PatientList

class Patients(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()
        self.load_patients()
        self.show_patients()

    def load_ui(self):
        self.ui = Ui_patients()
        self.ui.setupUi(self)

        self.ui.bt_add_new_patient.set_position(2)

        # organizer

        self.ui.bt_organizer_mosaico.set_icon(Button.IC_MOSAICO)
        self.ui.bt_organizer_list.set_icon(Button.IC_LIST)

        self.ui.bt_organizer_mosaico.select(True)
        self.ui.bt_organizer_asc.select(True)
        self.ui.bt_organizer_id.select(True)

        g1 = [self.ui.bt_organizer_mosaico, self.ui.bt_organizer_list]
        g2 = [self.ui.bt_organizer_asc, self.ui.bt_organizer_dsc]
        g3 = [self.ui.bt_organizer_id, self.ui.bt_organizer_name]

        self.ui.bt_organizer_mosaico.add_group(g1)
        self.ui.bt_organizer_list.add_group(g1)
        self.ui.bt_organizer_asc.add_group(g2)
        self.ui.bt_organizer_dsc.add_group(g2)
        self.ui.bt_organizer_id.add_group(g3)
        self.ui.bt_organizer_name.add_group(g3)

    def load_patients(self):
        self.p_list = PatientList()
        self.p_list.search_all_patients()
#        print(self.pl.to_string())

    s_change_view = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_add_new_patient.clicked.connect(self.add_new_patient)

        self.ui.bt_organizer_mosaico.clicked.connect(self.show_patients)
        self.ui.bt_organizer_list.clicked.connect(self.show_patients)
        self.ui.bt_organizer_asc.clicked.connect(self.show_patients)
        self.ui.bt_organizer_dsc.clicked.connect(self.show_patients)
        self.ui.bt_organizer_id.clicked.connect(self.show_patients)
        self.ui.bt_organizer_name.clicked.connect(self.show_patients)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    @Slot()
    def show_patients(self):
        self.filter_patients()
        self.organize_patients()
        self.ui.c_pagination.add_cards(self.p_organized)

    def filter_patients(self):
        self.p_list_filtered = self.p_list

    def organize_patients(self):
        if self.ui.bt_organizer_id.property("selected"):
            self.p_organized = self.p_list_filtered.get_list_of()
        else:
            self.p_organized = self.p_list_filtered.get_list_of("first_name")
        self.p_organized = util.sort_list(self.p_organized,
        self.ui.bt_organizer_asc.property("selected"))



    @Slot()
    def back(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.LOGIN_VIEW, None)

    @Slot()
    def add_new_patient(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.ADD_PATIENT_VIEW, None)
