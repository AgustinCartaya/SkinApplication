from .view_object import *
from .ui.ui_images import Ui_images

from .ui.promoted.skl_img_card import  SklImgCard
from .ui.promoted.label import Label

from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame, QFileDialog

from src.objects.image import Image
from src.objects.image_list import ImageList

from src.objects.ai import AI

from .image_viewer import ImageViewer

class ImagesView(ViewObject):
    def __init__(self, mv, images, patient, skin_lesion, collet_mode, selected_images=[]):
        super().__init__(mv)

        self.img_list = images
        self.p = patient
        self.skl = skin_lesion
        self.collet_mode = collet_mode
        self.selected_imgs = selected_images


        self.img_list_filtered = ImageList()
        self.img_list_filtered.join(self.img_list)
        self.img_list_sorted = None


        # modify when window type stablished
#        self.img_list = self.skl.get_all_skl_imgs()
        self.bt_command_text = ""
        self.image_viewers = []

        self.load_ui()
        self.connect_ui_signals()



        # no images
        if len(images) == 0:
            self.ui.c_left.hide()
            self.ui.c_pagination.set_grid_cards_size(1,1)
            lb_no_images = Label()
            lb_no_images.setText("No images to show", center=True)
            self.ui.c_pagination.add_cards([lb_no_images])
        else:
            self.__show_images()
            self.__create_image_type_filter()

            if collet_mode:
                self.__collet_mode()



    def load_ui(self):
        self.ui = Ui_images()
        self.ui.setupUi(self)

        # navigator
        self.ui.bt_command.set_position(2)
        self.bt_command_text = self.ui.bt_command.text()

        # filters
        self.ui.c_filter_date.hide()

        # organizer
        self.ui.bt_sorter_name.select(True)
        self.ui.bt_sorter_asc.select(True)

        g1 = [self.ui.bt_sorter_name, self.ui.bt_sorter_date]
        g2 = [self.ui.bt_sorter_asc, self.ui.bt_sorter_dsc]

        self.ui.bt_sorter_name.add_group(g1)
        self.ui.bt_sorter_date.add_group(g1)
        self.ui.bt_sorter_asc.add_group(g2)
        self.ui.bt_sorter_dsc.add_group(g2)

#        self.ui.c_sorter_name.hide()
        self.ui.bt_sorter_date.setEnabled(False)

        # pagination
        self.ui.c_pagination.set_grid_cards_size(4,6)
#        self.ui.c_pagination.set_cards_sep(0,5)


    def __create_image_type_filter(self):
        image_type_list = []
        for img_name, imgs in self.img_list.imgs_dict.items():
            image_type_list.append([img_name, len(imgs)])
        self.ui.c_filter_image_type.create_filters(image_type_list, self.filter_img_type_slot)
        self.ui.c_filter_image_type.check_all()


    s_change_view = Signal(str,str,dict)
    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)
        if self.collet_mode:
            self.ui.bt_command.clicked.connect(self.__collet_images)
        else:
            self.ui.bt_command.clicked.connect(self.__view_images)

        # organizer
        self.ui.bt_sorter_name.clicked.connect(self.__show_images)
        self.ui.bt_sorter_asc.clicked.connect(self.__show_images)
        self.ui.bt_sorter_dsc.clicked.connect(self.__show_images)


        # created signals
        self.s_change_view.connect(self.MW.change_view)

    Slot()
    def filter_img_type_slot(self):
        self.__filter_images()

    Slot()
    def __view_images(self):
        self.close_image_viewers()
        for img in self.selected_imgs:
            self.image_viewers.append(ImageViewer(img))
            self.image_viewers[-1].show()

    def close_image_viewers(self):
        self.image_viewers = []

    Slot(Image, bool)
    def image_clicked(self, img, selected):
        if selected:
            self.selected_imgs.append(img)
            # show image description
            self.__show_image_description(img)
        else:
            self.selected_imgs.remove(img)
            self.__clean_image_descriptions()

        # show selected images number
        self.__refresh_command_bt_text()

    # You may put it in a separeted file call skl_img_description_container
    def __clean_image_descriptions(self):
        for i in reversed(range(self.ui.ly_description_content.count())):
           self.ui.ly_description_content.itemAt(i).widget().setParent(None)

    def __show_image_description(self, img):
        self.__clean_image_descriptions()
        for info_name, info_value in img.info_dict.items():
            c_single_img_info = QFrame(self.ui.c_description_content)
            ly_single_img_info = QHBoxLayout(c_single_img_info)
            ly_single_img_info.setContentsMargins(0, 0, 0, 0)
            ly_single_img_info.setSpacing(4)

            lb_info_name = Label(c_single_img_info)
            lb_info_name.setText(info_name, colon=True, format=True)
            ly_single_img_info.addWidget(lb_info_name)

            i_info_value = Label(c_single_img_info)
            if info_name == "type":
                i_info_value.setText(info_value, format=True)
            else:
                i_info_value.setText(info_value)
#            i_info_value.set_decoration("mi_content")
            ly_single_img_info.addWidget(i_info_value)


            # spacer
            hs = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
            ly_single_img_info.addItem(hs)

            self.ui.ly_description_content.addWidget(c_single_img_info)

    @Slot()
    def __back(self):
        self.close_image_viewers()
        self.s_change_view.emit(cfg.IMAGES_VIEW, cfg.ANCIENT_VIEW, {})

    def __show_images(self):
        self.__sort_images()
        self.__create_img_cards()

    def __filter_images(self):
        self.img_list_filtered = ImageList()
        self.img_list_filtered.join(self.img_list)
        # filter image type
        self.img_list_filtered = self.img_list_filtered.get_filtered_by_types(self.ui.c_filter_image_type.get_checked_list())

        self.__show_images()

    # from here img_list_sorted is a single list
    def __sort_images(self):
#        self.img_list_sorted = self.img_list_filtered
        if self.ui.bt_sorter_name.is_selected():
            sort_by = "name"
        else:
            sort_by = "ceartion_date"
        self.img_list_sorted = self.img_list_filtered.get_all_images(sort_by, self.ui.bt_sorter_dsc.is_selected())

    def __create_img_cards(self):
        self.images_cards = []
        selected_src = [img.src for img in self.selected_imgs]
        for img in self.img_list_sorted:
            card = SklImgCard(self.ui.c_pagination, img, self.image_clicked)
#            if img.src in self.__get_selected_src():
            if img.src in selected_src:
                card.set_selected(True)
            self.ui.c_pagination.add_card_size_changed_receaver(card.size_changed)
            self.images_cards.append(card)
        self.ui.c_pagination.add_cards(self.images_cards)

    def __collet_mode(self):
        self.ui.bt_command.setText("Select")
        self.bt_command_text = self.ui.bt_command.text()
        self.__refresh_command_bt_text()

    def __collet_images(self):
#        print(self.img_list.get_types()[0])
        self.s_change_view.emit(cfg.IMAGES_VIEW, cfg.AI_LAUNCHER_VIEW, {"selected_images_name": self.img_list.get_types()[0], "selected_images":self.selected_imgs})

#    def __get_selected_src(self):
#        return [img.src for img in self.selected_imgs]

    def __refresh_command_bt_text(self):
        nb_selected = len(self.selected_imgs)
        if nb_selected > 0:
            self.ui.bt_command.setText(self.bt_command_text + " (" + str(nb_selected) + ")")
        else:
            self.ui.bt_command.setText(self.bt_command_text)
