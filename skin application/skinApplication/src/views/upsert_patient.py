from .view_object import *
from .ui.ui_upsert_patient import Ui_upsert_patient
from PySide6.QtCore import QDate

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
        self.ui.i_first_name.setValidator(self.create_text_validator(data_cleaner.regex_letters))
        self.ui.i_last_name.setValidator(self.create_text_validator(data_cleaner.regex_letters))

        self.ui.i_birth_date.setMaximumDate(QDate.currentDate())


        #buttons
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

        # labels
        self.ui.lb_title.set_title(1)


    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_next.clicked.connect(self.next)
        self.ui.bt_cancel.clicked.connect(self.cancel)

        self.ui.i_upsert_patient_mi_view.toggled.connect(self.rb_view)
        self.ui.i_upsert_patient_preview_view.toggled.connect(self.rb_view)

    def rb_view(self):
        if self.ui.i_upsert_patient_mi_view.isChecked():
            self.next()
        elif (self.ui.i_upsert_patient_preview_view.isChecked() and
            len(self.p.mi) > 0):
            self.__change_to_upsert_patient_view(3)
        self.ui.i_upsert_patient_view.setChecked(True)


    def catch_basic_info(self):
        if self.ui.i_gender_f.isChecked():
            gender = 0
        elif self.ui.i_gender_m.isChecked():
            gender = 1
        else:
            gender = 2


        self.p.initialize(self.p.id,
            self.ui.i_first_name.text(),
            self.ui.i_last_name.text(),
            self.ui.i_birth_date.date().toString("dd-MM-yyyy"),
            gender,
            self.p.mi
            )


    def next(self):
        self.__change_to_upsert_patient_view(2)

    def __change_to_upsert_patient_view(self, view):
        self.catch_basic_info()
        self.reset_inputs()
        try:
            # verify patient data
            self.p.verify_data()

            if view == 2:
                self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.UPSERT_PATIENT_MI_VIEW, {"patient":self.p, "mode":self.mode})
            else:
                self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.UPSERT_PATIENT_PREVIEW_VIEW, {"patient":self.p, "mode":self.mode})

        except ValueError as ve:
            err_msg = "ERROR"

            if ve.args[0] == err.EO_PATIENT_FIRST_NAME:
                self.ui.i_first_name.set_decorator("error")
                err_msg = "Invalid first name"

            elif ve.args[0] == err.EO_PATIENT_LAST_NAME:
                self.ui.i_last_name.set_decorator("error")
                err_msg = "Invalid last name"

            self.show_message(err_msg, cfg.MSG_ERROR)
            print(ve.args)

    def cancel(self):
        if self.mode == "edit":
            self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id": self.p.id})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)

    def charge_edit_mode(self):
        self.ui.lb_title.setText(tf.f("Edit patient"))

        self.ui.i_first_name.setText(tf.f(self.p.first_name, translate=False))
        self.ui.i_last_name.setText(tf.f(self.p.last_name, translate=False))
        self.ui.i_birth_date.setDate(QDate.fromString(self.p.birth_date.strftime('%d-%m-%Y'), "dd-MM-yyyy"))
        if self.p.gender == 0:
            self.ui.i_gender_f.setChecked(True)
        elif self.p.gender == 1:
            self.ui.i_gender_m.setChecked(True)
        else:
            self.ui.i_gender_o.setChecked(True)


    def reset_inputs(self):
        self.ui.i_first_name.set_decorator(None)
        self.ui.i_last_name.set_decorator(None)

    def fill_default_test(self):
        self.ui.i_first_name.setText('Agustin')
        self.ui.i_last_name.setText('Cartaya')
        self.ui.i_birth_date.setDate(QDate.fromString('10-11-2000', "dd-MM-yyyy"))
        self.ui.i_gender_m.setChecked(True)
