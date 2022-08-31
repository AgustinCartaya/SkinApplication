# @autor: Agustin CARTAYA

# class in charge of modeling an AI

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

    # loading ai requirements
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
            raise RuntimeError("NO " + cfg.AI_REQUIREMENTS_FILE_NAME + " FILE FOR: " + self.name)

    # load the images required by the ai
    def __charge_required_images(self, img_json):
        self.req_images = {}
        for img_name, values in  img_json.items():
           if "min" not in values or "max" not in values:
               raise RuntimeError("'MIN' OR 'MAX' PARAMETERS MISSING FOR " + img_name + " in: " + self.name)
        self.req_images = img_json

    # load the medical information required by the ai
    def __charge_required_patient_medical_information(self, mi_json):
        for mi_id, mi_content in mi_json.items():
            VariableInput.create_ai_variable_input(mi_id, mi_content, VariableInput.MI_INPUT, self.name)
            self.req_mi.append(mi_id)

    # load the skin lesion characteristics required by the ai
    def __charge_required_skin_lesion_characteristics(self, skl_charac_json):
        for skl_charac_id, skl_charac_content in skl_charac_json.items():
            VariableInput.create_ai_variable_input(skl_charac_id, skl_charac_content, VariableInput.SKL_INPUT, self.name)
            self.req_skl_charac.append(skl_charac_id)

    # load the description of the ai
    def __charge_description(self):
        if util.is_file(self.description_file_path_name()):
            self.description = util.read_file(self.description_file_path_name())
        else:
            print("No description file found in " + cfg.ACTUAL_LANGUAGE + " for: " + self.name)

    # getters and setters
    def get_info_folder(self):
        return util.gen_path(self.folder, cfg.AI_INFO_FOLDER_NAME)

    def required_images_folder_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_REQUIRED_IMAGES_FOLDER_NAME)

    def description_file_path_name(self):
        return util.gen_path(self.get_info_folder(), cfg.AI_DESCRIPTION_FILE_NAME + "." + cfg.ACTUAL_LANGUAGE)

    # set up a the lesion to study with the patient and load the required values
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

    # reset the lesion to study
    def reset_actual_patient_and_skin_lesion(self):
        self.actual_p = None
        self.actual_skl = None
        self.actual_images = None
        self.actual_bi = {}
        self.actual_mi = {}
        self.actual_skl_charac = {}

    # check if the ai contains all the necessary information to be launched
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

    # launch the ai
    def launch(self):
        # check if it is ready to be launched
        if not self.is_ready_to_launch():
            return False
        try:
            # import the ai launch file
            ai_run_file = importlib.import_module(cfg.AI_FOLDER_NAME + "." + self.name + "." + cfg.AI_RUN_FILE_NAME)
            # call the 'run' method of the launch file of the ai
            # passing the necessary images as a parameter and a dictionary with the necessary information
            results = ai_run_file.run(self.actual_images.get_src_dict(),
                            {"basic_information":self.actual_bi,
                            "medical_information":self.actual_mi,
                            "skin_lesion_characteristics":self.actual_skl_charac})

            # returns the results of the ai
            if (results is not None and type(results) is dict and len(results) > 0):
                return results
            else:
                return False
        except ValueError as err:
            print(err.args)
            return False
