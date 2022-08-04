from .view_object import *
from .ui.ui_ai_launcher import Ui_ai_launcher

from .ui.promoted.required_elements_container import  RequiredElementsContainer
from .ui.promoted.required_images_type_container import  RequiredImagesTypeContainer

from src.objects.ai import AI

class AILauncherView(ViewObject):
    def __init__(self, mv, ai, patient, skin_lesion):
        super().__init__(mv)

        self.ai = ai
        self.p = patient
        self.skl = skin_lesion

        self.load_ui()
        self.connect_ui_signals()

        self.__charge_required_info()
        self.__carge_required_images()



    def load_ui(self):
        self.ui = Ui_ai_launcher()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_learn_more.set_position(2)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)

        # created signals
        self.s_change_view.connect(self.MW.change_view)


    def __charge_required_info(self):
        self.__charge_skl_required_info()
        self.__charge_patient_required_info()

    def __charge_skl_required_info(self):
        req_skl_charac = []
        for req in self.ai.req_skl_charac:
            if req in self.skl.characteristics:
                req_skl_charac.append([req, self.skl.characteristics[req]])
            else:
                req_skl_charac.append([req, None])
        self.ui.c_skl_required_info_list.set_required_elements(req_skl_charac)


    def __charge_patient_required_info(self):
        req_mi = []
        for req in self.ai.req_mi:
            if req in self.p.mi:
                req_mi.append([req, self.p.mi[req]])
            else:
                req_mi.append([req, None])
        self.ui.c_patient_required_info_list.set_required_elements(req_mi)


    def __carge_required_images(self):
        self.ui.c_images_required_list.set_required_images_type(self.ai.req_images)


    @Slot()
    def __back(self):
        self.s_change_view.emit(cfg.AI_LAUNCHER_VIEW, cfg.UPSERT_SKIN_LESION_VIEW, {"patient" : self.p, "skin_lesion_nb": self.skl.number})

