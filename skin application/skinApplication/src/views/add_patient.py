from .view_object import *
from .ui.ui_add_patient import Ui_add_patient

from src.objects.patient import Patient


class AddPatientView(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)

        self.p_info = {"basic_info":{}, "medical_info":{} }

        self.load_ui()
        self.connect_ui_signals()

        #test
        self.fill_default_test()

    def load_ui(self):
        self.ui = Ui_add_patient()
        self.ui.setupUi(self)
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

        # inputs
        self.ui.i_first_name.setValidator(self.create_text_validator(data_cleaner.regex_name))
        self.ui.i_last_name.setValidator(self.create_text_validator(data_cleaner.regex_name))

        #buttons
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

        # labels
        self.ui.lb_title.set_title(1)

        

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_next.clicked.connect(self.next)
        self.ui.bt_cancel.clicked.connect(self.cancel)

        self.ui.i_add_patient_mi_view.toggled.connect(self.rb_view)
        self.ui.i_add_patient_preview_view.toggled.connect(self.rb_view)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def rb_view(self):
        if self.ui.i_add_patient_mi_view.isChecked():
            self.next()
        elif (self.ui.i_add_patient_preview_view.isChecked() and
            len(self.p_info["medical_info"]) > 0):
            self.__change_to_add_patient_view(3)
        self.ui.i_add_patient_view.setChecked(True)


    def catch_basic_info(self):
        self.p_info["basic_info"]["first_name"] = self.ui.i_first_name.text()
        self.p_info["basic_info"]["last_name"] = self.ui.i_last_name.text()
        self.p_info["basic_info"]["birth_date"] = self.ui.i_birth_date.date().toString("dd-MM-yyyy")
        self.p_info["basic_info"]["gender"] = int(self.ui.i_gender_m.isChecked())

    def next(self):
        self.__change_to_add_patient_view(2)

    def __change_to_add_patient_view(self, view):
        self.catch_basic_info()
        if view == 2:
            self.s_change_view.emit(cfg.ADD_PATIENT_VIEW, cfg.ADD_PATIENT_MI_VIEW, self.p_info)
        else:
            self.s_change_view.emit(cfg.ADD_PATIENT_VIEW, cfg.ADD_PATIENT_PREVIEW_VIEW, self.p_info)


    def cancel(self):
        self.s_change_view.emit(cfg.ADD_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)

    def fill_default_test(self):
        self.ui.i_first_name.setText('Agustin')
        self.ui.i_last_name.setText('Cartaya')
        self.ui.i_birth_date.setDate(QDate.fromString('10-11-2000', "dd-MM-yyyy"))
        self.ui.i_gender_m.setChecked(True)
