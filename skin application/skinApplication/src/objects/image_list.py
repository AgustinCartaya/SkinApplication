# This Python file uses the following encoding: utf-8
from operator import attrgetter

import src.config as cfg
import src.util.util as util


from .image import Image


class ImageList:
    def __init__(self, *args):
        self.imgs_dict ={}

        if len(args) >= 1:
            self.__duplicate(args)

    def __duplicate(self, image_list_list):
        for image_list in image_list_list:
            for img_type, imgs in image_list.imgs_dict.items():
                self.imgs_dict[img_type] = imgs

    def append_images(self, img_type, lst):
        self.imgs_dict[img_type] = lst

    def get_all_images(self, sorted_by="name", dsc=False ):
        img_list = []
        for _, imgs in self.imgs_dict.items():
            img_list = img_list + imgs
        img_list.sort(key=attrgetter(sorted_by), reverse=dsc)
        return img_list

    def get_filtered_by_types(self, types, inverse=False):
        filtered = ImageList()
        for img_type, imgs in self.imgs_dict.items():
            if (img_type in types) ^ inverse:
                filtered.append_images(img_type, imgs)
        return filtered

#    def get_list_sorted_by(self, by="id", dsc=True):
#        self.patients.sort(key=attrgetter(by), reverse=dsc)
#        self.sorted_by = by

    def get_types(self):
        return list(self.imgs_dict.keys())

