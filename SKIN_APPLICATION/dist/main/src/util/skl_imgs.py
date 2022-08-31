# @autor: Agustin CARTAYA

# this file is responsible for managing the different types of images
import src.util.util as util
import src.config as cfg


# search all types of images required by the ai
def get_availables_ai_skl_imgs():
    return util.get_file_list(cfg.FILES_AI_SKIN_LESION_IMAGES_PATH)


# search all types of images created by the doctor
def get_availables_created_skl_imgs():
    return util.get_file_list(cfg.FILES_CREATED_SKIN_LESION_IMAGES_PATH)


# search all types of images
def get_available_skl_imgs():
    return get_availables_ai_skl_imgs() + get_availables_created_skl_imgs()


# create a new image type
def create_new_image_type(name):
    util.create_file("", cfg.FILES_CREATED_SKIN_LESION_IMAGES_PATH, name)


# returns all accepted image extensions in string format
# used to filter the images
def get_accept_img_extensions_str():
    txt = ""
    ext_lst = util.str_to_list(cfg.IMG_ACCEPTED_EXTESIONS,",")
    nb = len(ext_lst)
    for i in range(nb):
        txt += " *." + ext_lst[i]
    return txt
