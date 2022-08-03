from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout,QHBoxLayout

from .button import Button
from .image_type import ImageType
from .image_type_creator import ImageTypeCreator
from .ai_preview import AIPreview

from .pagination import Pagination

import src.util.data_cleaner as data_cleaner
import src.util.util as util

class AIPreviewsContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, ai_infos, ai_launch_receaver):
        QFrame.__init__(self, parent)

        self.ai_infos = ai_infos
        self.ai_previews = {}
        self.ai_launch_receaver =ai_launch_receaver
        self.__create()

    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 10, 10)
        self.__create_ai_previews()

    def __create_ai_previews(self):

        self.c_pagination = Pagination(self, (1,1), (1,3), forced_empty_spaces = True)

        self.layout.addWidget(self.c_pagination)
        ls = []
        for ai_name, ai_content in self.ai_infos.items():
            ai_preview = AIPreview(self, ai_name, ai_content['description'], ai_content['results'], self.ai_launch_receaver)

#            self.layout.addWidget(ai_preview)
            self.ai_previews[ai_name] = ai_preview
            ls.append(ai_preview)
        self.c_pagination.add_cards(ls)


