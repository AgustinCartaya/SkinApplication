from .view_object import *
from .ui.ui_check_patient import Ui_check_patient

#from src.objects.patient_list import PatientList
from PySide6.QtWidgets import (QFormLayout, QVBoxLayout, QFrame)
from PySide6.QtCore import Qt

from .ui.promoted.label import Label
from .ui.promoted.skin_lesion_preview import SkinLesionPreview

from src.objects.patient import Patient

class CheckPatientView(ViewObject):
    def __init__(self, mw, patient_id):
        super().__init__(mw)

        self.load_patient(patient_id)
        self.load_ui()
        self.connect_ui_signals()

#        self.load_patients()
#        self.show_patients()

    def load_patient(self, patient_id):
        self.p = Patient.get_patient_by_id(patient_id)
#        self.p.load_skin_lesions()
#        print(self.p.to_string())

    def load_ui(self):
        self.ui = Ui_check_patient()
        self.ui.setupUi(self)

        #label
        self.ui.lb_title.set_title(1)
        self.ui.lb_patient_information.set_title(2)

        # basic information
        self.ui.i_first_name.setText(self.p.first_name)
        self.ui.i_last_name.setText(self.p.last_name)
        self.ui.i_age.setText(str(self.p.age))

        if self.p.gender:
            self.ui.i_gender.setText("Male")
        else:
            self.ui.i_gender.setText("Female")

        # navigator
        self.ui.bt_add_new_skin_part.set_position(2)

        # medical information
        self.c_mi_content_layout = QFormLayout(self.ui.c_mi_content)
        self.c_mi_content_layout.setVerticalSpacing(16)
        self.show_medical_information()

        # skin lesions preview
        self.skin_lesions_layout = QVBoxLayout(self.ui.c_skin_lesions)
        self.skin_lesions_layout.setSpacing(40)
        self.skin_lesions_layout.setContentsMargins(0, 0, 0, 0)
        for i in range(2):
            skp = SkinLesionPreview()
            self.skin_lesions_layout.addWidget(skp)


    def show_medical_information(self):
        form_index = 0
        for mi in self.p.mi:


            mi_title = Label(self.ui.c_mi_content)
            mi_title.setText(util.file_name_to_title(mi) + " :")
            self.c_mi_content_layout.setWidget(form_index, QFormLayout.LabelRole, mi_title)

#            mi_frame = QFrame(self.ui.c_mi_content)
#            mi_frame_layout = QVBoxLayout(mi_frame)
#            mi_frame_layout.setContentsMargins(0, 0, 0, 0)
#            self.c_mi_content_layout.setWidget(form_index, QFormLayout.FieldRole, mi_frame)

#            mi_content = Label(self.ui.c_mi_content)
#            mi_content.setText(self.p.mi[mi])
#            mi_content.set_decoration("mi_content")
#            mi_frame_layout.addWidget(mi_content,0, Qt.AlignLeft)

            mi_content = Label(self.ui.c_mi_content)
            mi_content.setText(self.p.mi[mi])
            self.c_mi_content_layout.setWidget(form_index, QFormLayout.FieldRole, mi_content)


            form_index = form_index + 1

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        # navigator
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_edit_patient_info.clicked.connect(self.edit_patient_info)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    @Slot()
    def back(self):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)

    @Slot()
    def edit_patient_info(self):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.UPSERT_PATIENT_VIEW, {"patient" : self.p})
