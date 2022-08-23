from PySide6.QtWidgets import (QWidget, QFrame, QVBoxLayout, QHBoxLayout,
        QSpacerItem, QSizePolicy)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .line_edit import LineEdit

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner

class AddSklImgCreator(QWidget):

    s_cancel = Signal()
    s_add = Signal(str)
    def __init__(self, add_receaver, cancel_receaver):
        super().__init__(None)

        self.s_add.connect(add_receaver)
        self.s_cancel.connect(cancel_receaver)
        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(20)

        self.__create_input_name()
        self.__create_buttons()

    def __create_input_name(self):
        self.c_name = QFrame(self)

        ly_name = QVBoxLayout(self.c_name)
        ly_name.setSpacing(4)
        ly_name.setContentsMargins(0, 0, 0, 0)

        self.lb_name = Label(self)
        self.lb_name.setText("Name")
        ly_name.addWidget(self.lb_name)

        self.i_name = LineEdit(self)
        ly_name.addWidget(self.i_name)
        self.i_name.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_letter_number_space))

        self.layout.addWidget(self.c_name)

    def __create_buttons(self):
        ly_bt = QHBoxLayout()

        vs_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_bt.addItem(vs_left)

        self.bt_cancel = Button(self)
        self.bt_cancel.setText("Cancel")
        self.bt_cancel.set_type(Button.BT_CANCEL)
        ly_bt.addWidget(self.bt_cancel)
        self.bt_cancel.clicked.connect(self.__cancel)

        self.bt_add = Button(self)
        self.bt_add.setText("Add")
        ly_bt.addWidget(self.bt_add)
        self.bt_add.clicked.connect(self.__add)

        vs_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_bt.addItem(vs_right)

        self.layout.addLayout(ly_bt)

    @Slot()
    def __cancel(self):
        self.s_cancel.emit()

    @Slot()
    def __add(self):
        name = self.i_name.text().strip()
        if name == "":
            raise ValueError('New skin lesion image name empty', "SKL_IMG_NAME", "EMPTY")
        self.s_add.emit(name)
