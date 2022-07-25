from .view_object import *
from .ui.ui_check_patient import Ui_check_patient

#from src.objects.patient_list import PatientList
from PySide6.QtWidgets import (QFormLayout, QVBoxLayout, QFrame)
from PySide6.QtCore import Qt

from .ui.promoted.label import Label
from .ui.promoted.skin_part_preview import SkinPartPreview

class CheckPatientView(ViewObject):
    def __init__(self, mw, patient):
        super().__init__(mw)

        self.patient = patient["patient"]

        self.load_ui()
        self.connect_ui_signals()

#        self.load_patients()
#        self.show_patients()

    def load_ui(self):
        self.ui = Ui_check_patient()
        self.ui.setupUi(self)

        # basic information
        self.ui.i_first_name.setText(self.patient.first_name)
        self.ui.i_last_name.setText(self.patient.last_name)
        self.ui.i_age.setText(str(self.patient.age))

        if self.patient.gender:
            self.ui.i_gender.setText("Male")
        else:
            self.ui.i_gender.setText("Female")

        # navigator
        self.ui.bt_add_new_skin_part.set_position(2)

        # medical information
        self.c_mi_content_layout = QFormLayout(self.ui.c_mi_content)
        self.c_mi_content_layout.setVerticalSpacing(16)
        self.show_medical_information()

        # skin part preview
        for i in range(1):
            skp = SkinPartPreview()
            self.ui.verticalLayout_4.addWidget(skp)


    def show_medical_information(self):
        form_index = 0
        for mi in self.patient.mi:


            mi_title = Label(self.ui.c_mi_content)
            mi_title.setText(util.file_name_to_title(mi) + " :")
            self.c_mi_content_layout.setWidget(form_index, QFormLayout.LabelRole, mi_title)

#            mi_frame = QFrame(self.ui.c_mi_content)
#            mi_frame_layout = QVBoxLayout(mi_frame)
#            mi_frame_layout.setContentsMargins(0, 0, 0, 0)
#            self.c_mi_content_layout.setWidget(form_index, QFormLayout.FieldRole, mi_frame)

#            mi_content = Label(self.ui.c_mi_content)
#            mi_content.setText(self.patient.mi[mi])
#            mi_content.set_decoration("mi_content")
#            mi_frame_layout.addWidget(mi_content,0, Qt.AlignLeft)

            mi_content = Label(self.ui.c_mi_content)
            mi_content.setText(self.patient.mi[mi])
            self.c_mi_content_layout.setWidget(form_index, QFormLayout.FieldRole, mi_content)


            form_index = form_index + 1

    s_change_view = Signal(str,str,str)
    def connect_ui_signals(self):
        # navigator
        self.ui.bt_back.clicked.connect(self.back)
#        self.ui.bt_add_new_patient.clicked.connect(self.add_new_patient)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    @Slot()
    def back(self):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)
