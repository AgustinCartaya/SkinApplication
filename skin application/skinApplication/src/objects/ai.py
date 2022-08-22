# This Python file uses the following encoding: utf-8
from .data_object import *
import importlib

from .image_list import ImageList

class AI(DataObject):
    def __init__(self, name):
        self.name = name

        self.folder = util.gen_path(cfg.AI_PATH, name)
        self.req_images = None
        self.description = ""
        self.req_mi = []
        self.req_skl_charac =[]

        # actual patient_skin_lesion = (patient, skin_lesion, images_dict, mi_list, req_skl_charac_list)
        self.actual_p = None
        self.actual_skl = None
        self.actual_images = None
        self.actual_bi = {}
        self.actual_mi = {}
        self.actual_skl_charac = {}

        self.__charge_required_images_dict()
        self.__charge_description()
        self.__charge_required_patient_medical_information_list()
        self.__charge_required_skin_lesion_characteristics_list()



#        print(self.name + " charged successfully")

#        print(self.req_images)
#        print(self.description)
#        print(self.req_mi)
#        print(self.req_skl_charac)


#    def __charge_required_patient_basic_information(self):
#        pass

    def __charge_required_images_dict(self):
        if util.is_dir(self.required_images_folder_path_name()):
            self.req_images = {}
            for skl_img in util.get_file_list(self.required_images_folder_path_name()):
                self.req_images[skl_img] = json.loads(util.read_file(self.required_images_folder_path_name(), skl_img))
        else:
            raise RuntimeError('FAILED TO OPEN REQUIRED IMAGES FOLDER FOR: ' + self.name)

    def __charge_description(self):
        if util.is_file(self.description_file_path_name()):
            self.description = util.read_file(self.description_file_path_name())
        else:
            print("No description file found in " + cfg.ACTUAL_LANGUAGE + " for: " + self.name)

    def __charge_required_patient_medical_information_list(self):
        if util.is_dir(self.required_mi_folder_path_name()):
            for req in util.get_file_list(self.required_mi_folder_path_name()):
                self.req_mi.append(req.split(".")[0])
        else:
            print("No " + cfg.AI_REQUIRED_MEDICAL_INFORMATION_FOLDER_NAME + " folder for: " + self.name)

    def __charge_required_skin_lesion_characteristics_list(self):
        if util.is_dir(self.required_skl_charac_folder_path_name()):
            for req in util.get_file_list(self.required_skl_charac_folder_path_name()):
                self.req_skl_charac.append(req.split(".")[0])
        else:
            print("No " + cfg.AI_REQUIRED_SKIN_LESION_CHARACTERISTICS_FOLDER_NAME + " folder for: " + self.name)

    def get_info_folder(self):
        return util.gen_path(self.folder, cfg.AI_INFO_FOLDER_NAME)

    def required_images_folder_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_REQUIRED_IMAGES_FOLDER_NAME)

    def description_file_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_DESCRIPTION_FILE_NAME + "." + cfg.ACTUAL_LANGUAGE)

    def required_mi_folder_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_REQUIRED_MEDICAL_INFORMATION_FOLDER_NAME)

    def required_skl_charac_folder_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_REQUIRED_SKIN_LESION_CHARACTERISTICS_FOLDER_NAME)

    def set_actual_patient_and_skin_lesion(self, patient, skin_lesion):
        self.actual_p = patient
        self.actual_skl = skin_lesion
        self.__charge_actual_req_images()
        self.__charge_actual_req_bi()
        self.__charge_actual_req_mi()
        self.__charge_actual_skl_charac()

    def __charge_actual_req_images(self):
        self.actual_images = ImageList()
        for img_name, img_info in self.req_images.items():
            self.actual_images.append_images(img_name, self.actual_skl.get_skl_imgs(img_name, img_info["max"]))

    def __charge_actual_req_bi(self):
        self.actual_bi["gender"] = self.actual_p.gender
        self.actual_bi["age"] = self.actual_p.age

    def __charge_actual_req_mi(self):
        for mi_name in self.req_mi:
            if mi_name in self.actual_p.mi:
                self.actual_mi[mi_name] = self.actual_p.mi[mi_name]
            else:
                self.actual_mi[mi_name] = None

    def __charge_actual_skl_charac(self):
        for skl_charac in self.req_skl_charac:
            if skl_charac in self.actual_skl.characteristics:
                self.actual_skl_charac[skl_charac] = self.actual_skl.characteristics[skl_charac]
            else:
                self.actual_skl_charac[skl_charac] = None

    def reset_actual_patient_and_skin_lesion(self):
        self.actual_p = None
        self.actual_skl = None
        self.actual_images = None
        self.actual_bi = {}
        self.actual_mi = {}
        self.actual_skl_charac = {}

    def is_ready_to_launch(self):
        # verifying existence of data
        if (self.actual_p is None or
            self.actual_skl is None or
            self.actual_images is None):

            return False

        # verifying images
        for img_name, img_data in self.req_images.items():
            if not (img_name in self.actual_images.imgs_dict and
                    len(self.actual_images.imgs_dict[img_name]) >= img_data["min"]):
                return False

        # verify medical information
        for mi_name, mi_value in self.actual_mi.items():
            if mi_value is None:
                return False

        # verify medical information
        for skl_charac_name, skl_charac_value in self.actual_skl_charac.items():
            if skl_charac_value is None:
                return False

        return True

    def launch(self):
        if not self.is_ready_to_launch():
            return False
        try:
            ai_run_file = importlib.import_module("ai." + self.name + ".run")
            results = ai_run_file.run(self.actual_images.get_src_dict(),
                            {"P_BI":self.actual_bi,
                            "P_MI":self.actual_mi,
                            "SKL_CHARAC":self.actual_skl_charac})

            if (results is not None and type(results) is dict and len(results) > 0):
                return results
            else:
                return False
        except ValueError as err:
            print(err.args)
            return False
