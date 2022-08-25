from .promoted_container import *

from .skl_img_card import SklImgCard

from PySide6.QtWidgets import QScrollArea, QWidget


class TimelineSklImgBlock(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)

        self._pre_charge()

    def initialize(self, img_type, imgs, image_clicked_receaver=None, double_click_receaver=None, img_width = 150):
        self.lb_title.setText(img_type, format=True, colon=True)
        max_height = 0
        for img in imgs:
            img_card = SklImgCard(self.c_images)
            img_card.initialize(img, image_clicked_receaver, double_click_receaver)
            self.ly_images.addWidget(img_card)

            h = img.get_resized_size(img_width, img_width)[1]
            img_card.change_size(img_width,h)

            if h > max_height:
                max_height = h

        self.setMinimumSize(QSize(16777215, max_height + 55))

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.__create_title()
        self.__create_scroll_area()
        self.__create_c_images()

    def __create_title(self):
        self.lb_title = Label(self)
        self.layout.addWidget(self.lb_title)

    def __create_scroll_area(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.c_scroll_area = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.c_scroll_area)

        self.ly_sc = QHBoxLayout(self.c_scroll_area)
        self.ly_sc.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.scroll_area)

    def __create_c_images(self):
        self.c_images = QFrame(self)
        self.ly_images = QHBoxLayout(self.c_images)

        self.ly_sc.addWidget(self.c_images)
        # spacer
        self.vs_description_down = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ly_sc.addItem(self.vs_description_down)







