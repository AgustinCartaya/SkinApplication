from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout
from .label import Label

from .required_image_type import  RequiredImageType

class RequiredImagesTypeContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, req_images_type_data = None):
        QFrame.__init__(self, parent)

        self.req_images_type_data = req_images_type_data
        self.req_images_type = {}
        self.__create()


    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)


    def create_required_images_type(self, req_images_type_data):
        if len(req_images_type_data) > 0:
            self.req_images_type_data = req_images_type_data
            for img_name, img_data in req_images_type_data.items():
                rk_img = RequiredImageType(self, img_name, img_data["min"], img_data["max"])
                self.layout.addWidget(rk_img)
                self.req_images_type[img_name] = rk_img
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText("No required information")
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

    def set_selected_number(self, image_type, number):
        if image_type in self.req_images_type:
            self.req_images_type[image_type].set_selected_number(number)



