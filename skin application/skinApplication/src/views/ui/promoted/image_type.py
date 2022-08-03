from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QComboBox, QDoubleSpinBox, QSpinBox, QFileDialog)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .image_type_creator import ImageTypeCreator

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner

class ImageType(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, id, name, nb_images = 0, new_images = []):
        QFrame.__init__(self, parent)

        self.id = id
        self.name = name
        self.nb_images = nb_images
        self.new_images = new_images
        self.img_path_name = set()

        self.__create()


    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # title
        self.lb_name = Label(self)
        self.lb_name.setText(self.name)
        self.lb_name.setMinimumSize(QSize(125, 0))
        self.lb_name.setMaximumSize(QSize(100, 16777215))
        self.layout.addWidget(self.lb_name)

        # nb images
        self.lb_nb_images = Label(self)
        self.layout.addWidget(self.lb_nb_images)

        # nb new images
        self.lb_nb_new_images = Label(self)
        self.layout.addWidget(self.lb_nb_new_images)

    def set_nb_images(self, nb_images):
        self.nb_images = nb_images
        self.lb_nb_images.setText("(" + str(self.nb_images) + ")")

    def __update_nb_new_images(self):
        if len(self.img_path_name) > 0:
            self.lb_nb_new_images.setText("+" + str(len(self.img_path_name)))

    def mousePressEvent(self, arg):
        self.loadFiles()

    def loadFiles(self):
        img_path_name, _ = QFileDialog.getOpenFileNames(self, 'Open file',
             'D:\\Documents\\Internship Documents\\Image data\\1AA\\images\\Microscopy\\MALAIRE DTE',"Image files (*.png *.jpg *.gif *.svg *.bmp)")
        self.img_path_name.update(img_path_name)
        self.__update_nb_new_images()

    def get_image_path_names(self):
        return self.img_path_name
