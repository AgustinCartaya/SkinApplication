from .view_object import *
from .ui.ui_upsert_patient_mi import Ui_upsert_patient_mi

from src.objects.patient import Patient

from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QLineEdit,QGridLayout, QLabel, QComboBox, QInputDialog)

from .ui.promoted.line_edit import LineEdit
from .ui.promoted.medical_information_input import MedicalInformationInput


class UpsertPatientMiView(ViewObject):
    def __init__(self, mw, patient, mode="add"):
        super().__init__(mw)

        self.p = patient
        self.mode = mode
        self.mi_inputs = {}

        self.load_ui()
        self.connect_ui_signals()

        if mode == "edit":
            self.charge_edit_mode()

    def load_ui(self):
        self.ui = Ui_upsert_patient_mi()
        self.ui.setupUi(self)

        #buttons
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

        # labels
        self.ui.lb_title.set_title(1)


        # buttons
        self.ui.c_new_mi_content.hide()
        self.ui.bt_cancel_new_mi.set_type(Button.BT_CANCEL)
        self.ui.i_new_mi_name.setValidator(self.create_text_validator(data_cleaner.regex_letter_number_space))

        self.charge_medical_information()

    def charge_medical_information(self):
        for file_name in util.get_file_list(cfg.FILES_MEDICAL_INFORMATION_PATH):

            mi_id = file_name.split(".")[0]

            mi_title = util.file_name_to_title(mi_id)
            mi_values = util.read_file_list(file_name, path=cfg.FILES_MEDICAL_INFORMATION_PATH)

            self.show_single_medica_information(mi_id, mi_title, mi_values)

    def show_single_medica_information(self, mi_id, mi_title, mi_values):
        mi_input = MedicalInformationInput(mi_id, mi_title, mi_values, self, True)
        self.ui.ly_medical_information.addWidget(mi_input)
        self.mi_inputs[mi_id] = mi_input

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_next.clicked.connect(self.next)
        self.ui.bt_cancel.clicked.connect(self.cancel)
        self.ui.bt_back.clicked.connect(self.back)

        self.ui.bt_create_new_mi.clicked.connect(self.show_add_new_mi_c)
        self.ui.bt_add_new_mi.clicked.connect(self.add_new_mi)
        self.ui.bt_cancel_new_mi.clicked.connect(self.cancel_new_mi)

        self.ui.scrollArea.verticalScrollBar().rangeChanged.connect(self.scroll_down)

        self.ui.i_upsert_patient_view.toggled.connect(self.rb_view)
        self.ui.i_upsert_patient_preview_view.toggled.connect(self.rb_view)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def rb_view(self):
        if self.ui.i_upsert_patient_view.isChecked():
            self.back()
        elif self.ui.i_upsert_patient_preview_view.isChecked():
            self.next()
        self.ui.i_upsert_patient_mi_view.setChecked(True)

    def catch_medical_info(self):
        medical_info = {}
        for mi in self.mi_inputs:
            medical_info[mi] = self.mi_inputs[mi].selected_item()

        self.p.mi = medical_info

    def next(self):
        self.__change_to_upsert_patient_view(3)

    def cancel(self):
        if self.mode == "edit":
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.CHECK_PATIENT_VIEW,  {"patient_id": self.p.id})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.PATIENTS_VIEW, None)

    @Slot()
    def back(self):
        self.__change_to_upsert_patient_view(1)

    @Slot()
    def show_add_new_mi_c(self):
        self.ui.c_new_mi_content.show()

    @Slot()
    def add_new_mi(self):
        mi_title = self.ui.i_new_mi_name.text()
        mi_values = util.str_to_list(self.ui.i_new_mi_value.text(),",")

        mi_file_name = util.title_to_file_name(mi_title)
        mi_file_content = '\n'.join(mi_values)

        with open(cfg.FILES_MEDICAL_INFORMATION_PATH + cfg._S + mi_file_name + ".options", 'w') as f:
            f.write(mi_file_content)

        self.show_single_medica_information(mi_file_name, mi_title, mi_values)
        self.cancel_new_mi()

    def __change_to_upsert_patient_view(self, view):
        self.catch_medical_info()
        if view == 1:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.UPSERT_PATIENT_VIEW, {"patient":self.p, "mode":self.mode})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.UPSERT_PATIENT_PREVIEW_VIEW, {"patient":self.p, "mode":self.mode})


    @Slot()
    def cancel_new_mi(self):
        self.ui.i_new_mi_name.setText("")
        self.ui.i_new_mi_value.setText("")
        self.ui.c_new_mi_content.hide()

    @Slot()
    def scroll_down(self, min, maxi):
        self.ui.scrollArea.verticalScrollBar().setValue(maxi)

    @Slot(str)
    def add_new_mi_item(self, mi_input_id):
        new_item_s, ok = QInputDialog.getText(self.ui.c_medical_information,
            'Add new "' + self.mi_inputs[mi_input_id].title + '"',
            "Actual values:\n" + ", ".join(self.mi_inputs[mi_input_id].get_items(False)))
        if ok:
            new_item_s = util.str_to_list(new_item_s, ",")
        if len(new_item_s) > 0:
            util.apped_to_file(mi_input_id+".options", "\n" + "\n".join(new_item_s), cfg.FILES_MEDICAL_INFORMATION_PATH)
            self.mi_inputs[mi_input_id].append_items(new_item_s)

    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit medical information")
        for p_mi in self.p.mi:
            self.mi_inputs[p_mi].select_item(self.p.mi[p_mi])