from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QGridLayout)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QSize
from .label import Label

from src.objects.image import Image
from PySide6.QtCore import Signal, Slot


class SklImgCard(QFrame):

    s_clicked = Signal(Image, bool)
    def __init__(self, parent, image, click_receaver):
        QFrame.__init__(self, None)

        self.img = image
        self.click_receaver = click_receaver

        if self.click_receaver is not None:
            self.s_clicked.connect(self.click_receaver)

        self.__create()

        self.setProperty("selected", False)

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_image_container()

    def __create_image_container(self):
        self.lb_image = Label()
#        self.lb_image.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.pxm_image = QPixmap(self.img.src)
        self.layout.addWidget(self.lb_image, 0, Qt.AlignHCenter|Qt.AlignVCenter)

    def mousePressEvent(self, arg):
        self.s_open_image.emit(self.img)

    def __show_image(self):
#        print(self.size())

#        self.lb_image.setScaledContents(True)
#        self.lb_image.setPixmap(QPixmap(self.img.src))

        myScaledPixmap = self.pxm_image.scaled(self.size(), Qt.KeepAspectRatio)
#        print(myPixmap.size())
#        print(myScaledPixmap.size())
        self.lb_image.setPixmap(myScaledPixmap)

    Slot(int, int)
    def size_changed(self, w, h):
        self.setMinimumSize(QSize(w,h))
        self.setMaximumSize(QSize(w,h))

        self.__show_image()

    def mousePressEvent(self, arg):
        if self.click_receaver is not None:
            self.set_selected(not self.property("selected"))
            self.s_clicked.emit(self.img, self.property("selected"))

    def repaint(self):
        self.setStyle(QApplication.style())

    def set_selected(self, selected):
        self.setProperty("selected", selected)
        self.repaint()


