from .view_object import *
from .ui.ui_upsert_patient_preview import Ui_upsert_patient_preview

from src.objects.patient import Patient

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QLineEdit,QGridLayout, QComboBox)

from .ui.promoted.label import Label
from .ui.promoted.variable_input_creator import VariableInputCreator


class UpsertPatientPreiewView(ViewObject):
    def __init__(self, mw, patient, mode="add"):
        super().__init__(mw)

        self.p = patient
        self.mode = mode

        self.load_ui()
        self.connect_ui_signals()
        self.show_information()

        if mode == "edit":
            self.charge_edit_mode()

    def load_ui(self):
        self.ui = Ui_upsert_patient_preview()
        self.ui.setupUi(self)
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

#        self.ui.i_first_name.setValidator(self.create_text_validator(data_cleaner.regex_name))
#        self.ui.i_last_name.setValidator(self.create_text_validator(data_cleaner.regex_name))

#        # labels
        self.ui.lb_title.set_title(1)
        self.ui.lb_basic_information_title.set_title(2)
        self.ui.lb_medical_information_title.set_title(2)

        self.ui.i_first_name.set_decoration("mi_content")
        self.ui.i_last_name.set_decoration("mi_content")
        self.ui.i_birth_date.set_decoration("mi_content")
        self.ui.i_gender.set_decoration("mi_content")

        # medical information frame
#        self.mi_content_layout = QVBoxLayout(self.ui.c_medical_information)
#        self.mi_content_layout.setSpacing(16)
#        self.mi_content_layout.setContentsMargins(0, 0, 0, 0)



    def show_information(self):
        self.show_basic_information()
        self.show_medical_information()

    def show_basic_information(self):
        self.ui.i_first_name.setText(self.p.first_name)
        self.ui.i_last_name.setText(self.p.last_name)
        self.ui.i_birth_date.setText(self.p.birth_date.strftime('%d-%m-%Y'))
        if self.p.gender == 0:
            self.ui.i_gender.setText("Woman")
        elif self.p.gender == 1:
            self.ui.i_gender.setText("Man")
        else:
            self.ui.i_gender.setText("Other")


    def show_medical_information(self):
        for mi_name, mi_content in self.p.mi.items():
            ly_single_mi = QVBoxLayout()
            ly_single_mi.setSpacing(4)

            lb_mi_title = Label(self.ui.c_patient_information_preview)
            lb_mi_title.setText(mi_name, colon=True, format=True)
            ly_single_mi.addWidget(lb_mi_title)

            # scales to modify if possible
            if type(mi_content) in (int, float):
                if type(mi_content) == int:
                    mi_fine_name = mi_name + "." + VariableInputCreator.INPUT_INT
                else:
                    mi_fine_name = mi_name + "." + VariableInputCreator.INPUT_FLOAT
                scale = util.get_mi_mesure(mi_fine_name)
                if scale != "":
                    mi_content = util.to_sub_unit(mi_content, util.get_scale_units_and_multipliers(scale))
                    mi_content = " ".join([str(mi_content[0]), mi_content[1]])
            # ----------------------

            i_mi_content = Label(self.ui.c_patient_information_preview)
            i_mi_content.setText(mi_content)
            i_mi_content.set_decoration("mi_content")
            ly_single_mi.addWidget(i_mi_content)

            self.ui.ly_mi_content.addLayout(ly_single_mi)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_upsert.clicked.connect(lambda: self.update_patient() if (self.mode ==  "edit") else self.add_patient() )
        self.ui.bt_cancel.clicked.connect(self.cancel)
        self.ui.bt_back.clicked.connect(self.back)

        self.ui.i_upsert_patient_view.toggled.connect(self.rb_view)
        self.ui.i_upsert_patient_mi_view.toggled.connect(self.rb_view)
        # created signals
        self.s_change_view.connect(self.MW.change_view)


    def rb_view(self):
        if self.ui.i_upsert_patient_view.isChecked():
            self.__change_to_upsert_patient_view(1)
        elif self.ui.i_upsert_patient_mi_view.isChecked():
            self.back()
        self.ui.i_upsert_patient_preview_view.setChecked(True)

    def __change_to_upsert_patient_view(self, view):
        if view == 1:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_PREVIEW_VIEW, cfg.UPSERT_PATIENT_VIEW, None)
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_PREVIEW_VIEW, cfg.UPSERT_PATIENT_MI_VIEW, {"patient":self.p, "mode":self.mode})



    #no pulido
    def add_patient(self):
        try:  
            self.p.create_patient()
            self.s_change_view.emit(cfg.UPSERT_PATIENT_PREVIEW_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            print(err.args)
        
    def cancel(self):
        if self.mode == "edit":
            self.s_change_view.emit(cfg.UPSERT_PATIENT_PREVIEW_VIEW, cfg.CHECK_PATIENT_VIEW,  {"patient_id": self.p.id})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_PREVIEW_VIEW, cfg.PATIENTS_VIEW, None)

    def update_patient(self):
        try:
            self.p.update_data()
            self.s_change_view.emit(cfg.UPSERT_PATIENT_PREVIEW_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id": self.p.id})
        except ValueError as err:
            print(err.args)


    @Slot()
    def back(self):
        self.__change_to_upsert_patient_view(2)

    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit patient preview")
        self.ui.bt_upsert.setText("Save")
