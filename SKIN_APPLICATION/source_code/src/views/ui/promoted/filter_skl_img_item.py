from .promoted_container import *
from PySide6.QtWidgets import QCheckBox


class FilterSklImgItem(PromotedContainer):

    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.img_name = ""
        self._pre_charge()

    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

    def initialize(self, img_name, img_number, filter_receaver):
        self.img_name = img_name
        self.filter_receaver = filter_receaver

        self.__create_check_box()
        self.__create_lb_number()

        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.sp)

        self.refresh_lb_number(img_number)

    def __create_check_box(self):
        self.input = QCheckBox(self)
        self.input.setText(tf.f(self.img_name, translate=False))
        self.layout.addWidget(self.input)
        self.input.stateChanged.connect(self.filter_receaver)

    def __create_lb_number(self):
        self.lb_number = Label(self)
        self.layout.addWidget(self.lb_number)

    def set_checked(self, checked):
        self.input.setChecked(checked)

    def is_checked(self):
        return self.input.isChecked()

    def refresh_lb_number(self, img_number):
        self.lb_number.setText(tf.f(img_number, parenthesis=True))

