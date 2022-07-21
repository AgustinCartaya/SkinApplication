# This Python file uses the following encoding: utf-8
from src.db_controllers.db_controller import DBController
import src.util.data_cleaner as dc
import src.config as cfg
import src.util.util as util

from operator import attrgetter
from .patient import Patient

class PatientList:
    def __init__(self):
        self.patients = []

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


