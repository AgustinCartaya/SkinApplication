from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton,
        QSpacerItem, QSizePolicy, QCheckBox)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .check_button import CheckButton

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner
import src.util.util as util

class VariableInputCreator(QFrame):

    INPUT_OPTIONS = "options"
    INPUT_INT = "int"
    INPUT_FLOAT = "float"
    INPUT_TEXT = "text"
    INPUT_BOOL = "bool"
    INPUT_DATE = "date"

    s_cancel = Signal()
    s_add = Signal(str, list, str)
    def __init__(self, parent, add_receaver, cancel_receaver):
        QFrame.__init__(self, parent)

        self.input_type = ""

        self.s_add.connect(add_receaver)
        self.s_cancel.connect(cancel_receaver)
        self.__create()


    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)

        self.__create_bt_type()
        self.__create_input_name()
        self.__create_add_decimals()
        self.__create_values()
        self.__create_add_scales()
        self.__create_scales()
        self.__create_buttons()

        self.c_name.hide()
        self.i_decimals.hide()
        self.i_add_scales.hide()
        self.c_scales.hide()
        self.c_values.hide()
        self.bt_add.hide()

    def __create_bt_type(self):
        ly_type = QVBoxLayout()
        ly_type_up = QHBoxLayout()
        ly_type_down = QHBoxLayout()
        ly_type.addLayout(ly_type_up)
        ly_type.addLayout(ly_type_down)

#        vs_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
#        ly_type.addItem(vs_left)

        self.bt_options = CheckButton(self)
        self.bt_options.setText("Options")
        ly_type_up.addWidget(self.bt_options)
        self.bt_options.clicked.connect( lambda: self.__type_selected(self.INPUT_OPTIONS) )

        self.bt_number = CheckButton(self)
        self.bt_number.setText("Number")
        ly_type_up.addWidget(self.bt_number)
        self.bt_number.clicked.connect( lambda: self.__type_selected(self.INPUT_INT) )

        self.bt_text = CheckButton(self)
        self.bt_text.setText("Text")
        ly_type_up.addWidget(self.bt_text)
        self.bt_text.clicked.connect( lambda: self.__type_selected(self.INPUT_TEXT) )

        self.bt_bool = CheckButton(self)
        self.bt_bool.setText("Yes/No")
        ly_type_down.addWidget(self.bt_bool)
        self.bt_bool.clicked.connect( lambda: self.__type_selected(self.INPUT_BOOL) )

        self.bt_date = CheckButton(self)
        self.bt_date.setText("Date")
        ly_type_down.addWidget(self.bt_date)
        self.bt_date.clicked.connect( lambda: self.__type_selected(self.INPUT_DATE) )

        g = [self.bt_options, self.bt_number, self.bt_text, self.bt_bool, self.bt_date]
        self.bt_options.add_group(g)
        self.bt_number.add_group(g)
        self.bt_text.add_group(g)
        self.bt_bool.add_group(g)
        self.bt_date.add_group(g)

        vs_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_type.addItem(vs_right)

        self.layout.addLayout(ly_type)

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

    def __create_add_decimals(self):
        self.i_decimals = QCheckBox(self)
        self.i_decimals.setText("Number with decimals")
        self.i_decimals.stateChanged.connect(self.__number_with_decimal)
        self.layout.addWidget(self.i_decimals)


    def __create_values(self):
        self.c_values = QFrame(self)

        ly_values = QVBoxLayout(self.c_values)
        ly_values.setSpacing(4)
        ly_values.setContentsMargins(0, 0, 0, 0)

        self.lb_values = Label(self.c_values)
        self.lb_values.setText("Values")
        ly_values.addWidget(self.lb_values)

        self.i_values = LineEdit(self.c_values)
        self.i_values.setPlaceholderText("E.g: Value 1, Value 2, Value 3")
        ly_values.addWidget(self.i_values)

        self.layout.addWidget(self.c_values)

    def __create_add_scales(self):
        self.i_add_scales = QCheckBox(self)
        self.i_add_scales.setText("Add scale")
        self.i_add_scales.stateChanged.connect(self.__input_with_scale)
        self.layout.addWidget(self.i_add_scales)

    def __create_scales(self):
        self.c_scales = QFrame(self)

        ly_scales = QVBoxLayout(self.c_scales)
        ly_scales.setContentsMargins(0, 0, 0, 0)
#        ly_scales.setSpacing(4)

        self.qbt_scale_group = QButtonGroup()
        self.scales_index = []
        counter = 0
        for scale in util.get_availables_scales():
            ly_scale = QVBoxLayout()
            ly_scales.addLayout(ly_scale)

            i_scale = QRadioButton(self.c_scales)
            i_scale.setText(util.file_name_to_title(scale))
            self.qbt_scale_group.addButton(i_scale, counter)
            ly_scale.addWidget(i_scale)

            self.scales_index.append(scale)
            counter = counter + 1

            # units preview
            ly_units_preview = QVBoxLayout()
            ly_units_preview.setContentsMargins(20, 0, 0, 0)
            ly_scale.addLayout(ly_units_preview)

            lb_units = Label(self.c_scales)
            lb_units.setText(", ".join(util.get_scale_units(scale)), parenthesis=True)
            ly_units_preview.addWidget(lb_units)

#            vs_right = QSpacerItem(20, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)
#            ly_scale.addItem(vs_right)



        self.layout.addWidget(self.c_scales)


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

    @Slot(str)
    def __type_selected(self, t):
        self.c_name.show()
        self.bt_add.show()
        if t == self.INPUT_OPTIONS:
            self.i_decimals.hide()
            self.i_add_scales.hide()
            self.c_values.show()
            self.c_scales.hide()
            self.input_type = t

        else:
            self.c_values.hide()
            if t == self.INPUT_INT:
                self.i_decimals.show()
                self.i_add_scales.show()
                if not self.i_add_scales.isChecked():
                    self.c_scales.hide()
                if self.input_type != self.INPUT_FLOAT:
                    self.input_type = t

            elif t in (self.INPUT_TEXT, self.INPUT_BOOL, self.INPUT_DATE):
                self.i_decimals.hide()
                self.i_add_scales.hide()
                if not self.i_add_scales.isChecked():
                    self.c_scales.hide()
                self.input_type = t

    @Slot()
    def __number_with_decimal(self):
        if self.i_decimals.isChecked():
            self.input_type = self.INPUT_FLOAT
        else:
            self.input_type = self.INPUT_INT

    @Slot()
    def __input_with_scale(self):
        if self.i_add_scales.isChecked():
            self.c_scales.show()
        else:
            self.c_scales.hide()

    @Slot()
    def __cancel(self):
        self.s_cancel.emit()

    @Slot()
    def __add(self):
        title = self.i_name.text().strip()
        values = []
        if title == "":
            raise ValueError('New input title empty', "INPUT TITLE", "EMPTY")
        if self.input_type == self.INPUT_OPTIONS:
            values = util.str_to_list(self.i_values.text(),",")
            if len(values) == 0:
                raise ValueError('New input values empty', "INPUT VALUES", "EMPTY")
            else:
                values.insert(0,"--e")
        elif self.input_type in (self.INPUT_INT, self.INPUT_FLOAT) and self.i_add_scales.isChecked():
            if self.qbt_scale_group.checkedId() == -1:
                raise ValueError('New input Scale not selected', "INPUT_SCALE", "NOT_SELECTED")
            else:
                values.append(self.scales_index[self.qbt_scale_group.checkedId()])

        self.s_add.emit(title, values, self.input_type)
