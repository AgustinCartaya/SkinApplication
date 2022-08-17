#from PySide6.QtWidgets import QPushButton
#from PySide6.QtWidgets import QApplication
from .check_button import CheckButton
from PySide6.QtCore import Signal, Slot, Qt

class CheckButtonGroup:
    def __init__(self, multiple_selection = False):
        self.buttons = []
        self.multiple_selection = multiple_selection

    def add_buttons(self, *bts):
        for bt in bts:
            self.add_button(bt)

    def add_button(self, bt):
        self.buttons.append(bt)
        bt.add_group(self.button_switched)

    def set_multiple_selection(self, ms):
        self.multiple_selection = ms

    Slot(CheckButton)
    def button_switched(self, bt):

        # check box
        if self.multiple_selection:
            bt.switch()

        # radio button
        else:
            selected_bt = self.get_selected_button()
            if selected_bt is not bt:
                if selected_bt is not None:
                    self.get_selected_button().switch()
                bt.switch()

    def get_selected_button(self):
        for bt in self.buttons:
            if bt.is_selected():
                return bt
        return None

    def get_selected_buttons(self):
        selected = []
        for bt in self.buttons:
            if bt.is_selected():
                selected.append(bt)
        return selected

    def get_selected_action_values(self):
        return [bt.action_value for bt in self.get_selected_buttons()]

    def get_selected_number(self):
        return len(self.get_selected_buttons())


    def unselect_all(self):
        for bt in self.buttons:
            if bt.is_selected():
                bt.switch()
