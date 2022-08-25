from .promoted_container import *

from .filters_content import FiltersContent
from .filter_variable_input import FilterVariableInput

from src.objects.variable_input import VariableInput


class FilterVariableInputsContainer(FiltersContent):

    def __init__(self, parent):
        super().__init__(parent)

        self.filters = {}
        self.filters_family = ""
        self.filter_receaver = None
        self._pre_charge()

    def initialize(self, filters_family, filter_receaver):
        self.filters_family = filters_family
        self.filter_receaver = filter_receaver
        self.__create_filters()

    def show_virtual_filters(self, vi_list, filter_receaver):
        self.filter_receaver = filter_receaver
        for vi in vi_list:
            self.__show_single_filter(vi)

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)

    def __create_filters(self):
        for vi in VariableInput.get_available_variable_inputs(self.filters_family):
            self.__show_single_filter(vi)

    def __show_single_filter(self, variable_input):
        filter = FilterVariableInput(self)
        filter.initialize(variable_input, self.filter_receaver)
        self.layout.addWidget(filter)
        self.filters[variable_input.id] = filter

    def get_selected_filters(self):
        f_selected = {}
        for f_id, filter in self.filters.items():
            if filter.get_selected_filter() is not None:
                f_selected[f_id] = filter.get_selected_filter()
        return f_selected

    def reset_filters(self):
        for _, filter in self.filters.items():
            filter.reset()
