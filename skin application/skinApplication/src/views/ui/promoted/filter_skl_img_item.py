from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QFrame, QHBoxLayout, QCheckBox, QSpacerItem, QSizePolicy

from .label import Label


import src.util.data_cleaner as data_cleaner
import src.util.util as util

class FilterSklImgItem(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self,
        parent,
        img_name,
        img_number = 0,
        state_changed_receaver = None
        ):

        self.img_name = img_name
        self.img_number = img_number
        QFrame.__init__(self, parent)

        self.state_changed_receaver = state_changed_receaver

        self.__create()

    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

        self.__create_check_box()
        self.__create_lb_number()

        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.sp)

    def __create_check_box(self):
        self.input = QCheckBox(self)
        self.input.setText(self.img_name)
        self.layout.addWidget(self.input)

        if self.state_changed_receaver is not None:
            self.input.stateChanged.connect(self.state_changed_receaver)

    def __create_lb_number(self):
        self.lb_number = Label(self)
        self.lb_number.setText(self.img_number, parenthesis=True)
        self.layout.addWidget(self.lb_number)

    def set_checked(self, checked):
        self.input.setChecked(checked)

    def is_checked(self):
        return self.input.isChecked()
