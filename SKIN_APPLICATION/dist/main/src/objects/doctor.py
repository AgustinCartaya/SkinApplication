# @autor: Agustin CARTAYA

# class modeling a doctor

from .data_object import *

class Doctor(DataObject):
    def __init__(self, *args):
        if len(args) > 0:
            if len(args) == 5:
                self.initialize(args[0], args[1], args[2], args[3], args[4])
            if len(args) == 4:
                self.initialize("", args[0], args[1], args[2], args[3])
        else:
            self.id = ""
            self.first_name = ""
            self.last_name = ""
            self.password = ""
            self.email = ""

    def initialize(self, id, first_name, last_name, password, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
    
    # create a doctor
    def create(self):
        # error thrown if data not accepted
        self.verify_data()

        self.save_data()

    # verification of doctor's data
    def verify_data(self):
        self._verify(self.first_name, self.VAR_NAME, err.EO_DOCTOR_FIRST_NAME)
        self._verify(self.last_name, self.VAR_NAME, err.EO_DOCTOR_LAST_NAME)
        self._verify(self.email, self.VAR_EMAIL, err.EO_DOCTOR_EMAIL)
        self._verify(self.password, self.VAR_PASSWORD, err.EO_DOCTOR_PASSWORD)

    # save the doctor's data in the database
    def save_data(self):
        dbc = DBController()
        dbc.insert(cfg.TABLE_DOCTORS,(self.first_name,
            self.last_name,
            self.password,
            self.email))
        
    # returns a doctor by his last name and password
    @classmethod
    def get_doctor(cls, last_name, password):
        if cls._verify(password, cls.VAR_PASSWORD, err.EO_DOCTOR_PASSWORD):
            dbc = DBController()
            obj = dbc.secure_select(cfg.TABLE_DOCTORS,
                                    (last_name, password),
                                    False)

            if len(obj) > 0:
                return Doctor(obj[0], obj[1], obj[2], obj[3], obj[4])
            else:
                raise ValueError(err.EO_DOCTOR_PASSWORD, err.ET_INCORRECT)

    # returns all the names of the doctors contained in the database
    @classmethod
    def get_doctors_last_name(cls):
        dbc = DBController()
        doctors_last_name = []
        for d in dbc.secure_select(cfg.TABLE_DOCTORS):
            doctors_last_name.append(d[2])
        return doctors_last_name
