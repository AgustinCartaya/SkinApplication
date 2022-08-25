from .promoted_container import *
from src.objects.variable_input import VariableInput


class FormItem(PromotedContainer):

    DISPOSITION_V = "V"
    DISPOSITION_H = "H"

    def __init__(self, parent):
        super().__init__(parent)
        self.title = ""
        self.content = ""
        self.disposition = self.DISPOSITION_V


    def initialize(self, title, content, vi_family=None, disposition=DISPOSITION_H):
        if vi_family is not None:
            vi = VariableInput.get_variable_input(title, vi_family)
            self.title = vi.name
            if content is not None:
                self.content = vi.get_scalized_str(content)
            else:
                self.content = ""
        else:
            self.title = title
            self.content = content

        self.disposition = disposition

        self.__create()
        self.__fill_content()

    def _pre_charge(self):
        pass

    def __create(self):
        if self.disposition == self.DISPOSITION_H:
            self.layout = QHBoxLayout(self)
            self.layout.setSpacing(12)
            self.layout.setContentsMargins(0, 0, 0, 0)

        else:
            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_lb_title()
        self.__create_lb_value()

        if self.disposition == self.DISPOSITION_H:
            # spacer
            sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.layout.addItem(sp)



    def __create_lb_title(self):
        self.lb_title = Label(self)
        self.layout.addWidget(self.lb_title)

    def __create_lb_value(self):
        self.lb_value = Label(self)
        self.layout.addWidget(self.lb_value)

    def __fill_content(self):
        self.lb_title.setText(self.title, colon=True, format=True)
        self.lb_value.setText(self.content)





