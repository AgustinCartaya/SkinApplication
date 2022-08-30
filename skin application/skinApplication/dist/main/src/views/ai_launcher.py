from .view_object import *
from .ui.ui_ai_launcher import Ui_ai_launcher

from src.objects.ai import AI
from src.objects.image_list import ImageList
from src.objects.variable_input import VariableInput

class AILauncherView(ViewObject):
    def __init__(self, mv, ai, patient, skin_lesion):
        super().__init__(mv)

        self.ai = ai
        self.ai.set_actual_patient_and_skin_lesion(patient, skin_lesion)
        self.p = patient
        self.skl = skin_lesion

        self.load_ui()
        self.connect_ui_signals()
        self.__activate_bt_launch()

    def load_ui(self):
        self.ui = Ui_ai_launcher()
        self.ui.setupUi(self)

        # labels
        self.ui.lb_title.set_title(1)
        self.ui.lb_required_images.set_title(2)
        self.ui.lb_required_information.set_title(2)

        self.ui.lb_patient_required_info.set_title(3)
        self.ui.lb_skl_required_info.set_title(3)

        self.ui.lb_image_name.set_bold(True)
        self.ui.lb_max_images.set_bold(True)
        self.ui.lb_min_images.set_bold(True)
        self.ui.lb_selected_images.set_bold(True)

        # navigator
        self.ui.bt_learn_more.set_position(2)

        # required info
        self.ui.c_patient_required_info_list.initialize(self.ai.actual_mi, VariableInput.MI_INPUT)
        self.ui.c_skl_required_info_list.initialize(self.ai.actual_skl_charac, VariableInput.SKL_INPUT)
        self.ui.c_required_skl_imgs.initialize(self.ai.req_images, self.edit_selected_images)
        self.__carge_selected_images()


    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)
        self.ui.bt_launch.clicked.connect(self.__launch)

    def __carge_selected_images(self):
        for img_name, img_list in self.ai.actual_images.imgs_dict.items():
            self.ui.c_required_skl_imgs.set_selected_number(img_name, len(img_list))

    @Slot()
    def __back(self):
        self.ai.reset_actual_patient_and_skin_lesion()
        self.s_change_view.emit(cfg.AI_LAUNCHER_VIEW, cfg.UPSERT_SKIN_LESION_VIEW, {"patient" : self.p, "skin_lesion": self.skl})

    @Slot(str)
    def edit_selected_images(self, image_type):
        images_to_show = ImageList()
        images_to_show.append_images(image_type, self.skl.get_skl_imgs(image_type))
        selected_images = self.ai.actual_images.imgs_dict[image_type]
        self.s_change_view.emit(cfg.AI_LAUNCHER_VIEW, cfg.IMAGES_VIEW, {"images":images_to_show, "patient" : self.p, "skin_lesion": self.skl, 'collet_mode':True, 'selected_images':selected_images})

    def set_selected_images(self, name, imgs):
        self.ai.actual_images.imgs_dict[name] = imgs
        self.ui.c_required_skl_imgs.set_selected_number(name, len(imgs))
        self.__activate_bt_launch()


    def __activate_bt_launch(self):
        if self.ai.is_ready_to_launch():
            self.ui.bt_launch.setEnabled(True)
            self.ui.lb_error.hide()
        else:
            self.ui.bt_launch.setEnabled(False)
            self.ui.lb_error.show()

    def __launch(self):
        results = self.ai.launch()
        if results:
            self.s_change_view.emit(cfg.AI_LAUNCHER_VIEW, cfg.AI_RESULTS_VIEW, {"results":results, "ai":self.ai,  "patient" : self.p, "skin_lesion": self.skl})



