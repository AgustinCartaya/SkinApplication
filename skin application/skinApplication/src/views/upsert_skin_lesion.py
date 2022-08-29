from .view_object import *
from .ui.ui_upsert_skin_lesion import Ui_upsert_skin_lesion


from .ui.promoted.variable_inputs_container import VariableInputsContainer
from .ui.promoted.variable_input_creator import VariableInputCreator
from .ui.promoted.variable_input_item import VariableInputItem


from .ui.promoted.add_skl_img_container import AddSklImgContainer
from .ui.promoted.add_skl_img_creator import AddSklImgCreator


from .ui.promoted.ai_previews_container import AIPreviewsContainer
from .ui.promoted.button import Button


from src.objects.skin_lesion import SkinLesion
from src.objects.timeline_point import TimelinePoint
from src.objects.image import Image
from src.objects.variable_input import VariableInput


import src.util.skl_imgs as skl_imgs



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
        else:
            self.charge_body2d()

        self.skl_img_creator = None
        self.variable_input_creator = None
        self.charge_ai_previews()

    def charge_body2d(self, skl_location=[]):
        body2d_images = [Image(cfg.IMG_BODY2D_FRONT_PATH_NAME, cfg.IMG_TYPE_BODY2D),
                        Image(cfg.IMG_BODY2D_RIGHT_PATH_NAME, cfg.IMG_TYPE_BODY2D),
                        Image(cfg.IMG_BODY2D_BACK_PATH_NAME, cfg.IMG_TYPE_BODY2D),
                        Image(cfg.IMG_BODY2D_LEFT_PATH_NAME, cfg.IMG_TYPE_BODY2D)]
        if len(skl_location) > 0:
            self.ui.c_body2d.set_images(body2d_images, skl_location[0], skl_location[1], skl_location[2])
        else:
            self.ui.c_body2d.set_images(body2d_images)

    def load_ui(self):
        self.ui = Ui_upsert_skin_lesion()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_complete.set_position(2)

        # characteristic
        self.ui.c_characteristics.initialize(VariableInput.SKL_INPUT, self.show_variable_input_editor, VariableInputItem.DISPOSITION_H)


    def charge_ai_previews(self):
        ai_infos = {}
        for ai_name, ai in self.ai_dict.items():
            # description
            ai_infos[ai_name] = {"description": ai.description, "results":{}}

            # results
            if self.skl is not None and ai_name in self.skl.ai_results:
                ai_infos[ai_name]["results"] = self.skl.ai_results[ai_name]

        self.ui.c_ai_previews.initialize(ai_infos, self.launch_ai)

    def connect_ui_signals(self):
        self.ui.bt_complete.clicked.connect(self.__complete)
        self.ui.bt_back.clicked.connect(self.__back)
        self.ui.bt_see_images.clicked.connect(self.__see_images)

        # add new image type
        self.ui.bt_add_new_skl_image_type.clicked.connect(self.__show_skl_img_creator)
        self.ui.bt_add_new_skl_charac.clicked.connect(self.__show_variable_input_creator)

    def __save_information(self):
        if self.skl is None:
            self.skl = SkinLesion(len(self.p.skin_lesions), self.p.id, self.ui.c_body2d.get_point_info(), self.__catch_characteristics())
            self.skl.create_skin_lesion()
            self.p.skin_lesions.append(self.skl)

        else:
            self.skl.characteristics = self.__catch_characteristics()
            self.skl.location = self.ui.c_body2d.get_point_info()
            self.skl.update_data()

        selected_images = self.ui.c_add_skl_img.get_selected_images()
        saved_images = self.skl.save_images(selected_images)

        TimelinePoint.upsert_point(self.skl, saved_images)

        # when skin lesion updated without scaping from the view
        self.charge_edit_mode()


    def __catch_characteristics(self):
        characteristics = {}
        for charac_name, charac_value in self.ui.c_characteristics.get_selected_items().items():
            if charac_value is None:
                    continue
            characteristics[charac_name] = charac_value
        return characteristics

    @Slot()
    def __complete(self):
        self.__save_information()
        self.__back()

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
        self.ui.c_characteristics.select_default_values(self.skl.characteristics)

        # images
        self.ui.c_add_skl_img.set_number_images(self.skl.get_skl_img_numbers())
        self.ui.bt_see_images.setEnabled(True)

        # body 2d
        self.charge_body2d(self.skl.location)



    def __see_images(self):
        self.__save_information()
        self.s_change_view.emit(cfg.UPSERT_SKIN_LESION_VIEW, cfg.IMAGES_VIEW, {"images":self.skl.get_all_skl_imgs(), "patient" : self.p, "skin_lesion": self.skl, 'collet_mode':False})


    def refresh(self):
        self.ui.c_add_skl_img.set_number_images(self.skl.get_skl_img_numbers())

    # Add new variable input (skl characteristics)
    @Slot()
    def __show_variable_input_creator(self):
        self.variable_input_creator = VariableInputCreator(self.mv, VariableInput.SKL_INPUT, self.create_new_variable_input)
        self.variable_input_creator.show()

    Slot(VariableInput)
    def create_new_variable_input(self, variable_input):
        try:
            variable_input.create()
            self.ui.c_characteristics.append_new_variable_input(variable_input)
        except ValueError as err:
            print(err.args)

    # edit variable input (skl characteristics)
    Slot(VariableInput)
    def show_variable_input_editor(self, variable_input):
        self.variable_input_creator = VariableInputCreator(self.mv, VariableInput.SKL_INPUT, self.edit_variable_input)
        self.variable_input_creator.activate_edit_mode(variable_input, self.delete_variable_input)
        self.variable_input_creator.show()

    Slot(VariableInput)
    def edit_variable_input(self, variable_input):
        try:
            variable_input.update()
            self.ui.c_characteristics.variable_input_edited(variable_input)
        except ValueError as err:
            print(err.args)

    Slot(VariableInput)
    def delete_variable_input(self, variable_input):
        try:
            variable_input.delete()
            self.ui.c_characteristics.variable_input_deleted(variable_input)
        except ValueError as err:
            print(err.args)

    # Add new skl image type
    @Slot()
    def __show_skl_img_creator(self):
        self.skl_img_creator = AddSklImgCreator(self.mv, self.new_skl_img_created)
        self.skl_img_creator.show()

    Slot(str)
    def new_skl_img_created(self, skl_img_name):
        self.ui.c_add_skl_img.append_new_skl_img(skl_img_name)

    def close(self):
        self.skl_img_creator = None
        self.variable_input_creator = None
