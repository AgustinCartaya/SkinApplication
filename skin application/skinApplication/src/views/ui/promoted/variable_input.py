from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QComboBox, QDoubleSpinBox, QSpinBox, QInputDialog)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .variable_input_creator import VariableInputCreator

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner

class VariableInput(QFrame):

    DISPOSITION_V = "V"
    DISPOSITION_H = "H"

    s_edit_items = Signal(str)
    def __init__(self,
        id,
        title,
        items = [],
        edit_receaver = None,
        input_type = VariableInputCreator.INPUT_OPTIONS,
        add_null = False,
        disposition = DISPOSITION_V,
        null_value = None,
        *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.id = id
        self.title = title
        self.items = items
        self.add_null = add_null
        self.input_type = input_type
        self.disposition = disposition
        self.edit_receaver = edit_receaver
        self.null_value = null_value

        self.second_input = None

        if len(items) > 0 and add_null:
            self.items.insert(0, "")

        if edit_receaver is not None:
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
        self.lb_title.setText(self.title + " :")
        self.layout.addWidget(self.lb_title)

    def __create_input(self):
        self.c_input = QFrame(self)

        self.input_layout = QHBoxLayout(self.c_input)
        self.input_layout.setContentsMargins(0, 0, 0, 0)

        # input
        if self.input_type == VariableInputCreator.INPUT_OPTIONS:
            self.input = QComboBox(self.c_input)
            self.input.addItems(self.items)

        elif self.input_type == VariableInputCreator.INPUT_INT:
            self.input = QSpinBox(self.c_input)

        elif self.input_type == VariableInputCreator.INPUT_FLOAT:
            self.input = QDoubleSpinBox(self.c_input)

        elif self.input_type == VariableInputCreator.INPUT_TEXT:
            self.input = LineEdit(self.c_input)
            self.input.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_letter_number_space))

        self.input_layout.addWidget(self.input)

        # Edit button
        if self.edit_receaver is not None:
            self.bt_add = Button(self.c_input)
            self.bt_add.setText("+")
            self.bt_add.setMinimumSize(QSize(0, 0))
            self.bt_add.setMaximumSize(QSize(25, 25))
            self.input_layout.addWidget(self.bt_add)
            self.bt_add.clicked.connect(self.__add_items)

        # second input
        if self.input_type != VariableInputCreator.INPUT_OPTIONS and len(self.items) != 0:
            self.__create_second_input()

        self.layout.addWidget(self.c_input)

        if self.disposition == self.DISPOSITION_H:
            self.layout.setStretch(0, 1)
            self.layout.setStretch(1, 2)

    def __create_second_input(self):
        self.second_input = QComboBox(self.c_input)
        self.second_input.addItems(self.items)
        self.input_layout.insertWidget(self.input_layout.count()-1, self.second_input)

    @Slot()
    def __add_items(self):
        self.s_edit_items.emit(self.id)

    def get_selected_items(self):
        return (self.get_selected_item(), self.get_second_item_selected())

    def get_selected_item(self):
        if self.input_type == VariableInputCreator.INPUT_OPTIONS:
            return self.input.currentText()

        elif (self.input_type == VariableInputCreator.INPUT_INT or
            self.input_type == VariableInputCreator.INPUT_FLOAT):
            if (self.null_value is not None and
                self.input.value() == self.null_value):
                    return ""
            else:
                return str(self.input.value())

        elif self.input_type == VariableInputCreator.INPUT_TEXT:
            return self.input.text().strip()

    def get_second_item_selected(self):
        if self.second_input is not None:
            return self.second_input.currentText()
        else:
            return None

    def append_items(self, items):
        if len(self.items) == 0 and self.add_null:
            self.items.append("")

        self.items = self.items + items

        if self.input_type == VariableInputCreator.INPUT_OPTIONS:
            self.input.addItems(items)
        else:
            if self.second_input is not None:
                self.second_input.addItems(items)
            else:
                self.__create_second_input()

    def select_default_value(self, item):
        if self.input_type == VariableInputCreator.INPUT_OPTIONS:
            index = self.input.findText(item)
            if index != -1:
                self.input.setCurrentIndex(index)
            else:
                print("error finding " + item)
        else:
            value = item
            if self.second_input is not None:
                value = item[0]
                value_2 = item[1]

                index = self.second_input.findText(value_2)
                if index != -1:
                    self.second_input.setCurrentIndex(index)
                else:
                    print("error finding " + value_2)
            if self.input_type == VariableInputCreator.INPUT_TEXT:
                self.input.setText(value)
            elif self.input_type == VariableInputCreator.INPUT_INT:
                self.input.setValue(int(value))
            elif self.input_type == VariableInputCreator.INPUT_FLOAT:
                self.input.setValue(float(value))

    def get_items(self, null_item = True):
        if self.add_null and not null_item:
            return self.items[1:]
        else:
            return self.items

