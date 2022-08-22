# This Python file uses the following encoding: utf-8
from .data_object import *

from .image import Image
from .image_list import ImageList

class SkinLesion(DataObject):
    def __init__(self, number, patient_id, characteristics, ai_results = {}, location=None):

        self.number = number
        self.patient_id = patient_id
        self.location = location

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
            return True
        except ValueError as err:
            print(err.args)

    def create_skin_lesion(self):
        if not self.save_data():
            raise ValueError('Skin lesion not created', "SKIN_LESION", "NO_CREATED")

    def save_images(self, images):
        saved_images = ImageList()
        for img_type, imgs in images.imgs_dict.items():
            if len(imgs) > 0:
                self.verify_skl_img_folder(img_type)
                path = self.get_skl_img_folder_path(img_type)
#                saved_images_list = []
                # the image will be saved if there is not anothe images with the same content
                # if alrready exists an image with the same name but with diferent content a new name is created
                # failure: open an image X called 01.png, opend a diferent image X2 also called 01.png and will be saved with the name 01_2.png
                #   then open the same last image (X2), this last image will be compared withe the fisrt image (X) and no with se second one (X2)
                #   so the image X2 will be save twice with the names 01_2.png, 01_3.png
                # solution: compare each image with all the others, what will take time
                for img in imgs:
                    if not self.exists_image(img, img_type):
                        img_src = util.gen_path(path, self.__gen_image_name(img, img_type))
                        util.copy_file(img.src, img_src)
                        saved_images.append_image(img_type, Image(img_src, img_type))

#                        saved_images_list.append(Image(img_src, img_type))
        return saved_images


    def exists_image(self, img, img_type):
        skl_img_src = util.gen_path(self.get_skl_img_folder_path(img_type), img.name_extension)
        return (util.is_file(skl_img_src) and img == Image(skl_img_src, img_type))

    def __gen_image_name(self, img, img_type):
        if util.is_file(self.get_skl_img_folder_path(img_type), img.name_extension):
            nb = 2
            while util.is_file(util.gen_path(self.get_skl_img_folder_path(img_type), img.name + "_" + str(nb) + "." + img.info_dict["image_format"])):
                nb = nb+1
            return img.name + "_" + str(nb) + "." + img.info_dict["image_format"]
        else:
            return img.name_extension

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
        if "photography" in img_dirs and self.get_skl_img_number("photography") > 0:
            return self.get_skl_imgs("photography", 1)[0]
        elif "medical_image" in img_dirs and self.get_skl_img_number("medical_image") > 0:
            return self.get_skl_imgs("medical_image", 1)[0]
        elif "dermoscopy" in img_dirs and self.get_skl_img_number("dermoscopy") > 0:
            return self.get_skl_imgs("dermoscopy", 1)[0]
        else:
            return None

    def get_risk(self):
        return self.__calc_risk()

    def is_benign(self):
        return (self.__calc_risk() == 0)

    def is_malignant(self):
        return (self.__calc_risk() == 1)

    def is_indeterminate(self):
        return (self.__calc_risk() == 2)

    def __calc_risk(self):
        for ai_name, ai_content in self.ai_results.items():
            for label, result in ai_content.items():
                if type(result) is str and "benign" == result.lower():
                    return 0
                elif type(result) is str and "malignant" == result.lower():
                    return 1
                elif type(result) is str and "indeterminate" == result.lower():
                    return 2
        return -1

    def has_carach_value(self, charac_name, charac_value):
        if charac_name in self.characteristics:
            return util.compare_with_dates(charac_value, self.characteristics[charac_name])

    def has_carach_value_in_range(self, charac_name, min, max, include=True):
        if charac_name in self.characteristics:
            return util.in_range_with_dates(self.characteristics[charac_name], min, max, include)

    def has_charach_value_containing_one(self, charac_name, charac_values, case_sensitive=True):
        if charac_name in self.characteristics:
            return util.contains_one(self.characteristics[charac_name], charac_values, case_sensitive)
