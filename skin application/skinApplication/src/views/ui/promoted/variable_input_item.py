from .promoted_container import *

from PySide6.QtWidgets import QButtonGroup, QRadioButton, QDateEdit, QComboBox, QDoubleSpinBox, QSpinBox, QInputDialog
from PySide6.QtCore import QDate
from src.objects.variable_input import VariableInput


class VariableInputItem(PromotedContainer):

    DISPOSITION_V = "V"
    DISPOSITION_H = "H"

    s_edit_input = Signal(VariableInput)
    def __init__(self, parent):
        super().__init__(parent)

        self.vi = None
        self.disposition = VariableInputItem.DISPOSITION_V
        self.input = None


    def initialize(self, variable_input, edit_receaver, disposition=DISPOSITION_V):
        self.vi = variable_input
        self.disposition = disposition

        if self.vi.is_editable():
            self.s_edit_input.connect(edit_receaver)

        self.__create()

    def _pre_charge(self):
        pass

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
        self.lb_title.setText(self.vi.name, format=True, colon=True)
        self.layout.addWidget(self.lb_title)

    def __create_input(self):
        self.c_input = QFrame(self)

        self.TYPE_layout = QHBoxLayout(self.c_input)
        self.TYPE_layout.setContentsMargins(0, 0, 0, 0)

        # input
        # OPTIONS / BOOL
        if self.vi.type in (VariableInput.TYPE_OPTIONS, VariableInput.TYPE_BOOL):
            self.input = QComboBox(self.c_input)

#            if self.vi.type == VariableInput.TYPE_OPTIONS:
            self.input.addItems([""] + self.vi.items)
#            else:
#                self.input.addItems([""] + self.vi.items)

        # NUMBER
        elif self.vi.type == VariableInput.TYPE_INT:
            self.input = QSpinBox(self.c_input)
            self.input.setMaximum(1000000)

        # NUMBER WITH DECIMALS
        elif self.vi.type == VariableInput.TYPE_FLOAT:
            self.input = QDoubleSpinBox(self.c_input)
            self.input.setMaximum(1000000)

        # TEXT
        elif self.vi.type == VariableInput.TYPE_TEXT:
            self.input = LineEdit(self.c_input)
            self.input.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_letter_number_space))

        # DATE
        elif self.vi.type == VariableInput.TYPE_DATE:
            self.input = QDateEdit(self.c_input)
            self.input.setMinimumDate(QDate(1900, 1, 1))
            self.input.setDate(QDate(1900, 1, 1))
            self.input.setDisplayFormat("dd-MM-yyyy")

        self.TYPE_layout.addWidget(self.input)

        # scale input
        if self.vi.has_scale():
            self.__create_scale_input()

        # Edit button
        if self.vi.is_editable():
            self.bt_edit = Button(self.c_input)
            self.bt_edit.setText("Edit")
#            self.bt_edit.setMinimumSize(QSize(0, 0))
            self.bt_edit.setMaximumSize(QSize(80, 30))
            self.TYPE_layout.addWidget(self.bt_edit)
            self.bt_edit.clicked.connect(self.__edit_input)

        self.layout.addWidget(self.c_input)

        if self.disposition == self.DISPOSITION_H:
            self.layout.setStretch(0, 1)
            self.layout.setStretch(1, 2)

    def __create_scale_input(self):
        self.scale_input = QComboBox(self.c_input)
        self.scale_input.addItems([""]+ self.vi.get_scale_units())
        self.TYPE_layout.addWidget(self.scale_input)


    @Slot()
    def __edit_input(self):
        self.s_edit_input.emit(self.vi)

    def get_selected_item(self):
        item = None
        if self.vi.type == VariableInput.TYPE_OPTIONS and self.input.currentText() != "":
            item = self.input.currentText()

        elif self.vi.type == VariableInput.TYPE_BOOL and self.input.currentIndex() != 0:
            item = bool(self.input.currentIndex()-1)

        elif self.vi.is_numeric() and self.input.value() != 0:
            if self.vi.has_scale():
                if self.scale_input.currentText() != "":
                    item = VariableInput.to_basic_unit(self.vi.scale, self.input.value(), self.scale_input.currentText())
            else:
                item = self.input.value()

        elif self.vi.type == VariableInput.TYPE_TEXT and self.input.text().strip() != "":
            item = self.input.text().strip()

        elif self.vi.type == VariableInput.TYPE_DATE and self.input.date() > QDate.fromString('01-01-1900', "dd-MM-yyyy"):
            item = self.input.date().toString("dd-MM-yyyy")
        return item

    def append_items(self, items):
        self.vi.items = self.vi.items + items
        if self.vi.type == VariableInput.TYPE_OPTIONS:
            self.input.addItems(items)

    def select_default_value(self, item):
        if self.vi.type == VariableInput.TYPE_OPTIONS:
            index = self.input.findText(item)
            if index != -1:
                self.input.setCurrentIndex(index)
            else:
                print("error finding " + item)

        elif self.vi.type == VariableInput.TYPE_TEXT:
            self.input.setText(item)

        elif self.vi.is_numeric():
            if self.vi.has_scale():
                values = VariableInput.to_sub_unit(self.vi.scale, item)
                self.scale_input.setCurrentIndex(self.scale_input.findText(values[1]))
                self.input.setValue(values[0])
            else:
                self.input.setValue(item)

        elif self.vi.type == VariableInput.TYPE_BOOL:
            self.input.setCurrentIndex(int(item)+1)

        elif self.vi.type == VariableInput.TYPE_DATE:
            self.input.setDate(QDate.fromString(item, "dd-MM-yyyy"))

    def get_items(self, null_item = True):
        return self.vi.items
