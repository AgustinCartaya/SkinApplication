from .view_object import *
from .ui.ui_upsert_skin_lesion import Ui_upsert_skin_lesion


from .ui.promoted.variable_inputs_container import VariableInputsContainer
from .ui.promoted.variable_input import VariableInput

from .ui.promoted.images_type_container import ImagesTypeContainer

from .ui.promoted.ai_previews_container import AIPreviewsContainer
from .ui.promoted.button import Button

from src.objects.skin_lesion import SkinLesion

class UpsertSkinLesionView(ViewObject):
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

        self.charge_ai_previews()

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


    def charge_ai_previews(self):
        ai_dict = {}
        actual_language = "en"
        for ai_disponible in util.get_dir_list(cfg.AI_PATH):
            ai_info_folder_path = cfg.AI_PATH + cfg._S + ai_disponible + cfg._S + cfg.AI_INFO_FOLDER_NAME
            if util.is_dir(ai_info_folder_path):

                # description
                ai_description = util.read_file(ai_info_folder_path + cfg._S + cfg.AI_DESCRIPTION_FILE_NAME + "." + actual_language)
                ai_dict[ai_disponible] = {'description': ai_description, 'results':{}}

                # results
                if self.skl is not None and ai_disponible in self.skl.ai_results:
                    ai_dict[ai_disponible]['results'] = self.skl.ai_results[ai_disponible]

        self.c_ai_previews = AIPreviewsContainer(self.ui.c_ai_results, ai_dict, self.launch_ai)
        self.ui.ly_ai_results.addWidget(self.c_ai_previews)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_complete.clicked.connect(self.__complete)
        self.ui.bt_back.clicked.connect(self.__back)

        self.ui.sc_caracteristics.verticalScrollBar().rangeChanged.connect(self.__c_caracteristics_scroll_down)
        self.ui.sc_images.verticalScrollBar().rangeChanged.connect(self.__c_images_scroll_down)


        # created signals
        self.s_change_view.connect(self.MW.change_view)

#    def __catch_information(self):

    def __save_information(self):
        if self.skl_id < 0:
            self.skl_id = len(self.p.skin_lesions)
            self.skl = SkinLesion(self.skl_id, self.p.id, self.__catch_caracteristics())
            self.skl.create_skin_lesion()
            self.p.skin_lesions.apped(self.skl)

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
    def __c_images_scroll_down(self, min, maxi):
        self.ui.sc_images.verticalScrollBar().setValue(maxi)

    @Slot()
    def __back(self):
        self.s_change_view.emit(cfg.UPSERT_SKIN_LESION_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id":self.p.id})

    @Slot(str)
    def launch_ai(self, ai_name):
        print("launch: " + ai_name)
        self.s_change_view.emit(cfg.UPSERT_SKIN_LESION_VIEW, cfg.AI_LAUNCHER_VIEW, {"patient":self.p, "skin_lesion":self.skl, "ai_name":ai_name })


    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit skin lesion")

        # caracteristics
        self.c_caracteristics.select_default_values(self.skl.caracteristics)

        # images
        self.c_images_type.set_number_images(self.skl.get_number_images_type())


