from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QComboBox, QInputDialog)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button

from src.objects.patient import Patient
from PySide6.QtCore import Signal


class MedicalInformationInput(QFrame):

    s_add_new_mi_item = Signal(str)
    def __init__(self, id, title, items, receaver, add_null = False, *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.id = id
        self.title = title
        self.items = items
        self.add_null = add_null
        if add_null:
            self.items.insert(0, "")

        self.__create()

        self.s_add_new_mi_item.connect(receaver.add_new_mi_item)

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_title()
        self.__create_input()

    def __create_title(self):
        mi_title = Label(self)
        mi_title.setText(self.title)
        self.layout.addWidget(mi_title)

    def __create_input(self):
        self.c_input = QFrame(self)

        self.input_layout = QHBoxLayout(self.c_input)
        self.input_layout.setContentsMargins(0, 0, 0, 0)

        # QComboBox
        self.mi_combo_box = QComboBox(self.c_input)
        self.mi_combo_box.addItems(self.items)
        self.input_layout.addWidget(self.mi_combo_box)

        # Edit button
        self.bt_add = Button(self.c_input)
        self.bt_add.setText("+")
#        self.bt_add.set_icon("plus")
        self.bt_add.setMinimumSize(QSize(0, 0))
        self.bt_add.setMaximumSize(QSize(25, 25))
        self.input_layout.addWidget(self.bt_add)
        self.bt_add.clicked.connect(self.add_new_mi_item)

        self.layout.addWidget(self.c_input)

    def selected_item(self):
        return self.mi_combo_box.currentText()

    def add_new_mi_item(self):
        self.s_add_new_mi_item.emit(self.id)

    def append_items(self, items):
        self.mi_combo_box.addItems(items)

    def select_item(self, item):
        index = self.mi_combo_box.findText(item)
        if index != -1:
            self.mi_combo_box.setCurrentIndex(index)
        else:
            print("error finding " + item)

    def get_items(self, null_item = True):
        if self.add_null and not null_item:
            return self.items[1:]
        else:
            return self.items

