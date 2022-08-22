from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QFrame, QHBoxLayout, QCheckBox, QSpacerItem, QSizePolicy

from .label import Label


import src.util.data_cleaner as data_cleaner
import src.util.util as util

class FilterSklImgItem(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.img_name = ""

        self.__create()

    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

    def create_contet(self, img_name, img_number, filter_receaver):
        self.img_name = img_name
        self.filter_receaver = filter_receaver

        self.__create_check_box()
        self.__create_lb_number()

        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.sp)

        self.refresh_lb_number(img_number)

    def __create_check_box(self):
        self.input = QCheckBox(self)
        self.input.setText(self.img_name)
        self.layout.addWidget(self.input)
        self.input.stateChanged.connect(self.filter_receaver)

    def __create_lb_number(self):
        self.lb_number = Label(self)
#        self.lb_number.setText(self.img_number, parenthesis=True)
        self.layout.addWidget(self.lb_number)

    def set_checked(self, checked):
        self.input.setChecked(checked)

    def is_checked(self):
        return self.input.isChecked()

    def refresh_lb_number(self, img_number):
        self.lb_number.setText(img_number, parenthesis=True)

