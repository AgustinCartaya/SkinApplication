from .view_object import *
from PySide6.QtGui import QPixmap
from .ui.ui_image_viewer import Ui_image_viewer

from src.objects.image import Image

class ImageViewer(ViewObject):
    def __init__(self, image):
        super().__init__(None)
        self.img = image

        self.load_ui()
        self.connect_ui_signals()

        self.__show_image()

    def load_ui(self):
        self.ui = Ui_image_viewer()
        self.ui.setupUi(self)

    def __show_image(self):
        self.ui.lb_image.setPixmap(QPixmap(self.img.src))

#    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        pass

