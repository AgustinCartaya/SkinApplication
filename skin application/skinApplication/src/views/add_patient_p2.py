from .view_object import *
from .ui.ui_add_patient_p2 import Ui_add_patient_p2

from src.objects.patient import Patient


class AddPatientP2View(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()


    def load_ui(self):
        self.ui = Ui_add_patient_p2()
        self.ui.setupUi(self)
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

        # labels
        self.ui.lb_title.set_title(1)

        self.ui.i_hair_color.addItems(util.read_file_list("hair_color.txt"))
        self.ui.i_eye_color.addItems(util.read_file_list("eye_color.txt"))

    s_change_view = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_add.clicked.connect(self.add_patient)
        self.ui.bt_cancel.clicked.connect(self.cancel)
        self.ui.bt_back.clicked.connect(self.back)
        # created signals
        self.s_change_view.connect(self.MW.change_view)

    #no pulido
    def add_patient(self):
        try:  
#            patient = Patient(self.ui.i_first_name.text(),
#                self.ui.i_last_name.text(),
#                self.ui.i_birth_date.date().toString("dd-MM-yyyy"),
#                int(self.ui.i_gender_m.isChecked()))
#            patient.save_data()
            self.s_change_view.emit(cfg.ADD_PATIENT_P2_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            print(err.args)
        
    def cancel(self):
        self.s_change_view.emit(cfg.ADD_PATIENT_P2_VIEW, cfg.PATIENTS_VIEW, None)

    def back(self):
        self.s_change_view.emit(cfg.ADD_PATIENT_P2_VIEW, cfg.ADD_PATIENT_VIEW, None)
