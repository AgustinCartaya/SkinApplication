from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,  QButtonGroup, QRadioButton, QDateEdit,
        QComboBox, QDoubleSpinBox, QSpinBox, QInputDialog)

from PySide6.QtCore import Qt, QSize, QDate
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .variable_input_creator import VariableInputCreator

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner
import src.util.util as util

class VariableInput(QFrame):

    DISPOSITION_V = "V"
    DISPOSITION_H = "H"

    s_edit_items = Signal(str)
    def __init__(self,
        parent,
        id,
        title,
        items = [],
        edit_receaver = None,
        input_type = VariableInputCreator.INPUT_OPTIONS,
        add_null = False,
        disposition = DISPOSITION_V,
        editable=False
        ):
        QFrame.__init__(self, parent)

        self.id = id
        self.title = title
        self.items = items
        self.add_null = add_null
        self.input_type = input_type
        self.disposition = disposition
        self.edit_receaver = edit_receaver
        self.editable = editable

        self.scale_input = None
        self.units_and_multipliers = None

        if self.editable and self.edit_receaver is not None:
            self.s_edit_items.connect(edit_receaver)

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
        self.lb_title.setText(self.title, colon=True)
        self.layout.addWidget(self.lb_title)

    def __create_input(self):
        self.c_input = QFrame(self)

        self.input_layout = QHBoxLayout(self.c_input)
        self.input_layout.setContentsMargins(0, 0, 0, 0)

        # input
        # OPTIONS / BOOL
        if self.input_type in (VariableInputCreator.INPUT_OPTIONS, VariableInputCreator.INPUT_BOOL):
            self.input = QComboBox(self.c_input)

            if self.input_type == VariableInputCreator.INPUT_OPTIONS:
                self.input.addItems([""]+self.items)
            else:
                self.input.addItems(["","No","Yes"])

        # NUMBER
        elif self.input_type == VariableInputCreator.INPUT_INT:
            self.input = QSpinBox(self.c_input)
            self.input.setMaximum(1000000);

        # NUMBER WITH DECIMALS
        elif self.input_type == VariableInputCreator.INPUT_FLOAT:
            self.input = QDoubleSpinBox(self.c_input)
            self.input.setMaximum(1000000);

        # TEXT
        elif self.input_type == VariableInputCreator.INPUT_TEXT:
            self.input = LineEdit(self.c_input)
            self.input.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_letter_number_space))

        # DATE
        elif self.input_type == VariableInputCreator.INPUT_DATE:
            self.input = QDateEdit(self.c_input)
            self.input.setDisplayFormat("dd-MM-yyyy")
            self.input.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))

        self.input_layout.addWidget(self.input)

        # second input
        if self.input_type in (VariableInputCreator.INPUT_INT, VariableInputCreator.INPUT_FLOAT)  and len(self.items) != 0:
            self.__create_scale_input()

        # Edit button
        if self.editable and self.edit_receaver is not None and self.input_type == VariableInputCreator.INPUT_OPTIONS:
            self.bt_add = Button(self.c_input)
            self.bt_add.setText("+")
            self.bt_add.setMinimumSize(QSize(0, 0))
            self.bt_add.setMaximumSize(QSize(25, 25))
            self.input_layout.addWidget(self.bt_add)
            self.bt_add.clicked.connect(self.__add_items)

        self.layout.addWidget(self.c_input)

        if self.disposition == self.DISPOSITION_H:
            self.layout.setStretch(0, 1)
            self.layout.setStretch(1, 2)

    def __create_scale_input(self):
        self.units_and_multipliers = util.get_scale_units_and_multipliers(self.items[0])
        self.scale_input = QComboBox(self.c_input)
        self.scale_input.addItems([""]+[ele[0] for ele in self.units_and_multipliers])
        self.input_layout.addWidget(self.scale_input)


    @Slot()
    def __add_items(self):
        self.s_edit_items.emit(self.id)

    def get_selected_item(self):
        item = None
        if self.input_type == VariableInputCreator.INPUT_OPTIONS and self.input.currentText() != "":
            item = self.input.currentText()

        elif self.input_type == VariableInputCreator.INPUT_BOOL and self.input.currentIndex() != 0:
            item = bool(self.input.currentIndex()-1)

        elif self.input_type in (VariableInputCreator.INPUT_INT, VariableInputCreator.INPUT_FLOAT) and self.input.value() != 0:
            item = util.to_basic_unit(self.input.value(), self.scale_input.currentText(), self.units_and_multipliers)

        elif self.input_type == VariableInputCreator.INPUT_TEXT and self.input.text().strip() != "":
            item = self.input.text().strip()

        elif self.input_type == VariableInputCreator.INPUT_DATE and self.input.date() > QDate.fromString('01-01-1900', "dd-MM-yyyy"):
            item = self.input.date().toString("dd-MM-yyyy")
        return item

    def append_items(self, items):
        self.items = self.items + items
        if self.input_type == VariableInputCreator.INPUT_OPTIONS:
            self.input.addItems(items)

    def select_default_value(self, item):
        if self.input_type == VariableInputCreator.INPUT_OPTIONS:
            index = self.input.findText(item)
            if index != -1:
                self.input.setCurrentIndex(index)
            else:
                print("error finding " + item)

        elif self.input_type == VariableInputCreator.INPUT_TEXT:
            self.input.setText(item)
        elif (self.input_type in (VariableInputCreator.INPUT_INT, VariableInputCreator.INPUT_FLOAT) and
                self.scale_input is not None):
                values = util.to_sub_unit(item, self.units_and_multipliers)

                index = self.scale_input.findText(values[1])
                if index != -1:
                    self.scale_input.setCurrentIndex(index)
                else:
                    print("error finding scale unit: " + values[1])

                if self.input_type == VariableInputCreator.INPUT_INT:
                    self.input.setValue(int(values[0]))
                else:
                    self.input.setValue(float(values[0]))

        elif self.input_type == VariableInputCreator.INPUT_INT:
            self.input.setValue(int(item))
        elif self.input_type == VariableInputCreator.INPUT_FLOAT:
            self.input.setValue(float(item))

        elif self.input_type == VariableInputCreator.INPUT_BOOL:
            self.input.setCurrentIndex(int(item)+1)

        elif self.input_type == VariableInputCreator.INPUT_DATE:
            self.input.setDate(QDate.fromString(item, "dd-MM-yyyy"))


    def get_items(self, null_item = True):
        return self.items

#    def __to_basic_unit(self, value, unit):
#        for units in self.units_and_multipliers:
#            if units[0] == unit:
#                return value * units[1]
#        return None

#    def __to_sub_unit(self, value):
#        index = 0
#        while (index < len(self.units_and_multipliers) and
#            value % self.units_and_multipliers[index][1] == 0):
#            index = index+1
#        if index > 0:
#            index = index -1
#        return (value/self.units_and_multipliers[index][1], self.units_and_multipliers[index][0])
