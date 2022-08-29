from .view_object import *
from .ui.ui_upsert_patient_preview import Ui_upsert_patient_preview

from .ui.promoted.form_item import FormItem

#from src.objects.patient import Patient
from src.objects.variable_input import VariableInput


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

        # labels
        self.ui.lb_title.set_title(1)
        self.ui.lb_basic_information_title.set_title(2)
        self.ui.lb_medical_information_title.set_title(2)

        self.ui.i_first_name.set_decoration("mi_content")
        self.ui.i_last_name.set_decoration("mi_content")
        self.ui.i_birth_date.set_decoration("mi_content")
        self.ui.i_gender.set_decoration("mi_content")

    def show_information(self):
        self.show_basic_information()
        self.show_medical_information()

    def show_basic_information(self):
        self.ui.i_first_name.setText(tf.f(self.p.first_name, translate=False))
        self.ui.i_last_name.setText(tf.f(self.p.last_name, translate=False))
        self.ui.i_birth_date.setText(tf.f(self.p.birth_date.strftime('%d-%m-%Y'), translate=False))
        if self.p.gender == 0:
            self.ui.i_gender.setText(tf.f("Woman"))
        elif self.p.gender == 1:
            self.ui.i_gender.setText(tf.f("Man"))
        else:
            self.ui.i_gender.setText(tf.f("Other"))

    def show_medical_information(self):
        for mi_name, mi_content in self.p.mi.items():
            mi_preview = FormItem(self.ui.c_patient_information_preview)
            mi_preview.initialize(mi_name, mi_content, VariableInput.MI_INPUT, FormItem.DISPOSITION_V)
            self.ui.ly_mi_content.addWidget(mi_preview)

    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_upsert.clicked.connect(lambda: self.update_patient() if (self.mode ==  "edit") else self.add_patient() )
        self.ui.bt_cancel.clicked.connect(self.cancel)
        self.ui.bt_back.clicked.connect(self.back)

        self.ui.i_upsert_patient_view.toggled.connect(self.rb_view)
        self.ui.i_upsert_patient_mi_view.toggled.connect(self.rb_view)



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
        self.ui.lb_title.setText(tf.f("Edit patient preview"))
        self.ui.bt_upsert.setText(tf.f("Save"))
