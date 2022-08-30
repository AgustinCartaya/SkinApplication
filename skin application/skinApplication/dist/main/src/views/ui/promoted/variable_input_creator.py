from PySide6.QtWidgets import (QWidget, QFrame, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton,
        QSpacerItem, QSizePolicy, QCheckBox, QScrollArea, QWidget, QMessageBox)

from PySide6.QtCore import Qt, QSize, QTimer, Signal, Slot
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .check_button import CheckButton


import src.util.data_cleaner as data_cleaner
import src.util.util as util
import src.util.text_filter as tf

import src.internal.errors as err

from .check_button_group import CheckButtonGroup

from src.objects.variable_input import VariableInput


class VariableInputCreator(QWidget):

    s_upsert = Signal(VariableInput)
#    s_edit = Signal(VariableInput)
    s_delete = Signal(VariableInput)
    def __init__(self, parent, vi_family, upsert_receaver):
        super().__init__(None)

        self.vi_family = vi_family
        self.vi = None
        self.input_type = ""
        self.parent = parent
        self.s_upsert.connect(upsert_receaver)

        self.edit_mode = False

        self.setWindowModality(Qt.ApplicationModal)
        self.setMinimumSize(QSize(300, 400))

        if parent is not None:
            self.setStyleSheet(parent.styleSheet())

        self.__create()

    def __create(self):
        self.p_layout = QVBoxLayout(self)
        self.p_layout.setSpacing(12)

        self.__create_scroll_area()
        self.__create_bt_type()
        self.__create_input_name()
        self.__create_add_decimals()
        self.__create_values()
        self.__create_add_scales()
        self.__create_scales()
        self.__create_buttons()
        self.__create_erros()

        vs_left = QSpacerItem(2, 40, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.layout.addItem(vs_left)

        self.c_name.hide()
        self.i_decimals.hide()
        self.i_add_scales.hide()
        self.c_scales.hide()
        self.c_values.hide()
        self.bt_add.hide()

    def __create_scroll_area(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.p_layout.addWidget(self.scroll_area)

        self.c_scroll_area = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.c_scroll_area)
        self.ly_scroll_area = QVBoxLayout(self.c_scroll_area)

        # content layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.ly_scroll_area.addLayout(self.layout)

        # spacer
        self.vs_description_down = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ly_scroll_area.addItem(self.vs_description_down)

    def __create_bt_type(self):
        ly_type = QVBoxLayout()
        ly_type_up = QHBoxLayout()
        ly_type_down = QHBoxLayout()
        ly_type.addLayout(ly_type_up)
        ly_type.addLayout(ly_type_down)

#        vs_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
#        ly_type.addItem(vs_left)

        self.bt_options = CheckButton(self)
        self.bt_options.setText(tf.f("Options"))
        ly_type_up.addWidget(self.bt_options)
        self.bt_options.clicked.connect( lambda: self.__type_selected(VariableInput.TYPE_OPTIONS) )

        self.bt_number = CheckButton(self)
        self.bt_number.setText(tf.f("Number"))
        ly_type_up.addWidget(self.bt_number)
        self.bt_number.clicked.connect( lambda: self.__type_selected(VariableInput.TYPE_INT) )

        self.bt_text = CheckButton(self)
        self.bt_text.setText(tf.f("Text"))
        ly_type_up.addWidget(self.bt_text)
        self.bt_text.clicked.connect( lambda: self.__type_selected(VariableInput.TYPE_TEXT) )

        self.bt_bool = CheckButton(self)
        self.bt_bool.setText(tf.f("Yes/No"))
        ly_type_down.addWidget(self.bt_bool)
        self.bt_bool.clicked.connect( lambda: self.__type_selected(VariableInput.TYPE_BOOL) )

        self.bt_date = CheckButton(self)
        self.bt_date.setText(tf.f("Date"))
        ly_type_down.addWidget(self.bt_date)
        self.bt_date.clicked.connect( lambda: self.__type_selected(VariableInput.TYPE_DATE) )

        self.g_bt_type = CheckButtonGroup()
        self.g_bt_type.add_buttons(self.bt_options, self.bt_number, self.bt_text, self.bt_bool, self.bt_date)

        vs_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_type.addItem(vs_right)

        self.layout.addLayout(ly_type)

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

    def __create_add_decimals(self):
        self.i_decimals = QCheckBox(self)
        self.i_decimals.setText(tf.f("Number with decimals"))
        self.i_decimals.stateChanged.connect(self.__number_with_decimal)
        self.layout.addWidget(self.i_decimals)


    def __create_values(self):
        self.c_values = QFrame(self)

        ly_values = QVBoxLayout(self.c_values)
        ly_values.setSpacing(4)
        ly_values.setContentsMargins(0, 0, 0, 0)

        self.lb_values = Label(self.c_values)
        self.lb_values.setText(tf.f("Values"))
        ly_values.addWidget(self.lb_values)

        self.i_values = LineEdit(self.c_values)
        self.i_values.setPlaceholderText(tf.f("E.g: Value 1, Value 2, Value 3"))
        ly_values.addWidget(self.i_values)

        self.layout.addWidget(self.c_values)

    def __create_add_scales(self):
        self.i_add_scales = QCheckBox(self)
        self.i_add_scales.setText(tf.f("Add scale"))
        self.i_add_scales.stateChanged.connect(self.__input_with_scale)
        self.layout.addWidget(self.i_add_scales)

    def __create_scales(self):
        self.c_scales = QFrame(self)

        ly_scales = QVBoxLayout(self.c_scales)
        ly_scales.setContentsMargins(9, 0, 0, 0)
#        ly_scales.setSpacing(4)

        self.qbt_scale_group = QButtonGroup()
        self.scales_index = []
        counter = 0
        for scale in VariableInput.get_available_scales():
            ly_scale = QVBoxLayout()
            ly_scales.addLayout(ly_scale)

            i_scale = QRadioButton(self.c_scales)
            i_scale.setText(tf.f(scale, translate=False, format=True))
            self.qbt_scale_group.addButton(i_scale, counter)
            ly_scale.addWidget(i_scale)

            self.scales_index.append(scale)
            counter = counter + 1

            # units preview
            ly_units_preview = QVBoxLayout()
            ly_units_preview.setContentsMargins(20, 0, 0, 0)
            ly_scale.addLayout(ly_units_preview)

            lb_units = Label(self.c_scales)
            lb_units.setText(tf.f(", ".join(VariableInput.get_available_scale_units(scale)), translate=False, parenthesis=True))
            ly_units_preview.addWidget(lb_units)

        self.layout.addWidget(self.c_scales)

    def __create_buttons(self):
        self.ly_bt = QHBoxLayout()

        vs_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ly_bt.addItem(vs_left)

        self.bt_cancel = Button(self)
        self.bt_cancel.setText(tf.f("Cancel"))
        self.bt_cancel.set_type(Button.BT_CANCEL)
        self.ly_bt.addWidget(self.bt_cancel)
        self.bt_cancel.clicked.connect(self.__cancel)

        self.bt_add = Button(self)
        self.bt_add.setText(tf.f("Add"))
        self.ly_bt.addWidget(self.bt_add)
        self.bt_add.clicked.connect(self.__add)

        vs_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ly_bt.addItem(vs_right)

        self.layout.addLayout(self.ly_bt)

    def __create_erros(self):
        self.c_errors = QFrame(self)
        self.c_errors.setObjectName(u"c_errors")

        ly_errors = QVBoxLayout(self.c_errors)
        ly_errors.setContentsMargins(0, 0, 0, 0)

        self.lb_error = Label(self.c_errors)
        ly_errors.addWidget(self.lb_error)

        self.p_layout.addWidget(self.c_errors, 0, Qt.AlignLeft)
        self.c_errors.hide()

    @Slot(str)
    def __type_selected(self, t):
        self.c_name.show()
        self.bt_add.show()
        if t == VariableInput.TYPE_OPTIONS:
            self.i_decimals.hide()
            self.i_add_scales.hide()
            self.c_values.show()
            self.c_scales.hide()
            self.input_type = t

        else:
            self.c_values.hide()
            if t == VariableInput.TYPE_INT:
                self.i_decimals.show()
                self.i_add_scales.show()
                if not self.i_add_scales.isChecked():
                    self.c_scales.hide()
                else:
                    self.c_scales.show()
                if self.input_type != VariableInput.TYPE_FLOAT:
                    self.input_type = t

            elif t in (VariableInput.TYPE_TEXT, VariableInput.TYPE_BOOL, VariableInput.TYPE_DATE):
                self.i_decimals.hide()
                self.i_add_scales.hide()
                self.c_scales.hide()
                if not self.i_add_scales.isChecked():
                    self.c_scales.hide()
                self.input_type = t

    @Slot()
    def __number_with_decimal(self):
        if self.i_decimals.isChecked():
            self.input_type = VariableInput.TYPE_FLOAT
        else:
            self.input_type = VariableInput.TYPE_INT

    @Slot()
    def __input_with_scale(self):
        if self.i_add_scales.isChecked():
            self.c_scales.show()
        else:
            self.c_scales.hide()

    @Slot()
    def __cancel(self):
        self.close()

    @Slot()
    def __add(self):
        self.reset_inputs_decorators()

        info_dict = self.__catch_info()
        available_vi_names = VariableInput.get_available_variable_input_names(self.vi_family)

        try:
            if info_dict["name"] == "":
                raise ValueError(err.EO_VARIABLE_INPUT_NAME, err.ET_EMPTY)
            elif not self.edit_mode  and info_dict["name"] in available_vi_names:
                raise ValueError(err.EO_VARIABLE_INPUT_NAME, err.ET_EXISTS)
            elif self.edit_mode and info_dict["name"] != self.vi.name and info_dict["name"] in available_vi_names:
                raise ValueError(err.EO_VARIABLE_INPUT_NAME, err.ET_EXISTS)
            elif self.input_type == VariableInput.TYPE_OPTIONS and info_dict["items"] is None:
                raise ValueError(err.EO_VARIABLE_INPUT_VALUES, err.ET_EMPTY)
            elif self.input_type in VariableInput.numeric_input() and self.i_add_scales.isChecked() and info_dict["scale"] is None:
                raise ValueError(err.EO_VARIABLE_INPUT_SCALE, err.ET_NOT_SELECTED)
            else:
                if self.edit_mode:
                    self.vi.name = info_dict["name"]
                    self.vi.type = self.input_type
                    self.vi.items = info_dict["items"]
                    self.vi.scale = info_dict["scale"]
    #                self.s_edit.emit(self.vi)
                else:
                    self.vi = VariableInput(None,
                                        self.vi_family,
                                        VariableInput.OWNER_DOCTOR,
                                        self.input_type,
                                        info_dict["name"],
                                        info_dict["items"],
                                        info_dict["scale"])
                self.s_upsert.emit(self.vi)
                self.close()
        except ValueError as ve:
            err_msg = "ERROR"

            if ve.args[0] == err.EO_VARIABLE_INPUT_NAME:
                self.i_name.set_decorator("error")
                if ve.args[1] == err.ET_EMPTY:
                    err_msg = "Please fill the name"
                if ve.args[1] == err.ET_EXISTS:
                    err_msg = "This name is already used"

            elif ve.args[0] == err.EO_VARIABLE_INPUT_VALUES:
                self.i_values.set_decorator("error")
                err_msg = "Please fill the values"

            self.__show_error(err_msg)
            print(ve.args)


    def __catch_info(self):
        info_dict = {}
        info_dict["name"] = util.clean_title(self.i_name.text())
        info_dict["items"] = util.str_to_list(self.i_values.text(),",")
        info_dict["scale"] = None

        if len(info_dict["items"]) == 0:
            info_dict["items"] = None

        if self.i_add_scales.isChecked() and self.qbt_scale_group.checkedId() >= 0:
            info_dict["scale"] = self.scales_index[self.qbt_scale_group.checkedId()]

        return info_dict

    @Slot()
    def __delete(self):
        reply = QMessageBox.question(self,
                                    'Delete',
                                    tf.f('Are you sure you want to delete this input?'),
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.s_delete.emit(self.vi)
            self.close()

    def reset_inputs_decorators(self):
        self.i_name.set_decorator(None)
        self.i_values.set_decorator(None)

    def __show_error(self, text):
        self.lb_error.setText(tf.f(text))
        self.c_errors.show()
        QTimer.singleShot(4000, self.hide_error)

    def hide_error(self):
        self.c_errors.hide()

    def activate_edit_mode(self, variable_input, delete_receaver):
        self.vi = variable_input
        self.edit_mode = True
        self.input_type = self.vi.type

        self.s_delete.connect(delete_receaver)

        self.bt_add.setText(tf.f("Save"))

        self.bt_delete = Button(self)
        self.bt_delete.setText(tf.f("Delete"))
        self.bt_delete.set_type(Button.BT_DELETE)
        self.ly_bt.insertWidget(1, self.bt_delete)
        self.bt_delete.clicked.connect(self.__delete)

        # select type
        self.__type_selected(self.vi.type)

        # inhabilitate inputs
        self.bt_options.hide()
        self.bt_number.hide()
        self.bt_text.hide()
        self.bt_bool.hide()
        self.bt_date.hide()

        if self.vi.type == VariableInput.TYPE_OPTIONS:
            self.bt_options.select(True)
            self.bt_options.show()

        elif self.vi.is_numeric():
            self.bt_number.select(True)
            self.bt_number.show()
            self.i_add_scales.show()

            if self.vi.type == VariableInput.TYPE_FLOAT:
                self.i_decimals.setChecked(True)
                self.i_decimals.show()

            if self.vi.has_scale():
                self.i_add_scales.setChecked(True)
                bt_scale = self.qbt_scale_group.button(self.scales_index.index(self.vi.scale))
                bt_scale.setChecked(True)

        elif self.vi.type == VariableInput.TYPE_TEXT:
            self.bt_text.select(True)
            self.bt_text.show()

        elif self.vi.type == VariableInput.TYPE_BOOL:
            self.bt_bool.select(True)
            self.bt_bool.show()

        elif self.vi.type == VariableInput.TYPE_DATE:
            self.bt_date.select(True)
            self.bt_date.show()

        # write name
        self.i_name.setText(tf.f(self.vi.name, translate=False))

        # if type options
        if self.vi.items is not None:
            self.i_values.setText(tf.f(", ".join(self.vi.items), translate=False))




