from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout
from .label import Label

from .required_image_type import  RequiredImageType

class RequiredImagesTypeContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, required_images_type = None):
        QFrame.__init__(self, parent)

        self.required_images_type = required_images_type
        self.__create()


    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)


    def set_required_images_type(self, required_images_type):
        if len(required_images_type) > 0:
            self.required_images_type = required_images_type
            for img_name, img_data in required_images_type.items():
                rk_img = RequiredImageType(self, img_name, img_data["min"], img_data["max"])
                self.layout.addWidget(rk_img)
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText("No required information")
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

