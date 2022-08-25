from .promoted_container import *
from src.objects.variable_input import VariableInput


class VariableInputPreview(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)
        self._pre_charge()

    def initialize(self, vi_id, vi_content):
        vi = VariableInput.get_variable_input(vi_id)


    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_lb_name()
        self.__create_lb_value()

        # spacer
        sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(sp)

    def __create_lb_name(self):
        self.lb_name = Label(self)
        self.layout.addWidget(self.lb_name)

    def __create_lb_name(self):
        self.lb_value = Label(self)
        self.layout.addWidget(self.lb_value)





