# This Python file uses the following encoding: utf-8
from src.db_controllers.db_controller import DBController
import src.util.data_cleaner as dc
import src.config as cfg
import src.util.util as util

from operator import attrgetter
from .patient import Patient

class PatientList:
    def __init__(self, *args):
        self.patients = []

        if len(args) >= 1:
            self.extract_patients(args[0])

    def search_all_patients(self):
        dbc = DBController()
        for p in dbc.select(cfg.TABLE_PATIENTS):
            self.patients.append(Patient(p[0], p[1], p[2], p[3], p[4]))

    def to_string(self):
        str = "["
        for p in self.patients:
            str = str + p.to_string() + "\n"
        str = str + "]"
        return str

    def sort_by(self, by="id"):
        self.patients.sort(key=attrgetter(by))

    def get_list_of(self, of="id"):
        if of == "id":
            return [x.id for x in self.patients]
        elif of == "first_name":
            return [x.first_name for x in self.patients]

    def append_patient(self, patient):
        self.patients.append(patient)

    def extract_patients(self, pl):
        for patient in pl.patients:
            self.patients.append(patient)

    def get_filtered(self, key, value):
        filtered = PatientList()
        for patient in self.patients:
            if getattr(patient, key) == value:
                filtered.append_patient(patient)
        return filtered

    def get_filtered_rangue(self, key, min, max, include = True):
        filtered = PatientList()
        for patient in self.patients:
            if include:
                if getattr(patient, key) >= min and getattr(patient, key) <= max:
                    filtered.append_patient(patient)
            else:
                if getattr(patient, key) > min and getattr(patient, key) < max:
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_greater_than(self, key, base, include = True):
        filtered = PatientList()
        for patient in self.patients:
            if include:
                if getattr(patient, key) >= base:
                    filtered.append_patient(patient)
            else:
                if getattr(patient, key) > base:
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_conains(self, key, value):
        filtered = PatientList()
        for patient in self.patients:
            if value in getattr(patient, key):
                filtered.append_patient(patient)
        return filtered

    def get_filtered_starts_with(self, key, value):
        filtered = PatientList()
        for patient in self.patients:
            if getattr(patient, key).startswith(value):
                filtered.append_patient(patient)
        return filtered
