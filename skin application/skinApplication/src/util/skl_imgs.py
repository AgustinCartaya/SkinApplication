import src.util.util as util
import src.config as cfg

def get_available_skl_imgs():
    return util.get_file_list(cfg.FILES_SKIN_LESION_IMAGES_PATH)
