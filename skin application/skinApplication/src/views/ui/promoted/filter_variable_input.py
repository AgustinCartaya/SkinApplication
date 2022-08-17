from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,QSpacerItem,QSizePolicy, QDateEdit,
        QComboBox, QDoubleSpinBox, QSpinBox, QInputDialog)

from PySide6.QtCore import Qt, QSize, QDate
from .label import Label
from .button import Button
from .line_edit import LineEdit
from .variable_input_creator import VariableInputCreator
from .filters_header import FiltersHeader

from PySide6.QtCore import Signal, Slot

import src.util.data_cleaner as data_cleaner

class FilterVariableInput(QFrame):

    s_filter = Signal()
    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.id = ""
        self.filter_type = ""
        self.title = ""
        self.items = []

        self.range_filter = False

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(9, 0, 0, 0)
#        self.layout.setSpacing(50)

    def create_filter(self, id, filter_type, receaver, title="", items=[]):
        self.s_filter.connect(receaver)

        self.id = id
        self.filter_type = filter_type
        self.title = title
        self.items = items

        self.__create_filter()

    def __create_filter(self):
        self.__create_title()
        self.__create_content()

    def __create_title(self):
        self.lb_title = Label(self)
        self.lb_title.setText(self.title, format=True)
        self.layout.addWidget(self.lb_title)

    def __create_content(self):
        # DATE / INT / FLOAT
        if self.filter_type in (VariableInputCreator.INPUT_INT,
                                    VariableInputCreator.INPUT_FLOAT,
                                    VariableInputCreator.INPUT_DATE
                                    ):
            self.range_filter = True
            self.__create_range_filter()
        else:
            self.__create_simple_filter()

    def __create_simple_filter(self):
        # OPTIONS
        if self.filter_type == VariableInputCreator.INPUT_OPTIONS:
            self.i_filter = QComboBox(self)
            self.i_filter.addItems([""]+self.items)
            self.i_filter.currentIndexChanged.connect(self.call_filter)

        # BOOL
        elif self.filter_type == VariableInputCreator.INPUT_BOOL:
            self.i_filter = QComboBox(self)
            self.i_filter.addItems(["","No","Yes"])
            self.i_filter.currentIndexChanged.connect(self.call_filter)

        # TEXT
        elif self.filter_type == VariableInputCreator.INPUT_TEXT:
            self.i_filter = LineEdit(self)
            self.i_filter.returnPressed.connect(self.call_filter)

        ly_content = QHBoxLayout()
        ly_content.setContentsMargins(9, 0, 0, 0)
        self.layout.addLayout(ly_content)

        ly_content.addWidget(self.i_filter)

        sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_content.addItem(sp)

    def __create_range_filter(self):
        self.c_precise_content = QFrame(self)
        self.c_range_content = QFrame(self)

        # NUMBER
        if self.filter_type == VariableInputCreator.INPUT_INT:
            self.i_precise = QSpinBox(self.c_precise_content)
            self.i_precise.setMinimumSize(QSize(80, 0))
            self.i_precise.editingFinished.connect(self.call_filter)

            self.i_range_min = QSpinBox(self.c_range_content)
            self.i_range_min.setMinimumSize(QSize(80, 0))
            self.i_range_min.editingFinished.connect(self.call_filter)

            self.i_range_max = QSpinBox(self.c_range_content)
            self.i_range_max.setMinimumSize(QSize(80, 0))
            self.i_range_max.editingFinished.connect(self.call_filter)

        # NUMBER WITH DECIMALS
        elif self.filter_type == VariableInputCreator.INPUT_FLOAT:
            self.i_precise = QDoubleSpinBox(self.c_precise_content)
            self.i_precise.setMinimumSize(QSize(80, 0))
            self.i_precise.editingFinished.connect(self.call_filter)

            self.i_range_min = QDoubleSpinBox(self.c_range_content)
            self.i_range_min.setMinimumSize(QSize(80, 0))
            self.i_range_min.editingFinished.connect(self.call_filter)

            self.i_range_max = QDoubleSpinBox(self.c_range_content)
            self.i_range_max.setMinimumSize(QSize(80, 0))
            self.i_range_max.editingFinished.connect(self.call_filter)

        # DATE
        elif self.filter_type == VariableInputCreator.INPUT_DATE:
            self.i_precise = QDateEdit(self.c_precise_content)
            self.i_precise.setMinimumSize(QSize(100, 0))
            self.i_precise.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))
            self.i_precise.editingFinished.connect(self.call_filter)

            self.i_range_min = QDateEdit(self.c_range_content)
            self.i_range_min.setMinimumSize(QSize(100, 0))
            self.i_range_min.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))
            self.i_range_min.editingFinished.connect(self.call_filter)

            self.i_range_max = QDateEdit(self.c_range_content)
            self.i_range_max.setMinimumSize(QSize(100, 0))
            self.i_range_max.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))
            self.i_range_max.editingFinished.connect(self.call_filter)


        ly_content = QVBoxLayout()
        ly_content.setContentsMargins(9, 0, 0, 0)
        self.layout.addLayout(ly_content)

        # ----------- precise
        ly_precise = QVBoxLayout()
        ly_precise.setSpacing(0)
        ly_precise.setContentsMargins(9, 0, 0, 0)
        ly_content.addLayout(ly_precise)

        #   header
        self.c_precise_header = FiltersHeader(self)
        ly_precise.addWidget(self.c_precise_header)
        self.c_precise_header.add_filters_content(self.c_precise_content)
        self.c_precise_header.add_open_receaver(self.close_range)

        ly_precise_header = QHBoxLayout(self.c_precise_header)
        ly_precise_header.setContentsMargins(5, 5, 5, 5)

        lb_precise = Label(self.c_precise_header)
        lb_precise.setText("Precise", format=True)
        ly_precise_header.addWidget(lb_precise)

        #   content
        ly_precise.addWidget(self.c_precise_content)
        ly_precise_content = QHBoxLayout(self.c_precise_content)
        ly_precise_content.setContentsMargins(5, 5, 5, 5)

        #   FILTER VARIABLE
        ly_precise_content.addWidget(self.i_precise)

        #   spacer
        sp_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_precise_content.addItem(sp_3)

        # ----------- range
        ly_range = QVBoxLayout()
        ly_range.setSpacing(0)
        ly_range.setContentsMargins(9, 0, 0, 0)
        ly_content.addLayout(ly_range)

        #   header
        self.c_range_header = FiltersHeader(self)
        ly_range.addWidget(self.c_range_header)
        self.c_range_header.add_filters_content(self.c_range_content)
        self.c_range_header.add_open_receaver(self.close_precise)

        ly_precise_header = QHBoxLayout(self.c_range_header)
        ly_precise_header.setContentsMargins(5, 5, 5, 5)

        lb_range = Label(self.c_range_header)
        lb_range.setText("Range", format=True)
        ly_precise_header.addWidget(lb_range)

        #   content
        ly_range.addWidget(self.c_range_content)
        ly_range_content = QHBoxLayout(self.c_range_content)
        ly_range_content.setContentsMargins(5, 5, 5, 5)

        #   FILTER VARIABLE
        ly_range_content.addWidget(self.i_range_min)

        lb_range_sep = Label(self.c_range_content)
        lb_range_sep.setText("-")
        ly_range_content.addWidget(lb_range_sep)

        #   Filter VARIABLE
        ly_range_content.addWidget(self.i_range_max)

        #   spacer
        sp_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ly_range_content.addItem(sp_2)

    def get_selected_filter(self):
        filter = None
        if self.filter_type == VariableInputCreator.INPUT_OPTIONS and self.i_filter.currentText() != "":
            filter = self.i_filter.currentText()

        elif self.filter_type == VariableInputCreator.INPUT_TEXT and self.i_filter.text().strip() != "":
            filter = self.i_filter.text().strip()

        elif self.filter_type == VariableInputCreator.INPUT_BOOL and self.i_filter.currentIndex() != 0:
            filter = bool(self.i_filter.currentIndex()-1)

        elif self.filter_type in (VariableInputCreator.INPUT_INT,
                                    VariableInputCreator.INPUT_FLOAT,
                                    VariableInputCreator.INPUT_DATE
                                    ):
            if self.c_precise_header.open:
                if self.filter_type in (VariableInputCreator.INPUT_INT, VariableInputCreator.INPUT_FLOAT) and self.i_precise.value() != 0:
                    filter = self.i_precise.value()
                elif self.filter_type == VariableInputCreator.INPUT_DATE and self.i_precise.date() > QDate.fromString('01-01-1900', "dd-MM-yyyy"):
                    filter = self.i_precise.date().toString("dd-MM-yyyy")
#                   filter = util.to_basic_unit(self.i_precise.value(), self.scale_input.currentText())
            elif self.c_range_header.open:
                if (self.filter_type in (VariableInputCreator.INPUT_INT, VariableInputCreator.INPUT_FLOAT) and
                        (self.i_range_min.value() != 0 or self.i_range_max.value() != 0)):
                    filter = (self.i_range_min.value(), self.i_range_max.value())

                elif (self.filter_type == VariableInputCreator.INPUT_DATE and
                        (self.i_range_min.date() > QDate.fromString('01-01-1900', "dd-MM-yyyy") or
                        self.i_range_max.date() > QDate.fromString('01-01-1900', "dd-MM-yyyy") )):
                    filter = (self.i_range_min.date().toString("dd-MM-yyyy"), self.i_range_max.date().toString("dd-MM-yyyy"))
        return filter

    @Slot()
    def call_filter(self):
        self.s_filter.emit()

    @Slot()
    def close_precise(self):
        self.c_precise_header.close_content()

    @Slot()
    def close_range(self):
        self.c_range_header.close_content()

    def reset(self):
        if self.filter_type == VariableInputCreator.INPUT_OPTIONS:
            self.i_filter.setCurrentIndex(0)

        elif self.filter_type == VariableInputCreator.INPUT_TEXT:
            self.i_filter.setText("")

        elif self.filter_type == VariableInputCreator.INPUT_BOOL:
            self.i_filter.setCurrentIndex(0)

        elif self.filter_type in (VariableInputCreator.INPUT_INT, VariableInputCreator.INPUT_FLOAT):
            self.i_precise.setValue(0)
            self.i_range_min.setValue(0)
            self.i_range_max.setValue(0)

        elif self.filter_type == VariableInputCreator.INPUT_DATE:
            self.i_precise.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))
            self.i_range_min.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))
            self.i_range_max.setDate(QDate.fromString('01-01-1900', "dd-MM-yyyy"))
