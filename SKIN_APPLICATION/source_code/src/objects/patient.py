# @autor: Agustin CARTAYA

# class modeling a patient

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
            self.folder_path  = util.gen_path(cfg.PATIENTS_DATA_PATH,self.id)
            self.verify_patient_folder()

    def create(self, doctor_id):
        # error thrown if data not accepted
        self.verify_data()
        self.__save_data(doctor_id)

        self.folder_path  = util.gen_path(cfg.PATIENTS_DATA_PATH, self.id)
        self.verify_patient_folder()

    def verify_data(self):
        self._verify(self.first_name, self.VAR_NAME, err.EO_PATIENT_FIRST_NAME)
        self._verify(self.last_name, self.VAR_NAME, err.EO_PATIENT_LAST_NAME)

    def __save_data(self, doctor_id):
        dbc = DBController()
        self.id = util.generate_id(self.first_name+self.last_name)
        while dbc.secure_exists(cfg.TABLE_PATIENTS, (self.id,)):
            self.id = util.generate_id(self.first_name+self.last_name)

        dbc.insert(cfg.TABLE_PATIENTS,(self.id,
            self.first_name,
            self.last_name,
            self.birth_date.strftime('%d-%m-%Y'),
            self.gender,
            json.dumps(self.mi),
            doctor_id)
            )

    def update(self):
        self.verify_data()
        dbc = DBController()
        dbc.update(cfg.TABLE_PATIENTS,
            (self.first_name,
            self.last_name,
            self.birth_date.strftime('%d-%m-%Y'),
            self.gender,
            json.dumps(self.mi)),
            (self.id,)
            )

    def delete(self):
        dbc = DBController()
        dbc.delete(cfg.TABLE_PATIENTS,(self.id,))
        util.delete_dir(self.folder_path)

    @classmethod
    def get_patient_by_id(cls, patient_id):
        dbc = DBController()
        obj =  dbc.secure_select(cfg.TABLE_PATIENTS, (patient_id,), False)

        if len(obj) > 0:
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
        for skl in dbc.secure_select(cfg.TABLE_SKIN_LESIONS, (self.id,)):
            self.skin_lesions.append(SkinLesion(skl[0], skl[1], skl[2], skl[3], skl[4]))

    def get_next_skl_number(self):
        max = 0
        for skl in self.skin_lesions:
            if skl.number >= max:
                max = skl.number + 1
        return max

    def has_benign_skl(self):
        for skl in self.skin_lesions:
            if skl.is_benign():
                return True

    def has_malignant_skl(self):
        for skl in self.skin_lesions:
            if skl.is_malignant():
                return True

    def has_indeterminate_skl(self):
        for skl in self.skin_lesions:
            if skl.is_indeterminate():
                return True

    def get_skl_risks(self):
        risks = []
        for skl in self.skin_lesions:
            risks.append(skl.get_risk())
        return risks

    def has_mi_value(self, mi_name, mi_value):
        if mi_name in self.mi:
            return util.compare_with_dates(mi_value, self.mi[mi_name])

    def has_mi_value_in_range(self, mi_name, min, max, include=True):
        if mi_name in self.mi:
            return util.in_range_with_dates(self.mi[mi_name], min, max, include)

    def has_mi_value_containing_one(self, mi_name, mi_values, case_sensitive=True):
        if mi_name in self.mi:
            return util.contains_one(self.mi[mi_name], mi_values, case_sensitive)

    def has_one_skl_with_charac_value(self, charac_name, charac_value):
        for skl in self.skin_lesions:
            if skl.has_carach_value(charac_name, charac_value):
                return True

    def has_one_skl_with_charac_value_in_range(self, charac_name, min, max, include=True):
        for skl in self.skin_lesions:
            if skl.has_carach_value_in_range(charac_name, min, max, include):
                return True

    def has_one_skl_with_charac_value_containing_one(self, charac_name, charac_values, case_sensitive=True):
        for skl in self.skin_lesions:
            if skl.has_charach_value_containing_one(charac_name, charac_values, case_sensitive):
                return True
