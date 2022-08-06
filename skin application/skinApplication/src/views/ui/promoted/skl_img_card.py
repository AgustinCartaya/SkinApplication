from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QGridLayout)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .label import Label

from src.objects.image import Image
from PySide6.QtCore import Signal


class SklImgCard(QFrame):

    s_open_image = Signal(str)
    def __init__(self, parent, image, receaver):
        QFrame.__init__(self, None)

        self.img = image
        self.s_open_image.connect(receaver)

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_image_container()

    def __create_image_container(self):
        self.lb_image = Label()
        self.pxm_image = QPixmap(self.img.src)
        self.layout.addWidget(self.lb_image,0, Qt.AlignHCenter)

    def mousePressEvent(self, arg):
        self.s_open_image.emit(self.img)

    def show_image(self):
#        print(self.size())

#        self.lb_image.setScaledContents(True)
#        self.lb_image.setPixmap(QPixmap(self.img.src))

        myScaledPixmap = self.pxm_image.scaled(self.size(), Qt.KeepAspectRatio)
#        print(myPixmap.size())
#        print(myScaledPixmap.size())
        self.lb_image.setPixmap(myScaledPixmap)
