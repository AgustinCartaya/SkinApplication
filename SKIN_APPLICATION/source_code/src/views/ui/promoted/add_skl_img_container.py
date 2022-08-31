from .promoted_container import *

from PySide6.QtWidgets import QInputDialog

from .add_skl_img_item import AddSklImgItem
import src.util.skl_imgs as skl_imgs

from src.objects.image_list import ImageList


class AddSklImgContainer(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)

        self.skl_img_items = {}
        self._pre_charge()

    def initialize(self):
        pass

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(30)

        self.__create_skl_imgs_items()

    def __create_skl_imgs_items(self):
        self.skl_img_layout = QVBoxLayout()
        self.skl_img_layout.setContentsMargins(0, 0, 0, 0)
        self.skl_img_layout.setSpacing(0)
        self.layout.addLayout(self.skl_img_layout)

        for file_name in skl_imgs.get_available_skl_imgs():
            self.__show_single_skl_img(file_name)

    def __show_single_skl_img(self, skl_img_id):
        skl_img = AddSklImgItem(self)
        skl_img.initialize(skl_img_id)

        self.skl_img_layout.addWidget(skl_img)
        self.skl_img_items[skl_img_id] = skl_img

    def get_selected_images(self):
        images = ImageList()
        for id, item in self.skl_img_items.items():
            images.append_images(id, list(item.get_image_path_names()))
        return images

    def set_number_images(self, skl_imgs_number_list):
        for element in skl_imgs_number_list:
            if element[0] in self.skl_img_items:
                self.skl_img_items[element[0]].set_nb_images(element[1])
#            else:
#                raise ValueError('Image skin lesion image not admited', "skl_img", "NOT_ADMITED")

    def append_new_skl_img(self, skl_img_id):
        self.__show_single_skl_img(skl_img_id)
