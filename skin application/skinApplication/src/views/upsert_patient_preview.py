from .view_object import *
from .ui.ui_upsert_patient_preview import Ui_upsert_patient_preview

from src.objects.patient import Patient

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QLineEdit,QGridLayout, QComboBox)

from .ui.promoted.label import Label

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
        self.c_medical_information_layout = QVBoxLayout(self.ui.c_medical_information)
        self.c_medical_information_layout.setSpacing(16)
        self.c_medical_information_layout.setContentsMargins(0, 0, 0, 0)



    def show_information(self):
        self.show_basic_information()
        self.show_medical_information()

    def show_basic_information(self):
        self.ui.i_first_name.setText(self.p.first_name)
        self.ui.i_last_name.setText(self.p.last_name)
        self.ui.i_birth_date.setText(self.p.birth_date.strftime('%d-%m-%Y'))
        if self.p.gender:
            self.ui.i_gender.setText("Male")
        else:
            self.ui.i_gender.setText("Female")


    def show_medical_information(self):
        for medical_info in self.p.mi:
            mi_frame = QFrame(self.ui.c_medical_information)
            mi_frame_layout = QVBoxLayout(mi_frame)
            mi_frame_layout.setContentsMargins(0, 0, 0, 0)

            mi_title = Label(mi_frame)
            mi_title.setText(util.file_name_to_title(medical_info) + " :")
            mi_frame_layout.addWidget(mi_title)

            mi_content = Label(mi_frame)
            mi_content.setText(self.p.mi[medical_info])
            mi_content.set_decoration("mi_content")
            mi_frame_layout.addWidget(mi_content)

            self.c_medical_information_layout.addWidget(mi_frame,0, Qt.AlignLeft)

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
            self.p.save_data()
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
