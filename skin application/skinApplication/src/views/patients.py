from .view_object import *
from .ui.ui_patients import Ui_patients

from src.objects.patient_list import PatientList
from src.objects.patient import Patient

from PySide6.QtCore import QSize
from .ui.promoted.patient_card import PatientCard
from .ui.promoted.variable_input_creator import VariableInputCreator

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
        self.p_list.search_all_patients()
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

        self.ui.c_filter_age_precise_header.add_filters_content(self.ui.c_filter_age_precise_content)
        self.ui.c_filter_age_range_header.add_filters_content(self.ui.c_filter_age_range_content)

        self.ui.c_filter_age_precise_header.add_open_receaver(lambda: (self.slot_filter_age("precise") ))
        self.ui.c_filter_age_range_header.add_open_receaver(lambda: (self.slot_filter_age("range") ))

        self.ui.bt_age_range_1.setText("0 - 20")
        self.ui.bt_age_range_2.setText("20 - 50")
        self.ui.bt_age_range_3.setText("50+")

        self.ui.bt_age_range_1.action_value =  self.ui.bt_age_range_1.text().replace(" ", "")
        self.ui.bt_age_range_2.action_value =  self.ui.bt_age_range_2.text().replace(" ", "")
        self.ui.bt_age_range_3.action_value =  self.ui.bt_age_range_3.text().replace(" ", "")

        # AQUI TE QUEDASTE
        self.ui.c_filter_mi_content.show_filters(cfg.FILES_MEDICAL_INFORMATION_PATH, self.filter_patients)
        self.ui.c_filter_skl_charac_content.show_filters(cfg.FILES_SKIN_LESION_CHARACTERISTICS_PATH, self.filter_patients)


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

        # Number of Patients
        self.ui.i_number_of_patients.setText(len(self.p_list))

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        # navigator
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_add_new_patient.clicked.connect(self.add_new_patient)

        # sorter
        self.ui.bt_sorter_mosaico.clicked.connect(self.show_patients)
        self.ui.bt_sorter_list.clicked.connect(self.show_patients)
        self.ui.bt_sorter_asc.clicked.connect(self.show_patients)
        self.ui.bt_sorter_dsc.clicked.connect(self.show_patients)
        self.ui.bt_sorter_id.clicked.connect(lambda: (self.slot_organizer_id_name("id") ) )
        self.ui.bt_sorter_name.clicked.connect(lambda: (self.slot_organizer_id_name("name") ) )
        # filters

        #   search
        self.ui.i_search.returnPressed.connect(self.filter_patients)
        self.ui.bt_search.clicked.connect(self.filter_patients)

        #   basic information
        self.ui.i_male.stateChanged.connect(self.filter_patients)
        self.ui.i_female.stateChanged.connect(self.filter_patients)

        self.ui.i_agre_precise.editingFinished.connect(self.filter_patients)
        self.ui.bt_age_range_1.clicked.connect(self.filter_patients)
        self.ui.bt_age_range_2.clicked.connect(self.filter_patients)
        self.ui.bt_age_range_3.clicked.connect(self.filter_patients)
        self.ui.i_age_range_min.editingFinished.connect(self.filter_patients)
        self.ui.i_age_range_max.editingFinished.connect(self.filter_patients)

        # AI results
        self.ui.i_air_benign.stateChanged.connect(self.filter_patients)
        self.ui.i_air_indeterminate.stateChanged.connect(self.filter_patients)
        self.ui.i_air_malignant.stateChanged.connect(self.filter_patients)

        # reset filters
        self.ui.bt_reset_filters.clicked.connect(self.reset_filters)


        # created signals
        self.s_change_view.connect(self.MW.change_view)

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
        self.ui.i_female.setChecked(False)
        self.ui.i_male.setChecked(False)
        self.ui.i_agre_precise.setValue(0)
        self.ui.i_age_range_min.setValue(0)
        self.ui.i_age_range_max.setValue(0)
        self.ui.bt_age_range_1.select(False)
        self.ui.bt_age_range_2.select(False)
        self.ui.bt_age_range_3.select(False)

        self.ui.c_filter_mi_content.reset_filters()
        self.ui.c_filter_skl_charac_content.reset_filters()

        self.p_list_filtered = PatientList.duplicate_list(self.p_list)
        self.show_patients()
        self.__refresh_number_of_patients()


    @Slot()
    def show_patients(self):
        self.sort_patients()
        self.create_patient_cards()


    @Slot(str)
    def slot_filter_age(self, type_filter):
        if type_filter == "precise":
            self.ui.c_filter_age_range_header.close_content()
        elif type_filter == "range":
            self.ui.c_filter_age_precise_header.close_content()

    @Slot(str)
    def slot_organizer_id_name(self, organizer):
        place_holder = ""
#        regex = ""
        if organizer == "id":
            place_holder = "E.g: AG4432YA"
        elif organizer == "name":
            place_holder = "E.g: Alex"

        self.ui.i_search.setPlaceholderText(place_holder)
        self.show_patients()

    @Slot()
    def filter_patients(self):
#        print()
        print(self.ui.c_filter_skl_charac_content.get_selected_filters())

        self.p_list_filtered = PatientList.duplicate_list(self.p_list)
        self.__filter_search()
        if self.ui.c_filter_bi_header.open:
            self.__filter_basic_information()
        if self.ui.c_filter_mi_header.open:
            self.__filter_medical_information()
        if self.ui.c_filter_ai_results_header.open:
            self.__filter_ai_results()

        self.show_patients()
        self.__refresh_number_of_patients()

    def __filter_search(self):
        # search
        if len(self.ui.i_search.text()) > 0:
            if self.ui.bt_sorter_id.is_selected():
                self.p_list_filtered = self.p_list_filtered.get_filtered_starts_with("id", self.ui.i_search.text(), False)
            else:
                self.p_list_filtered = self.p_list_filtered.get_filtered_conains("first_name", self.ui.i_search.text(), False)

    def __filter_basic_information(self):
        # ---- gender
        if (self.ui.i_female.isChecked() ^ self.ui.i_male.isChecked()):
            gender = int(self.ui.i_male.isChecked())
            self.p_list_filtered = self.p_list_filtered.get_filtered("gender",gender)

        # ---- age
        if self.ui.c_filter_age_precise_header.open and self.ui.i_agre_precise.value() > 0:
            p_age = self.ui.i_agre_precise.value()
            self.p_list_filtered = self.p_list_filtered.get_filtered("age",p_age)

        elif self.ui.c_filter_age_range_header.open:
            if self.ui.i_age_range_min.value() > 0 or self.ui.i_age_range_max.value() > 0:
                self.p_list_filtered = self.p_list_filtered.get_filtered_range("age", self.ui.i_age_range_min.value(), self.ui.i_age_range_max.value())
            # esto era un elif
            if self.ui.bt_age_range_1.is_selected() or self.ui.bt_age_range_2.is_selected() or self.ui.bt_age_range_3.is_selected():
                plf_age_1 = PatientList()
                plf_age_2 = PatientList()
                plf_age_3 = PatientList()

                if self.ui.bt_age_range_1.is_selected():
                    rg = self.ui.bt_age_range_1.action_value.split("-")
                    plf_age_1 = self.p_list_filtered.get_filtered_range("age", int(rg[0]), int(rg[1]))

                if self.ui.bt_age_range_2.is_selected():
                    rg = self.ui.bt_age_range_2.action_value.split("-")
                    plf_age_2 = self.p_list_filtered.get_filtered_range("age", int(rg[0]), int(rg[1]))

                if self.ui.bt_age_range_3.is_selected():
                    rg = self.ui.bt_age_range_3.action_value.replace("+","")
                    plf_age_3 = self.p_list_filtered.get_filtered_greater_than("age", int(rg))

                self.p_list_filtered = PatientList.join_lists(plf_age_1, plf_age_2, plf_age_3)

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

    def sort_patients(self):
        if self.ui.bt_sorter_id.is_selected():
            sort_by = "id"
        else:
            sort_by = "first_name"
        self.p_list_filtered.sort_by(sort_by, self.ui.bt_sorter_dsc.is_selected())
        self.p_list_sortered = self.p_list_filtered

    def create_patient_cards(self):
        card_patients = []
        for p in self.p_list_sortered:
            bt = PatientCard(self.ui.c_pagination, p, self)
#            bt.setPatient(p)
            # a modificar
            bt.setTitle(self.p_list_sortered.sorted_by)

            card_patients.append(bt)
        self.ui.c_pagination.add_cards(card_patients)

    def __refresh_number_of_patients(self):
        self.ui.i_number_of_patients.setText(len(self.p_list_filtered))

