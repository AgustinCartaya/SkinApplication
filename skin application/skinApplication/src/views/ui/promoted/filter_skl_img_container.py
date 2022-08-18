from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QFrame, QVBoxLayout

from .filter_skl_img_item import FilterSklImgItem
from .label import Label


import src.util.data_cleaner as data_cleaner
import src.util.util as util

class FilterSklImgContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.inputs = {}

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(9, 0, 0, 0)


    def create_filters(self, images, state_changed_receaver):
        for img in images:
            image_type_cb = FilterSklImgItem(self)
            image_type_cb.create_contet(util.file_name_to_title(img[0]), img[1], state_changed_receaver)
            self.layout.addWidget(image_type_cb)
            self.inputs[img[0]] = image_type_cb

    def check_all(self):
        for _, input in self.inputs.items():
            input.set_checked(True)

    def get_checked_list(self):
        lst = []
        for image_type, input in self.inputs.items():
            if input.is_checked():
                lst.append(image_type)
        return lst

    def refrsh_lb_numbers(self, lst):
        for ele in lst:
            self.inputs[ele[0]].refresh_lb_number(ele[1])
