from .view_object import *
from .ui.ui_add_patient_preview import Ui_add_patient_preview

from src.objects.patient import Patient


from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QLineEdit,QGridLayout, QLabel, QComboBox)

class AddPatientPreiewView(ViewObject):
    def __init__(self, mw, p_info):
        super().__init__(mw)
        self.p_info = p_info

        self.load_ui()
        self.connect_ui_signals()
        self.show_information()

        #test
#        self.fill_default_test()

    def load_ui(self):
        self.ui = Ui_add_patient_preview()
        self.ui.setupUi(self)
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

#        self.ui.i_first_name.setValidator(self.create_text_validator(data_cleaner.regex_name))
#        self.ui.i_last_name.setValidator(self.create_text_validator(data_cleaner.regex_name))

#        # labels
        self.ui.lb_title.set_title(1)
        self.ui.lb_basic_information_title.set_title(2)
        self.ui.lb_medical_information_title.set_title(2)

        # medical information frame
        self.c_medical_information_layout = QVBoxLayout(self.ui.c_medical_information)
        self.c_medical_information_layout.setSpacing(16)
        self.c_medical_information_layout.setContentsMargins(0, 0, 0, 0)



    def show_information(self):
        self.show_basic_information()
        self.show_medical_information()

    def show_basic_information(self):
        self.ui.i_first_name.setText(self.p_info["basic_info"]["first_name"])
        self.ui.i_last_name.setText(self.p_info["basic_info"]["last_name"])
        self.ui.i_birth_date.setText(self.p_info["basic_info"]["birth_date"])
        if self.p_info["basic_info"]["gender"]:
            self.ui.i_gender.setText("Male")
        else:
            self.ui.i_gender.setText("Female")


    def show_medical_information(self):
        for medical_info in self.p_info["medical_info"]:
            mi_frame = QFrame(self.ui.c_medical_information)
            mi_frame_layout = QVBoxLayout(mi_frame)
            mi_frame_layout.setContentsMargins(0, 0, 0, 0)

            mi_title = QLabel(mi_frame)
            mi_title.setText(util.file_name_to_title(medical_info))
            mi_frame_layout.addWidget(mi_title)

            mi_content = QLabel(mi_frame)
            mi_content.setText(self.p_info["medical_info"][medical_info])
            mi_frame_layout.addWidget(mi_content)

            self.c_medical_information_layout.addWidget(mi_frame)

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_add.clicked.connect(self.add_patient)
        self.ui.bt_cancel.clicked.connect(self.cancel)
        self.ui.bt_back.clicked.connect(self.back)

        self.ui.i_add_patient_view.toggled.connect(self.rb_view)
        self.ui.i_add_patient_mi_view.toggled.connect(self.rb_view)
        # created signals
        self.s_change_view.connect(self.MW.change_view)


    def rb_view(self):
        if self.ui.i_add_patient_view.isChecked():
            self.__change_to_add_patient_view(1)
        elif self.ui.i_add_patient_mi_view.isChecked():
            self.back()
        self.ui.i_add_patient_preview_view.setChecked(True)

    def __change_to_add_patient_view(self, view):
        if view == 1:
            self.s_change_view.emit(cfg.ADD_PATIENT_PREVIEW_VIEW, cfg.ADD_PATIENT_VIEW, self.p_info)
        else:
            self.s_change_view.emit(cfg.ADD_PATIENT_PREVIEW_VIEW, cfg.ADD_PATIENT_MI_VIEW, self.p_info)



    #no pulido
    def add_patient(self):
        try:  
            print(self.p_info)
            patient = Patient(self.p_info["basic_info"]["first_name"],
                self.p_info["basic_info"]["last_name"],
                self.p_info["basic_info"]["birth_date"],
                self.p_info["basic_info"]["gender"],
                self.p_info["medical_info"])
            patient.save_data()
            self.s_change_view.emit(cfg.ADD_PATIENT_PREVIEW_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            print(err.args)
        

    def cancel(self):
        self.s_change_view.emit(cfg.ADD_PATIENT_PREVIEW_VIEW, cfg.PATIENTS_VIEW, None)

    @Slot()
    def back(self):
        self.__change_to_add_patient_view(2)

