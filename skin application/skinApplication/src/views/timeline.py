from .view_object import *
from .ui.ui_timeline import Ui_timeline

from src.objects.timeline import Timeline
from src.objects.image import Image
from .ui.promoted.skin_lesion_preview_info import SkinLesionPreviewInfo
from .ui.promoted.timeline_skl_img_block import TimelineSklImgBlock
from .image_viewer import ImageViewer

class TimelineView(ViewObject):
    def __init__(self, mv, patient, skin_lesion):
        super().__init__(mv)

        self.p = patient
        self.skl = skin_lesion
        self.timeline = Timeline(self.skl)
        self.image_viewers = []

        self.load_ui()
        self.connect_ui_signals()

        self.__charge_patient_info_line()

    def load_ui(self):
        self.ui = Ui_timeline()
        self.ui.setupUi(self)

        # timeline points
        self.ui.c_timeline_points.initialize(self.timeline, self.switch_point)

    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)
#        self.ui.bt_relaunch.clicked.connect(self.__relaunch)


    @Slot()
    def __back(self):
        self.close_image_viewers()
        self.s_change_view.emit(cfg.IMAGES_VIEW, cfg.ANCIENT_VIEW, {})

    @Slot(int)
    def switch_point(self, point):
        skl = self.timeline.timeline_points[point].skl

        # skin lesion results
        self.ui.c_skl_characteristics.show_info(skl.characteristics, "characteristics")
        self.ui.c_ai_results.show_info(skl.ai_results, "AI results", True)
        self.__show_images(self.timeline.timeline_points[point])

    def __show_images(self, tlp):
        for i in reversed(range(self.ui.ly_images.count())):
            self.ui.ly_images.itemAt(i).widget().setParent(None)

        for img_type, imgs in tlp.images.imgs_dict.items():
            img_block = TimelineSklImgBlock(self.ui.c_images)
            img_block.initialize(img_type, imgs, double_click_receaver=self.open_single_image)
            self.ui.ly_images.addWidget(img_block)

    Slot(Image)
    def open_single_image(self, img):
        self.image_viewers.append(ImageViewer(img))
        self.image_viewers[-1].show()

    def close_image_viewers(self):
        self.image_viewers = []

    def close(self):
        self.close_image_viewers()

    def __charge_patient_info_line(self):
        info_line = []
        info_line.append(["Patient ID", self.p.id])
        info_line.append(["First name", self.p.first_name])
        info_line.append(["Last name", self.p.last_name])
        self.ui.c_patient_info_line.initialize(info_line)
