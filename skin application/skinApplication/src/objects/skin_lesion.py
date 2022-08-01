# This Python file uses the following encoding: utf-8
from .data_object import *

class SkinLesion(DataObject):
    def __init__(self, number, patient_id, caracteristics):

        self.number = number
        self.patient_id = patient_id
        if type(caracteristics) is str:
            self.caracteristics = json.loads(caracteristics)
        elif type(caracteristics) is dict:
            self.caracteristics = caracteristics

        self.folder_path = cfg.PATIENTS_DATA_PATH + cfg._S + self.patient_id + cfg._S + cfg.SKL_FOLDER_SUFIX +  str(self.number)

        self.verify_skl_folder()


    def save_data(self):
        try:
            dbc = DBController()

            dbc.insert(cfg.TABLE_SKIN_LESIONS,(self.number,
                self.patient_id,
                json.dumps(self.caracteristics)
                ))
            return True
        except ValueError as err:
            print(err.args)

    def update_data(self):
        try:
            dbc = DBController()
            dbc.update(cfg.TABLE_SKIN_LESIONS,
                (json.dumps(self.caracteristics)),
                {"number":str(self.number), "id_patient":self.patient_id}
                )
        except ValueError as err:
            print(err.args)

    def create_skin_lesion(self):
        if not self.save_data():
            raise ValueError('Skin lesion not created', "SKIN_LESION", "NO_CREATED")

    def save_images(self, images_dic):
        for img_type, image_path_names in images_dic.items():
            if len(image_path_names) > 0:
                self.verify_image_folder(img_type)
                for src_image in image_path_names:
                    shutil.copy(src_image, self.get_image_type_folder_path(img_type))

    def get_image_type_folder_path(self, img_type):
        return self.get_images_folder_path() + cfg._S + img_type

    def verify_image_folder(self, img_type):
        if not os.path.isdir(self.get_image_type_folder_path(img_type)):
            os.mkdir(self.get_image_type_folder_path(img_type))

    def verify_skl_folder(self):
        if not os.path.isdir(self.folder_path):
            os.mkdir(self.folder_path)

        if not os.path.isdir(self.get_images_folder_path()):
            os.mkdir(self.get_images_folder_path())

        if not os.path.isdir(self.get_ai_results_folder_path()):
            os.mkdir(self.get_ai_results_folder_path())

        if not os.path.isdir(self.get_timeline_folder_path()):
            os.mkdir(self.get_timeline_folder_path())

    def get_images_folder_path(self):
        return self.folder_path + cfg._S + cfg.SKL_IMAGES_FOLDER_NAME

    def get_ai_results_folder_path(self):
        return self.folder_path + cfg._S + cfg.SKL_AI_RESULTS_FOLDER_NAME

    def get_timeline_folder_path(self):
        return self.folder_path + cfg._S + cfg.SKL_TIMELINE_FOLDER_NAME


    def to_string(self):
        return ("(" + str(self.number) + ", " +
            self.patient_id + ", " +
            json.dumps(self.caracteristics) +
            ")")
