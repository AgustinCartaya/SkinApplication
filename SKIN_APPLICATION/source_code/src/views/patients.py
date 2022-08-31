# @autor: Agustin CARTAYA

from .view_object import *
from .ui.ui_patients import Ui_patients

from src.objects.patient_list import PatientList
from src.objects.patient import Patient
from src.objects.variable_input import VariableInput


from PySide6.QtCore import QSize
from .ui.promoted.patient_card import PatientCard

from .ui.promoted.check_button_group import CheckButtonGroup


class PatientsView(ViewObject):

    def __init__(self, mw):
        super().__init__(mw)

        self.p_list = PatientList()
        self.p_list_filtered = None
        self.p_list_sortered = None
        self.__load_patients()

        self.load_ui()
        self.connect_ui_signals()

        self.show_patients()

    def __load_patients(self):
        self.p_list.search_all_patients(self.GLOBAL["doctor"].id)
        self.p_list_filtered = PatientList.duplicate_list(self.p_list)

    def load_ui(self):
        self.ui = Ui_patients()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_add_new_patient.set_position(2)

        # labels
        self.ui.lb_title.set_title(1)
        self.ui.lb_filters_title.set_title(2)

        # filters
        self.ui.c_filter_bi_header.add_filters_content(self.ui.c_filter_bi_content)
        self.ui.c_filter_mi_header.add_filters_content(self.ui.c_filter_mi_content)
        self.ui.c_filter_ai_results_header.add_filters_content(self.ui.c_filter_ai_results_content)
        self.ui.c_filter_skl_charac_header.add_filters_content(self.ui.c_filter_skl_charac_content)

        # filters creation
        f_gender = VariableInput("gender", VariableInput.VIRTUAL_INPUT, VariableInput.OWNER_VIRTUAL, VariableInput.TYPE_OPTIONS, "gender")
        f_gender.set_items(["Women", "Man", "Other"], [0,1,2])
        f_age = VariableInput("age", VariableInput.VIRTUAL_INPUT, VariableInput.OWNER_VIRTUAL, VariableInput.TYPE_INT, "age")
        self.ui.c_filter_bi_content.show_virtual_filters([f_gender, f_age], self.filter_patients)
        self.ui.c_filter_mi_content.initialize(VariableInput.MI_INPUT, self.filter_patients)
        self.ui.c_filter_skl_charac_content.initialize(VariableInput.SKL_INPUT, self.filter_patients)


        # organizer
        self.ui.bt_sorter_mosaico.set_icon(Button.IC_MOSAICO)
        self.ui.bt_sorter_list.set_icon(Button.IC_LIST)

        self.ui.bt_sorter_mosaico.select(True)
        self.ui.bt_sorter_asc.select(True)
        self.ui.bt_sorter_id.select(True)

        self.g_sorter_mosaico = CheckButtonGroup()
        self.g_sorter_mosaico.add_buttons(self.ui.bt_sorter_mosaico, self.ui.bt_sorter_list)

        self.g_sorter_asc = CheckButtonGroup()
        self.g_sorter_asc.add_buttons(self.ui.bt_sorter_asc, self.ui.bt_sorter_dsc)

        self.g_sorter_id = CheckButtonGroup()
        self.g_sorter_id.add_buttons(self.ui.bt_sorter_id, self.ui.bt_sorter_name)


        self.ui.c_sorter_mosaico.hide()
        self.ui.bt_sorter_list.setEnabled(False)

#        self.ui.bt_sorter_list.hide()
#        self.ui.hs_sorter_2.changeSize(0,0)

        # pagination
        self.ui.c_pagination.set_grid_cards_size(3,4)
#        self.ui.c_pagination.forced_empty_spaces = True

        # Number of Patients
        self.ui.i_number_of_patients.setText(tf.f(len(self.p_list)))


    def connect_ui_signals(self):
        # navigator
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_add_new_patient.clicked.connect(self.add_new_patient)

        # sorter
        self.ui.bt_sorter_mosaico.clicked.connect(self.show_patients)
        self.ui.bt_sorter_list.clicked.connect(self.show_patients)
        self.ui.bt_sorter_asc.clicked.connect(self.show_patients)
        self.ui.bt_sorter_dsc.clicked.connect(self.show_patients)
        self.ui.bt_sorter_id.clicked.connect(self.show_patients)
        self.ui.bt_sorter_name.clicked.connect(self.show_patients)

        # reset filters
        self.ui.bt_reset_filters.clicked.connect(self.reset_filters)
        self.ui.bt_filter.clicked.connect(self.filter_patients)

        #   search
        self.ui.i_search.returnPressed.connect(self.filter_patients)
        self.ui.bt_search.clicked.connect(self.filter_patients)

    @Slot()
    def back(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.LOGIN_VIEW, None)

    @Slot()
    def add_new_patient(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.UPSERT_PATIENT_VIEW, None)

    @Slot(str)
    def check_patient(self, patient_id):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id": patient_id})

    @Slot()
    def reset_filters(self):
        # reseting filters
        self.ui.c_filter_bi_content.reset_filters()
        self.ui.c_filter_mi_content.reset_filters()
        self.ui.c_filter_skl_charac_content.reset_filters()

        self.p_list_filtered = PatientList.duplicate_list(self.p_list)
        self.show_patients()
        self.__refresh_number_of_patients()

    @Slot()
    def show_patients(self):
        self.sort_patients()
        self.create_patient_cards()

    @Slot()
    def filter_patients(self):
        self.p_list_filtered = PatientList.duplicate_list(self.p_list)
        self.__filter_search()
        if self.ui.c_filter_bi_header.open:
            self.__filter_basic_information()
        if self.ui.c_filter_mi_header.open:
            self.__filter_medical_information()
        if self.ui.c_filter_ai_results_header.open:
            self.__filter_ai_results()
        if self.ui.c_filter_skl_charac_header.open:
            self.__filter_skin_lesion_characteristics()

        self.show_patients()
        self.__refresh_number_of_patients()

    def __filter_search(self):
        # search
        if len(self.ui.i_search.text()) > 0:
            p_list_filtered_id = self.p_list_filtered.get_filtered_conains("id", self.ui.i_search.text(), False)
            p_list_filtered_last_name = self.p_list_filtered.get_filtered_conains("last_name", self.ui.i_search.text(), False)
            p_list_filtered_first_name = self.p_list_filtered.get_filtered_conains("first_name", self.ui.i_search.text(), False)
            self.p_list_filtered = PatientList.join_lists(p_list_filtered_id, p_list_filtered_last_name, p_list_filtered_first_name)


    def __filter_basic_information(self):
        for mi_name, mi_value in self.ui.c_filter_bi_content.get_selected_filters().items():
            if type(mi_value) is list:
                self.p_list_filtered = self.p_list_filtered.get_filtered_conains(mi_name, mi_value, info="bi")
            elif type(mi_value) is tuple:
                self.p_list_filtered = self.p_list_filtered.get_filtered_range(mi_name, mi_value[0], mi_value[1], info="bi")
            else:
                self.p_list_filtered = self.p_list_filtered.get_filtered(mi_name, mi_value, info="bi")


    def __filter_ai_results(self):
        risks = []
        if self.ui.i_air_benign.isChecked():
            risks.append(0)
        if self.ui.i_air_malignant.isChecked():
            risks.append(1)
        if self.ui.i_air_indeterminate.isChecked():
            risks.append(2)
        self.p_list_filtered = self.p_list_filtered.get_filtered_skl_risks(risks)

    def __filter_medical_information(self):
        for mi_name, mi_value in self.ui.c_filter_mi_content.get_selected_filters().items():
            if type(mi_value) is list:
                self.p_list_filtered = self.p_list_filtered.get_filtered_conains(mi_name, mi_value, info="mi")
            elif type(mi_value) is tuple:
                self.p_list_filtered = self.p_list_filtered.get_filtered_range(mi_name, mi_value[0], mi_value[1], info="mi")
            else:
                self.p_list_filtered = self.p_list_filtered.get_filtered(mi_name, mi_value, info="mi")

    def __filter_skin_lesion_characteristics(self):
        for mi_name, mi_value in self.ui.c_filter_skl_charac_content.get_selected_filters().items():
            if type(mi_value) is list:
                self.p_list_filtered = self.p_list_filtered.get_filtered_conains(mi_name, mi_value, info="skl_charac")
            elif type(mi_value) is tuple:
                self.p_list_filtered = self.p_list_filtered.get_filtered_range(mi_name, mi_value[0], mi_value[1], info="skl_charac")
            else:
                self.p_list_filtered = self.p_list_filtered.get_filtered(mi_name, mi_value, info="skl_charac")

    def sort_patients(self):
        if self.ui.bt_sorter_id.is_selected():
            sort_by = "id"
        else:
            sort_by = "last_name"
        self.p_list_filtered.sort_by(sort_by, self.ui.bt_sorter_dsc.is_selected())
        self.p_list_sortered = self.p_list_filtered

    def create_patient_cards(self):
        card_patients = []
        for p in self.p_list_sortered:
            patient_card = PatientCard(self.ui.c_pagination)
            patient_card.initialize(p, self.check_patient)
            card_patients.append(patient_card)
        self.ui.c_pagination.add_cards(card_patients)

    def __refresh_number_of_patients(self):
        self.ui.i_number_of_patients.setText(tf.f(len(self.p_list_filtered)))

