from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout

from .button import Button
from .variable_input import VariableInput
from .variable_input_creator import VariableInputCreator
import src.util.variable_inputs as var_inputs

import src.util.util as util

class VariableInputsContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self,
        folder,
        bt_text = "Add new Input",
        inputs_disposition = VariableInput.DISPOSITION_V,
        *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.inputs = {}
        self.folder = folder
        self.bt_text = bt_text
        self.inputs_disposition = inputs_disposition

        self.input_creator = None

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(50)

        self.__show_inputs()
        self.__create_bt_creator()

    def __show_inputs(self):
        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.setSpacing(20)
        self.layout.addLayout(self.inputs_layout)

        for file_name in util.get_file_list(self.folder):
            (i_id, i_type) = file_name.split(".")
            i_title = util.file_name_to_title(i_id)
            i_values = util.read_file_list(self.folder, file_name)


            self.__show_single_input(i_id, i_title, i_values, i_type)

    def __show_single_input(self, i_id, i_title, i_values, i_type):
        if i_type ==  var_inputs.INPUT_OPTIONS and i_values[0].startswith("--e"):
            editable = True
            i_values = i_values[1:]
        else:
            editable = False

        input = VariableInput(self,
            i_id,
            i_title,
            items=i_values,
            edit_receaver=self.__add_new_input_item,
            input_type=i_type,
            disposition=self.inputs_disposition,
            add_null=True,
            editable=editable)

        self.inputs_layout.addWidget(input)
        self.inputs[i_id] = input

    def __create_bt_creator(self):
        self.bt_creator = Button(self)
        self.bt_creator.setText(self.bt_text)
        self.layout.addWidget(self.bt_creator,0, Qt.AlignHCenter)
        self.bt_creator.clicked.connect(self.__show_input_creator)

    @Slot()
    def __show_input_creator(self):
        if self.input_creator is None:
            self.input_creator = VariableInputCreator(self, self.__create_new_input, self.__cancel_new_input)
            self.layout.addWidget(self.input_creator)

    Slot(str, list, str)
    def __create_new_input(self, input_title, input_values, input_type):
        file_name = util.title_to_file_name(input_title)
        if file_name in self.inputs:
            raise ValueError('Caracteristic input already exists', "CARACTERISTIC_INPUT", "REPEATED")

        file_content = ""
        if len(input_values) > 0:
            file_content = '\n'.join(input_values)
        util.create_file(file_content, self.folder, file_name + "." + input_type)

        self.__show_single_input(file_name, input_title, input_values, input_type)
        self.__cancel_new_input()

    @Slot()
    def __cancel_new_input(self):
        self.input_creator.setParent(None)
        self.input_creator = None

    @Slot(str)
    def __add_new_input_item(self, input_id):
        new_item_s, ok = QInputDialog.getText(self,
            'Add new "' + self.inputs[input_id].title + '"',
            "Actual values:\n" + ", ".join(self.inputs[input_id].get_items(False)))
        if ok:
            new_item_s = util.str_to_list(new_item_s, ",")
        if len(new_item_s) > 0:
            util.apped_to_file("\n" + "\n".join(new_item_s),
                self.folder,
                input_id + "." + self.inputs[input_id].input_type,
                )
            self.inputs[input_id].append_items(new_item_s)

    def get_selected_items(self):
        selected_items = {}
        for selected_item in self.inputs:
            selected_items[selected_item] = self.inputs[selected_item].get_selected_item()
        return selected_items

    def select_default_values(self, default):
        for key, value in default.items():
            if key in self.inputs:
                self.inputs[key].select_default_value(value)