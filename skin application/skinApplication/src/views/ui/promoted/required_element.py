from .promoted_container import *
from .form_item import FormItem
#from src.objects.variable_input import VariableInput


class RequiredElement(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)

        req_element_family = None
        self.satisfied = False
        self.info_name = ""
        self.info_content = ""

        self._pre_charge()

    def initialize(self, satisfied, info_name, info_content, req_element_family):
        self.satisfied = satisfied
        self.info_name = info_name
        self.info_content = info_content
        self.req_element_family = req_element_family
        self.__fill_content()


    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_bt_satisfied()

    def __create_bt_satisfied(self):
        self.bt_satisfied = Button(self)
        self.bt_satisfied.setMaximumSize(QSize(28, 28))
        self.layout.addWidget(self.bt_satisfied)

    def __fill_content(self):

        if self.satisfied:
            self.bt_satisfied.setText("/")
        else:
            self.bt_satisfied.setText("X")
            self.bt_satisfied.set_type("cancel")

        req_info = FormItem(self)
        req_info.initialize(self.info_name, self.info_content, self.req_element_family)
        self.layout.addWidget(req_info)

        # spacer
        self.sp_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.sp_right)

