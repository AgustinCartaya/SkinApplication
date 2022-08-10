# This Python file uses the following encoding: utf-8
from .data_object import *

#from .skin_lesion import SkinLesion
from .image import Image
from .image_list import ImageList

class TimeLinePoint(DataObject):
    def __init__(self, skin_lesion, images=None, date=None):
        self.skl = skin_lesion
        self.images = images

        if date is None:
            self.date = datetime.today()
        else:
            self.date = date

    def __create_data(self, images):
        info_dict = {
        "skin_lesion": [self.skl.number, self.skl.patient_id, json.dumps(self.skl.characteristics), json.dumps(self.skl.ai_results)],
        "images":json.dumps(images)
        }
        return json.dumps(info_dict)

    def upsert(self, images=None):
        data = ""
        path = self.skl.get_timeline_folder_path()
        name = self.date.strftime('%Y-%m-%d')
        if images is None:
            images = ImageList()
        if util.is_file(path, name):
            data = self.__get_data_update(images, path, name)
        else:
            data = self.__get_data_insert(images)
        util.create_file(data, path, name)

    def __get_data_insert(self, images):
        imgs_dict = {}
        for img_name, imgs in images.imgs_dict.items():
            imgs_dict[img_name] = [img.src for img in imgs]

        return self.__create_data(imgs_dict)

    def __get_data_update(self, images, path, name):
        tlp = TimeLinePoint.read_point(path, name)
        joined_images = ImageList(tlp.images, images)

        imgs_dict = {}
        for img_name, imgs in joined_images:
            imgs_dict[img_name] = [img.src for img in imgs]

        return self.__create_data(imgs_dict)

    @classmethod
    def read_point(csl, path, name):
        data = util.read_file(path, name)
        tlp_dict = json.loads(data)

        skl_data = tlp_dict["skin_lesion"]
        images_data = tlp_dict["images"]

        skl = SkinLesion(skl_data[0], skl_data[1], skl_data[2], skl_data[3])
        images = ImageList()
        for img_name, imgs in images_data.items():
            images.append_images(imgs)

        return TimeLinePoint(skl, images, name)
#self.img_path_name = set()
#self.img_path_name.update(img_path_name)
