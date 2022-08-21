from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout
from .label import Label

from .required_element import  RequiredElement

class RequiredElementsContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)


    def set_required_elements(self, required_elements, scale_input):
        if len(required_elements) > 0:
            for req_element_name, req_element_value in required_elements.items():
                rk_e = RequiredElement(self)
                satisfied = req_element_value is not None
                rk_e.fill_content(satisfied, req_element_name, req_element_value, scale_input)
                self.layout.addWidget(rk_e)
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText("No required information")
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

