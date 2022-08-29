from PySide6.QtWidgets import (QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)

from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer
from .label import Label
from .button import Button
from .line_edit import LineEdit

import src.internal.errors as err

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
        self.__create_erros()

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

    def __create_erros(self):
        self.c_errors = QFrame(self)
        self.c_errors.setObjectName(u"c_errors")

        ly_errors = QVBoxLayout(self.c_errors)
        ly_errors.setContentsMargins(0, 0, 0, 0)

        self.lb_error = Label(self.c_errors)
        ly_errors.addWidget(self.lb_error)

        self.layout.addWidget(self.c_errors, 0, Qt.AlignLeft)
        self.c_errors.hide()

    @Slot()
    def __cancel(self):
        self.close()

    @Slot()
    def __add(self):
        self.reset_inputs_decorators()

        try:
            name = util.title_to_file_name(self.i_name.text())

            if name == "":
                raise ValueError(err.EO_SKL_IMG_NAME, err.ET_EMPTY)
            elif name in skl_imgs.get_available_skl_imgs():
                raise ValueError(err.EO_SKL_IMG_NAME, err.ET_EXISTS)

            skl_imgs.create_new_image_type(name)
            self.s_add.emit(name)
            self.close()

        except ValueError as ve:
            err_msg = "ERROR"

            if ve.args[0] == err.EO_SKL_IMG_NAME:
                self.i_name.set_decorator("error")
                if ve.args[1] == err.ET_EMPTY:
                    err_msg = "Please fill the name"
                if ve.args[1] == err.ET_EXISTS:
                    err_msg = "This name is already used"

            self.__show_error(err_msg)
            print(ve.args)

    def show_error(self, error_object, type_error):
        if error_object == "SKL_IMG_NAME":
            if type_error == "EMPTY":
                print(error_object + " " + type_error)
            elif type_error == "EXISTS":
                print(error_object + " " + type_error)

    def reset_inputs_decorators(self):
        self.i_name.set_decorator(None)

    def __show_error(self, text):
        self.lb_error.setText(tf.f(text))
        self.c_errors.show()
        QTimer.singleShot(4000, self.hide_error)

    def hide_error(self):
        self.c_errors.hide()
