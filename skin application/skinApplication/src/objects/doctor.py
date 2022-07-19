# This Python file uses the following encoding: utf-8
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
    

    def verify_data(self):
        if (self._verify(self.first_name, "NAME", "FIRST_NAME") and
            self._verify(self.last_name, "NAME", "LAST_NAME") and 
            self._verify(self.email, "EMAIL", "EMAIL") and
            self._verify(self.password, "PASSWORD", "PASSWORD")
            ):
            return True
        return False 

    def save_data(self):
        if self.verify_data():
            try:
                dbc = DBController()
                dbc.insert(cfg.TABLE_DOCTORS,(self.first_name,
                    self.last_name,
                    self.password,
                    self.email))
            except ValueError as err:
                # If doctor already exists
                print(err.args)
            
    def obtain_doctors_name(self):
        dbc = DBController()
        return dbc.select(cfg.TABLE_DOCTORS,
            cfg.COLUMN_DOCTORS_LAST_NAME)
        
    def get_doctor_by_last_name_and_password(self, last_name, password):
        if (self._verify(last_name, "NAME", "LAST_NAME") and
           self._verify(password, "PASSWORD", "PASSWORD")
           ):
            dbc = DBController()
            obj = dbc.select(cfg.TABLE_DOCTORS,
                last_name = last_name,
                password = password)

            if len(obj) > 0:
                obj = obj[0]
                self.initialize(obj[0], obj[1], obj[2], obj[3], obj[4])
            else:
                raise ValueError('No object found', "DOCTOR", "NOT_FOUND")


        
