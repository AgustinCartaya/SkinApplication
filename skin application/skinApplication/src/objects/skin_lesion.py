# This Python file uses the following encoding: utf-8
from .data_object import *

from .image import Image
from .image_list import ImageList
from .time_line_point import TimeLinePoint

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

        self.time_line_point = TimeLinePoint(self)


    def save_data(self):
        try:
            dbc = DBController()

            dbc.insert(cfg.TABLE_SKIN_LESIONS,(self.number,
                self.patient_id,
                json.dumps(self.characteristics),
                json.dumps(self.ai_results)
                ))
            self.time_line_point.upsert()
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
            self.time_line_point.upsert()
            return True
        except ValueError as err:
            print(err.args)

    def create_skin_lesion(self):
        if not self.save_data():
            raise ValueError('Skin lesion not created', "SKIN_LESION", "NO_CREATED")

    def save_images(self, images):
        for img_type, imgs in images.imgs_dict.items():
            if len(imgs) > 0:
                self.verify_skl_img_folder(img_type)
                for img in imgs:
                    util.copy_file(img.src, self.get_skl_img_folder_path(img_type))
        self.time_line_point.upsert(images)

    def get_images_folder_path(self):
        return util.gen_path(self.folder_path, cfg.SKL_IMAGES_FOLDER_NAME)

    def get_timeline_folder_path(self):
        return util.gen_path(self.folder_path, cfg.SKL_TIMELINE_FOLDER_NAME)

    def get_skl_img_folder_path(self, skl_img):
        return util.gen_path(self.get_images_folder_path(), skl_img)

    def verify_skl_img_folder(self, skl_img):
        if not util.is_dir(self.get_skl_img_folder_path(skl_img)):
            util.create_dir(self.get_skl_img_folder_path(skl_img))

    def verify_skl_folder(self):
        if not util.is_dir(self.folder_path):
            util.create_dir(self.folder_path)

        if not util.is_dir(self.get_images_folder_path()):
            util.create_dir(self.get_images_folder_path())

        if not util.is_dir(self.get_timeline_folder_path()):
            util.create_dir(self.get_timeline_folder_path())

    def get_available_skl_img_names(self):
        return util.get_dir_list(self.get_images_folder_path())

    def get_all_skl_imgs(self):
        image_list = ImageList()
        for name in self.get_available_skl_img_names():
            image_list.append_images(name, self.get_skl_imgs(name))
        return image_list

    def get_skl_imgs(self, name, nb_of_images=0, filtered_by="name"):
        img_list = []
        if util.is_dir(self.get_skl_img_folder_path(name)):
            if nb_of_images == 0:
                img_list = [Image(util.gen_path(self.get_skl_img_folder_path(name), src), name) for src in util.get_file_list(self.get_skl_img_folder_path(name))]
            else:
                img_list = [Image(util.gen_path(self.get_skl_img_folder_path(name), src), name) for src in util.get_file_list(self.get_skl_img_folder_path(name))[:nb_of_images]]
        return img_list

    def get_skl_img_number(self, skl_img):
        if util.is_dir(self.get_skl_img_folder_path(skl_img)):
            return len(util.get_file_list(self.get_skl_img_folder_path(skl_img)))
        else:
            return 0

    def get_skl_img_numbers(self):
        number_skl_imgs = []
        for skl_img in self.get_available_skl_img_names():
            number_skl_imgs.append([skl_img, self.get_skl_img_number(skl_img)])
        return number_skl_imgs

    def to_string(self):
        return ("(" + str(self.number) + ", " +
            self.patient_id + ", " +
            json.dumps(self.characteristics) +
            ")")

    def get_photography(self):
        img_dirs = [dir_name.lower() for dir_name in self.get_available_skl_img_names()]
        if "photography" in img_dirs:
            return self.get_skl_imgs("photography", 1)[0]
        elif "medical_image" in img_dirs:
            return self.get_skl_imgs("medical_image", 1)[0]
        else:
            return None

