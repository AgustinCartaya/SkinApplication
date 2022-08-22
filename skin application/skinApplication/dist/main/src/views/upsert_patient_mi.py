from .view_object import *
from .ui.ui_upsert_patient_mi import Ui_upsert_patient_mi

from src.objects.patient import Patient

from .ui.promoted.variable_inputs_container import VariableInputsContainer

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

        # navigator
        self.ui.bt_cancel.set_type(Button.BT_CANCEL)

        # labels
        self.ui.lb_title.set_title(1)

        # medical information
        self.c_mi = VariableInputsContainer(cfg.FILES_MEDICAL_INFORMATION_PATH,
            "Create new medical information")
        self.ui.ly_medical_information.addWidget(self.c_mi)

    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_next.clicked.connect(self.__next)
        self.ui.bt_cancel.clicked.connect(self.__cancel)
        self.ui.bt_back.clicked.connect(self.__back)

        self.ui.scrollArea.verticalScrollBar().rangeChanged.connect(self.scroll_down)

        self.ui.i_upsert_patient_view.toggled.connect(self.rb_view)
        self.ui.i_upsert_patient_preview_view.toggled.connect(self.rb_view)

    def rb_view(self):
        if self.ui.i_upsert_patient_view.isChecked():
            self.__back()
        elif self.ui.i_upsert_patient_preview_view.isChecked():
            self.__next()
        self.ui.i_upsert_patient_mi_view.setChecked(True)

    def catch_medical_info(self):
        medical_info = {}
        for mi_name, mi_value in self.c_mi.get_selected_items().items():
            if mi_value is None:
                    continue
            medical_info[mi_name] = mi_value

        self.p.mi = medical_info

    def __next(self):
        self.__change_to_upsert_patient_view(3)

    def __cancel(self):
        if self.mode == "edit":
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.CHECK_PATIENT_VIEW,  {"patient_id": self.p.id})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.PATIENTS_VIEW, None)

    @Slot()
    def __back(self):
        self.__change_to_upsert_patient_view(1)

    def __change_to_upsert_patient_view(self, view):
        self.catch_medical_info()
        if view == 1:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.UPSERT_PATIENT_VIEW, {"patient":self.p, "mode":self.mode})
        else:
            self.s_change_view.emit(cfg.UPSERT_PATIENT_MI_VIEW, cfg.UPSERT_PATIENT_PREVIEW_VIEW, {"patient":self.p, "mode":self.mode})

    @Slot()
    def scroll_down(self, min, maxi):
        self.ui.scrollArea.verticalScrollBar().setValue(maxi)

    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit medical information")
        self.c_mi.select_default_values(self.p.mi)
#        for p_mi in self.p.mi:
#            self.mi_inputs[p_mi].select_item(self.p.mi[p_mi])
