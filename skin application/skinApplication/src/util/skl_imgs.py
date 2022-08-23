import src.util.util as util
import src.config as cfg


def get_availables_ai_skl_imgs():
    return util.get_file_list(cfg.FILES_AI_SKIN_LESION_IMAGES_PATH)

def get_availables_created_skl_imgs():
    return util.get_file_list(cfg.FILES_CREATED_SKIN_LESION_IMAGES_PATH)


def get_available_skl_imgs():
    return get_availables_ai_skl_imgs() + get_availables_created_skl_imgs()

def create_new_image_type(name):
    util.create_file("", cfg.FILES_CREATED_SKIN_LESION_IMAGES_PATH, name)
