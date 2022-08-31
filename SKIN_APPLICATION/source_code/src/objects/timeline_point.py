# @autor: Agustin CARTAYA

# class modeling a point of the time line

from .data_object import *

from .skin_lesion import SkinLesion
from .image import Image
from .image_list import ImageList
import pickle

class TimelinePoint(DataObject):
    def __init__(self, skin_lesion, images, date):
        self.skl = skin_lesion
        self.images = images
        self.date = date

    @classmethod
    def upsert_point(csl, skin_lesion, images=None):
        date = datetime.today()
        path = skin_lesion.get_timeline_folder_path()
        file_name = date.strftime('%d-%m-%Y')
        images_to_save = {}
        if images is not None:
            # compressing images
            # update time line point
            if util.is_file(path, file_name):
                with open(util.gen_path(path, file_name), 'rb') as f:
                    tlp = pickle.load(f)
                    images_to_save = tlp.images
                    for img_type, img_nes in images.get_name_extension_dict().items():
                        if img_type in images_to_save:
                            images_to_save[img_type] = list(set(images_to_save[img_type] + img_nes))
                        else:
                            images_to_save[img_type] = img_nes
            # create time line point
            else:
                images_to_save = images.get_name_extension_dict()

        # creatinf serialized TimelinePoint
        with open(util.gen_path(path, file_name), 'wb') as f:
            pickle.dump(TimelinePoint(skin_lesion, images_to_save, date), f)


    @classmethod
    def read_point(csl, path, file_name):
        with open(util.gen_path(path, file_name), 'rb') as f:
            data = pickle.load(f)

            # decompressing images
            img_name_extension_dict = data.images
            data.images = ImageList()
            for img_type, img_nes in img_name_extension_dict.items():
                for img_ne in img_nes:
                    img_src = util.gen_path(data.skl.get_skl_img_folder_path(img_type),img_ne)
                    if util.is_file(img_src):
                        data.images.append_image(img_type, Image(img_src, img_type))
        return data

    # for test
    @classmethod
    def create_test_points(csl, skin_lesion):
        for i in range(1,4):
            date = datetime.now() - timedelta(i)
            path = skin_lesion.get_timeline_folder_path()
            file_name = date.strftime('%d-%m-%Y')
            images_to_save = {}
            with open(util.gen_path(path, file_name), 'wb') as f:
                pickle.dump(TimelinePoint(skin_lesion, images_to_save, date), f)

            date = datetime.now() - timedelta(i) - timedelta(30)
            path = skin_lesion.get_timeline_folder_path()
            file_name = date.strftime('%d-%m-%Y')
            images_to_save = {}
            with open(util.gen_path(path, file_name), 'wb') as f:
                pickle.dump(TimelinePoint(skin_lesion, images_to_save, date), f)

