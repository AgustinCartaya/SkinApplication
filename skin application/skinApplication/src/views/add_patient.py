from .view_object import *
from .ui.ui_add_patient import Ui_add_patient

from src.objects.patient import Patient


class AddPatientView(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()

        #test
        self.fill_default_test()

    def load_ui(self):
        self.ui = Ui_add_patient()
        self.ui.setupUi(self)
        

    mySignam = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_add.clicked.connect(self.add_patient)
        # created signals
        self.mySignam.connect(self.MW.change_view)

    #no pulido
    def add_patient(self):
        try:  
            patient = Patient(self.ui.i_first_name.text(),
                self.ui.i_last_name.text(),
                self.ui.i_birth_date.date().toString(),
                int(self.ui.i_gender_m.isChecked()))
            patient.save_data()
            self.mySignam.emit(cfg.ADD_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            print(err.args)
        

    def fill_default_test(self):
        self.ui.i_first_name.setText('Agustin')
        self.ui.i_last_name.setText('Cartaya')
        self.ui.i_birth_date.setDate(QDate.fromString('10-11-2000', "dd-MM-yyyy"))
        self.ui.i_gender_m.setChecked(True)
