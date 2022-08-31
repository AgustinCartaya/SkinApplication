# @autor: Agustin CARTAYA

import src.config as cfg
import src.util.util as util
from src.db_controllers.db_controller import DBController


# check the existence of the neccesary directories
def check_directories():
    # Data base
    if not util.is_dir(cfg.DB_PATH):
        raise RuntimeError(cfg.DB_PATH + " DIRECTORY NOT EXISTS", "DB_DIR", "NOT_EXISTS")

    # Assets
    # ...
    if not util.is_dir(cfg.ASSETS_PATH):
        util.create_dir(cfg.ASSETS_PATH)

    if not util.is_dir(cfg.IMAGES_PATH):
        util.create_dir(cfg.IMAGES_PATH)

    if not util.is_dir(cfg.FILES_PATH):
        util.create_dir(cfg.FILES_PATH)

    # variable information
    if not util.is_dir(cfg.FILES_SKIN_LESION_IMAGES_PATH):
        util.create_dir(cfg.FILES_SKIN_LESION_IMAGES_PATH)

    # ai
    if not util.is_dir(cfg.FILES_AI_SKIN_LESION_IMAGES_PATH):
        util.create_dir(cfg.FILES_AI_SKIN_LESION_IMAGES_PATH)

    # created
    if not util.is_dir(cfg.FILES_CREATED_SKIN_LESION_IMAGES_PATH):
        util.create_dir(cfg.FILES_CREATED_SKIN_LESION_IMAGES_PATH)


# checking the existence of the data base
def chech_db():
    if not util.is_file(cfg.DB_PATH_NAME):
        dbc = DBController()
        dbc.db.verify_db_existence()


# checking
def check():
    check_directories()
    chech_db()
