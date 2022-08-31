# @autor: Agustin CARTAYA

# class a list of images

from operator import attrgetter

import src.config as cfg
import src.util.util as util


from .image import Image


class ImageList:
    def __init__(self):
        self.imgs_dict ={}

    def __len__(self):
        return len(self.get_all_images())

    # unifies several lists of images without repetitions
    def join(self, *args):
        for image_list in args:
            for img_type, imgs in image_list.imgs_dict.items():
                if img_type in self.imgs_dict:
                    for img in imgs:
                        if img not in self.imgs_dict[img_type]:
                            self.append_image(img_type, img)
                else:
                    self.append_images(img_type, imgs)

    def append_images(self, img_type, lst):
        self.imgs_dict[img_type] = lst

    def append_image(self, img_type, img):
        if img_type in self.imgs_dict:
            self.imgs_dict[img_type].append(img)
        else:
            self.imgs_dict[img_type] = [img]

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

    def get_types(self):
        return list(self.imgs_dict.keys())

    def get_src_dict(self):
        src_dict = {}
        for img_type, imgs in self.imgs_dict.items():
            src_dict[img_type] = [img.src for img in imgs]
        return src_dict

    def get_name_extension_dict(self):
        src_dict = {}
        for img_type, imgs in self.imgs_dict.items():
            src_dict[img_type] = [img.name_extension for img in imgs]
        return src_dict

    def remove_image(self, img):
        self.imgs_dict[img.info_dict["type"]].remove(img)
