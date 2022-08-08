from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout
from .label import Label

from .required_element import  RequiredElement

class RequiredElementsContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, required_elements = None):
        QFrame.__init__(self, parent)

        self.required_elements = required_elements
        self.__create()


    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)


    def set_required_elements(self, required_elements):
        if len(required_elements) > 0:
            self.required_elements = required_elements
            for rk in required_elements:
#                print(type( rk[1]))
                rk_e = RequiredElement(self, rk[0], rk[1])
                self.layout.addWidget(rk_e)
        else:
            lb_no_required_info = Label(self)
            lb_no_required_info.setText("No required information")
            self.layout.addWidget(lb_no_required_info,0, Qt.AlignHCenter)

