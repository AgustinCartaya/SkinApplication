from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout

from .button import Button
from .add_skl_img_item import AddSklImgItem
from .add_skl_img_creator import AddSklImgCreator


import src.util.data_cleaner as data_cleaner
import src.util.util as util

class AddSklImgContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self,
        parent,
        folder,
        bt_text = "Create new type of image",
        ):
        QFrame.__init__(self, parent)

        self.skl_img_items = {}
        self.folder = folder
        self.bt_text = bt_text

        self.skl_img_creator = None

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(30)

        self.__show_skl_img()
        self.__create_bt_creator()

    def __show_skl_img(self):
        self.skl_img_layout = QVBoxLayout()
        self.skl_img_layout.setContentsMargins(0, 0, 0, 0)
        self.skl_img_layout.setSpacing(0)
        self.layout.addLayout(self.skl_img_layout)

        for file_name in util.get_file_list(self.folder):
            skl_img_title = util.file_name_to_title(file_name)

            self.__show_single_skl_img(file_name, skl_img_title)

    def __show_single_skl_img(self, skl_img_id, skl_img_title):
        skl_img = AddSklImgItem(self, skl_img_id, skl_img_title)

        self.skl_img_layout.addWidget(skl_img)
        self.skl_img_items[skl_img_id] = skl_img

    def __create_bt_creator(self):
        self.bt_creator = Button(self)
        self.bt_creator.setText(self.bt_text)
        self.layout.addWidget(self.bt_creator,0, Qt.AlignHCenter)
        self.bt_creator.clicked.connect(self.__show_skl_img_creator)

    @Slot()
    def __show_skl_img_creator(self):
        if self.skl_img_creator is None:
            self.skl_img_creator = AddSklImgCreator(self, self.__create_new_skl_img, self.__cancel_new_skl_img)
            self.layout.addWidget(self.skl_img_creator)

    Slot(str)
    def __create_new_skl_img(self, skl_img_name):
        file_name = util.title_to_file_name(skl_img_name)
        if file_name in self.skl_img_items:
            raise ValueError('Caracteristic input already exists', "CARACTERISTIC_INPUT", "REPEATED")

        util.create_file("", self.folder, file_name)

        self.__show_single_skl_img(file_name, skl_img_name)
        self.__cancel_new_skl_img()

    @Slot()
    def __cancel_new_skl_img(self):
        self.skl_img_creator.setParent(None)
        self.skl_img_creator = None

    def get_selected_image_path_names(self):
        selected_images = {}
        for id, item in self.skl_img_items.items():
            selected_images[id] = item.get_image_path_names()
        return selected_images

#    def get_skl_img_ids(self):
#        return list(self.skl_img_items.keys())

    def set_number_images(self, skl_imgs_number_list):
        for element in skl_imgs_number_list:
            if element[0] in self.skl_img_items:
                self.skl_img_items[element[0]].set_nb_images(element[1])
            else:
                raise ValueError('Image skin lesion image not admited', "skl_img", "NOT_ADMITED")



