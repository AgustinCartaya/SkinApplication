from .promoted_container import *

from .filter_skl_img_item import FilterSklImgItem


class FilterSklImgContainer(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)

        self.inputs = {}
        self._pre_charge()

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(9, 0, 0, 0)

    def initialize(self, images, state_changed_receaver):
        for img in images:
            image_type_cb = FilterSklImgItem(self)
            image_type_cb.initialize(util.file_name_to_title(img[0]), img[1], state_changed_receaver)
            self.layout.addWidget(image_type_cb)
            self.inputs[img[0]] = image_type_cb

    def get_checked_list(self):
        lst = []
        for image_type, input in self.inputs.items():
            if input.is_checked():
                lst.append(image_type)
        return lst

    def check_all(self):
        for _, input in self.inputs.items():
            input.set_checked(True)

    def refrsh_lb_numbers(self, lst):
        for ele in lst:
            self.inputs[ele[0]].refresh_lb_number(ele[1])
