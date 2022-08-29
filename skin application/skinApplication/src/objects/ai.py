# This Python file uses the following encoding: utf-8
from .data_object import *
import importlib

from .image_list import ImageList
from .variable_input import VariableInput

class AI(DataObject):
    def __init__(self, name):
        self.name = name

        self.folder = util.gen_path(cfg.AI_PATH, name)
        self.req_images = None
        self.description = ""
        self.req_mi = []
        self.req_skl_charac = []

        # actual patient_skin_lesion = (patient, skin_lesion, images_dict, mi_list, req_skl_charac_list)
        self.actual_p = None
        self.actual_skl = None
        self.actual_images = None
        self.actual_bi = {}
        self.actual_mi = {}
        self.actual_skl_charac = {}

        self.__charge_requirements()
        self.__charge_description()

    def __charge_requirements(self):
        req_file = util.search_file(self.get_info_folder(), cfg.AI_REQUIREMENTS_FILE_NAME, True)
        if req_file is not None:
            req = json.loads(util.read_file(self.get_info_folder(), req_file))

            if cfg.AI_REQUIRED_IMAGES_JSON in req:
                self.__charge_required_images(req[cfg.AI_REQUIRED_IMAGES_JSON])

            if cfg.AI_REQUIRED_MEDICAL_INFORMATION_JSON in req:
                self.__charge_required_patient_medical_information(req[cfg.AI_REQUIRED_MEDICAL_INFORMATION_JSON])

            if cfg.AI_REQUIRED_SKIN_LESION_CHARACTERISTICS_JSON in req:
                self.__charge_required_skin_lesion_characteristics(req[cfg.AI_REQUIRED_SKIN_LESION_CHARACTERISTICS_JSON])

        else:
            raise RuntimeError("No " + cfg.AI_REQUIREMENTS_FILE_NAME + " file for: " + self.name)


    def __charge_required_images(self, img_json):
        self.req_images = {}
        for img_name, values in  img_json.items():
           if "min" not in values or "max" not in values:
               raise RuntimeError("'min' or 'max' parameter missing for " + img_name + " in: " + self.name)
        self.req_images = img_json

    def __charge_required_patient_medical_information(self, mi_json):
        for mi_id, mi_content in mi_json.items():
            VariableInput.create_ai_variable_input(mi_id, mi_content, VariableInput.MI_INPUT, self.name)
            self.req_mi.append(mi_id)

    def __charge_required_skin_lesion_characteristics(self, skl_charac_json):
        for skl_charac_id, skl_charac_content in skl_charac_json.items():
            VariableInput.create_ai_variable_input(skl_charac_id, skl_charac_content, VariableInput.SKL_INPUT, self.name)
            self.req_skl_charac.append(skl_charac_id)

    def __charge_description(self):
        if util.is_file(self.description_file_path_name()):
            self.description = util.read_file(self.description_file_path_name())
        else:
            print("No description file found in " + cfg.ACTUAL_LANGUAGE + " for: " + self.name)

    def get_info_folder(self):
        return util.gen_path(self.folder, cfg.AI_INFO_FOLDER_NAME)

    def required_images_folder_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_REQUIRED_IMAGES_FOLDER_NAME)

    def description_file_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_DESCRIPTION_FILE_NAME + "." + cfg.ACTUAL_LANGUAGE)

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
