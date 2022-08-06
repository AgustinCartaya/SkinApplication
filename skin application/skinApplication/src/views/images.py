from .view_object import *
from .ui.ui_images import Ui_images

from .ui.promoted.skl_img_card import  SklImgCard
from src.objects.image import Image
from PySide6.QtCore import QTimer
from src.objects.ai import AI

class ImagesView(ViewObject):
    def __init__(self, mv, patient, skin_lesion):
        super().__init__(mv)

        self.p = patient
        self.skl = skin_lesion
        self.imgs = self.skl.get_all_skl_imgs()

        self.load_ui()
        self.connect_ui_signals()

        self.__show_images()

    def load_ui(self):
        self.ui = Ui_images()
        self.ui.setupUi(self)

        # filters
        self.ui.c_filter_skl_imgs.create_filters([["medical_image",1], ["dermatoscopy",5], ["microscopy",15]])

        # pagination
        self.ui.c_pagination.set_grid_cards_size(5,5)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def __show_images(self):

        self.images_cards = []
        for img_name, imgs in self.imgs.items():
            for img in imgs:
                card = SklImgCard(self.ui.c_pagination, img, self.open_image)
                self.ui.c_pagination.add_card_size_changed_receaver(card.show_image)
                self.images_cards.append(card)
        self.ui.c_pagination.add_cards(self.images_cards)

#        QTimer.singleShot(500, self.__load_images)

#    def __load_images(self):
#        for img_card in self.images_cards:
#            img_card.show_image()

    Slot(Image)
    def open_image(self, img):
        pass

    @Slot()
    def __back(self):
        self.s_change_view.emit(cfg.IMAGES_VIEW, cfg.ANCIENT_VIEW, {})

