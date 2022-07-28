from .view_object import *
from .ui.ui_upsert_patient import Ui_upsert_patient

from src.objects.patient import Patient
from datetime import datetime


class UpsertPatientView(ViewObject):
    def __init__(self, mw, patient = Patient(), mode="add"):
        super().__init__(mw)

        self.p = patient
        self.mode = mode
        self.load_ui()
        self.connect_ui_signals()

        if mode == "edit":
            self.charge_edit_mode()
        #test
        else:
            self.fill_default_test()


    def load_ui(self):
        self.ui = Ui_upsert_patient()
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

        self.ui.i_upsert_patient_mi_view.toggled.connect(self.rb_view)
        self.ui.i_upsert_patient_preview_view.toggled.connect(self.rb_view)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def rb_view(self):
        if self.ui.i_upsert_patient_mi_view.isChecked():
            self.next()
        elif (self.ui.i_upsert_patient_preview_view.isChecked() and
            len(self.p.mi) > 0):
            self.__change_to_upsert_patient_view(3)
        self.ui.i_upsert_patient_view.setChecked(True)

    def catch_basic_info(self):
        # if patient exists setting id = old id, else id = ""
        # if patient exists setting mi = old mi, else mi = {}
        self.p.initialize(self.p.id,
            self.ui.i_first_name.text(),
            self.ui.i_last_name.text(),
            self.ui.i_birth_date.date().toString("dd-MM-yyyy"),
            int(self.ui.i_gender_m.isChecked()),
            self.p.mi
            )
#        self.p_info["basic_info"]["first_name"] = self.ui.i_first_name.text()
#        self.p_info["basic_info"]["last_name"] = self.ui.i_last_name.text()
#        self.p_info["basic_info"]["birth_date"] = self.ui.i_birth_date.date().toString("dd-MM-yyyy")
#        self.p_info["basic_info"]["gender"] = int(self.ui.i_gender_m.isChecked())

    def next(self):
        self.__change_to_upsert_patient_view(2)

    def __change_to_upsert_patient_view(self, view):
        self.catch_basic_info()
        if view == 2:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.UPSERT_PATIENT_MI_VIEW, {"patient":self.p, "mode":self.mode})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.UPSERT_PATIENT_PREVIEW_VIEW, {"patient":self.p, "mode":self.mode})

    def cancel(self):
        if self.mode == "edit":
            self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id": self.p.id})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)

    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit patient")

        self.ui.i_first_name.setText(self.p.first_name)
        self.ui.i_last_name.setText(self.p.last_name)
        self.ui.i_birth_date.setDate(QDate.fromString(self.p.birth_date.strftime('%d-%m-%Y'), "dd-MM-yyyy"))
        if self.p.gender:
            self.ui.i_gender_m.setChecked(True)
        else:
            self.ui.i_gender_f.setChecked(True)

    def fill_default_test(self):
        self.ui.i_first_name.setText('Agustin')
        self.ui.i_last_name.setText('Cartaya')
        self.ui.i_birth_date.setDate(QDate.fromString('10-11-2000', "dd-MM-yyyy"))
        self.ui.i_gender_m.setChecked(True)
