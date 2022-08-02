# This Python file uses the following encoding: utf-8
from .data_object import *

from .skin_lesion import SkinLesion

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

            # patient foler
            self.folder_path = ""


        # skin lesions
        self.skin_lesions = []

    def verify_data(self):
        if (self._verify(self.first_name, "NAME", "FIRST_NAME") and
            self._verify(self.last_name, "NAME", "LAST_NAME") 
            ):
            return True
        return False 

    def initialize(self, id, first_name, last_name, birth_date, gender, mi = {}):
        # basic information
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, '%d-%m-%Y')
        self.gender = gender
        self.mi = mi

        #    calculated
        self.age = util.calc_age(self.birth_date)

        # medical information
        if type(mi) is str:
            self.mi = json.loads(mi)

        # folders
        if len(self.id) > 0:
            self.folder_path  = cfg.PATIENTS_DATA_PATH + cfg._S + self.id
            self.verify_patient_folder()

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
                return True
            except ValueError as err:
                print(err.args)

    def create_patient(self):
        if self.save_data():
            self.folder_path  = cfg.PATIENTS_DATA_PATH + cfg._S + self.id
            self.verify_patient_folder()

    def update_data(self):
        if self.verify_data():
            try:
                dbc = DBController()
                dbc.update(cfg.TABLE_PATIENTS,
                    (self.first_name,
                    self.last_name,
                    self.birth_date.strftime('%d-%m-%Y'),
                    self.gender,
                    json.dumps(self.mi)),
                    (self.id,)
                    )
            except ValueError as err:
                print(err.args)

    @classmethod
    def get_patient_by_id(cls, patient_id):
        dbc = DBController()
        obj =  dbc.select(cfg.TABLE_PATIENTS, id = patient_id)

        if len(obj) > 0:
            obj = obj[0]
            return Patient(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        else:
            raise ValueError('No object found', "PATIENT", "NOT_FOUND")

    def to_string(self):
        return  ("(" + self.id + ", " +
            self.first_name + ", " +
            self.last_name + ", " +
            self.birth_date.strftime('%d-%m-%Y') + ", " +
            str(self.gender) + ", " +
            str(self.age) + ", " +
            json.dumps(self.mi) + ", " +
            ")")

    def verify_patient_folder(self):
        if not util.is_dir(self.folder_path):
            util.create_dir(self.folder_path)


    def load_skin_lesions(self):
        dbc = DBController()
        for skl in dbc.select(cfg.TABLE_SKIN_LESIONS, id_patient = self.id):
            self.skin_lesions.append(SkinLesion(skl[0], skl[1], skl[2]))

