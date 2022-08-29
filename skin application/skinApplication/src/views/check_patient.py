from .view_object import *
from .ui.ui_check_patient import Ui_check_patient

#from src.objects.patient_list import PatientList
from PySide6.QtWidgets import (QFormLayout, QVBoxLayout, QFrame)
from PySide6.QtCore import Qt

from .ui.promoted.label import Label
from .ui.promoted.skin_lesion_preview import SkinLesionPreview
from .ui.promoted.form_item import FormItem

from src.objects.patient import Patient
from src.objects.image import Image
from src.objects.variable_input import VariableInput


class CheckPatientView(ViewObject):
    def __init__(self, mw, patient_id):
        super().__init__(mw)

        self.load_patient(patient_id)

        self.load_ui()
        self.connect_ui_signals()

        self.load_skin_lesions()

    def load_patient(self, patient_id):
        self.p = Patient.get_patient_by_id(patient_id)

    def load_skin_lesions(self):
        self.p.load_skin_lesions()
        for skl in self.p.skin_lesions:
            skl_preview = SkinLesionPreview(self.ui.c_skin_lesions_preview)
            skl_preview.initialize(skl, self.update_skin_lesion, self.see_timeline, self.see_images)
            skl_photography = skl.get_photography()
            if skl_photography is not None:
                skl_preview.set_image(skl_photography)
            else:
                skl_preview.set_image(Image(cfg.IMG_LOGO_PATH_NAME, "logo"))

            self.ui.ly_skin_lesions_preview.addWidget(skl_preview)

    Slot(int)
    def update_skin_lesion(self, skin_lesion_nb):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.UPSERT_SKIN_LESION_VIEW, {"patient" : self.p, "skin_lesion": self.p.skin_lesions[skin_lesion_nb]})

    Slot(int)
    def see_timeline(self, skin_lesion_nb):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.TIMELINE_VIEW, {"patient" : self.p, "skin_lesion": self.p.skin_lesions[skin_lesion_nb]})

    Slot(int)
    def see_images(self, skin_lesion_nb):
        skl = self.p.skin_lesions[skin_lesion_nb]
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.IMAGES_VIEW, {"images":skl.get_all_skl_imgs(), "patient" : self.p, "skin_lesion": skl, 'collet_mode':False})

    def load_ui(self):
        self.ui = Ui_check_patient()
        self.ui.setupUi(self)

        #label
        self.ui.lb_title.set_title(1)
        self.ui.lb_patient_information.set_title(2)

        # id
        self.ui.i_id.setText(tf.f(self.p.id, translate=False))

        # basic information
        self.ui.i_first_name.setText(tf.f(self.p.first_name, translate=False))
        self.ui.i_last_name.setText(tf.f(self.p.last_name, translate=False))
        self.ui.i_age.setText(tf.f(self.p.age, translate=False))

        if self.p.gender == 0:
            self.ui.i_gender.setText(tf.f("Woman"))
        elif self.p.gender == 1:
            self.ui.i_gender.setText(tf.f("Man"))
        else:
            self.ui.i_gender.setText(tf.f("Other"))

        # navigator
        self.ui.bt_add_lesion.set_position(2)

        # medical information
#        self.c_mi_content_layout = QFormLayout(self.ui.c_mi_content)
#        self.c_mi_content_layout.setVerticalSpacing(16)
        self.show_medical_information()

        # skin lesions preview
#        self.skin_lesions_layout = QVBoxLayout(self.ui.c_skin_lesions)
#        self.skin_lesions_layout.setSpacing(40)
#        self.skin_lesions_layout.setContentsMargins(0, 0, 0, 0)

    def connect_ui_signals(self):
        # navigator
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_edit_patient_info.clicked.connect(self.edit_patient_info)

        self.ui.bt_add_lesion.clicked.connect(self.add_new_skin_lesion)

    def show_medical_information(self):
        form_index = 0
        for mi_name, mi_content in self.p.mi.items():
            mi_preview = FormItem(self.ui.c_patient_information_content)
            mi_preview.initialize(mi_name, mi_content, VariableInput.MI_INPUT)
            self.ui.ly_mi_content.addWidget(mi_preview)

    @Slot()
    def back(self):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.PATIENTS_VIEW, None)

    @Slot()
    def edit_patient_info(self):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.UPSERT_PATIENT_VIEW, {"patient" : self.p})

    @Slot()
    def add_new_skin_lesion(self):
        self.s_change_view.emit(cfg.CHECK_PATIENT_VIEW, cfg.UPSERT_SKIN_LESION_VIEW, {"patient" : self.p, "skin_lesion": None})

#    def refresh(self):
#        for skl in self.p.skin_lesions:
#            skl_photography = skl.get_photography()
#            if skl_photography is not None:
#                self.skin_lesion_previews[skl.number].refresh_image(skl_photography)
#            else:
#                self.skin_lesion_previews[skl.number].refresh_image(Image(cfg.IMG_LOGO_PATH_NAME, "logo"))

