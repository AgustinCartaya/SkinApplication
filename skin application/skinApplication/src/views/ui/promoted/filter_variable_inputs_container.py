
from .filters_content import FiltersContent
from .filter_variable_input import FilterVariableInput

from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout

from .button import Button
import src.util.util as util
import src.util.variable_inputs as var_inputs


class FilterVariableInputsContainer(FiltersContent):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        FiltersContent.__init__(self, parent)
        self.filters = {}
        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
#        self.layout.setContentsMargins(0, 0, 0, 0)
#        self.layout.setSpacing(50)

    def show_filters(self, input_type, filter_receaver):
        if type(input_type) is list:
            for filter in input_type:
                f_id = filter[0]
                f_type = filter[1]
                f_title = util.file_name_to_title(f_id)
                f_values = filter[2]
                self.__show_single_filter(f_id, f_type, filter_receaver, f_title, f_values)

                if len(filter) == 4:
                    self.filters[f_id].set_action_values(filter[3])

        else:
            for file_name in var_inputs.get_availables_variable_inputs(input_type):
                (f_id, f_type) = file_name.split(".")
                f_title = util.file_name_to_title(f_id)
                f_values = var_inputs.get_variable_input_content(input_type, file_name)

                self.__show_single_filter(f_id, f_type, filter_receaver, f_title, f_values)

    def __show_single_filter(self, f_id, f_type, filter_receaver, f_title, f_values):
        if f_type ==  var_inputs.INPUT_OPTIONS and f_values[0].startswith("--e"):
            f_values = f_values[1:]

        filter = FilterVariableInput(self)
        filter.create_filter(
            f_id,
            f_type,
            filter_receaver,
            f_title,
            f_values,
            )

        self.layout.addWidget(filter)
        self.filters[f_id] = filter

    def get_selected_filters(self):
        f_selected = {}
        for f_id, filter in self.filters.items():
            if filter.get_selected_filter() is not None:
                f_selected[f_id] = filter.get_selected_filter()
        return f_selected

    def reset_filters(self):
        for _, filter in self.filters.items():
            filter.reset()
