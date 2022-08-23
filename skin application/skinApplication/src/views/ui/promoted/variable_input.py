from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,  QButtonGroup, QRadioButton, QDateEdit,
        QComboBox, QDoubleSpinBox, QSpinBox, QInputDialog)

from PySide6.QtCore import Qt, QSize, QDate
from .label import Label
from .button import Button
from .line_edit import LineEdit

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner
import src.util.util as util
import src.util.variable_inputs as var_inputs


class VariableInput(QFrame):

    DISPOSITION_V = "V"
    DISPOSITION_H = "H"

    s_edit_input = Signal(str)
    def __init__(self,
        parent,
        id,
        items = [],
        edit_receaver = None,
        input_type = var_inputs.INPUT_OPTIONS,
        add_null = False,
        disposition = DISPOSITION_V,
        editable=False
        ):
        QFrame.__init__(self, parent)

        self.id = id
        self.items = items
        self.add_null = add_null
        self.input_type = input_type
        self.disposition = disposition
        self.edit_receaver = edit_receaver
        self.editable = editable

        if self.editable and self.edit_receaver is not None:
            self.s_edit_input.connect(edit_receaver)

        self.__create()


    def __create(self):
        if self.disposition == self.DISPOSITION_H:
            self.layout = QHBoxLayout(self)
            self.layout.setContentsMargins(0, 0, 0, 0)
        else:
            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_title()
        self.__create_input()

    def __create_title(self):
        self.lb_title = Label(self)
        self.lb_title.setText(self.id, format=True, colon=True)
        self.layout.addWidget(self.lb_title)

    def __create_input(self):
        self.c_input = QFrame(self)

        self.input_layout = QHBoxLayout(self.c_input)
        self.input_layout.setContentsMargins(0, 0, 0, 0)

        # input
        # OPTIONS / BOOL
        if self.input_type in (var_inputs.INPUT_OPTIONS, var_inputs.INPUT_BOOL):
            self.input = QComboBox(self.c_input)

            if self.input_type == var_inputs.INPUT_OPTIONS:
                self.input.addItems([""]+self.items)
            else:
                self.input.addItems(["","No","Yes"])

        # NUMBER
        elif self.input_type == var_inputs.INPUT_INT:
            self.input = QSpinBox(self.c_input)
            self.input.setMaximum(1000000)

        # NUMBER WITH DECIMALS
        elif self.input_type == var_inputs.INPUT_FLOAT:
            self.input = QDoubleSpinBox(self.c_input)
            self.input.setMaximum(1000000)

        # TEXT
        elif self.input_type == var_inputs.INPUT_TEXT:
            self.input = LineEdit(self.c_input)
            self.input.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_letter_number_space))

        # DATE
        elif self.input_type == var_inputs.INPUT_DATE:
            self.input = QDateEdit(self.c_input)
            self.input.setMinimumDate(QDate(1900, 1, 1))
            self.input.setDate(QDate(1900, 1, 1))
            self.input.setDisplayFormat("dd-MM-yyyy")

        self.input_layout.addWidget(self.input)

        # second input
        if self.input_type in (var_inputs.INPUT_INT, var_inputs.INPUT_FLOAT)  and len(self.items) != 0:
            self.__create_scale_input()

        # Edit button
        if self.editable and self.edit_receaver is not None:
            self.bt_edit = Button(self.c_input)
            self.bt_edit.setText("Edit")
#            self.bt_edit.setMinimumSize(QSize(0, 0))
            self.bt_edit.setMaximumSize(QSize(80, 30))
            self.input_layout.addWidget(self.bt_edit)
            self.bt_edit.clicked.connect(self.__edit_input)

        self.layout.addWidget(self.c_input)

        if self.disposition == self.DISPOSITION_H:
            self.layout.setStretch(0, 1)
            self.layout.setStretch(1, 2)

    def __create_scale_input(self):
        self.scale_input = QComboBox(self.c_input)
        self.scale_input.addItems([""]+ var_inputs.get_scale_units(self.items[0]))
        self.input_layout.addWidget(self.scale_input)


    @Slot()
    def __edit_input(self):
        self.s_edit_input.emit(self.id)

    def get_selected_item(self):
        item = None
        if self.input_type == var_inputs.INPUT_OPTIONS and self.input.currentText() != "":
            item = self.input.currentText()

        elif self.input_type == var_inputs.INPUT_BOOL and self.input.currentIndex() != 0:
            item = bool(self.input.currentIndex()-1)

        elif self.input_type in (var_inputs.INPUT_INT, var_inputs.INPUT_FLOAT) and self.input.value() != 0:
            if len(self.items) > 0:
                if self.scale_input.currentText() != "":
                    item = var_inputs.to_basic_unit(self.items[0], self.input.value(), self.scale_input.currentText())
            else:
                item = self.input.value()

        elif self.input_type == var_inputs.INPUT_TEXT and self.input.text().strip() != "":
            item = self.input.text().strip()

        elif self.input_type == var_inputs.INPUT_DATE and self.input.date() > QDate.fromString('01-01-1900', "dd-MM-yyyy"):
            item = self.input.date().toString("dd-MM-yyyy")
        return item

    def append_items(self, items):
        self.items = self.items + items
        if self.input_type == var_inputs.INPUT_OPTIONS:
            self.input.addItems(items)

    def select_default_value(self, item):
        if self.input_type == var_inputs.INPUT_OPTIONS:
            index = self.input.findText(item)
            if index != -1:
                self.input.setCurrentIndex(index)
            else:
                print("error finding " + item)

        elif self.input_type == var_inputs.INPUT_TEXT:
            self.input.setText(item)

        elif self.input_type in (var_inputs.INPUT_INT, var_inputs.INPUT_FLOAT):
            if len(self.items) > 0:
                values = var_inputs.to_sub_unit(self.items[0], item)
                self.scale_input.setCurrentIndex(self.scale_input.findText(values[1]))
                self.input.setValue(values[0])
            else:
                self.input.setValue(item)

        elif self.input_type == var_inputs.INPUT_BOOL:
            self.input.setCurrentIndex(int(item)+1)

        elif self.input_type == var_inputs.INPUT_DATE:
            self.input.setDate(QDate.fromString(item, "dd-MM-yyyy"))

    def get_items(self, null_item = True):
        return self.items
