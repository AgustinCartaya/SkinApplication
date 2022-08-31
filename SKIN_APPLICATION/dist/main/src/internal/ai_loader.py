# @autor: Agustin CARTAYA

import src.config as cfg
from src.objects.ai import AI
import src.util.util as util


# loading the required images for the AI
# for each required image a new file named with the name of the required image
# is created in the FILES_AI_SKIN_LESION_IMAGES_PATH folder
def load_ai_images(ai):
    if ai.req_images is not None:
        for img_name in ai.req_images:
            if not util.is_file(cfg.FILES_AI_SKIN_LESION_IMAGES_PATH, img_name):
                util.create_file("", cfg.FILES_AI_SKIN_LESION_IMAGES_PATH, img_name)
                print(img_name + " file created")


# checking the existence of the run.py file of the ai
# this file allow the communication between the ai and the application
def check_ai_run_file(ai):
    if not util.is_file(ai.folder, cfg.AI_RUN_FILE_NAME + ".py"):
        raise RuntimeError("NO run.py FILE FOUND FOR " + ai.name)


# loading the existents AI
# if any AI does not meet any of the requirements, it will not be charged.
def load_ai():
    ai_dict = {}
    for ai_name in util.get_dir_list(cfg.AI_PATH):
        if ai_name != "__pycache__":
            try:
                ai = AI(ai_name)
                check_ai_run_file(ai)
                load_ai_images(ai)
                ai_dict[ai_name] = ai
                print(ai_name + " loaded successfully")
            except RuntimeError as rr:
                print(rr.args)
                print(ai_name + " UPLOAD ABORTED")
    return ai_dict


