from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QComboBox, QDoubleSpinBox, QSpinBox, QFileDialog)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .add_skl_img_creator import AddSklImgCreator

from PySide6.QtCore import Signal, Slot

import src.util.util as util

from src.objects.image import Image

class AddSklImgItem(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, id, nb_images = 0, new_images = []):
        QFrame.__init__(self, parent)

        self.id = id
        self.nb_images = nb_images
        self.new_images = new_images
        self.img_path_name = set()

        self.__create()


    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # title
        self.lb_name = Label(self)
        self.lb_name.setText(self.id, format=True)
        self.lb_name.setMinimumSize(QSize(125, 0))
        self.lb_name.setMaximumSize(QSize(100, 16777215))
        self.layout.addWidget(self.lb_name)

        # nb images
        self.lb_nb_images = Label(self)
        self.layout.addWidget(self.lb_nb_images)

        # nb new images
        self.lb_nb_new_images = Label(self)
        self.layout.addWidget(self.lb_nb_new_images)

        # cancel images
        self.bt_cancel_new_images = Button(self)
        self.bt_cancel_new_images.setText("-")
        self.bt_cancel_new_images.setMaximumSize(QSize(22, 22))
        self.bt_cancel_new_images.set_type(Button.BT_CANCEL)
        self.bt_cancel_new_images.set_padding(Button.PADDING_S)
        self.layout.addWidget(self.bt_cancel_new_images)
        self.bt_cancel_new_images.clicked.connect(self.__cancel_new_images)

        self.bt_cancel_new_images.hide()


    def set_nb_images(self, nb_images):
        self.nb_images = nb_images
        self.lb_nb_images.setText(self.nb_images, parenthesis=True)
        self.__cancel_new_images()

    @Slot()
    def __cancel_new_images(self):
        self.img_path_name = set()
        self.__update_nb_new_images()

    def __update_nb_new_images(self):
        if len(self.img_path_name) > 0:
            self.lb_nb_new_images.setText(len(self.img_path_name), before="+")
            self.bt_cancel_new_images.show()
        else:
            self.lb_nb_new_images.setText("")
            self.bt_cancel_new_images.hide()

    def mousePressEvent(self, arg):
        self.loadFiles()

    def loadFiles(self):
        img_path_name, _ = QFileDialog.getOpenFileNames(self, 'Open ' + util.file_name_to_title(self.id) ,
             'D:\\Documents\\Internship Documents\\Image data\\2AO\\images',"Image files (*.png *.jpg *.jpeg *.gif *.tif *.tiff *.raw *. *.svg *.bmp *.)")

        self.img_path_name.update([Image(src, self.id) for src in img_path_name])
        self.__update_nb_new_images()

    def get_image_path_names(self):
        return self.img_path_name
