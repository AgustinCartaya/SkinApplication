from .promoted_container import *

from .variable_input_item import VariableInputItem
from src.objects.variable_input import VariableInput


class VariableInputsContainer(PromotedContainer):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.inputs = {}
        self.inputs_family = None
        self.inputs_disposition = None

        self._pre_charge()

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(50)

    def initialize(self, inputs_family, inputs_disposition=VariableInputItem.DISPOSITION_V):
        self.inputs_family = inputs_family
        self.inputs_disposition = inputs_disposition

        self.__create_inputs()

    def __create_inputs(self):
        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.setSpacing(20)
        self.layout.addLayout(self.inputs_layout)

        for vi in VariableInput.get_available_variable_inputs(self.inputs_family):
            self.__create_single_input(vi)

    def __create_single_input(self, variable_input):
        input = VariableInputItem(self)
        input.initialize(variable_input, self.__edit_input, self.inputs_disposition)
        self.inputs_layout.addWidget(input)
        self.inputs[variable_input.id] = input

    @Slot(str)
    def __edit_input(self, input_id):
        pass

    def get_selected_items(self):
        selected_items = {}
        for selected_item in self.inputs:
            selected_items[selected_item] = self.inputs[selected_item].get_selected_item()
        return selected_items

    def append_new_variable_input(self, variable_input):
        self.__create_single_input(variable_input)

    def select_default_values(self, default):
        for key, value in default.items():
            if key in self.inputs:
                self.inputs[key].select_default_value(value)
