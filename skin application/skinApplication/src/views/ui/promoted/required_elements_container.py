from .promoted_container import *

from .required_element import  RequiredElement

class RequiredElementsContainer(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)
        self._pre_charge()

    def initialize(self, required_elements, req_element_family):
        if len(required_elements) > 0:
            for req_element_name, req_element_value in required_elements.items():
                rk_e = RequiredElement(self)
                satisfied = req_element_value is not None
                rk_e.initialize(satisfied, req_element_name, req_element_value, req_element_family)
                self.layout.addWidget(rk_e)
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText("No required information")
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)
