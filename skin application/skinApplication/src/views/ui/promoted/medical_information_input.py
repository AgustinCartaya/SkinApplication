from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QComboBox, QInputDialog)

from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button

from src.objects.patient import Patient
from PySide6.QtCore import Signal


class MedicalInformationInput(QFrame):

    s_add_new_mi_item = Signal(str, str)
    def __init__(self, title, items, receaver, id, *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.title = title
        self.items = items
        self.id = id

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
        text, ok = QInputDialog.getText(self,
            'Add new "' + self.title + '"',
            "Actual values:\n" + "; ".join(self.items[1:]))
        if ok:
            self.s_add_new_mi_item.emit(self.id, text)

    def append_item(self, item):
        self.mi_combo_box.addItem(item)

    def select_item(self, item):
        index = self.mi_combo_box.findText(item)
        if index != -1:
            self.mi_combo_box.setCurrentIndex(index)
        else:
            print("error finding " + item)


