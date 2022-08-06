from .view_object import *
from .ui.ui_upsert_skin_lesion import Ui_upsert_skin_lesion


from .ui.promoted.variable_inputs_container import VariableInputsContainer
from .ui.promoted.variable_input import VariableInput

from .ui.promoted.add_skl_img_container import AddSklImgContainer

from .ui.promoted.ai_previews_container import AIPreviewsContainer
from .ui.promoted.button import Button

from src.objects.skin_lesion import SkinLesion

class UpsertSkinLesionView(ViewObject):
    def __init__(self, mw, ai_dict, patient, skin_lesion):
        super().__init__(mw)

        self.ai_dict = ai_dict

        self.p = patient
        self.skl = skin_lesion

        self.load_ui()
        self.connect_ui_signals()

        if self.skl is not None:
            self.charge_edit_mode()

        self.charge_ai_previews()

    def load_ui(self):
        self.ui = Ui_upsert_skin_lesion()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_complete.set_position(2)

        # characteristic
        self.c_characteristics = VariableInputsContainer(cfg.FILES_SKIN_LESION_CHARACTERISTICS_PATH,
            "Create new characteristic",
            VariableInput.DISPOSITION_H)
        self.ui.ly_characteristics_content.addWidget(self.c_characteristics)

        # skin lesion images
        self.c_add_skl_img = AddSklImgContainer(self.ui.c_images_content, cfg.FILES_SKIN_LESION_IMAGES_PATH)
        self.ui.ly_add_skl_img.addWidget(self.c_add_skl_img)


    def charge_ai_previews(self):
        ai_infos = {}
        for ai_name, ai in self.ai_dict.items():
            # description
            ai_infos[ai_name] = {"description": ai.description, "results":{}}

            # results
            if self.skl is not None and ai_name in self.skl.ai_results:
                ai_infos[ai_name]["results"] = self.skl.ai_results[ai_name]

        self.c_ai_previews = AIPreviewsContainer(self.ui.c_ai_results, ai_infos, self.launch_ai)
        self.ui.ly_ai_results.addWidget(self.c_ai_previews)


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_complete.clicked.connect(self.__complete)
        self.ui.bt_back.clicked.connect(self.__back)

        self.ui.sc_characteristics.verticalScrollBar().rangeChanged.connect(self.__c_characteristics_scroll_down)
        self.ui.sc_images.verticalScrollBar().rangeChanged.connect(self.__c_images_scroll_down)


        # created signals
        self.s_change_view.connect(self.MW.change_view)

#    def __catch_information(self):

    def __save_information(self):
        if self.skl is None:
            self.skl = SkinLesion(len(self.p.skin_lesions), self.p.id, self.__catch_characteristics())
            self.skl.create_skin_lesion()
            self.p.skin_lesions.append(self.skl)

        else:
            self.skl.characteristics = self.__catch_characteristics()
            self.skl.update_data()

        self.skl.save_images(self.c_add_skl_img.get_selected_image_path_names())

        # when skin lesion updated without scaping from the view
#        self.charge_edit_mode()


    def __catch_characteristics(self):
        characteristics = {}
        for charac_name, charac_value in self.c_characteristics.get_selected_items().items():
            if ((charac_value[1] is None and charac_value[0] == "") or
                charac_value[1] == ""):
                    continue

            if charac_value[1] is None:
                charac_value = charac_value[0]
            characteristics[charac_name] = charac_value

        return characteristics
    @Slot()
    def __complete(self):
        self.__save_information()
        self.__back()
#        print(self.c_characteristics.get_selected_items())
#        print(self.c_add_skl_img.get_selected_image_path_names())

    @Slot()
    def __c_characteristics_scroll_down(self, min, maxi):
        self.ui.sc_characteristics.verticalScrollBar().setValue(maxi)

    @Slot()
    def __c_images_scroll_down(self, min, maxi):
        self.ui.sc_images.verticalScrollBar().setValue(maxi)

    @Slot()
    def __back(self):
        self.s_change_view.emit(cfg.UPSERT_SKIN_LESION_VIEW, cfg.CHECK_PATIENT_VIEW, {"patient_id":self.p.id})

    @Slot(str)
    def launch_ai(self, ai_name):
        self.__save_information()
        self.s_change_view.emit(cfg.UPSERT_SKIN_LESION_VIEW, cfg.AI_LAUNCHER_VIEW, {"ai":self.ai_dict[ai_name] , "patient":self.p, "skin_lesion":self.skl})


    def charge_edit_mode(self):
        self.ui.lb_title.setText("Edit skin lesion")

        # characteristics
        self.c_characteristics.select_default_values(self.skl.characteristics)

        # images
        self.c_add_skl_img.set_number_images(self.skl.get_skl_img_numbers())


