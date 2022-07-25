# This Python file uses the following encoding: utf-8
from .data_object import *

class Patient(DataObject):
    def __init__(self, *args):
        if len(args) > 0:

            if len(args) == 5:
                self.initialize("", args[0], args[1], args[2], args[3], args[4])
            if len(args) == 6:
                self.initialize(args[0], args[1], args[2], args[3], args[4], args[5])
        else:
            self.id = ""
            self.first_name = ""
            self.last_name = ""
            self.birth_date = ""
            self.gender = ""

            # calculated
            self.age = 0

            # medical information
            self.mi = {}


    def verify_data(self):
        if (self._verify(self.first_name, "NAME", "FIRST_NAME") and
            self._verify(self.last_name, "NAME", "LAST_NAME") 
            ):
            return True
        return False 

    def initialize(self, id, first_name, last_name, birth_date, gender, mi = {}):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, '%d-%m-%Y')
        self.gender = gender
        self.mi = mi
        if type(mi) is str:
            self.mi = json.loads(mi)


        self.age = util.calc_age(self.birth_date)

#        (QDate.currentDate().year() - QDate.fromString(birth_date).year())

    def save_data(self):
        if self.verify_data():
            try:
                dbc = DBController()

                self.id = util.generate_id(self.first_name+self.last_name)
                while dbc.exists(cfg.TABLE_PATIENTS, id=self.id):
                    self.id = util.generate_id(self.first_name+self.last_name)

                dbc.insert(cfg.TABLE_PATIENTS,(self.id,
                    self.first_name,
                    self.last_name,
                    self.birth_date.strftime('%d-%m-%Y'),
                    self.gender,
                    json.dumps(self.mi))
                    )
            except ValueError as err:
                # If doctor already exists
                print(err.args)

    def get_patient_by_id(self, id):
        dbc = DBController()
        obj =  dbc.select(cfg.TABLE_PATIENTS,
            id = '1')[0]

        if len(obj) > 0:
            obj = obj[0]
            self.initialize(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        else:
            raise ValueError('No object found', "DOCTOR", "NOT_FOUND")

    def to_string(self):
        return  ("(" + self.id + ", " +
            self.first_name + ", " +
            self.last_name + ", " +
            self.birth_date.strftime('%d-%m-%Y') + ", " +
            str(self.gender) + ", " +
            str(self.age) + ", " +
            json.dumps(self.mi) + ", " +
            ")")
