from .promoted_container import *

from .pagination import Pagination
from .ai_preview import AIPreview

class AIPreviewsContainer(PromotedContainer):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.ai_infos = None
        self.ai_launch_receaver = None
        self._pre_charge()

    def initialize(self, ai_infos, ai_launch_receaver):
        self.ai_infos = ai_infos
        self.ai_launch_receaver = ai_launch_receaver

        self.__create_ai_previews()

    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 10, 10)

        self.c_pagination = Pagination(self, (1,1), (1,3))
        self.layout.addWidget(self.c_pagination)

    def __create_ai_previews(self):
        if len(self.ai_infos) < 3:
            self.c_pagination.set_grid_cards_size(1,len(self.ai_infos))
        else:
            self.c_pagination.set_grid_cards_size(1,3)

        ai_cards = []
        for ai_name, ai_content in self.ai_infos.items():
            ai_preview = AIPreview(self.c_pagination)
            ai_preview.initialize(ai_name, ai_content['description'], ai_content['results'], self.ai_launch_receaver)
            ai_cards.append(ai_preview)
        self.c_pagination.add_cards(ai_cards)


