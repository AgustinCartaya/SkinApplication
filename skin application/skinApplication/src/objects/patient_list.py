# This Python file uses the following encoding: utf-8
from src.db_controllers.db_controller import DBController
import src.config as cfg
import src.util.util as util

from operator import attrgetter
from .patient import Patient

class PatientList:
    def __init__(self):
        self.patients = []
        self.sorted_by = None

    def __len__(self):
        return len(self.patients)

    def __iter__(self):
        return iter(self.patients)

    @classmethod
    def duplicate_list(csl, patient_list):
        p_list = PatientList()
        for p in patient_list:
            p_list.append_patient(p)
        return p_list

    @classmethod
    def join_lists(csl, *patient_lists):
        p_list = PatientList()
        for patient_list in patient_lists:
            for p in patient_list:
                p_list.append_patient(p)
        # deleting duplicates
        p_list.patients = list(set(p_list.patients))
        return p_list

    def search_all_patients(self):
        dbc = DBController()
        for p in dbc.select(cfg.TABLE_PATIENTS):
            patient = Patient(p[0], p[1], p[2], p[3], p[4], p[5])
            patient.load_skin_lesions()
            self.patients.append(patient)

    def to_string(self):
        str = "["
        for p in self:
            str = str + p.to_string() + "\n"
        str = str + "]"
        return str

    def sort_by(self, by="id", dsc=True):
        self.patients.sort(key=attrgetter(by), reverse=dsc)
        self.sorted_by = by

    def get_list_of(self, of="id"):
        if of == "id":
            return [x.id for x in self]
        elif of == "first_name":
            return [x.first_name for x in self]

    def append_patient(self, patient):
        self.patients.append(patient)

    def get_filtered(self, key, value):
        filtered = PatientList()
        for patient in self:
            if getattr(patient, key) == value:
                filtered.append_patient(patient)
        return filtered

    def get_filtered_range(self, key, min, max, include = True):
        filtered = PatientList()
        for patient in self:
            if include:
                if getattr(patient, key) >= min and getattr(patient, key) <= max:
                    filtered.append_patient(patient)
            else:
                if getattr(patient, key) > min and getattr(patient, key) < max:
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_lower_than(self, key, base, include = True):
        filtered = PatientList()
        for patient in self:
            if include:
                if getattr(patient, key) <= base:
                    filtered.append_patient(patient)
            else:
                if getattr(patient, key) < base:
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_greater_than(self, key, base, include = True):
        filtered = PatientList()
        for patient in self:
            if include:
                if getattr(patient, key) >= base:
                    filtered.append_patient(patient)
            else:
                if getattr(patient, key) > base:
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_conains(self, key, value, case_sensitive =  True):
        filtered = PatientList()
        for patient in self:
            if case_sensitive:
                if value in getattr(patient, key):
                    filtered.append_patient(patient)
            else:
                if value.lower() in getattr(patient, key).lower():
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_starts_with(self, key, value, case_sensitive =  True):
        filtered = PatientList()
        for patient in self:
            if case_sensitive:
                if getattr(patient, key).startswith(value):
                    filtered.append_patient(patient)
            else:
                if getattr(patient, key).lower().startswith(value.lower()):
                    filtered.append_patient(patient)
        return filtered

    def get_filtered_skl_risks(self, risks):
        filtered = PatientList()
        for patient in self:
            if not set(risks).isdisjoint(patient.get_skl_risks()):
                filtered.append_patient(patient)
        return filtered
