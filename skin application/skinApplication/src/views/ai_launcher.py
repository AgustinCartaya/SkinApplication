from .view_object import *
from .ui.ui_ai_launcher import Ui_ai_launcher

from .ui.promoted.required_elements_container import  RequiredElementsContainer
from .ui.promoted.required_images_type_container import  RequiredImagesTypeContainer

from src.objects.ai import AI

class AILauncherView(ViewObject):
    def __init__(self, mv, ai, patient, skin_lesion):
        super().__init__(mv)

        self.ai = ai
        self.ai.set_actual_patient_and_skin_lesion(patient, skin_lesion)
        self.p = patient
        self.skl = skin_lesion

        self.load_ui()
        self.connect_ui_signals()





    def load_ui(self):
        self.ui = Ui_ai_launcher()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_learn_more.set_position(2)

        # required info
        self.ui.c_skl_required_info_list.set_required_elements(self.ai.actual_skl_charac)
        self.ui.c_patient_required_info_list.set_required_elements(self.ai.actual_mi)
        self.ui.c_images_required_list.create_required_images_type(self.ai.req_images)
        self.__carge_selected_images()


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def __carge_selected_images(self):
        for img_name, img_list in self.ai.actual_images.items():
            self.ui.c_images_required_list.set_selected_number(img_name, len(img_list))


    @Slot()
    def __back(self):
        self.ai.reset_actual_patient_and_skin_lesion()
        self.s_change_view.emit(cfg.AI_LAUNCHER_VIEW, cfg.UPSERT_SKIN_LESION_VIEW, {"patient" : self.p, "skin_lesion": self.skl})

