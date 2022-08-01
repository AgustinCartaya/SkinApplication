from .view_object import *
from .ui.ui_upsert_skin_lesion import Ui_upsert_skin_lesion


from .ui.promoted.variable_inputs_container import VariableInputsContainer
from .ui.promoted.variable_input import VariableInput

from .ui.promoted.images_type_container import ImagesTypeContainer

from .ui.promoted.ai_previews_container import AIPreviewsContainer
from .ui.promoted.button import Button

from src.objects.skin_lesion import SkinLesion

class UpsertSkinLesion(ViewObject):
    def __init__(self, mw, patient, skin_lesion_id):
        super().__init__(mw)

        self.p = patient
        self.skl_id = skin_lesion_id
        self.skl = None

        self.load_ui()
        self.connect_ui_signals()

        if self.skl_id >= 0:
            self.skl = self.p.skin_lesions[self.skl_id]
            self.charge_edit_mode()

    def load_ui(self):
        self.ui = Ui_upsert_skin_lesion()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_complete.set_position(2)

        # caracteristic
        self.c_caracteristics = VariableInputsContainer(cfg.FILES_SKIN_LESION_CARACTERISTICS_PATH,
            "Create new caracteristic",
            VariableInput.DISPOSITION_H)
        self.ui.ly_caracteristics_content.addWidget(self.c_caracteristics)

        # image type
        self.c_images_type = ImagesTypeContainer(cfg.FILES_IMAGES_TYPE_PATH)
        self.ui.ly_images_type_content.addWidget(self.c_images_type)

        # AI
        ai_tests = {'AI-1':{'description':'desc ai 1', 'results':{'r1':'cr1'}},
            'AI-2':{'description':'desc ai 2', 'results':{'r2':'cr2'}},
            'AI-3':{'description':'desc ai 3', 'results':{}}
            }
        self.c_ai_previews = AIPreviewsContainer(ai_tests)
        self.ui.ly_ai_results.addWidget(self.c_ai_previews)

    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_complete.clicked.connect(self.__complete)
        self.ui.bt_back.clicked.connect(self.__back)

        self.ui.sc_caracteristics.verticalScrollBar().rangeChanged.connect(self.__c_caracteristics_scroll_down)


        # created signals
        self.s_change_view.connect(self.MW.change_view)

#    def __catch_information(self):

    def __save_information(self):
        if self.skl_id < 0:
            self.skl_id = len(self.p.skin_lesions)
            self.skl = SkinLesion(self.skl_id, self.p.id, self.__catch_caracteristics())
            self.skl.create_skin_lesion()
#            self.skl.save_images(self.c_images_type.get_selected_image_path_names())
        else:
            self.skl.caracteristics = self.__catch_caracteristics()
            self.skl.update_data()
        self.skl.save_images(self.c_images_type.get_selected_image_path_names())

        # when skin lesion updated without scaping from the view
#        self.charge_edit_mode()


    def __catch_caracteristics(self):
        caracteristics = {}
        for carac_name, carac_value in self.c_caracteristics.get_selected_items().items():
            if ((carac_value[1] is None and carac_value[0] == "") or
                carac_value[1] == ""):
                    continue

            if carac_value[1] is None:
                carac_value = carac_value[0]
            caracteristics[carac_name] = carac_value

        return caracteristics
    @Slot()
    def __complete(self):
        self.__save_information()
        self.__back()
#        print(self.c_caracteristics.get_selected_items())
#        print(self.c_images_type.get_selected_image_path_names())

    @Slot()
    def __c_caracteristics_scroll_down(self, min, maxi):
        self.ui.sc_caracteristics.verticalScrollBar().setValue(maxi)

    @Slot()
    def __back(self):
        self.s_change_view.emit(cfg.UPSERT_SKIN_LESION_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id":self.p.id})


    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit skin lesion")

        # caracteristics
        self.c_caracteristics.select_default_values(self.skl.caracteristics)

        # images
        self.c_images_type.set_number_images(self.skl.get_number_images_type())


