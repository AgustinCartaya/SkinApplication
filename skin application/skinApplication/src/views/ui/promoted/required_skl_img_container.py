from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout
from .label import Label

from .required_skl_img_item import  RequiredSklImgItem

class RequiredSklImgContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, req_skl_imgs_data = None):
        QFrame.__init__(self, parent)

        self.req_skl_imgs_data = req_skl_imgs_data
        self.req_skl_img_items = {}
        self.__create()


    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)


    def create_required_skl_imgs(self, req_skl_imgs_data):
        if len(req_skl_imgs_data) > 0:
            self.req_skl_imgs_data = req_skl_imgs_data
            for img_name, img_data in req_skl_imgs_data.items():
                rk_img = RequiredSklImgItem(self, img_name, img_data["min"], img_data["max"])
                self.layout.addWidget(rk_img)
                self.req_skl_img_items[img_name] = rk_img
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText("No required information")
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

    def set_selected_number(self, skl_img, number):
        if skl_img in self.req_skl_img_items:
            self.req_skl_img_items[skl_img].set_selected_number(number)



