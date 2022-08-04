from PySide6.QtWidgets import QFrame, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner

class RequiredElement(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, info_name, info_content=None):
        QFrame.__init__(self, parent)

        self.info_name = info_name

        if (info_content is None or info_content == "") :
            self.satisfied = False
            self.info_content = ""
        else:
            self.satisfied = True
            self.info_content = info_content

        self.__create()


    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_bt_satisfied()
        self.__create_content()

    def __create_bt_satisfied(self):
        self.bt_satisfied = Button(self)
        self.bt_satisfied.setMaximumSize(QSize(28, 28))
        if self.satisfied:
            self.bt_satisfied.setText("/")
        else:
            self.bt_satisfied.setText("X")
            self.bt_satisfied.set_type("cancel")

        self.layout.addWidget(self.bt_satisfied)

    def __create_content(self):
        self.lb_info_name = Label(self)
        self.lb_info_name.setText(self.info_name, colon=True)
        self.layout.addWidget(self.lb_info_name)

        self.lb_info_content = Label(self)
        self.lb_info_content.setText(self.info_content)
        self.layout.addWidget(self.lb_info_content)

        # spacer
        self.sp_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.sp_right)
