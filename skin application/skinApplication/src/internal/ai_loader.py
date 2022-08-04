import src.config as cfg

from src.objects.ai import AI
import src.util.util as util


def load_ai_requirements(ai):
    # load required images
    for img_name in util.get_file_list(ai.required_images_folder_path_name()):
        if not util.is_file(cfg.FILES_IMAGES_TYPE_PATH, img_name):
            util.create_file("", cfg.FILES_IMAGES_TYPE_PATH, img_name)
            print(img_name + " file created")

    # load required medical information
    for mi_name in util.get_file_list(ai.required_mi_folder_path_name()):
        if not util.is_file(cfg.FILES_MEDICAL_INFORMATION_PATH, mi_name):
            util.copy_file(util.gen_path(ai.required_mi_folder_path_name(),mi_name),
                           util.gen_path(cfg.FILES_MEDICAL_INFORMATION_PATH, mi_name))
            print(mi_name + " file created")

   # load required skin lesion characeristics
    for skl_charac_name in util.get_file_list(ai.required_skl_charac_folder_path_name()):
        if not util.is_file(cfg.FILES_SKIN_LESION_CHARACTERISTICS_PATH, skl_charac_name):
            util.copy_file(util.gen_path(ai.required_skl_charac_folder_path_name(),skl_charac_name),
                                        util.gen_path(cfg.FILES_SKIN_LESION_CHARACTERISTICS_PATH, skl_charac_name))
            print(skl_charac_name + " file created")

def load_ai():
    ai_dict = {}
    for ai_name in util.get_dir_list(cfg.AI_PATH):
        try:
            ai = AI(ai_name)
            load_ai_requirements(ai)
            ai_dict[ai_name] = ai
        except RuntimeError as rr:
            print(ai_name + " upload aborted")
            print(rr.args)
    return ai_dict


