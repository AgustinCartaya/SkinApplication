
from .filters_content import FiltersContent
from .filter_variable_input import FilterVariableInput

from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QInputDialog, QFrame, QVBoxLayout

from .button import Button
from .variable_input_creator import VariableInputCreator
import src.util.util as util


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

    def show_filters(self, folder, filter_receaver):
        for file_name in util.get_file_list(folder):
            (f_id, f_type) = file_name.split(".")
            f_title = util.file_name_to_title(f_id)
            f_values = util.read_file_list(folder, file_name)

            self.__show_single_filter(f_id, f_type, filter_receaver, f_title, f_values)

    def __show_single_filter(self, f_id, f_type, filter_receaver, f_title, f_values):
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
