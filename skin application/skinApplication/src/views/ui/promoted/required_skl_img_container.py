from .promoted_container import *

from .required_skl_img_item import  RequiredSklImgItem


class RequiredSklImgContainer(PromotedContainer):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.req_skl_imgs_data = None
        self.req_skl_img_items = {}
        self._pre_charge()

    def initialize(self, req_skl_imgs_data, click_receaver):
        if len(req_skl_imgs_data) > 0:
            self.req_skl_imgs_data = req_skl_imgs_data
            for img_name, img_data in req_skl_imgs_data.items():
                rk_img = RequiredSklImgItem(self)
                rk_img.initialize(img_name, img_data["min"], img_data["max"], 0, click_receaver)
                self.layout.addWidget(rk_img)
                self.req_skl_img_items[img_name] = rk_img
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText(tf.f("No required images"))
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def set_selected_number(self, skl_img, number):
        if skl_img in self.req_skl_img_items:
            self.req_skl_img_items[skl_img].set_selected_number(number)



