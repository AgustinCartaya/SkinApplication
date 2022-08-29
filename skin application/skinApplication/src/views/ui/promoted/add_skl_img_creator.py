from PySide6.QtWidgets import (QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .line_edit import LineEdit

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner
import src.util.skl_imgs as skl_imgs
import src.util.util as util
import src.util.text_filter as tf


class AddSklImgCreator(QWidget):

    s_add = Signal(str)
    def __init__(self, parent, add_receaver):
        super().__init__(None)      

        self.parent = parent
        self.s_add.connect(add_receaver)

        self.setWindowModality(Qt.ApplicationModal)
        if parent is not None:
            self.setStyleSheet(parent.styleSheet())

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
        self.lb_name.setText(tf.f("Name"))
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
        self.bt_cancel.setText(tf.f("Cancel"))
        self.bt_cancel.set_type(Button.BT_CANCEL)
        ly_bt.addWidget(self.bt_cancel)
        self.bt_cancel.clicked.connect(self.__cancel)

        self.bt_add = Button(self)
        self.bt_add.setText(tf.f("Add"))
        ly_bt.addWidget(self.bt_add)
        self.bt_add.clicked.connect(self.__add)

        vs_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_bt.addItem(vs_right)

        self.layout.addLayout(ly_bt)

    @Slot()
    def __cancel(self):
        self.close()

    @Slot()
    def __add(self):
        name = util.title_to_file_name(self.i_name.text())
        if name == "":
            self.show_error("SKL_IMG_NAME", "EMPTY")
        elif name in skl_imgs.get_available_skl_imgs():
            self.show_error("SKL_IMG_NAME", "EXISTS")
        else:
            skl_imgs.create_new_image_type(name)
            self.s_add.emit(name)
            self.close()

    def show_error(self, error_object, type_error):
        if error_object == "SKL_IMG_NAME":
            if type_error == "EMPTY":
                print(error_object + " " + type_error)
            elif type_error == "EXISTS":
                print(error_object + " " + type_error)



