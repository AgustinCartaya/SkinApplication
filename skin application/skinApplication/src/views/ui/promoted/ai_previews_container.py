from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout,QHBoxLayout

from .button import Button
from .image_type import ImageType
from .image_type_creator import ImageTypeCreator
from .ai_preview import AIPreview

import src.util.data_cleaner as data_cleaner
import src.util.util as util

class AIPreviewsContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, ai_infos, *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.ai_infos = ai_infos
        self.ai_previews = {}
        self.__create()

    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 10, 10)
        self.__create_ai_previews()

    def __create_ai_previews(self):
        for ai_name, ai_content in self.ai_infos.items():
            ai_preview = AIPreview(ai_name, ai_content['description'], ai_content['results'])
            self.layout.addWidget(ai_preview)
            self.ai_previews[ai_name] = ai_preview

