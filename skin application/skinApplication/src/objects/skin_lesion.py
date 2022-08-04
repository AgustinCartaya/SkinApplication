# This Python file uses the following encoding: utf-8
from .data_object import *

class SkinLesion(DataObject):
    def __init__(self, number, patient_id, characteristics, ai_results = {}):

        self.number = number
        self.patient_id = patient_id

        if type(characteristics) is str:
            self.characteristics = json.loads(characteristics)
        elif type(characteristics) is dict:
            self.characteristics = characteristics

        if type(ai_results) is str:
            self.ai_results = json.loads(ai_results)
        elif type(ai_results) is dict:
            self.ai_results = ai_results

        self.folder_path = util.gen_path(cfg.PATIENTS_DATA_PATH, self.patient_id, cfg.SKL_FOLDER_SUFIX +  str(self.number))

        self.verify_skl_folder()


    def save_data(self):
        try:
            dbc = DBController()

            dbc.insert(cfg.TABLE_SKIN_LESIONS,(self.number,
                self.patient_id,
                json.dumps(self.characteristics),
                json.dumps(self.ai_results)
                ))
            return True
        except ValueError as err:
            print(err.args)

    def update_data(self):
        try:
            dbc = DBController()
            dbc.update(cfg.TABLE_SKIN_LESIONS,
                (json.dumps(self.characteristics),json.dumps(self.ai_results)),
                (str(self.number), self.patient_id)
                )
        except ValueError as err:
            print(err.args)

    def create_skin_lesion(self):
        if not self.save_data():
            raise ValueError('Skin lesion not created', "SKIN_LESION", "NO_CREATED")

    def save_images(self, images_dic):
        for img_type, image_path_names in images_dic.items():
            if len(image_path_names) > 0:
                self.verify_image_type_folder(img_type)
                for src_image in image_path_names:
                    util.copy_file(src_image, self.get_image_type_folder_path(img_type))

    def get_images_folder_path(self):
        return util.gen_path(self.folder_path, cfg.SKL_IMAGES_FOLDER_NAME)

    def get_ai_results_folder_path(self):
        return util.gen_path(self.folder_path, cfg.SKL_AI_RESULTS_FOLDER_NAME)

    def get_timeline_folder_path(self):
        return util.gen_path(self.folder_path, cfg.SKL_TIMELINE_FOLDER_NAME)

    def get_image_type_folder_path(self, img_type):
        return util.gen_path(self.get_images_folder_path(), img_type)

    def verify_image_type_folder(self, img_type):
        if not util.is_dir(self.get_image_type_folder_path(img_type)):
            util.create_dir(self.get_image_type_folder_path(img_type))

    def verify_skl_folder(self):
        if not util.is_dir(self.folder_path):
            util.create_dir(self.folder_path)

        if not util.is_dir(self.get_images_folder_path()):
            util.create_dir(self.get_images_folder_path())

        if not util.is_dir(self.get_timeline_folder_path()):
            util.create_dir(self.get_timeline_folder_path())

    def get_number_image_type(self, image_type):
        if util.is_dir(self.get_image_type_folder_path(image_type)):
            return len(util.get_file_list(self.get_image_type_folder_path(image_type)))
        else:
            return 0

    def get_images_type_available(self):
        return util.get_dir_list(self.get_images_folder_path())

    def get_number_images_type(self):
        number_images_type = {}
        for image_type in self.get_images_type_available():
            number_images_type[image_type] = self.get_number_image_type(image_type)
        return number_images_type

    def to_string(self):
        return ("(" + str(self.number) + ", " +
            self.patient_id + ", " +
            json.dumps(self.characteristics) +
            ")")
