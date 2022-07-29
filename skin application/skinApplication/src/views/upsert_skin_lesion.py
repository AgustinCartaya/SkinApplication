from .view_object import *
from .ui.ui_upsert_skin_lesion import Ui_upsert_skin_lesion


class UpsertSkinLesion(ViewObject):
    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()

    def load_ui(self):
        self.ui = Ui_upsert_skin_lesion()
        self.ui.setupUi(self)

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        pass
