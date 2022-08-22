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
    s_double_click = Signal(Image)
    def __init__(self, parent, image, click_receaver=None, double_click_receaver=None):
        QFrame.__init__(self, None)

        self.img = image
        self.click_receaver = click_receaver
        self.double_click_receaver = double_click_receaver

        if self.click_receaver is not None:
            self.s_clicked.connect(self.click_receaver)

        if self.double_click_receaver is not None:
            self.s_double_click.connect(self.double_click_receaver)

        self.__create()

        self.setProperty("selected", False)

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_image_container()

    def __create_image_container(self):
        self.lb_image = Label()
        self.pxm_image = QPixmap(self.img.src)
        self.layout.addWidget(self.lb_image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


    def __show_image(self):
        myScaledPixmap = self.pxm_image.scaled(self.size(), Qt.KeepAspectRatio)
        self.lb_image.setPixmap(myScaledPixmap)

    Slot(int, int)
    def size_changed(self, w, h):
        self.__show_image()

    def change_size(self, w, h):
        self.setMinimumSize(QSize(w, h))
        self.setMaximumSize(QSize(w, h))
        self.size_changed(w, h)

    def mousePressEvent(self, arg):
        if self.click_receaver is not None:
            self.set_selected(not self.property("selected"))
            self.s_clicked.emit(self.img, self.property("selected"))

    def mouseDoubleClickEvent(self, event):
        if self.double_click_receaver is not None:
            self.s_double_click.emit(self.img)

    def repaint(self):
        self.setStyle(QApplication.style())

    def set_selected(self, selected):
        self.setProperty("selected", selected)
        self.repaint()


