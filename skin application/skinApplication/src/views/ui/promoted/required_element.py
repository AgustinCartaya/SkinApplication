from .promoted_container import *


class RequiredElement(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)
        self._pre_charge()

    def initialize(self, satisfied, info_name, info_content, scale_input=None):
        if satisfied:
            self.bt_satisfied.setText("/")
        else:
            self.bt_satisfied.setText("X")
            self.bt_satisfied.set_type("cancel")

        self.lb_info_name.setText(info_name, colon=True, format=True)
        self.lb_info_content.setText(info_content, scale_input=[info_name,scale_input])

    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_bt_satisfied()
        self.__create_content()

    def __create_bt_satisfied(self):
        self.bt_satisfied = Button(self)
        self.bt_satisfied.setMaximumSize(QSize(28, 28))
        self.layout.addWidget(self.bt_satisfied)

    def __create_content(self):
        self.lb_info_name = Label(self)
        self.layout.addWidget(self.lb_info_name)

        self.lb_info_content = Label(self)
        self.layout.addWidget(self.lb_info_content)

        # spacer
        self.sp_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.sp_right)

