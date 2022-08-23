from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout

from .button import Button
from .variable_input import VariableInput
from .variable_input_creator import VariableInputCreator

import src.util.variable_inputs as var_inputs

import src.util.util as util

class VariableInputsContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.inputs = {}
        self.variable_input_type = ""
        self.inputs_disposition = None

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(50)


    def show_inputs(self, input_type, inputs_disposition=VariableInput.DISPOSITION_V):
        self.variable_input_type = input_type
        self.inputs_disposition = inputs_disposition

        self.__create_inputs()

    def __create_inputs(self):
        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.setSpacing(20)
        self.layout.addLayout(self.inputs_layout)

        # AI inputs
        for file_name in var_inputs.get_availables_ai_variable_inputs(self.variable_input_type):
            (i_id, i_type) = file_name.split(".")
            i_values = var_inputs.get_variable_input_content(self.variable_input_type, file_name)
            self.__create_single_input(i_id, i_type, i_values, False)

        # created inputs
        for file_name in var_inputs.get_availables_created_variable_inputs(self.variable_input_type):
            (i_id, i_type) = file_name.split(".")
            i_values = var_inputs.get_variable_input_content(self.variable_input_type, file_name)
            self.__create_single_input(i_id, i_type, i_values, True)

    def __create_single_input(self, i_id, i_type, i_values, editable=True):
        input = VariableInput(self,
            i_id,
            items=i_values,
            edit_receaver=self.__edit_input,
            input_type=i_type,
            disposition=self.inputs_disposition,
            add_null=True,
            editable=editable)

        self.inputs_layout.addWidget(input)
        self.inputs[i_id] = input

    def append_new_variable_input(self, input_id, input_type, input_values):
        self.__create_single_input(input_id, input_type, input_values, True)

    @Slot(str)
    def __edit_input(self, input_id):
        self.variable_input_editor = VariableInputEditor(self.variable_input_type, input_id, self.inputs[input_id].input_type, self.inputs[input_id].items)
        self.variable_input_editor.show()

        # HASTA AQUI LLEGASTE AHORA TIENES QUE CREAR EL VariableInputEditor Y LOGRAR QUE SE EDITE

#        new_item_s, ok = QInputDialog.getText(self,
#            'Add new "' + self.inputs[input_id].title + '"',
#            "Actual values:\n" + ", ".join(self.inputs[input_id].get_items(False)))
#        if ok:
#            new_item_s = util.str_to_list(new_item_s, ",")
#        if len(new_item_s) > 0:
#            util.apped_to_file("\n" + "\n".join(new_item_s),
#                self.folder,
#                input_id + "." + self.inputs[input_id].input_type,
#                )
#            self.inputs[input_id].append_items(new_item_s)

    def get_selected_items(self):
        selected_items = {}
        for selected_item in self.inputs:
            selected_items[selected_item] = self.inputs[selected_item].get_selected_item()
        return selected_items

    def select_default_values(self, default):
        for key, value in default.items():
            if key in self.inputs:
                self.inputs[key].select_default_value(value)
