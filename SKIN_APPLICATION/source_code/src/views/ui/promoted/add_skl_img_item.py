from .promoted_container import *

from PySide6.QtWidgets import QFileDialog

import src.util.util as util
import src.util.skl_imgs as skl_imgs

from src.objects.image import Image


class AddSklImgItem(PromotedContainer):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.id = ""
        self.nb_images = 0
        self.new_images = 0
        self.img_path_name = set()

        self._pre_charge()

    def initialize(self, id, nb_images = 0, new_images = []):
        self.id = id
        self.nb_images = nb_images
        self.new_images = new_images

        self.__create_content()

    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def __create_content(self):
        # title
        self.lb_name = Label(self)
        self.lb_name.setText(tf.f(self.id, translate=False, format=True))
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
        self.bt_cancel_new_images.setText(tf.f("-"))
        self.bt_cancel_new_images.setMaximumSize(QSize(22, 22))
        self.bt_cancel_new_images.set_type(Button.BT_CANCEL)
        self.bt_cancel_new_images.set_padding(Button.PADDING_S)
        self.layout.addWidget(self.bt_cancel_new_images)
        self.bt_cancel_new_images.clicked.connect(self.__cancel_new_images)

        self.bt_cancel_new_images.hide()

    def __update_nb_new_images(self):
        if len(self.img_path_name) > 0:
            self.lb_nb_new_images.setText(tf.f(len(self.img_path_name), before="+"))
            self.bt_cancel_new_images.show()
        else:
            self.lb_nb_new_images.setText(tf.f(""))
            self.bt_cancel_new_images.hide()

    def __loadFiles(self):
        img_path_name, _ = QFileDialog.getOpenFileNames(self, tf.f('Open ') + util.file_name_to_title(self.id),
             '',"Image files (" + skl_imgs.get_accept_img_extensions_str() +")")

        self.img_path_name.update([Image(src, self.id) for src in img_path_name])
        self.__update_nb_new_images()

    @Slot()
    def __cancel_new_images(self):
        self.img_path_name = set()
        self.__update_nb_new_images()

    def set_nb_images(self, nb_images):
        self.nb_images = nb_images
        self.lb_nb_images.setText(tf.f(self.nb_images, parenthesis=True))
        self.__cancel_new_images()

    def get_image_path_names(self):
        return self.img_path_name

    def mousePressEvent(self, arg):
        self.__loadFiles()
