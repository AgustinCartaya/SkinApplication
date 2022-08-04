from .view_object import *
from .ui.ui_images import Ui_images

from .ui.promoted.required_elements_container import  RequiredElementsContainer
from .ui.promoted.required_images_type_container import  RequiredImagesTypeContainer

from src.objects.ai import AI

class ImagesView(ViewObject):
    def __init__(self, mv):
        super().__init__(mv)

        self.load_ui()
        self.connect_ui_signals()

    def load_ui(self):
        self.ui = Ui_images()
        self.ui.setupUi(self)

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    @Slot()
    def __back(self):
        self.s_change_view.emit(cfg.IMAGES_VIEW, cfg.ANCIENT_VIEW, {})

