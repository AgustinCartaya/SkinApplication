from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
QSpacerItem, QVBoxLayout, QWidget)

from PySide6.QtCore import Signal, Slot

from .button import Button
from .skin_lesion_preview_info import SkinLesionPreviewInfo

from .line_edit import LineEdit

import src.util.data_cleaner as data_cleaner

from src.objects.skin_lesion import SkinLesion

class SkinLesionPreview(QFrame):

    s_update = Signal(int)
    s_see_timeline = Signal(int)
    s_see_images = Signal(int)
    def __init__(self,
        parent,
        skin_lesion,
        update_receaver,
        see_timeline_receaver,
        see_images_receaver):
        QFrame.__init__(self, parent)

        self.skl = skin_lesion

        self.s_update.connect(update_receaver)
        self.s_see_timeline.connect(see_timeline_receaver)
        self.s_see_images.connect(see_images_receaver)
        self.__create()


    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_c_n1()
        self.__create_c_n2()
        self.__create_c_n3()

        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 6)
        self.layout.setStretch(2, 1)

    def __create_c_n1(self):
        # c_n1 frame
        self.c_n1 = QFrame(self)

        self.c_n1_layout = QVBoxLayout(self.c_n1)
        self.c_n1_layout.setContentsMargins(0, 0, 0, 0)



        # image
        self.c_image = QFrame(self.c_n1)

        self.c_image_layout = QHBoxLayout(self.c_image)
        self.c_image_layout.setContentsMargins(0, 0, 0, 0)

        self.lb_image = QLabel(self.c_image)
        self.lb_image.setMinimumSize(QSize(150, 0))
        self.lb_image.setAlignment(Qt.AlignCenter)
#        self.lb_image.setScaledContents(True)
#        self.lb_image.setStyleSheet("background-color: yellow;")

        self.c_image_layout.addWidget(self.lb_image)
        self.c_n1_layout.addWidget(self.c_image)

        # spacer
        self.vs_image = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.c_n1_layout.addItem(self.vs_image)

        self.layout.addWidget(self.c_n1)


    def __create_c_n2(self):
        # c_n2 frame
        self.c_n2 = QFrame(self)

        self.c_n2_layout = QVBoxLayout(self.c_n2)
        self.c_n2_layout.setContentsMargins(0, 0, 0, 0)
        self.c_n2_layout.setSpacing(20)

        # up
        self.c_n2_up = QFrame(self)

        self.c_n2_up_layout = QHBoxLayout(self.c_n2_up)
        self.c_n2_up_layout.setSpacing(12)
        self.c_n2_up_layout.setContentsMargins(0, 0, 0, 0)

        # Anotations
        annotations = SkinLesionPreviewInfo(self.c_n2)
        ai_results = SkinLesionPreviewInfo(self.c_n2)

        annotations.show_info(self.skl.characteristics, "characteristics")
        ai_results.show_info(self.skl.ai_results, "AI results", True)

        self.c_n2_up_layout.addWidget(annotations)
        self.c_n2_up_layout.addWidget(ai_results)


        self.c_n2_layout.addWidget(self.c_n2_up)


        # update button
        self.bt_update = Button(self.c_n2)
        self.bt_update.setText("Update")
        self.bt_update.setMinimumSize(QSize(300, 16777215))
        self.bt_update.setMaximumSize(QSize(300, 16777215))
        self.c_n2_layout.addWidget(self.bt_update,0, Qt.AlignHCenter)

        self.bt_update.clicked.connect(self.__update)


        self.layout.addWidget(self.c_n2)


    def __create_c_n3(self):
        self.c_n3 = QFrame(self)

        self.c_n3_layout = QVBoxLayout(self.c_n3)
        self.c_n3_layout.setContentsMargins(0, 0, 0, 0)

        self.c_buttons = QFrame(self.c_n3)

        self.c_buttons_layout = QVBoxLayout(self.c_buttons)
        self.c_buttons_layout.setContentsMargins(0, 0, 0, 0)

        # bt see time line
        self.bt_see_timeline = Button(self.c_buttons)
        self.bt_see_timeline.setText("Time line")
        self.bt_see_timeline.setMinimumSize(QSize(100, 0))
        self.bt_see_timeline.setMaximumSize(QSize(100, 16777215))
        self.c_buttons_layout.addWidget(self.bt_see_timeline)
        self.bt_see_timeline.clicked.connect(self.__see_timeline)

        # bt see imgaes
        self.bt_see_images = Button(self.c_buttons)
        self.bt_see_images.setText("Images")
        self.bt_see_images.setMinimumSize(QSize(100, 0))
        self.bt_see_images.setMaximumSize(QSize(100, 16777215))
        self.c_buttons_layout.addWidget(self.bt_see_images)
        self.bt_see_images.clicked.connect(self.__see_images)

        # bt more
        self.bt_more_options = Button(self.c_buttons)
        self.bt_more_options.setText("More")
        self.bt_more_options.setMinimumSize(QSize(100, 0))
        self.bt_more_options.setMaximumSize(QSize(100, 16777215))

        self.c_buttons_layout.addWidget(self.bt_more_options)


        self.c_n3_layout.addWidget(self.c_buttons)

        # spacer
        self.vs_buttons = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.c_n3_layout.addItem(self.vs_buttons)

        self.layout.addWidget(self.c_n3)

    def __update(self):
        self.s_update.emit(self.skl.number)

    def __see_timeline(self):
        self.s_see_timeline.emit(self.skl.number)

    def __see_images(self):
        self.s_see_images.emit(self.skl.number)

#    def set_image(self, img):
#        self.lb_image.setMinimumSize(QSize(150, 150))

#        resized_size = img.get_resized_size(150)
#        pxm_image = QPixmap(img.src).scaled(resized_size[0], resized_size[1], mode=Qt.SmoothTransformation)
#        self.lb_image.setPixmap(pxm_image)

    def set_image(self, img):
        self.pxm_image = QPixmap(img.src)
        self.lb_image.setPixmap(self.pxm_image)

#        resized_size = img.get_resized_size(150)
#        pxm_image = QPixmap(img.src).scaled(resized_size[0], resized_size[1], mode=Qt.SmoothTransformation)

    def __show_image(self):
        myScaledPixmap = self.pxm_image.scaled(self.lb_image.size().width(), self.lb_image.size().width(), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
        self.lb_image.setPixmap(myScaledPixmap)

    def resizeEvent(self, event):
        self.__show_image()
