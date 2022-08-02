from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout

from .button import Button
from .image_type import ImageType
from .image_type_creator import ImageTypeCreator


import src.util.data_cleaner as data_cleaner
import src.util.util as util

class ImagesTypeContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self,
        folder,
        bt_text = "Add new image type",
        *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.images_type = {}
        self.folder = folder
        self.bt_text = bt_text

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(30)

        self.__show_image_type()
        self.__create_bt_creator()

    def __show_image_type(self):
        self.image_type_layout = QVBoxLayout()
        self.image_type_layout.setContentsMargins(0, 0, 0, 0)
        self.image_type_layout.setSpacing(0)
        self.layout.addLayout(self.image_type_layout)

        for file_name in util.get_file_list(self.folder):
            image_type_title = util.file_name_to_title(file_name)

            self.__show_single_image_type(file_name, image_type_title)

    def __show_single_image_type(self, image_type_id, image_type_title):
        image_type = ImageType(image_type_id, image_type_title)

        self.image_type_layout.addWidget(image_type)
        self.images_type[image_type_id] = image_type

    def __create_bt_creator(self):
        self.bt_creator = Button(self)
        self.bt_creator.setText(self.bt_text)
        self.layout.addWidget(self.bt_creator,0, Qt.AlignHCenter)
        self.bt_creator.clicked.connect(self.__show_image_type_creator)

    @Slot()
    def __show_image_type_creator(self):
        self.image_type_creator = ImageTypeCreator(self.__create_new_image_type, self.__cancel_new_image_type)
        self.layout.addWidget(self.image_type_creator)

    Slot(str)
    def __create_new_image_type(self, image_type_name):
        file_name = util.title_to_file_name(image_type_name)
        if file_name in self.images_type:
            raise ValueError('Caracteristic input already exists', "CARACTERISTIC_INPUT", "REPEATED")

        util.create_file("", self.folder, file_name)

        self.__show_single_image_type(file_name, image_type_name)
        self.__cancel_new_image_type()

    @Slot()
    def __cancel_new_image_type(self):
        self.image_type_creator.setParent(None)
        self.image_type_creator = None

    def get_selected_image_path_names(self):
        selected_images = {}
        for image_type_id, image_type in self.images_type.items():
            selected_images[image_type_id] = image_type.get_image_path_names()
        return selected_images

#    def get_image_type_ids(self):
#        return list(self.images_type.keys())

    def set_number_images(self, images_type_number_dict):
        for image_type, number in images_type_number_dict.items():
            if image_type in self.images_type:
                self.images_type[image_type].set_nb_images(number)
            else:
                raise ValueError('Image type  not admited', "IMAGE_TYPE", "NOT_ADMITED")



