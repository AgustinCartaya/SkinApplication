# This Python file uses the following encoding: utf-8
from .data_object import *

from .skin_lesion import SkinLesion
from .image import Image
from .image_list import ImageList
import pickle

class TimeLinePoint(DataObject):
    def __init__(self, skin_lesion, images, date=None):
        self.skl = skin_lesion
        self.images = images

        if date is None:
            self.date = datetime.today()
        else:
            self.date = date

    def __create_data(self, images):
        info_dict = {
        "skin_lesion": [self.skl.number, self.skl.patient_id, json.dumps(self.skl.characteristics), json.dumps(self.skl.ai_results)],
        "images":json.dumps(images.get_src_dict())
        }
        return json.dumps(info_dict)

    def upsert(self):
        data = ""
        path = self.skl.get_timeline_folder_path()
        file_name = self.date.strftime('%Y-%m-%d')

        if util.is_file(path, file_name):
            data = self.__get_data_update(path, file_name)
        else:
            data = self.__create_data(self.images)
#        util.create_file(data, path, file_name)

        with open(util.gen_path(path, file_name), 'wb') as f:
            pickle.dump(self, f)

    def __get_data_update(self, path, name):
        tlp = TimeLinePoint.read_point(path, name)
        joined_images = ImageList(tlp.images, self.images)

        return self.__create_data(joined_images)

    @classmethod
    def read_point(csl, path, file_name):
        with open(util.gen_path(path, file_name), 'rb') as f:
            data = pickle.load(f)
            for img_type, imgs in data.images.imgs_dict.items():
                for img in imgs:
                    print(img.src)
        return data

