import src.config as cfg

from src.objects.ai import AI
import src.util.util as util

from src.objects.variable_input import VariableInput
import json

def load_ai_requirements(ai):
    # load required images
    for img_name in util.get_file_list(ai.required_images_folder_path_name()):
        if not util.is_file(cfg.FILES_AI_SKIN_LESION_IMAGES_PATH, img_name):
            util.create_file("", cfg.FILES_AI_SKIN_LESION_IMAGES_PATH, img_name)
            print(img_name + " file created")

def load_ai():
    ai_dict = {}
    for ai_name in util.get_dir_list(cfg.AI_PATH):
        if ai_name != "__pycache__":
            try:
                ai = AI(ai_name)
                load_ai_requirements(ai)
                ai_dict[ai_name] = ai
            except RuntimeError as rr:
                print(ai_name + " UPLOAD ABORTED")
                print(rr.args)
    return ai_dict


