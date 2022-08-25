from .view_object import *
from .ui.ui_upsert_patient_mi import Ui_upsert_patient_mi

from src.objects.patient import Patient
from src.objects.variable_input import VariableInput


from .ui.promoted.variable_inputs_container import VariableInputsContainer
from .ui.promoted.variable_input_creator import VariableInputCreator


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
        self.ui.c_mi.initialize(VariableInput.MI_INPUT, self.edit_variable_input)


    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_next.clicked.connect(self.__next)
        self.ui.bt_cancel.clicked.connect(self.__cancel)
        self.ui.bt_back.clicked.connect(self.__back)

        self.ui.bt_create_new_mi.clicked.connect(self.__show_variable_input_creator)

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
        for mi_name, mi_value in self.ui.c_mi.get_selected_items().items():
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


    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit medical information")
        self.ui.c_mi.select_default_values(self.p.mi)

    # Add new variable input (Medical information)
    @Slot()
    def __show_variable_input_creator(self):
        self.variable_input_creator = VariableInputCreator(self.mv, VariableInput.MI_INPUT, self.new_variable_input_created)
        self.variable_input_creator.show()

    Slot(VariableInput)
    def new_variable_input_created(self, variable_input):
        try:
            variable_input.create()
            self.ui.c_mi.append_new_variable_input(variable_input)
        except ValueError as err:
            print(err.args)

    # edit variable input(Medical information)
    Slot(VariableInput)
    def edit_variable_input(self, variable_input):
        print(variable_input)
