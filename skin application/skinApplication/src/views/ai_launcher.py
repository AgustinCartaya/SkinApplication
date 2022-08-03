from .view_object import *
from .ui.ui_ai_launcher import Ui_ai_launcher

class AILauncherView(ViewObject):
    def __init__(self, mv, patient, skin_lesion, ai_name):
        super().__init__(mv)

        self.p = patient
        self.skl = skin_lesion
#        self.p = patient


        self.load_ui()

    def load_ui(self):
        self.ui = Ui_ai_launcher()
        self.ui.setupUi(self)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):


        # created signals
        self.s_change_view.connect(self.MW.change_view)
