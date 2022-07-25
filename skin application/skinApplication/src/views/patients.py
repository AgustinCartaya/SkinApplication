from .view_object import *
from .ui.ui_patients import Ui_patients

from src.objects.patient_list import PatientList
from src.objects.patient import Patient

from PySide6.QtCore import QSize
from .ui.promoted.patient_card import PatientCard

class PatientsView(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()
        self.load_patients()
        self.show_patients()

    def load_patients(self):
        self.p_list = PatientList()
        self.p_list.search_all_patients()
        self.p_list_filtered = PatientList(self.p_list)

    def load_ui(self):
        self.ui = Ui_patients()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_add_new_patient.set_position(2)

        # labels
        self.ui.lb_title.set_title(1)
        self.ui.lb_filters_title.set_title(2)

        # filters
        self.ui.i_male.setChecked(True)
        self.ui.i_female.setChecked(True)

        self.ui.i_agre_precise.setValidator(self.create_text_validator(data_cleaner.regex_age))
        self.ui.i_age_rangue.setValidator(self.create_text_validator(data_cleaner.regex_rangue))
        self.ui.i_agre_precise.set_marked_when_filled(True)
        self.ui.i_age_rangue.set_marked_when_filled(True)

        self.ui.bt_age_rangue_1.setText("0 - 20")
        self.ui.bt_age_rangue_2.setText("20 - 50")
        self.ui.bt_age_rangue_3.setText("50+")

        self.ui.bt_age_rangue_1.select(True)
        self.ui.bt_age_rangue_2.select(True)
        self.ui.bt_age_rangue_3.select(True)


        self.ui.bt_age_rangue_1.action_value =  self.ui.bt_age_rangue_1.text().replace(" ", "")
        self.ui.bt_age_rangue_2.action_value =  self.ui.bt_age_rangue_2.text().replace(" ", "")
        self.ui.bt_age_rangue_3.action_value =  self.ui.bt_age_rangue_3.text().replace(" ", "")

        # organizer
        self.ui.bt_sorter_mosaico.set_icon(Button.IC_MOSAICO)
        self.ui.bt_sorter_list.set_icon(Button.IC_LIST)

        self.ui.bt_sorter_mosaico.select(True)
        self.ui.bt_sorter_asc.select(True)
        self.ui.bt_sorter_id.select(True)

        g1 = [self.ui.bt_sorter_mosaico, self.ui.bt_sorter_list]
        g2 = [self.ui.bt_sorter_asc, self.ui.bt_sorter_dsc]
        g3 = [self.ui.bt_sorter_id, self.ui.bt_sorter_name]

        self.ui.bt_sorter_mosaico.add_group(g1)
        self.ui.bt_sorter_list.add_group(g1)
        self.ui.bt_sorter_asc.add_group(g2)
        self.ui.bt_sorter_dsc.add_group(g2)
        self.ui.bt_sorter_id.add_group(g3)
        self.ui.bt_sorter_name.add_group(g3)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        # navigator
        self.ui.bt_back.clicked.connect(self.back)
        self.ui.bt_add_new_patient.clicked.connect(self.add_new_patient)

        # organizer
        self.ui.bt_sorter_mosaico.clicked.connect(self.show_patients)
        self.ui.bt_sorter_list.clicked.connect(self.show_patients)
        self.ui.bt_sorter_asc.clicked.connect(self.show_patients)
        self.ui.bt_sorter_dsc.clicked.connect(self.show_patients)
#        self.ui.bt_sorter_id.clicked.connect(self.show_patients)
#        self.ui.bt_sorter_name.clicked.connect(self.show_patients)
        self.ui.bt_sorter_id.clicked.connect(lambda: (self.slot_organizer_id_name("id") ) )
        self.ui.bt_sorter_name.clicked.connect(lambda: (self.slot_organizer_id_name("name") ) )

        # filters
        self.ui.i_male.stateChanged.connect(self.filter_patients)
        self.ui.i_female.stateChanged.connect(self.filter_patients)

        self.ui.i_agre_precise.returnPressed.connect(lambda: (self.slot_filter_age("precise") ) )
        self.ui.bt_age_rangue_1.clicked.connect(lambda: (self.slot_filter_age("rangue_bt") ) )
        self.ui.bt_age_rangue_2.clicked.connect(lambda: (self.slot_filter_age("rangue_bt") ) )
        self.ui.bt_age_rangue_3.clicked.connect(lambda: (self.slot_filter_age("rangue_bt") ) )
        self.ui.i_age_rangue.returnPressed.connect(lambda: (self.slot_filter_age("rangue") ) )

        self.ui.i_search.returnPressed.connect(self.filter_patients)
        self.ui.bt_search.clicked.connect(self.filter_patients)
        # created signals
        self.s_change_view.connect(self.MW.change_view)

    @Slot()
    def back(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.LOGIN_VIEW, None)

    @Slot()
    def add_new_patient(self):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.ADD_PATIENT_VIEW, None)

    @Slot(Patient)
    def check_patient(self, patient):
        self.s_change_view.emit(cfg.PATIENTS_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient":patient})


    @Slot()
    def show_patients(self):
        self.sort_patients()
        self.create_patient_cards()


    @Slot(str)
    def slot_filter_age(self, type_filter):
        if type_filter == "precise":
            self.ui.i_age_rangue.setText("")
            self.ui.bt_age_rangue_1.select(False)
            self.ui.bt_age_rangue_2.select(False)
            self.ui.bt_age_rangue_3.select(False)

        elif type_filter == "rangue":
            self.ui.i_agre_precise.setText("")
            self.ui.bt_age_rangue_1.select(False)
            self.ui.bt_age_rangue_2.select(False)
            self.ui.bt_age_rangue_3.select(False)

        elif  type_filter == "rangue_bt":
            self.ui.i_agre_precise.setText("")
            self.ui.i_age_rangue.setText("")

        self.filter_patients()

    @Slot(str)
    def slot_organizer_id_name(self, organizer):
        place_holder = ""
#        regex = ""
        if organizer == "id":
            place_holder = "E.g: AG4432YA"
        elif organizer == "name":
            place_holder = "E.g: Alex"

#        self.ui.i_age_rangue.setValidator(self.create_text_validator(regex))
        self.ui.i_search.setPlaceholderText(place_holder)
        self.show_patients()


    def filter_patients(self):
        self.p_list_filtered = PatientList(self.p_list)

        # search
        if len(self.ui.i_search.text()) > 0:
            if self.ui.bt_sorter_id.is_selected():
                self.p_list_filtered = self.p_list_filtered.get_filtered_starts_with("id", self.ui.i_search.text(), False)
            else:
                self.p_list_filtered = self.p_list_filtered.get_filtered_starts_with("first_name", self.ui.i_search.text(), False)

        # Clinical attributes
        # ---- gender
        if self.ui.i_female.isChecked() and not self.ui.i_male.isChecked():
            self.p_list_filtered = self.p_list_filtered.get_filtered("gender",0)
#            print("just females")
        elif self.ui.i_male.isChecked() and not self.ui.i_female.isChecked():
            self.p_list_filtered = self.p_list_filtered.get_filtered("gender",1)
#            print("just males")

        # ---- age
        if len(self.ui.i_agre_precise.text()) > 0:
            p_age = int(self.ui.i_agre_precise.text())
            self.p_list_filtered = self.p_list_filtered.get_filtered("age",p_age)

        elif len(self.ui.i_age_rangue.text()) > 0:
                if self.ui.i_age_rangue.text().endswith("+"):
                    rg = self.ui.i_age_rangue.text().replace("+","")
                    self.p_list_filtered = self.p_list_filtered.get_filtered_greater_than("age", int(rg))

                elif self.ui.i_age_rangue.text().endswith("-"):
                    rg = self.ui.i_age_rangue.text().replace("-","")
                    self.p_list_filtered = self.p_list_filtered.get_filtered_lower_than("age", int(rg))
                else:
                    rg = self.ui.i_age_rangue.text().replace(" ","").split("-")
                    self.p_list_filtered = self.p_list_filtered.get_filtered_rangue("age", int(rg[0]), int(rg[1]))
        else:
            plf_age_1 = PatientList()
            plf_age_2 = PatientList()
            plf_age_3 = PatientList()

            if self.ui.bt_age_rangue_1.is_selected():
                rg = self.ui.bt_age_rangue_1.action_value.split("-")
                plf_age_1 = self.p_list_filtered.get_filtered_rangue("age", int(rg[0]), int(rg[1]))

            if self.ui.bt_age_rangue_2.is_selected():
                rg = self.ui.bt_age_rangue_2.action_value.split("-")
                plf_age_2 = self.p_list_filtered.get_filtered_rangue("age", int(rg[0]), int(rg[1]))

            if self.ui.bt_age_rangue_3.is_selected():
                rg = self.ui.bt_age_rangue_3.action_value.replace("+","")
                plf_age_3 = self.p_list_filtered.get_filtered_greater_than("age", int(rg))

            self.p_list_filtered = PatientList(plf_age_1, plf_age_2, plf_age_3)

        self.show_patients()

    def sort_patients(self):
        if self.ui.bt_sorter_id.is_selected():
            sort_by = "id"
        else:
            sort_by = "first_name"
        self.p_list_filtered.sort_by(sort_by, self.ui.bt_sorter_dsc.is_selected())
        self.p_list_sortered = self.p_list_filtered

    def create_patient_cards(self):
        card_patients = []
        for p in self.p_list_sortered.patients:
            bt = PatientCard(p, self)
#            bt.setPatient(p)
            # a modificar
            bt.setTitle(self.p_list_sortered.sorted_by)

            card_patients.append(bt)
        self.ui.c_pagination.add_cards(card_patients)



